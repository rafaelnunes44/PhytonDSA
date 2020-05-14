"""
Funções: Formato geral

def nome da função(arg1, arg2):
"""

#Definindo uma função
"""
def primeiraFunc():
    print("Hello World")

#Chamando a função
primeiraFunc()
"""

#Definindo uma função com parâmetro
"""
def primeiraFunc(nome):
    print("Hello {}".format(nome))
    
#Chamando a função
primeiraFunc("Rafael")
"""

#Definindo uma função com Loop For
"""
def funcLeitura():
    for i in range(0, 5):
        print("Número "+ str(i))

#Chamando a função
funcLeitura()
"""

#Função para somar número
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: "+ str(secondnum))
    print("Soma: ", firstnum + secondnum)

#Chamando a função
addNum(10, 60)


