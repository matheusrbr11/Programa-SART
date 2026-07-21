"""
Módulo de Processamento de Extrato (ETL)
========================================

Este script realiza a leitura de arquivos de extrato bancário (formato .xls),
aplica regras de negócios para classificação de lançamentos e persiste os 
dados válidos em um banco de dados SQLite.

Funcionalidades:
    - Leitura de planilhas Excel ignorando linhas irrelevantes.
    - Filtragem de linhas baseada em palavras-chave (ex: "TED-TRANSF").
    - Classificação de lançamentos em categorias (IDs 1 a 5) baseada na descrição.
    - Verificação de duplicidade antes da inserção no banco de dados.

Dependências:
    - pandas: Manipulação de dados tabulares.
    - sqlite3: Interação com o banco de dados local 'sart.db'.
    - xlrd: Leitura de arquivos .xls antigos.
"""

from tkinter import messagebox, filedialog
from pathlib import Path
import pandas as pd
import datetime
import warnings
import sqlite3
import tkinter
import sys
import os

# Suprimir avisos de versão/formato do Excel
warnings.simplefilter("ignore")

# --- CONFIGURAÇÃO DO AMBIENTE ---
PROJECT_BASE_PATH = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_BASE_PATH / "base de dados" / "sart.db"

# --- LÓGICA DE PROCESSAMENTO ---

