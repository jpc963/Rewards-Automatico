from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1000,1000")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 10)


def contas(conta=0):
    """Retorna um dicionário com as contas de e-mail e suas respectivas senhas."""

    lista_contas = {
        'conta1@gmail.com': 'senha1',
        'conta2@gmail.com': 'senha2',
    }

    # Caso queira dividir as contas em dois navegadores é só criar outro arquivo igual ao 'links.py' e colocar no parâmetro 'conta' um dos números abaixo
    if conta == 1:
        lista_contas = {k: v for k, v in lista_contas.items() if k in list(lista_contas.keys())[:6]}  # Pega as 6 primeiras contas do dicionário
        driver.set_window_position(0, 0)

    if conta == 2:
        lista_contas = {k: v for k, v in lista_contas.items() if k in list(lista_contas.keys())[6:]}  # Pega a partir da 6° conta do dicionário
        driver.set_window_position(1000, 0)

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
        numeros.append('cpf ' + str(random.randint(10_000_000, 99_999_999)))  # Qualquer coisa para ser pesquisada no Bing
    return numeros


def links_clicaveis(*partial_link_text):
    """Clica nos links disponíveis na página de recompensas do Bing.

    Parâmetros:
    partial_link_text: Nome do link

    Exemplo:
    links_clicaveis("National Flower Day", "A poet and didn't know it?", ...)
    """

    for link in partial_link_text:
        tem_link = True  # Variável para verificar se o link existe
        try:  # Tenta clicar no link, se não existir, passa para o próximo
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link))).click()
        except:
            tem_link = False
            pass
        if tem_link:  # Se o link existir, ele será aberto em uma nova aba e fechado após 3 segundos
            sleep(3)
            driver.switch_to.window(driver.window_handles[1])  # Muda para a nova aba
            driver.close()
            driver.switch_to.window(driver.window_handles[0])  # Muda para a aba principal
            sleep(1)
        elif not tem_link:
            pass


def quiz(partial_link_text, *answer):
    """Responde os 'quiz' disponíveis na página de recompensas do Rewards.

    Parâmetros:
    partial_link_text: Nome do quiz
    answer: Número inteiro que representa a resposta do quiz, um número para cada pergunta

    Exemplos:
    quiz('Supersonic quiz', 3,4,5,6,7, 2,3,4,5,6, 1,2,4,6,7, ...)
    quiz('Supersonic quiz', 3, 4, 5, 6)
    """

    tem_quiz = True  # Variável para verificar se o quiz existe e pode ser respondido
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, partial_link_text))).click()  # Clica no link do quiz
    sleep(7)
    driver.switch_to.window(driver.window_handles[1])
    try:
        wait.until(EC.element_to_be_clickable((By.ID, 'rqStartQuiz'))).click()  # Clica no botão 'Start quiz'
    except:  # Se não existir o botão 'Start quiz', significa que o quiz já foi respondido, então passa para o próximo
        tem_quiz = False
        pass
    if tem_quiz:  # Se o quiz existir, ele será respondido
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


def quiz_2(partial_link_text, qtd_perguntas):
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
    wait.until(EC.visibility_of_element_located((By.ID, 'ListOfQuestionAndAnswerPanes')))  # Espera o elemento que contém o quiz ficar visível
    sleep(2)
    try:  # Tenta responder a primeira pergunta do quiz, se não existir, passa para o próximo
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, f'ChoiceText_0_0')))
    except:
        tem_quiz = False
        pass
    if tem_quiz:  # Se o quiz existir, ele será respondido
        for i in range(0, qtd_perguntas):  # O número de perguntas do quiz é passado como parâmetro
            try:
                wait.until(EC.element_to_be_clickable((By.ID, f'ChoiceText_{i}_0'))).click()  # Clica na primeira opção de resposta para cada pergunta
                sleep(2)
                wait.until(EC.element_to_be_clickable((By.ID, f'nextQuestionbtn{i}'))).click()  # Clica no botão que vai para a próxima pergunta
                sleep(2)
            except:
                pass
    sleep(4)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(1)


def daily_poll(partial_link_text):
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
    resposta = random.choice(['btoption0', 'btoption1'])  # Escolhe aleatoriamente uma das opções de resposta
    sleep(1)
    while not deu_certo:  # Tenta clicar na opção de resposta, se não conseguir, tenta novamente
        try:
            wait.until(EC.element_to_be_clickable((By.ID, resposta))).click()
            deu_certo = True  # Se conseguir clicar, a variável deu_certo será True e o loop será interrompido
        except:
            pass
    sleep(4)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)


def login(conta, senha):
    """Faz o login na conta do Rewards.

    Parâmetros:
    conta: Email da conta do Rewards
    senha: Senha da conta do Rewards
    """

    driver.get('https://www.bing.com/')
    apareceu_email = False  # Variável para verificar se o campo de email apareceu
    while not apareceu_email:
        try:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'id_s'))).click()  # Clica no botão 'Sign in' enquanto o campo de email não aparecer
            except:
                pass
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]'))).send_keys(conta)  # Caso o campo de email apareça, ele será preenchido
            apareceu_email = True  # Se o campo de email aparecer, a variável apareceu_email será True e o loop será interrompido
        except:
            pass
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()

    conta_pessoal = False  # Variável para verificar se o botão 'Conta pessoal' apareceu
    while not conta_pessoal:
        try:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))
                ).clear()  # Caso o campo de senha apareça, o loop será interrompido e o campo será limpo
                break
            except:
                pass
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'msaTileTitle'))
            ).click()  # Caso o botão 'Conta pessoal' apareça, ele será clicado e o loop será interrompido
            conta_pessoal = True
        except:
            pass

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).clear()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]'))).send_keys(senha)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    sleep(1)

    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'bnp_btn_accept'))).click()  # Caso o botão 'Aceitar' apareça, ele será clicado
    except:
        pass
