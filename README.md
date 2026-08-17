# 🏛️ Programa SART

> Sistema de automação contábil desenvolvido pela **Equipe de Otimização Processual (EOP/SUPCONFI)** do **Tesouro do Estado do Rio de Janeiro**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)](https://www.selenium.dev/)
[![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-informational)](https://github.com/TomSchimansky/CustomTkinter)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)](https://www.sqlite.org/)
[![Versão](https://img.shields.io/badge/Versão-2.3.0-orange)](.)

---

## 📑 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Arquitetura](#-arquitetura)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Estrutura de Arquivos](#-estrutura-de-arquivos)
- [Como Usar](#-como-usar)
- [Banco de Dados](#-banco-de-dados)
- [Contribuição](#-contribuição)

---

## 📌 Sobre o Projeto

O **Programa SART** é uma ferramenta de automação desenvolvida para a **Coordenadoria de Conciliação Bancária (COCCB)** da Superintendência de Controles Financeiros (SUPCONFI), com o objetivo de automatizar a contabilização dos lançamentos identificados no **extrato bancário da Conta 3-5**, referentes a transferências de recursos extraorçamentários e orçamentários (Fundo Soberano) recebidos pelo Estado do Rio de Janeiro.

O sistema elimina a necessidade de lançamentos manuais no **SIAFE-Rio2**, reduzindo erros operacionais e o tempo gasto em tarefas repetitivas, processando automaticamente os seguintes tipos de lançamento identificados no extrato:

- **Regra Padrão** — depósitos de terceiros na Conta 35, gerando **GR** (Guia de Recolhimento) e **PD** (Programação de Desembolso de Transferência)
- **Regra "Fundo S"** — lançamentos com origem no Fundo Soberano, com rateio automático entre PD orçamentária (99,5%) e PD de emenda impositiva (0,5%), além da respectiva GR de IRRF

---

## ✨ Funcionalidades

### 1. Processamento do Extrato Bancário (ETL)
- Leitura assistida (via seleção manual de arquivo) do extrato `.xls` da Conta 3-5, disponibilizado na rede corporativa
- Filtragem de lançamentos relevantes
- Marcação automática para lançamentos acima de R$ 1.000.000,00, sinalizando execução "Por Ofício"
- Armazenamento estruturado em banco de dados **SQLite**, com verificação de duplicidade antes da inserção

### 2. Contabilização Automática no SIAFE-Rio2
- Preenchimento automático de todos os campos necessários via automação no navegador
- Suporte a dois tipos de documento:
  - **GR** — Guia de Recolhimento
  - **PD** — Programação de Desembolso de Transferência
- Atualização do banco de dados com o número do documento, usuário e tempo de contabilização a cada lançamento concluído com sucesso

### 3. Interface Gráfica (GUI)
- Tela de login com autenticação via CPF e senha do SIAFE-Rio2
- Menu principal com botões para **Processar Extrato** e **Contabilizar**, além de consulta ao **Banco de Dados**
- Seleção do tipo de contabilização (GR ou PD)
- Tela de execução com log em tempo real e barra de progresso
- Acesso rápido ao Manual de Uso (F2) e à tela "Sobre" (F1)

---

## 🏗️ Arquitetura

```
┌────────────────────────────────────────────────────────┐
│                     exe.py                             │
│            (ponto de entrada / atalho)                 │
└─────────────────┬──────────────────────────────────────┘
                  │ subprocess
                  ▼
┌────────────────────────────────────────────────────────┐
│                    main.py                             │
│         SARTApp (CustomTkinter + Siafe)                │
│  ┌──────────────┐        ┌─────────────────────────┐   │
│  │  GUI / Login │        │  Execução / Progresso   │   │
│  └──────┬───────┘        └────────────┬────────────┘   │
│         │                             │                │
│         ▼                             ▼                │
│  ┌──────────────┐        ┌─────────────────────────┐   │
│  │  extrato.py  │        │      jupiter-subtes     │   │
│  │  (ETL/XLS)   │        │   Automação SIAFE-Rio2  │   │
│  └──────┬───────┘        └─────────────────────────┘   │
│         │                                              │
│         ▼                                              │
│  ┌──────────────┐                                      │
│  │   sart.db    │  (SQLite)                            │
│  └──────────────┘                                      │
└────────────────────────────────────────────────────────┘
```

**Fluxo de dados:**

```
Extrato Bancário (.xls) ──► [extrato.py] ──► tabela contabilizacoes
                                                     │
                                                  [main.py]
                                                     │
                                              SIAFE-Rio2 (Edge)
```

---

## ⚙️ Pré-requisitos

- **Python** 3.10 ou superior
- **Microsoft Edge** instalado (WebDriver compatível com a versão do navegador) — necessário apenas para o fluxo via automação de navegador
- **Microsoft Edge WebDriver** no PATH do sistema
- Credenciais válidas no **SIAFE-Rio2**

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/matheusrbr11/SART.git
cd SART
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv env
# Windows
env\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> **Dependências principais:**

| Pacote | Uso |
|---|---|
| `customtkinter` | Interface gráfica |
| `selenium` | Automação web (SIAFE-Rio2) |
| `pandas` | Processamento e transformação dos dados do extrato |
| `numpy` | Operações numéricas auxiliares |
| `Pillow` | Carregamento de imagens na interface |
| `xlrd` | Leitura de arquivos `.xls` (Excel 97-2003) |
| `openpyxl` | Suporte à leitura/escrita de planilhas Excel |
| `office365-rest-python-client` | Integração com SharePoint/Microsoft Graph |
| `jupiter-subtes` | Biblioteca da EOP/SUPCONC para automação do SIAFE-Rio2 |

### 4. Execute o programa

```bash
python exe.py
```

---

## 📁 Estrutura de Arquivos

```
sart/
│
├── exe.py                  # Ponto de entrada (usado pelo atalho .exe)
├── main.py                 # Aplicação principal + GUI (SARTApp)
├── extrato.py               # ETL: parse do extrato .xls e carga no SQLite
├── tela_db.py               # Tela de consulta/gestão do banco de dados na GUI
├── dicts.py                 # Dicionários de mapeamento de campos e roteiros contábeis
│
├── base de dados/
│   └── sart.db               # Banco de dados SQLite
│
├── dist/
│   └── SART.exe              # Executável .exe
│
├── img/
│   ├── icon.ico               # Ícone do programa
│   ├── icon2.png              # Ícone do programa em PNG
│   ├── tesouro.png            # Logo do Tesouro RJ
│   └── voltar.png             # Ícone de voltar
│
├── Manual de Uso.pdf         # Manual do usuário
├── requirements.txt          # Dependências do projeto
├── .gitignore
└── README.md
```

---

## 🖥️ Como Usar

### Passo 1 — Login
Abra o programa pelo atalho ou via `exe.py`. Na tela de login, insira seu **CPF** (usuário) e **senha** do SIAFE-Rio2 e clique em **LOGIN**.

### Passo 2 — Processar Extrato
Na tela principal, clique em **PROCESSAR EXTRATO**. O programa irá:
1. Abrir uma janela para seleção do arquivo de extrato bancário `.xls` da Conta 3-5
2. Filtrar as transferências relevantes (TEDs recebidas)
3. Classificar cada lançamento nas regras contábeis aplicáveis, calculando os valores proporcionais quando necessário
4. Verificar duplicidade e carregar os novos registros no banco de dados

> ⚠️ Esta etapa **não realiza contabilizações** no SIAFE. Ela apenas prepara os dados.

### Passo 3 — Contabilizar
Selecione o tipo de contabilização no menu suspenso:
- **Guia de Recolhimento** — Para registrar os depósitos (GR padrão e GR do Fundo S)
- **PD de Transferência** — Para registrar as transferências de recursos à CUTE (PD padrão e PD do Fundo S)

Clique em **CONTABILIZAR**. O programa abrirá o SIAFE-Rio2 e preencherá automaticamente todos os campos para cada lançamento. Ao final, o número dos documentos contabilizados será exibido no log e atualizado no banco de dados.

### Passo 4 — Consultar Banco de Dados
Clique em **BANCO DE DADOS** para abrir o popup de consulta, alternando entre lançamentos **pendentes** (todos os programas) e **contabilizados** (Programa SART).

---

## 🗄️ Banco de Dados

O arquivo `base de dados/sart.db` contém a tabela principal utilizada pelo programa:

### Tabela `contabilizacoes`
Armazena os lançamentos a serem (ou já) contabilizados no SIAFE.

| Coluna | Tipo | Descrição |
|---|---|---|
| `data` | TEXT | Data do lançamento (DD/MM/AAAA) |
| `valor` | TEXT | Valor monetário do lançamento |
| `observacao` | TEXT | Descrição gerada automaticamente |
| `num_documento` | TEXT | Número do documento no SIAFE (preenchido após contabilização) |
| `tipo_id` | INTEGER | Identificador do tipo de transferência (1–22) |
| `usuario_inclusao` | TEXT | Login do usuário que processou |
| `data_hora_inclusao` | TEXT | Horário do processamento (AAAA-MM-DD HH:MM:SS) |
| `usuario_contab` | TEXT | Login do usuário que contabilizou |
| `data_hora_contab` | TEXT | Horário de contabilização (AAAA-MM-DD HH:MM:SS) |
| `tempo_contab` | TEXT | Tempo de execução da contabilização |

---

## 🤝 Contribuição

Este projeto é desenvolvido e mantido pela **Equipe de Otimização Processual (EOP)** da **SUPCONFI — Tesouro do Estado do Rio de Janeiro**.

Dúvidas, sugestões e reportes de inconsistências operacionais devem ser encaminhados diretamente à equipe. Em caso de mudanças nas premissas operacionais (estrutura do extrato bancário, roteiros contábeis, contas, etc.), a equipe deve ser notificada para atualização do sistema e do manual de uso.

O manual de uso está arquivado no **SEI-RJ** sob o processo `SEI-040009/000182/2026`, denominado *"Manual de Uso Nº 01/2026"*.

---

<div align="center">
  <sub>EOP / SUPCONC — Tesouro do Estado do Rio de Janeiro &nbsp;|&nbsp; Versão 2.3.0 &nbsp;|&nbsp; 17/08/2026</sub>
</div>
