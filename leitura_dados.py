from openpyxl import load_workbook

def remover_caracteres(dado):
    dado = dado.replace('.', '').replace('/', '').replace('-', '')
    return dado

def carregar_planilha():
    pasta_banco = load_workbook('informacoes.xlsx')
    planilha_banco = pasta_banco['Planilha1']
    cabecalho = True
    lista_informacoes = []
    for linha in planilha_banco.values:
        if not cabecalho:
        # print(type(linha[0]), type(linha[1]))
            dic_dados = {}
            # print(linha)
            # dic_dados[str(linha[0])] = str(linha[1])
            dic_dados['CNPJ'] = remover_caracteres(str(linha[0]))
            dic_dados['COD_EMPRESA'] = str(linha[1])
            dic_dados['COD_FUNCIONARIO'] = str(linha[2])
            dic_dados['PIS'] = remover_caracteres(str(linha[3]))
            dic_dados['MODALIDADE_DESLIGAMENTO'] = str(linha[4])
            lista_informacoes.append(dic_dados)
        cabecalho = False
    return lista_informacoes


if __name__ == '__main__':
    planilha_dados = carregar_planilha()

    print(planilha_dados)