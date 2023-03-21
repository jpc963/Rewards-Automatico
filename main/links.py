from selenium.webdriver.common.keys import Keys
from time import sleep

from funcoes.geral import *

for conta, senha in contas().items():
    # Faz o login
    login(conta, senha)

    # Após fazer o login, o programa vai ir para a página de recompensas e realizar os 'quiz' disponíveis, depois clicará nos links diários
    driver.get('https://rewards.bing.com/')
    sleep(6)

    # Realiza os 'quiz' disponíveis
    quiz('Supersonic quiz', 3,4,5,6,7, 2,3,4,5,6, 1,2,4,6,7)

    # Realiza o 'Daily poll'
    daily_poll('Daily poll')

    # Clica nos links diários
    links_clicaveis("National Flower Day", "Do you know the answer?", "How's that horoscope looking?", "A poet and didn't know it?",
    "Sharpen your skills", "International Day of Forests")

    # Limpa os dados do navegador
    driver.get('chrome://settings/clearBrowserData')
    sleep(2)
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.TAB + Keys.ENTER)
    sleep(2)
    print(conta + ' - OK')

driver.quit()
