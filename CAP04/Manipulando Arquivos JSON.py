#****************** Manipulando arquivos JSON ******************
# Java Script Object Notation

#Criando um dicionário
"""

dict = {'nome': 'Guido Van Rossum', 'linguagem': 'Python', 'similar': ['c', 'Modula-3', 'lisp'], 'users': '100000'}

for k,v in dict.items():
 print(k,v)
"""


#Importando o módulo Json
import json

#Converte o dicionário para um objeto Json
#json.dumps(dict)

#Criando um arquivo Json
"""
with open('../Arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict))
"""

#Leitura de um arquivo Json
"""
with open('../Arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

    print(data)

    #Acessando um valor a partir da chave
    print(data['nome'])
"""
#Imprimindo um arquivo Json copiado da
"""
from urllib.request import  urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]

print('Título: ', data['title'])
print('URL: ', data['url'])
print('Duração: ', data['duration'])
print('Número de Visualizações: ', data['stats_number_of_plays'])
"""

#Copiando o conteúdo de um arquivo para outro
import os
arquivo_fonte = ('../Arquivos/dados.json')
arquivo_destino =('../Arquivos/json_data.txt')

#Metodo 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

#Leitura de arquivos Json
with open('../Arquivos/json_data.txt', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)