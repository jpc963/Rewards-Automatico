from funcoes.geral import *

numeros = 30  # Quantidade de pesquisas a serem feitas no navegador de PC
numeros_cel = 20  # Quantidade de pesquisas a serem feitas no navegador de celular


def pc():
    """Faz as pesquisas no navegador de PC"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    wait = WebDriverWait(driver, 10)

    for conta, senha in contas().items():
        # Faz o login
        login(conta, senha, driver, wait)

        # Faz as pesquisas no navegador de PC
        pesquisas_pc(numeros, driver, wait)

        # Limpa os dados do navegador
        limpar_dados(driver, conta)

    driver.quit()  # Fecha o navegador


def cel():
    """Faz as pesquisas no navegador de celular"""

    mobile_emulation = {"deviceName": "iPhone XR"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    wait = WebDriverWait(driver, 10)

    for conta, senha in contas().items():
        login(conta, senha, driver, wait)

        pesquisas_cel(numeros_cel, driver, wait)

        limpar_dados(driver, conta)

    driver.quit()


# Executa as funções
pc()
cel()
