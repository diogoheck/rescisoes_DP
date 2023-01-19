import os
import shutil
from time import sleep

PASTA_RESCISOES = 'U:\TEMP_DP_RESCISOES'


def remover_arquivos():
    for arquivo in os.listdir(PASTA_RESCISOES):
        # print(os.listdir(PASTA_RESCISOES))
        if os.path.isfile(f'{PASTA_RESCISOES}{os.sep}{arquivo}'):
            os.remove(f'{PASTA_RESCISOES}{os.sep}{arquivo}')


def criar_nova_pasta(caminho):
    os.makedirs(caminho)


def existe_essa_pasta(caminho):
    return os.path.exists(caminho)


def copiar_arquivos(origem, destino):
    shutil.copyfile(origem, destino)


def mover_arquivo(origem, destino):
    shutil.move(origem, destino)


def copiar_arquivos_clientes():
    sleep(5)

    while(True):
        if len(os.listdir(PASTA_RESCISOES)) == 3:
            for arquivo in os.listdir(PASTA_RESCISOES):
                pasta_rede_destino = 'O:\Clientes\Kuchak\Dpto Pessoal\\2023\\2031 MATRIZ\\012023\RESCISÕES\ANELISE TOEBE\\'
                arquivo_origem = os.path.join(PASTA_RESCISOES, arquivo)
                if not existe_essa_pasta(pasta_rede_destino):
                    criar_nova_pasta(pasta_rede_destino)
                pasta_rede_destino = f'{pasta_rede_destino}\{arquivo.upper()}'
                mover_arquivo(arquivo_origem, pasta_rede_destino)
            # print('arquivos movidos com sucesso')
            break