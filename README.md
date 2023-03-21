# Rewards Automatico

## O que é este projeto?

Este projeto é um script que automatiza as atividades diárias do programa Rewards da Microsoft. O script é feito em Python e utiliza a biblioteca Selenium para automatizar
o processo de pesquisas, responder o quiz diário e clicar nos links que geram pontos.

## Como usar?

1. Baixe o arquivo [Rewards-Automatico]
2. Instale a última versão do [Python]
3. Instale as bibliotecas necessárias com o comando `pip install -r requirements.txt`
4. Execute o script com o comando `python pesquisas.py` ou `python links.py`

## Como funciona o script?

### Pesquisas

1. O script abre o navegador Chrome
2. Abre o site do Bing
3. Realiza o login no site do Bing
4. Faz as pesquisas diárias
5. Limpa os dados do navegador
6. Repete o processo para cada conta registrada no script
7. Fecha o navegador

### Links

1. O script abre o navegador Chrome
2. Abre o site do Bing
3. Realiza o login no site do Bing
4. Abre o site do Rewards
5. Responde o quiz diário
6. Clica nos links que geram pontos
7. Limpa os dados do navegador
8. Repete o processo para cada conta registrada no script
9. Fecha o navegador