def processar_arquivo_xls(caminho_arquivo):
    """
    Lê e processa um arquivo Excel de extrato bancário, aplicando regras de filtragem e categorização.

    A função procura por colunas específicas ('Lançamento', 'Crédito', 'Dcto'), converte tipos de dados
    e aplica filtros para manter apenas transferências relevantes (TEDs) que não sejam de origens ignoradas
    (ex: Ministério Público).
    
    Regras de Negócio Aplicadas:
        - Regra 1 (IDs 1, 2): Lançamentos padrões.
        - Regra 2 (IDs 3, 4, 5): Lançamentos identificados como "FUNDO S".

    Args:
        caminho_arquivo (str): O caminho absoluto para o arquivo .xls a ser processado.

    Returns:
        pd.DataFrame: Um DataFrame contendo as colunas:
            - 'data': Data do lançamento.
            - 'valor': Valor financeiro tratado.
            - 'observacao': Descrição concatenada com o número do documento e textos legais padrão.
            - 'tipo_id': Identificador numérico da regra de contabilização (1 a 5).
            Retorna um DataFrame vazio em caso de erro de leitura ou falta de colunas obrigatórias.
    """
    try:
        df = pd.read_excel(caminho_arquivo, skiprows=8)
    except ImportError:
        messagebox.showerror("Erro", "A biblioteca 'xlrd' necessária para ler XLS antigos não está instalada.\nInstale com: pip install xlrd")
        return pd.DataFrame()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo Excel:\n{e}")
        return pd.DataFrame()

    # Identificação das colunas
    df.columns = [str(c).strip() for c in df.columns]
    
    # Procura colunas chaves
    coluna_lancamento = [c for c in df.columns if 'Lançamento' in c]
    coluna_credito = [c for c in df.columns if 'Crédito' in c]
    coluna_dcto = [c for c in df.columns if 'Dcto' in c] 
    
    if not coluna_lancamento or not coluna_credito:
        messagebox.showerror("Erro", f"Colunas 'Lançamento' ou 'Crédito' não encontradas.\nColunas lidas: {list(df.columns)}")
        return pd.DataFrame()
        
    lancamento = coluna_lancamento[0]
    credito = coluna_credito[0]
    dcto = coluna_dcto[0] if coluna_dcto else None

    # Garante que 'Lançamento' seja string
    df[lancamento] = df[lancamento].astype(str)
    
    # Filtros iniciais
    palavra_chave = df[lancamento].str.contains("TED-TRANSF ELET DISPON", case=False, na=False)
    ignorar = ["MINISTERIO PUBLICO", "MINISTERIO P", "CAMARB"]
    ignorar_palavras = ~df[lancamento].str.contains('|'.join(ignorar), case=False, na=False)
    
    df_filtrado = df[palavra_chave & ignorar_palavras].copy()
    colunas_processadas = []

    for index, row in df_filtrado.iterrows():
        data_lancamento = row['Data']
        observacao_base = row[lancamento]
        valor_bruto = row[credito]
        dcto_bruto = row[dcto] if dcto else None
        
        numDoc = ""
        if dcto_bruto and not pd.isna(dcto_bruto) and dcto_bruto != '':
            try:
                # Converte float (ex: 123.0) para int e depois string
                numDoc = str(int(float(dcto_bruto)))
            except:
                numDoc = str(dcto_bruto).strip()

        observacao_final = f"{observacao_base} ({numDoc})"

        valor_float = 0.0
        if not (pd.isna(valor_bruto) or valor_bruto == ''):
            if isinstance(valor_bruto, (int, float)):
                valor_float = float(valor_bruto)
            else:
                try:
                    limpo = str(valor_bruto).replace('.', '').replace(',', '.')
                    valor_float = float(limpo)
                except ValueError:
                    valor_float = 0.0
        
        if valor_float <= 0:
            continue

        is_fundo_s = "FUNDO S" in observacao_base.upper()

        if is_fundo_s:
            # REGRA 2
            lista_regras = [3, 4, 5]
        else:
            # REGRA 1
            lista_regras = [1, 2]

        for tipo_id in lista_regras:
            
            # Observações
            match tipo_id:
                case 1:
                    observacao_final = "DEPÓSITO CONFORME EXTRATO BANCÁRIO, REGISTRADO EM DDO A PRIORI, PARA POSTERIOR RECLASSIFICAÇÃO. \n\n" + f"{observacao_final}" # GR 
                    valor_float_ajustado = valor_float             
                case 2:
                    observacao_final = "REGISTRO DA TRANSFERÊNCIA DOS RECURSOS DE RECEITA EXTRAORÇAMENTÁRIA DEPOSITADOS NA CONTA 35 À CUTE. \n\n" + f"{observacao_final}" # PD
                    valor_float_ajustado = valor_float
                case 3:
                    observacao_final = "REGISTRO DO RECOLHIMENTO DE RECURSOS DE RECEITA ORÇAMENTÁRIA REFERENTES A IRRF SOBRE OUTROS RENDIMENTOS. \n\n" + f"{observacao_final}" # GR Fundo S
                    valor_float_ajustado = valor_float
                case 4:
                    observacao_final = "REGISTRO DA TRANSFERÊNCIA DOS RECURSOS DE RECEITA ORÇAMENTÁRIA DEPOSITADOS NA CONTA 35 À CUTE. \n\n" + f"{observacao_final}" # PD Fundo S 100
                    valor_float_ajustado = valor_float * 0.995
                case 5:
                    observacao_final = "REGISTRO DA TRANSFERÊNCIA DOS RECURSOS DE EMENDA IMPOSITIVA REFERENTE A RECEITA ORÇAMENTÁRIA DE TRIBUTOS - IRRF DEPOSITADOS NA CONTA 35 À CUTE. \n\n" + f"{observacao_final}" # PD Fundo S 148
                    valor_float_ajustado = valor_float * 0.005
            
            item = {
                'data': data_lancamento,
                'valor': valor_float_ajustado,
                'observacao': observacao_final,
                'tipo_id': tipo_id
            }
            colunas_processadas.append(item)
    return pd.DataFrame(colunas_processadas)

