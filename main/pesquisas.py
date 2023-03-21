from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


def numeros_aleatorios(qtd):
    """Retorna uma lista com números aleatórios de CPFs."""
    numeros = []
    while len(numeros) < qtd:
        numeros.append('cpf ' + str(random.randint(10_000_000, 99_999_999)))  # Qualquer coisa para ser pesquisada no Bing
    return numeros


numeros = 2  # Quantidade de pesquisas a serem feitas no navegador de PC
numeros_cel = 2  # Quantidade de pesquisas a serem feitas no navegador de celular

# Dicionário com as contas de e-mail e suas respectivas senhas, quantas contas quiser
lista_contas = {
    'conta1@gmail.com': 'senha1',
    'conta2@gmail.com': 'senha2',
}

# Inicialização do navegador
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1000,1000")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # Instala o driver do Chrome
driver.set_window_position(0, 0)

wait = WebDriverWait(driver, 10)  # Tempo de espera máximo até carregar os elementos

# Loop para fazer as pesquisas no navegador de PC
for conta, senha in lista_contas.items():
    driver.get('https://www.bing.com/')
    apareceu_email = False  # Variável para verificar se o campo de colocar o e-mail já apareceu na tela
    while not apareceu_email:
        # Enquanto não aparecer o campo de colocar o e-mail, o programa vai tentar clicar no botão de fazer login do bing, é útil quando utiliza VPN
        try:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'id_s'))).click()
            except:
                pass
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]'))).send_keys(conta)
            apareceu_email = True  # Se o campo de colocar o e-mail apareceu, encerra o loop
        except:
            pass
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()

    conta_pessoal = False  # Variável para verificar se o campo de colocar a senha já apareceu na tela, se tiver uma conta pessoal e corporativa com o mesmo email, aparece uma
                           # tela para escolher qual conta quer usar, caso apareça essa tela, o programa vai clicar na conta pessoal, se não, vai direto para o campo de senha
    while not conta_pessoal:
        try:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
                break
            except:
                pass
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'msaTileTitle'))).click()
            conta_pessoal = True
        except:
            pass

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).send_keys(senha)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    sleep(1)

    # Aceita os cookies se aparecer para aceitar, se não, passa
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'bnp_btn_accept'))).click()
    except:
        pass

    wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).click()

    # Realiza as pesquisas
    for k, numero in enumerate(numeros_aleatorios(numeros)):
        if k == 10 or k == 20: # A cada 10 pesquisas, o navegador vai ser atualizado para evitar possíveis travamentos
            driver.refresh()
            sleep(2)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).clear()
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(numero)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(Keys.ENTER)
        sleep(.7)

    # Limpa todos os dados do navegador
    sleep(1)
    print(conta + ' - OK PC') # Printa o e-mail da conta que foi feito as pesquisas
    driver.get('chrome://settings/clearBrowserData')
    sleep(1)
    driver.find_element(By.XPATH, '//settings-ui').send_keys(Keys.TAB + Keys.ENTER)
    sleep(1)

driver.quit() # Fecha o navegador

# Inicialização do navegador de celular emulado
mobile_emulation = {"deviceName": "iPhone XR"}
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_window_rect(0, 0, 414, 830)

wait = WebDriverWait(driver, 10)

# Loop para fazer as pesquisas no navegador de celular
for conta, senha in lista_contas.items():
    # O navegador de celular tem um botão a mais a ser clicado para fazer login (os três tracinhos na navbar), então o programa vai tentar clicar nesse botão primeiro
    driver.get('https://www.bing.com/')
    apareceu_email = False
    while not apareceu_email:
        try:
            try:
                try:
                    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'mHamburger'))).click()
                except:
                    pass
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'hb_s'))).click()
            except:
                pass
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]'))).send_keys(conta)
            apareceu_email = True
        except:
            pass
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()

    conta_pessoal = False
    while not conta_pessoal:
        try:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
                break
            except:
                pass
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'msaTileTitle'))).click()
            conta_pessoal = True
        except:
            pass

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).send_keys(senha)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    sleep(1)

    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'bnp_btn_accept'))).click()
    except:
        pass

    wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).click()

    # faz a pesquisa de novo
    for k, numero in enumerate(numeros_aleatorios(numeros_cel)):
        if k == 10 or k == 20:
            driver.refresh()
            sleep(2)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).clear()
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(numero)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(Keys.ENTER)
        sleep(1)

    sleep(1)
    driver.get('chrome://settings/clearBrowserData')
    sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//settings-ui'))).send_keys(Keys.TAB + Keys.ENTER)
    sleep(2)
    print(conta + ' - OK CEL')

driver.quit()
