#****************** Automatizando o processo de gravação ******************
"""
filename = input("Digite o nome do arquivo: ")
filename = filename + ".txt"

arq3 = open(filename, "w")
arq3.write("Incluindo texto no arquivo criado")
arq3.close()

arq3 = open(filename, "r")
print(arq3.read())
arq3.close()
"""

#****************** Abrindo um dataset em uma única linha ******************
"""
f = open("../Arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
print(rows)
"""

#****************** Dividindo o dataset em colunas ******************
"""
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    print(full_data)
"""
#****************** Contando as linhas de um arquivo ******************
"""
f = open("../Arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count= 0
for row in full_data:
    count += 1

print(count)
"""

#****************** Contando as colunas de um arquivo ******************

f = open("../Arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count= 0


for column in first_row:
    count += 1

print(count)