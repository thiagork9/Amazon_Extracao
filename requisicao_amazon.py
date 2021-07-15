#abrir o site da Amazon, pesquisar por  iphone, pegar os resultados da primeira página (nome e preço) e criar uma planilha Excel com esses dados. 

from selenium import webdriver
import requests
from bs4 import BeautifulSoup


navegador = webdriver.Chrome()
#abertura do navegador
navegador.get('https://www.amazon.com.br/')
#entrando no input e digitando
elemento = navegador.find_element_by_id('twotabsearchtextbox')
elemento.send_keys('iphone')
elemento.submit()

#url após a pesquisa
url = 'https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser').get_text()
numero_paginas = 1

#interando os preços dos iphones

site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
produtos = soup.find_all('div', class_='s-expand-height s-include-content-margin s-latency-cf-section {{ borderCssClass }}')

#criando csv
with open('precos_iphones.csv', 'a', newline='',encoding='UTF-8') as f:
    #for criado para tratar o preço se existe ou não
    for produto in produtos:
        nome_iphone = produto.find('span', class_='a-size-base-plus a-color-base a-text-normal').get_text()
        #se o preço existir
        try:
            preco = produto.find('span', class_='a-offscreen').get_text()
        #senao existir, preço = 0 
        except:
            preco = '0'
        #inserindo nas linhas    
        linha = nome_iphone + ';' + preco + '\n'
        f.write(linha)

print("Busca e geração finalizadas")       

navegador.close()

