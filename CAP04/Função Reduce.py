"""
Função built in - Reduce

reduce(Função, Sequencia)

Aplica a função aos elementos da sequencia até que reste 1 elemento.

"""
from functools import reduce

def soma(a,b):
    x = a + b
    return x

lista_reduce = [10, 20, 30, 40, 50, 60, 70, 80, 90 , 100]

print(reduce(soma, lista_reduce))