def carregar_no_banco_de_dados(df_novos):
    """
    Insere novos registros no banco de dados SQLite, impedindo duplicidade.

    Realiza uma comparação entre os dados processados e os dados já existentes no banco
    utilizando uma estratégia de 'Left Join' nas chaves: data, valor, observacao e tipo_id.
    Apenas registros que não possuem correspondência no banco são inseridos.

    Args:
        df_novos (pd.DataFrame): DataFrame contendo os dados processados prontos para inserção.

    Returns:
        int: O número de registros efetivamente inseridos no banco de dados.
             Retorna 0 se o DataFrame estiver vazio ou ocorrer erro de conexão.
    """
    if df_novos.empty:
        return 0

    try:
        con = sqlite3.connect(DB_PATH)
        cursor = con.cursor()
        
        # 1. Carrega dados existentes para verificar duplicidade
        query_check = f"SELECT data, valor, observacao, tipo_id FROM contabilizacoes WHERE tipo_id IN (1, 2, 3, 4, 5)"
        df_db = pd.read_sql_query(query_check, con)
        
        # Padroniza tipos para comparação
        if not df_db.empty:
            df_db['valor'] = df_db['valor'].astype(float).round(2)
            df_db['tipo_id'] = df_db['tipo_id'].astype(int)
            df_db['chave_obs'] = df_db['observacao'].str.extract(r'\((\d+)\)', expand=False).fillna(df_db['observacao'])
            df_db['in_db'] = True
        
        # Prepara df_novos para comparação
        df_novos['valor'] = df_novos['valor'].astype(float).round(2)
        df_novos['tipo_id'] = df_novos['tipo_id'].astype(int)
        df_novos['chave_obs'] = df_novos['observacao'].str.extract(r'\((\d+)\)', expand=False).fillna(df_novos['observacao'])
        
        # 2. Verifica Duplicidade (Left Join)
        key_columns = ['data', 'valor', 'chave_obs', 'tipo_id']
        
        if not df_db.empty:
            df_merged = pd.merge(df_novos, df_db[key_columns + ['in_db']], on=key_columns, how='left')
            df_final = df_merged[df_merged['in_db'].isna()].copy()
        else:
            df_final = df_novos.copy()
            
        if df_final.empty:
            con.close()
            return 0 
        
        # 3. Inserção
        user = os.getlogin()
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        insercoes_feitas = 0

        for index, row in df_final.iterrows():
            valor_atual = float(row['valor'])
            tipo_id_atual = int(row['tipo_id'])
            
            num_doc_valor = None
            # Regra especial para documentos acima de 1 milhão na PD
            # Nesse caso, a PD deve ser executada por ofício e posteriormente regularizada
            if valor_atual > 1000000 and (tipo_id_atual == 1 or tipo_id_atual == 2):
                num_doc_valor = "Por Oficio"
            cursor.execute('''
                INSERT INTO contabilizacoes (data, valor, observacao, num_documento, tipo_id, usuario_inclusao, data_hora_inclusao)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', [row['data'], row['valor'], row['observacao'], num_doc_valor, tipo_id_atual, user, data_hora])
            insercoes_feitas += 1
            
        con.commit()
        con.close()
        return insercoes_feitas

    except Exception as e:
        messagebox.showerror("Erro", f"Erro no Banco de Dados: {e}")
        return 0

def main():
    """
    Função principal de entrada (Entry Point) para execução manual do script.

    Fluxo de Execução:
    1. Abre uma janela de diálogo para seleção do arquivo .xls, iniciando no diretório padrão.
    2. Chama `processar_arquivo_xls` para tratar os dados.
    3. Chama `carregar_no_banco_de_dados` para persistência.
    4. Exibe mensagens de sucesso, aviso ou erro ao usuário via `messagebox`.
    """
    root = tkinter.Tk()
    root.withdraw()
    
    caminho_inicial = Path(fr"\\cifs-zone1\tesouro\00 SUBFIN\SUCOMF\COCCB\EXTRATOS BRADESCO DIARIO\{datetime.date.today().year}")
    
    while True:
        try:
            arquivo_selecionado = filedialog.askopenfilename(
                initialdir=caminho_inicial,
                title="Selecione o Extrato da Conta 3-5",
                filetypes=(
                    ("Planilha Excel 97-2003", "*.xls"),
                    ("Todos os arquivos", "*.*")
                )
            )

            if not arquivo_selecionado:
                resposta = messagebox.askretrycancel(
                    "Atenção", 
                    "Nenhum arquivo foi selecionado.\nPor favor, selecione um arquivo."
                )
                if not resposta:
                    root.destroy()
                    return 
            else:
                break

        except Exception as e:
            messagebox.showerror("Erro", f"Erro na seleção de arquivo: {e}")
            root.destroy()
            return

    try:
        df_processado = processar_arquivo_xls(arquivo_selecionado)

        if df_processado.empty:
            messagebox.showinfo("Info", "Nenhum lançamento novo encontrado ou arquivo vazio.")
            return
        
        qtd_inserida = carregar_no_banco_de_dados(df_processado)
        
        if qtd_inserida == 0:
            messagebox.showinfo("Info", "Todos os documentos do extrato já foram processados anteriormente.")
        else:
            messagebox.showinfo(
                "Sucesso",
                f"Documentos processados com sucesso!\n"
                f"Novos lançamentos inseridos: {qtd_inserida}"
            )

    except Exception as e:
        messagebox.showerror("Erro", f"Erro na leitura do arquivo Excel: {e}")
    
    finally:
        if root:
            root.destroy()

if __name__ == "__main__":
    main()