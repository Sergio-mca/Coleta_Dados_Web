import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/cientifico/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir o texto
# print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
     titulo = linha_texto.text.strip()
     print('titulo: ', titulo)

...
# Desafio
# Filtrar tags ('h2', 'p')
# Contar quantas h2 e p no documento
...

# Contar a qtd de titulos e paragrafos
contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.nome == 'h2':
        contar_titulos += 1  # conta os titulos sempre somando 1
    elif linha_texto.nome == 'p':
        contar_paragrafos += 1
print('total de titulos', contar_titulos)
print('total de paragrafos', contar_paragrafos)
