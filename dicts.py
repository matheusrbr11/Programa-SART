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

dictPD_API = {
    "dataEmissao": "",
    "dataProcesso": "",
    "dataProgramacao": "",
    "dataVencimento": "",
    "codigoUgEmitente": 999900,
    "codigoUgFavorecida": 999900,
    "codigoUgPagadora": 999900,
    "origem": {
        "classificacao": [
            {
                "codigoTipoClassificador": 23,
                "nomeTipoClassificador": "Identificador Exercício Fonte",
                "nomeClassificador": "1",
                "valoresClassificador": [
                    "1"
                ]
            },
            {
                "codigoTipoClassificador": 28,
                "nomeTipoClassificador": "Fonte",
                "nomeClassificador": "8.62",
                "valoresClassificador": [
                    "8",
                    "62"
                ]
            },
            {
                "codigoTipoClassificador": 24,
                "nomeTipoClassificador": "Fonte RJ",
                "nomeClassificador": "8.62.081",
                "valoresClassificador": [
                    "8",
                    "62",
                    "081"
                ]
            },
            {
                "codigoTipoClassificador": 186,
                "nomeTipoClassificador": "Tipo de Detalhamento de Fonte",
                "nomeClassificador": "0",
                "valoresClassificador": [
                    "0"
                ]
            },
            {
                "codigoTipoClassificador": 159,
                "nomeTipoClassificador": "Detalhamento de Fonte",
                "nomeClassificador": "8.62.081.000000",
                "valoresClassificador": [
                    "8",
                    "62",
                    "081",
                    "000000"
                ]
            },
            {
                "codigoTipoClassificador": 38,
                "nomeTipoClassificador": "Convênio de Receita",
                "nomeClassificador": "000000",
                "valoresClassificador": [
                    "000000"
                ]
            }
        ],
        "domicilioBancario": {
            "bancoCodigo": "237",
            "agenciaCodigo": "6898",
            "codigo": "0000000035"
        }
    },
    "destino": {
        "classificacao": [
            {
                "codigoTipoClassificador": 23,
                "nomeTipoClassificador": "Identificador Exercício Fonte",
                "nomeClassificador": "1",
                "valoresClassificador": [
                    "1"
                ]
            },
            {
                "codigoTipoClassificador": 28,
                "nomeTipoClassificador": "Fonte",
                "nomeClassificador": "8.62",
                "valoresClassificador": [
                    "8",
                    "62"
                ]
            },
            {
                "codigoTipoClassificador": 24,
                "nomeTipoClassificador": "Fonte RJ",
                "nomeClassificador": "8.62.081",
                "valoresClassificador": [
                    "8",
                    "62",
                    "081"
                ]
            },
            {
                "codigoTipoClassificador": 186,
                "nomeTipoClassificador": "Tipo de Detalhamento de Fonte",
                "nomeClassificador": "0",
                "valoresClassificador": [
                    "0"
                ]
            },
            {
                "codigoTipoClassificador": 159,
                "nomeTipoClassificador": "Detalhamento de Fonte",
                "nomeClassificador": "8.62.081.000000",
                "valoresClassificador": [
                    "8",
                    "62",
                    "081",
                    "000000"
                ]
            },
            {
                "codigoTipoClassificador": 38,
                "nomeTipoClassificador": "Convênio de Receita",
                "nomeClassificador": "000000",
                "valoresClassificador": [
                    "000000"
                ]
            }
        ],
        "domicilioBancario": {
            "bancoCodigo": "237",
            "agenciaCodigo": "6898",
            "codigo": "0000000027"
        }
    },
    "competencia": "",
    "itens": [
        {
            "classificadores": [
                {
                    "codigoTipoClassificador": 116,
                    "nomeTipoClassificador": "Tipo Patrimonial",
                    "nomeClassificador": "198",
                    "valoresClassificador": [
                        "198"
                    ]
                },
                {
                    "codigoTipoClassificador": 109,
                    "nomeTipoClassificador": "Item Patrimonial",
                    "nomeClassificador": "4429",
                    "valoresClassificador": [
                        "4429"
                    ]
                },
                {
                    "codigoTipoClassificador": 115,
                    "nomeTipoClassificador": "Operação Patrimonial",
                    "nomeClassificador": "4074",
                    "valoresClassificador": [
                        "4074"
                    ]
                }
                
            ],
            "valor": ""
        }
    ],
    "observacao": ""
}

