"""
Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione
2 elementos a lista e imprima a lista.

"""


def novaLista(lista):
    print(lista.append(5))
    print(lista.append(6))


lista1 = [1, 2, 3, 4]
novaLista(lista1)
print(lista1)