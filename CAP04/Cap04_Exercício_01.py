# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

#Solução 1
list1 = [3,4,5]
quadrado = [item**3 for item in list1]
print(quadrado)

#Solução 2
def ter_pot(x):
    return x**3

lst = [2, 4, 6]

print(list(map(ter_pot,lst)))
