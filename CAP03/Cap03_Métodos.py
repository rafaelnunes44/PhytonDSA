#Métodos

#Criando uma lista
"""
lista = [10, 20, 30, 40, 50, 30, 30, 80, 90]
"""


#Método append, do objeto lista
"""
lista.append(60)

#Imprime lista
print(lista)

#Método count
print(lista.count(30))
"""

#A função dir() mostra todos os métodos e atributos de um objeto
"""
lista1 = [10, 50, 30]
print(dir(lista1))
"""

#A função help() explica como utilizar cada metodo do obeto
"""
help(lista.count)
"""

#O método de um objeto pode ser chamado dentro de uma função, com print()
a = "Isso é uma string"
print(a.split()) #split executa divisão por espaços
