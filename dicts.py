# =========================================================================
# DADOS ESTRUTURAIS (DICIONÁRIOS)
# =========================================================================
# Regra 1 (Padrão)
dictGR = {
    "ExtraOrcamentario": True,
    "TipoDocumento": "Extra-orçamentário",
    "UG": "999900",
    "DomicilioBancario": "0000000035",
    "DomicilioBancarioCompleto": "237 - 6898 - 0000000035",
    "IEF": "1 - Recursos do Exercício Corrente",
    "Fonte": "862 - Recursos de Depósitos de Terceiros",
    "FonteRJ": "081 - Recursos Não Orçamentários - Depósitos de Diversas Origens",
    "TipoDetalhamentoFonte": "0 - Sem Detalhamento",
    "Convenio": "000000 - Convênio não identificado",
    "TipoPatrimonial": "Valores Restituíveis (Cauções e Outros)",
    "ItemPatrimonial": "4486 - DEPÓSITOS DE TERCEIROS",
    "OperacaoPatrimonial": "233 - Depósito",
    "Ano": "2026",
    "TipoCredor": "UG",
    "Credor": "999900",
}
dictPD = {
    "ExtraOrcamentario": False,
    "UG": "999900",
    "DomicilioBancarioOrigem": "0000000035",
    "DomicilioBancarioDestino": "0000000027",
    "DomicilioBancarioOrigemCompleto": "237 - 6898 - 0000000035",
    "DomicilioBancarioDestinoCompleto": "237 - 6898 - 0000000027",
    "IEF": "1 - Recursos do Exercício Corrente",
    "Fonte": "862 - Recursos de Depósitos de Terceiros",
    "FonteRJ": "081 - Recursos Não Orçamentários - Depósitos de Diversas Origens",
    "TipoDetalhamentoFonte": "0 - Sem Detalhamento",
    "DetalhamentoFonte": "000000 - Sem detalhamento - (862.081)",
    "Convenio": "000000 - Convênio não identificado",
    "TipoPatrimonial": "Transferência Financeira entre UG's e na Própria UG",
    "ItemPatrimonial": "4429 - TRANSFERÊNCIA FINANCEIRA",
    "OperacaoPatrimonial": "4074 - Transferência financeira entre Contas Bancarias - Na UG",
}

# Regra 2 (Fundo Soberano)
dictFundoS = {
    "ExtraOrcamentario": False,
    "TipoDocumento": "Orçamentário",
    "UG": "999900",
    "DomicilioBancario": "0000000035",
    "DomicilioBancarioCompleto": "237 - 6898 - 0000000035",
    "IEF": "1 - Recursos do Exercício Corrente",
    "Fonte": "500 - Recursos não Vinculados de Impostos",
    "FonteRJ": "100 - Recursos não Vinculados de Impostos - Ordinários Provenientes de Impostos",
    "TipoDetalhamentoFonte": "0 - Sem Detalhamento",
    "Convenio": "000000 - Convênio não identificado",
    "TipoPatrimonial": "Receita de Tributos - IRRF",
    "ItemPatrimonial": "4776 - IRRF SOBRE OUTROS RENDIMENTOS",
    "OperacaoPatrimonial": "197 - Reconhecimento, Arrecadação e Recolhimento",
    "NaturezaReceita": "1113034101 - Imposto sobre a Renda - Retido na Fonte - Outros Rendimentos - Principal",
}
dictPDFundoS100 = {
    "ExtraOrcamentario": False,
    "UG": "999900",
    "DomicilioBancarioOrigem": "0000000035",
    "DomicilioBancarioDestino": "0000000027",
    "DomicilioBancarioOrigemCompleto": "237 - 6898 - 0000000035",
    "DomicilioBancarioDestinoCompleto": "237 - 6898 - 0000000027",
    "IEF": "1 - Recursos do Exercício Corrente",
    "Fonte": "500 - Recursos não Vinculados de Impostos",
    "FonteRJ": "100 - Recursos não Vinculados de Impostos - Ordinários Provenientes de Impostos",
    "TipoDetalhamentoFonte": "0 - Sem Detalhamento",
    "DetalhamentoFonte": "000000 - Sem detalhamento - (500.100)",
    "Convenio": "000000 - Convênio não identificado",
    "TipoPatrimonial": "Transferência Financeira entre UG's e na Própria UG",
    "ItemPatrimonial": "4429 - TRANSFERÊNCIA FINANCEIRA",
    "OperacaoPatrimonial": "4074 - Transferência financeira entre Contas Bancarias - Na UG",
}
dictPDFundoS148 = {
    "ExtraOrcamentario": False,
    "UG": "999900",
    "DomicilioBancarioOrigem": "0000000035",
    "DomicilioBancarioDestino": "0000000027",
    "DomicilioBancarioOrigemCompleto": "237 - 6898 - 0000000035",
    "DomicilioBancarioDestinoCompleto": "237 - 6898 - 0000000027",
    "IEF": "1 - Recursos do Exercício Corrente",
    "Fonte": "500 - Recursos não Vinculados de Impostos",
    "FonteRJ": "148 - Recurs. não Vinculados de Imp .- Ordinários Proven. de Imp. - Emenda Impositiva",
    "TipoDetalhamentoFonte": "0 - Sem Detalhamento",
    "DetalhamentoFonte": "000000 - Sem detalhamento - (500.148)",
    "Convenio": "000000 - Convênio não identificado",
    "TipoPatrimonial": "Transferência Financeira entre UG's e na Própria UG",
    "ItemPatrimonial": "4429 - TRANSFERÊNCIA FINANCEIRA",
    "OperacaoPatrimonial": "4074 - Transferência financeira entre Contas Bancarias - Na UG",
}

dict_map_gr = {1: dictGR, 3: dictFundoS}
dict_map_pd = {2: dictPD, 4: dictPDFundoS100, 5: dictPDFundoS148}