dictPDFundoS100_API = {
    "dataEmissao": "",
    "dataProcesso": "",
    "dataProgramacao": "",
    "dataVencimento": "",
    "codigoUgEmitente": 999900,
    "codigoUgFavorecida": 999900,
    "codigoUgPagadora": 999900,
    "origem": {
        "classificacao": [
            {
                "codigoTipoClassificador": 23,
                "nomeTipoClassificador": "Identificador Exercício Fonte",
                "nomeClassificador": "1",
                "valoresClassificador": [
                    "1"
                ]
            },
            {
                "codigoTipoClassificador": 28,
                "nomeTipoClassificador": "Fonte",
                "nomeClassificador": "5.00",
                "valoresClassificador": [
                    "5",
                    "00"
                ]
            },
            {
                "codigoTipoClassificador": 24,
                "nomeTipoClassificador": "Fonte RJ",
                "nomeClassificador": "5.00.100",
                "valoresClassificador": [
                    "5",
                    "00",
                    "100"
                ]
            },
            {
                "codigoTipoClassificador": 186,
                "nomeTipoClassificador": "Tipo de Detalhamento de Fonte",
                "nomeClassificador": "0",
                "valoresClassificador": [
                    "0"
                ]
            },
            {
                "codigoTipoClassificador": 159,
                "nomeTipoClassificador": "Detalhamento de Fonte",
                "nomeClassificador": "5.00.100.000000",
                "valoresClassificador": [
                    "5",
                    "00",
                    "100",
                    "000000"
                ]
            },
            {
                "codigoTipoClassificador": 38,
                "nomeTipoClassificador": "Convênio de Receita",
                "nomeClassificador": "000000",
                "valoresClassificador": [
                    "000000"
                ]
            }
        ],
        "domicilioBancario": {
            "bancoCodigo": "237",
            "agenciaCodigo": "6898",
            "codigo": "0000000035"
        }
    },
    "destino": {
        "classificacao": [
            {
                "codigoTipoClassificador": 23,
                "nomeTipoClassificador": "Identificador Exercício Fonte",
                "nomeClassificador": "1",
                "valoresClassificador": [
                    "1"
                ]
            },
            {
                "codigoTipoClassificador": 28,
                "nomeTipoClassificador": "Fonte",
                "nomeClassificador": "5.00",
                "valoresClassificador": [
                    "5",
                    "00"
                ]
            },
            {
                "codigoTipoClassificador": 24,
                "nomeTipoClassificador": "Fonte RJ",
                "nomeClassificador": "5.00.100",
                "valoresClassificador": [
                    "5",
                    "00",
                    "100"
                ]
            },
            {
                "codigoTipoClassificador": 186,
                "nomeTipoClassificador": "Tipo de Detalhamento de Fonte",
                "nomeClassificador": "0",
                "valoresClassificador": [
                    "0"
                ]
            },
            {
                "codigoTipoClassificador": 159,
                "nomeTipoClassificador": "Detalhamento de Fonte",
                "nomeClassificador": "5.00.100.000000",
                "valoresClassificador": [
                    "5",
                    "00",
                    "100",
                    "000000"
                ]
            },
            {
                "codigoTipoClassificador": 38,
                "nomeTipoClassificador": "Convênio de Receita",
                "nomeClassificador": "000000",
                "valoresClassificador": [
                    "000000"
                ]
            }
        ],
        "domicilioBancario": {
            "bancoCodigo": "237",
            "agenciaCodigo": "6898",
            "codigo": "0000000027"
        }
    },
    "competencia": "",
    "itens": [
        {
            "classificadores": [
                {
                    "codigoTipoClassificador": 116,
                    "nomeTipoClassificador": "Tipo Patrimonial",
                    "nomeClassificador": "198",
                    "valoresClassificador": [
                        "198"
                    ]
                },
                {
                    "codigoTipoClassificador": 109,
                    "nomeTipoClassificador": "Item Patrimonial",
                    "nomeClassificador": "4429",
                    "valoresClassificador": [
                        "4429"
                    ]
                },
                {
                    "codigoTipoClassificador": 115,
                    "nomeTipoClassificador": "Operação Patrimonial",
                    "nomeClassificador": "4074",
                    "valoresClassificador": [
                        "4074"
                    ]
                }
                
            ],
            "valor": ""
        }
    ],
    "observacao": ""
}

