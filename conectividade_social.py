from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from certificados import pesquisar_certificado 
from leitura_dados import carregar_planilha
import pyautogui

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Uso de configurações experimentais (instáveis)
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # Inicializando o webdriver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

def acessar_conectividade_social(lista_dados):
    # buscar certificado luciano
    print('*' * 100)
    print('*' * 100)
    print('Favor selecionar o certificado e depois clicar em qualquer tecla para continuar'.upper())
    print('*' * 100)
    print('*' * 100)


    # pesquisar_certificado('https://conectividade.caixa.gov.br/')
    driver = iniciar_driver()
    # entrar no conectividade.caixa.gov.br
    # entrar no conectividade.caixa.gov.br
    driver.get("https://conectividade.caixa.gov.br/")
    # driver.get("https://conectividade.caixa.gov.br/")
    driver.maximize_window()
    input('')
    # mudar frame
    frame = driver.find_element(By.ID, 
            'frmMenuCNSICP')
    driver.switch_to.frame(frame)
    # selecione empregador
    sleep(2)
    select = Select(driver.find_element(By.ID, 'cmbAplicativo'))
    select.select_by_visible_text('Empregador')
    # selecione certificado luciano
    print('*' * 100)
    print('*' * 100)
    print('Favor selecionar o certificado e depois clicar em qualquer tecla para continuar'.upper())
    print('*' * 100)
    print('*' * 100)
    input('')
    # acessar empresa outorgante
    select = Select(driver.find_element(By.NAME, 'sltOpcao'))
    select.select_by_value('32|AcessarOutorgante.Verificar')
    # CNPJ da empresa ortorgante 11173347000152
    driver.find_element(By.NAME, 'txtCNPJ').send_keys(lista_dados['CNPJ'])
    # clique em continuar
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    # input('')
    # selecione 
    # solicitar extrato do trabalhador
    select = Select(driver.find_element(By.NAME, 'sltOpcao'))
    select.select_by_value('24|ExtratoFgts.AcessarBaseConta')
    # rs - rio grande do sul
    select = Select(driver.find_element(By.NAME, 'sltRegiao'))
    select.select_by_value('RSD')
    # colocar o pis 12814775709
    PIS = driver.find_element(By.NAME, 'txtNumPisPasep')
    PIS.send_keys(lista_dados['PIS'])
    # continuar
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    # visualizar impressao
    botao_visualizar = driver.find_element(By.XPATH, '//img[@src="/sicse/_images/botao_visualizar_impressao.gif"]')
    botao_visualizar.click()
    
    # imprimir -> EXTRATO.PDF
    janela_inicial = driver.current_window_handle
    # 3) quais abas estão abertas
    abas = driver.window_handles
    for aba in abas:
        print(aba)
        if aba not in janela_inicial:
            # alterar para essa nova aba
            driver.switch_to.window(aba)
            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
            pyautogui.press('enter')
            sleep(2)
            pyautogui.press('enter')
            sleep(2)
            pyautogui.typewrite('U:\TEMP_DP_RESCISOES\EXTRATO.pdf')
            sleep(2)
            pyautogui.press('enter')
            driver.close()
    driver.switch_to.window(janela_inicial)
    input('')
    
    
    

    # sleep(2)
    # pyautogui.hotkey('ctrl', 'p')
    # sleep(1)
    # sleep(2)
    
    # botao_imprimir = driver.find_element(By.XPATH, '//a[@href="javascript:impr_extrato_fgts_trabalhador_impressao();"]')
    # botao_imprimir.click()u:\temp_dp_rescisoes\extrato





    # voltar
    # selecione comunicação de dispensa
    # colocar o pis
    # data do desligamento
    # modalidade da rescisão
    # salvar documento na pasta "CHAVE DE MOVIMENTAÇAO"


if __name__ == '__main__':
    plan_dados = carregar_planilha()
    for dado in plan_dados:
        acessar_conectividade_social(dado)    
