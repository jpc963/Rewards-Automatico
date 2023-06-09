from selenium.webdriver.common.keys import Keys
from time import sleep

from funcoes.geral import *

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 10)

for conta, senha in contas().items():
    login(conta, senha, driver, wait)

    driver.get('https://rewards.bing.com/')
    driver.set_page_load_timeout(15)

    quiz(wait, driver, 'Supersonic quiz', 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 1, 2, 4, 6, 7)

    daily_poll(wait, driver, 'Daily poll')

    links_clicaveis(wait, driver, "National Flower Day", "Do you know the answer?", "How's that horoscope looking?", "A poet and didn't know it?",
        "Sharpen your skills", "International Day of Forests")

    limpar_dados(driver, conta)

driver.quit()
