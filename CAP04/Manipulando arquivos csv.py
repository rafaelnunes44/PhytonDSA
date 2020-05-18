#****************** Manipulando arquivos .csv ******************

#Importando o módulo csv

import csv

#Escrita de arquivos csv
"""
with open('../Arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((10, 20, 30))
    writer.writerow((40, 50, 60))
"""

#Leitura de arquivos csv
"""
with open('../Arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for x in leitor:
        print('Número de colunas:', len(x))
        print(x)
"""

#Gerando uma lista com dados do arquivo csv
with open("../Arquivos/numeros.csv", 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)


#Imprimindo a partir da segunda linha

for linha in dados[1:]:
    print(linha)
