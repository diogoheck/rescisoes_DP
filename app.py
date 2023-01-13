from acesso_unico import gerar_relatorio_unico_TRCT
from acesso_unico import gerar_relatorio_unico_ANALITICO
from acesso_unico import gerar_relatorio_unico_FICHA_AUXILIAR
from salvar_relatorios_cliente import remover_arquivos, copiar_arquivos_clientes

if __name__ == '__main__':

    remover_arquivos()

    gerar_relatorio_unico_TRCT()
    gerar_relatorio_unico_ANALITICO()
    gerar_relatorio_unico_FICHA_AUXILIAR()

    copiar_arquivos_clientes()