"""
Função Zip
"""

"""
#Criando duas listas
x = [1, 2, 3]
y = [4, 5, 6]

#Unindo as listas.Em Python retornar iterator
zip(x, y)

#Perceba que o zip retorna tuplas.Neste caso, uma lista de tuplas
print(list(zip(x, y)))
"""

#Criando 2 dicionários
d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

#Zip vai unir as chaves
#print(list(zip(d1, d2)))

print(list(zip(d1, d2.values())))