dictPDFundoS148_API = {
    "dataEmissao": "",
    "dataProcesso": "",
    "dataProgramacao": "",
    "dataVencimento": "",
    "codigoUgEmitente": 999900,
    "codigoUgFavorecida": 999900,
    "codigoUgPagadora": 999900,
    "origem": {
        "classificacao": [
            {
                "codigoTipoClassificador": 23,
                "nomeTipoClassificador": "Identificador Exercício Fonte",
                "nomeClassificador": "1",
                "valoresClassificador": [
                    "1"
                ]
            },
            {
                "codigoTipoClassificador": 28,
                "nomeTipoClassificador": "Fonte",
                "nomeClassificador": "5.00",
                "valoresClassificador": [
                    "5",
                    "00"
                ]
            },
            {
                "codigoTipoClassificador": 24,
                "nomeTipoClassificador": "Fonte RJ",
                "nomeClassificador": "5.00.148",
                "valoresClassificador": [
                    "5",
                    "00",
                    "148"
                ]
            },
            {
                "codigoTipoClassificador": 186,
                "nomeTipoClassificador": "Tipo de Detalhamento de Fonte",
                "nomeClassificador": "0",
                "valoresClassificador": [
                    "0"
                ]
            },
            {
                "codigoTipoClassificador": 159,
                "nomeTipoClassificador": "Detalhamento de Fonte",
                "nomeClassificador": "5.00.148.000000",
                "valoresClassificador": [
                    "5",
                    "00",
                    "148",
                    "000000"
                ]
            },
            {
                "codigoTipoClassificador": 38,
                "nomeTipoClassificador": "Convênio de Receita",
                "nomeClassificador": "000000",
                "valoresClassificador": [
                    "000000"
                ]
            }
        ],
        "domicilioBancario": {
            "bancoCodigo": "237",
            "agenciaCodigo": "6898",
            "codigo": "0000000035"
        }
    },
    "destino": {
        "classificacao": [
            {
                "codigoTipoClassificador": 23,
                "nomeTipoClassificador": "Identificador Exercício Fonte",
                "nomeClassificador": "1",
                "valoresClassificador": [
                    "1"
                ]
            },
            {
                "codigoTipoClassificador": 28,
                "nomeTipoClassificador": "Fonte",
                "nomeClassificador": "5.00",
                "valoresClassificador": [
                    "5",
                    "00"
                ]
            },
            {
                "codigoTipoClassificador": 24,
                "nomeTipoClassificador": "Fonte RJ",
                "nomeClassificador": "5.00.148",
                "valoresClassificador": [
                    "5",
                    "00",
                    "148"
                ]
            },
            {
                "codigoTipoClassificador": 186,
                "nomeTipoClassificador": "Tipo de Detalhamento de Fonte",
                "nomeClassificador": "0",
                "valoresClassificador": [
                    "0"
                ]
            },
            {
                "codigoTipoClassificador": 159,
                "nomeTipoClassificador": "Detalhamento de Fonte",
                "nomeClassificador": "5.00.148.000000",
                "valoresClassificador": [
                    "5",
                    "00",
                    "148",
                    "000000"
                ]
            },
            {
                "codigoTipoClassificador": 38,
                "nomeTipoClassificador": "Convênio de Receita",
                "nomeClassificador": "000000",
                "valoresClassificador": [
                    "000000"
                ]
            }
        ],
        "domicilioBancario": {
            "bancoCodigo": "237",
            "agenciaCodigo": "6898",
            "codigo": "0000000027"
        }
    },
    "competencia": "",
    "itens": [
        {
            "classificadores": [
                {
                    "codigoTipoClassificador": 116,
                    "nomeTipoClassificador": "Tipo Patrimonial",
                    "nomeClassificador": "198",
                    "valoresClassificador": [
                        "198"
                    ]
                },
                {
                    "codigoTipoClassificador": 109,
                    "nomeTipoClassificador": "Item Patrimonial",
                    "nomeClassificador": "4429",
                    "valoresClassificador": [
                        "4429"
                    ]
                },
                {
                    "codigoTipoClassificador": 115,
                    "nomeTipoClassificador": "Operação Patrimonial",
                    "nomeClassificador": "4074",
                    "valoresClassificador": [
                        "4074"
                    ]
                }
                
            ],
            "valor": ""
        }
    ],
    "observacao": ""
}

dict_map_pd_API = {2: dictPD_API, 4: dictPDFundoS100_API, 5: dictPDFundoS148_API}