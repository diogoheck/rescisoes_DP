import winreg
from OpenSSL import crypto
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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



def UpdateStringValue(strigValueName,newValueOfStrinValue, stringValuePath):
  key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, stringValuePath, 0, winreg.KEY_ALL_ACCESS)
  winreg.SetValueEx(key, strigValueName, 0, winreg.REG_SZ, newValueOfStrinValue)
  winreg.CloseKey(key)


def GetCertificate(pathOfCertificate, passwordOfCertifcate):
    pkcs12 = crypto.load_pkcs12(open(pathOfCertificate, 'rb').read(), passwordOfCertifcate)   
    return pkcs12.get_certificate()


def pesquisar_certificado(url_where_certificate_will_be_send):
    pathOfstringValue = 'SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls'
    stringValueName = '1'

    certificate = GetCertificate("LUCIANO MORO.pfx", '2406')
    subject = certificate.get_subject()
    issuer = certificate.get_issuer()
    # url_where_certificate_will_be_send = "https://conectividade.caixa.gov.br/"
    # url = 'https://conectividade.caixa.gov.br/'
    json = '{"pattern":"' + url_where_certificate_will_be_send + '","filter":{"ISSUER":{"CN":"' + issuer.CN + '","C":"' + issuer.C + '","O":"' + issuer.O + '"},"SUBJECT":{"CN":"' + subject.CN + '","C":"' + subject.C + '","O":"' + subject.O + '"}}}'
    UpdateStringValue(stringValueName, json, pathOfstringValue)
    # path = 'C:\\Users\\rodrigo.peres\Downloads\chromedriver_win32\\'
    

    # btn_certificate_login = driver.find_element_by_id('ctl00_cphCabMenu_imgLoginICP')
    # btn_certificate_login.click()
