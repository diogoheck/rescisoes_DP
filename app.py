from acesso_unico import gerar_relatorio_unico_TRCT
from acesso_unico import gerar_relatorio_unico_ANALITICO
from acesso_unico import gerar_relatorio_unico_FICHA_AUXILIAR
from salvar_relatorios_cliente import remover_arquivos, copiar_arquivos_clientes
from conectividade_social import acessar_conectividade_social
from conexao_unico import conectar_unico
from leitura_dados import carregar_planilha
from juntar_pdfs import mesclar_pdf
if __name__ == '__main__':

    remover_arquivos()

    lista_dados = carregar_planilha()
    # for dado in lista_dados:
        # acessar_conectividade_social(dado)
    
    for dado in lista_dados:
        gerar_relatorio_unico_TRCT(dado)
        gerar_relatorio_unico_ANALITICO()
        gerar_relatorio_unico_FICHA_AUXILIAR(dado)

    copiar_arquivos_clientes()
    mesclar_pdf()

    