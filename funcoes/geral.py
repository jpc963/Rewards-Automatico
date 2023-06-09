from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from webdriver_manager.chrome import ChromeDriverManager


def contas(conta=0):
    """Retorna um dicionário com as contas de e-mail e suas respectivas senhas."""

    lista_contas = {
        'conta1@gmail.com': 'senha1',
        'conta2@gmail.com': 'senha2',
    }

    if conta == 1:
        lista_contas = {k: v for k, v in lista_contas.items() if k in list(lista_contas.keys())[:6]}

    if conta == 2:
        lista_contas = {k: v for k, v in lista_contas.items() if k in list(lista_contas.keys())[6:]}

    return lista_contas


def numeros_aleatorios(qtd):
    """Retorna uma lista com números aleatórios de CPFs.

    Parâmetros:
    qtd: Quantidade de números aleatórios

    Exemplo:
    numeros_aleatorios(10)
    """

    numeros = []
    while len(numeros) < qtd:
        numeros.append('cpf ' + str(random.randint(10_000_000, 99_999_999)))
    return numeros


def links_clicaveis(wait, driver, *partial_link_text):
    """Clica nos links disponíveis na página de recompensas do Bing.

    Parâmetros:
    partial_link_text: Nome do link

    Exemplo:
    links_clicaveis("National Flower Day", "A poet and didn't know it?", ...)
    """

    for link in partial_link_text:
        tem_link = True
        try:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link))).click()
        except:
            tem_link = False
            pass
        if tem_link:
            sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(1)
        elif not tem_link:
            pass


def quiz(wait, driver, partial_link_text, *answer):
    """Responde os 'quiz' disponíveis na página de recompensas do Rewards.

    Parâmetros:
    partial_link_text: Nome do quiz
    answer: Número inteiro que representa a resposta do quiz, um número para cada pergunta

    Exemplos:
    quiz('Supersonic quiz', 3,4,5,6,7, 2,3,4,5,6, 1,2,4,6,7, ...)
    quiz('Supersonic quiz', 3, 4, 5, 6)
    """

    tem_quiz = True
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, partial_link_text))).click()
    sleep(7)
    driver.switch_to.window(driver.window_handles[1])
    try:
        wait.until(EC.element_to_be_clickable((By.ID, 'rqStartQuiz'))).click()
    except:
        tem_quiz = False
        pass
    if tem_quiz:
        sleep(2)
        for i in answer:
            try:
                wait.until(EC.element_to_be_clickable((By.ID, 'rqAnswerOption' + str(i)))).click()
                sleep(2)
            except:
                pass
    sleep(4)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(1)


def quiz_2(wait, driver, partial_link_text, qtd_perguntas):
    """Responde os 'quiz' disponíveis na página de recompensas do Rewards. Essa função serve para o quiz que não tem o botão 'Start quiz' e é feito direto na página do bing.

    Parâmetros:
    partial_link_text: Nome do quiz
    qtd_perguntas: Quantidade de perguntas do quiz

    Exemplo:
    quiz_2('Supersonic quiz', 15)
    """

    tem_quiz = True
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, partial_link_text))).click()
    sleep(7)
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.visibility_of_element_located((By.ID, 'ListOfQuestionAndAnswerPanes')))
    sleep(2)
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, f'ChoiceText_0_0')))
    except:
        tem_quiz = False
        pass
    if tem_quiz:
        for i in range(0, qtd_perguntas):
            try:
                wait.until(EC.element_to_be_clickable((By.ID, f'ChoiceText_{i}_0'))).click()
                sleep(2)
                wait.until(EC.element_to_be_clickable((By.ID, f'nextQuestionbtn{i}'))).click()
                sleep(2)
            except:
                pass
    sleep(4)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(1)


def daily_poll(wait, driver, partial_link_text):
    """Responde a enquete diária disponível na página de recompensas do Rewards.

    Parâmetros:
    partial_link_text: Nome da enquete

    Exemplo:
    daily_poll('Daily Poll')
    """

    deu_certo = False
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, partial_link_text))).click()
    sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    resposta = random.choice(['btoption0', 'btoption1'])
    sleep(1)
    while not deu_certo:
        try:
            wait.until(EC.element_to_be_clickable((By.ID, resposta))).click()
            deu_certo = True
        except:
            pass
    sleep(4)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)


def login(conta, senha, driver, wait):
    """Faz o login na conta do Rewards.

    Parâmetro:
    conta: Conta do Rewards
    senha: Senha da conta do Rewards
    """

    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com')
    driver.set_page_load_timeout(10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]'))).send_keys(conta)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()

    while True:
        try:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
                break
            except:
                pass
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'msaTileTitle'))).click()
            break
        except:
            pass

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).send_keys(senha)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    sleep(1)

    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'bnp_btn_accept'))).click()
    except:
        pass


def pesquisas_pc(numeros, driver, wait):
    """Realiza pesquisas no Bing Rewards no computador.

    Parâmetros:
    numeros: Quantidade de pesquisas que serão realizadas

    Exemplo:
    pesquisas_pc(30)
    """

    wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).click()

    for k, numero in enumerate(numeros_aleatorios(numeros)):
        if k == 10 or k == 20:
            driver.refresh()
            sleep(2)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).clear()
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(numero)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(Keys.ENTER)
        sleep(.7)


def pesquisas_cel(numeros_cel, driver, wait):
    """Realiza pesquisas no celular.

    Parâmetros:
    numeros_cel: Quantidade de pesquisas que serão realizadas

    Exemplo:
    pesquisas_cel(30)
    """

    wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).click()

    for k, numero in enumerate(numeros_aleatorios(numeros_cel)):
        if k == 10 or k == 20:
            driver.refresh()
            sleep(2)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).clear()
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(numero)
        wait.until(EC.element_to_be_clickable((By.ID, 'sb_form_q'))).send_keys(Keys.ENTER)
        sleep(.7)


def limpar_dados(driver, conta):
    """Limpa os dados do navegador"""

    sleep(1)
    print(conta + ' - OK')
    driver.get('chrome://settings/clearBrowserData')
    sleep(1)
    driver.find_element(By.XPATH, '//settings-ui').send_keys(Keys.TAB + Keys.ENTER)
    sleep(1)
