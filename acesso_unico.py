# relatorios unico
import pyautogui
from time import sleep


def gerar_relatorio_unico_TRCT():
    # 1
    sleep(1)
    # Clicar na tela do unico para ativar
    pyautogui.click(34,5)
    sleep(0.5)
    # calculos -> folha normal individual (ctrl + N)
    pyautogui.hotkey('ctrl', 'n')
    sleep(2)
    # selecionar empresa (2031)
    pyautogui.hotkey('esc')
    pyautogui.typewrite('2031')
    pyautogui.press('enter')
    sleep(2)
    # selecionar colaborador (ANELISE - 3124)
    pyautogui.typewrite('3124')
    pyautogui.press('enter')
    # sleep(0.5)
    # sleep(1)
    # colocar competencia
    # enter
    pyautogui.press('enter')
    sleep(1)
    # imprimir
    pyautogui.click(459,209)
    sleep(4)
    # portaria MTE
    pyautogui.click(360,264)
    pyautogui.move(0,40)
    sleep(0.5)
    pyautogui.click()
    sleep(1)
    # visualizar
    pyautogui.click(23,166)
    # salvar (icone excel)
    sleep(4)
    pyautogui.click(635,121)
    pyautogui.move(0, 40)
    sleep(0.5)
    # adobe
    pyautogui.click()
    # janela configuração impressao ok (enter)
    sleep(1) 
    pyautogui.press('enter')
    # renomear "TRCT" e transferir para pasta O:\Clientes\Kuchak\Dpto Pessoal\2023\2031 MATRIZ\012023\RESCISÕES\RES ANELISE TOEBE
    sleep(1)
    pyautogui.typewrite('x:\TEMP_DP_RESCISOES\TRCT')
    # salvar (confirmar)
    pyautogui.press('enter')

def gerar_relatorio_unico_ANALITICO():
    # 2 (igual ao 1)
    sleep(1)
    # fechar relatorio TRCT
    pyautogui.click(1344,95)
    # mudar o modelo do relatório -> verbas por classificacao com valores para GRRF
    pyautogui.click(360,264)
    pyautogui.move(0,80)
    sleep(0.5)
    pyautogui.click()
    sleep(1)
    pyautogui.click(23,166)
    # salvar (icone excel)
    sleep(4)
    pyautogui.click(635,121)
    pyautogui.move(0, 40)
    sleep(0.5)
    # adobe
    pyautogui.click()
    # janela configuração impressao ok (enter)
    sleep(1) 
    pyautogui.press('enter')
    # renomear "TRCT" e transferir para pasta O:\Clientes\Kuchak\Dpto Pessoal\2023\2031 MATRIZ\012023\RESCISÕES\RES ANELISE TOEBE
    sleep(1)
    pyautogui.typewrite('x:\TEMP_DP_RESCISOES\ANALITICO')
    # salvar (confirmar)
    pyautogui.press('enter')
    # fechar relatorio analitco
    pyautogui.click(1344,95)
    # fechar os outros dois relatorios
    sleep(0.5)
    pyautogui.click(658,95)
    sleep(0.5)
    pyautogui.click(920,123)

def gerar_relatorio_unico_FICHA_AUXILIAR():
    # 3
    sleep(1)
    # Clicar na tela do unico para ativar
    pyautogui.click(34,5)
    # relatórios -> periódicos -> ficha registro auxiliar
    pyautogui.hotkey('alt', 'r', 'i', 'f')
    # selecionar colaborador
    sleep(2)
    pyautogui.typewrite('3124')
    # enter
    pyautogui.press('enter')
    # visualizar
    sleep(0.5)
    pyautogui.click(23,166)
    # salvar (icone excel)
    sleep(4)
    pyautogui.click(635,121)
    pyautogui.move(0, 40)
    sleep(0.5)
    # adobe
    pyautogui.click()
    # janela configuração impressao ok (enter)
    sleep(1) 
    pyautogui.press('enter')
    # renomear "TRCT" e transferir para pasta O:\Clientes\Kuchak\Dpto Pessoal\2023\2031 MATRIZ\012023\RESCISÕES\RES ANELISE TOEBE
    sleep(1)
    pyautogui.typewrite('x:\TEMP_DP_RESCISOES\FICHA AUXILIAR')
    # salvar (confirmar)
    pyautogui.press('enter')
    # fechar relatorio analitco
    pyautogui.click(1344,95)
    sleep(0.5)
    pyautogui.click(633,96)

    # JUNTAR TODOS PDFS (VALIDAR CNPJ ANTES) -> O:\Clientes\Kuchak\Dpto Pessoal\2023\2031 MATRIZ\012023\RESCISÕES\RES ANELISE TOEBE