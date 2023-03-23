from selenium.webdriver.common.keys import Keys
from time import sleep

from funcoes.geral import *

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 10)

for conta, senha in contas().items():
    # Faz o login
    login(conta, senha, driver, wait)

    # Após fazer o login, o programa vai ir para a página de recompensas
    driver.get('https://rewards.bing.com/')
    driver.set_page_load_timeout(15)

    # Realiza os 'quiz' disponíveis
    quiz(wait, driver, 'Supersonic quiz', 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 1, 2, 4, 6, 7)

    # Realiza o 'Daily poll'
    daily_poll(wait, driver, 'Daily poll')

    # Clica nos links diários
    links_clicaveis(wait, driver, "National Flower Day", "Do you know the answer?", "How's that horoscope looking?", "A poet and didn't know it?",
        "Sharpen your skills", "International Day of Forests"
    )

    # Limpa os dados do navegador
    limpar_dados(driver, conta)

driver.quit()
