"""
São imutáveis , ou seja não permite que os dados sejam alterados.

Tuplas não suportam append() - tupla1.append("Chocolate")
Tuplas não suportam delete de um item  - del tupla1("Chocolate")

"""

tupla1 = ("Geografia", 23, "Elefantes")
print(tupla1)

#Retorna um único elemento da Tupla
print(tupla1[0])

#Verifica o comprimento da tupla
print(len(tupla1))

#Imprime o indice do elemente
print(tupla1.index("Elefantes"))

#Deleta toda tupla, isso sim é possível
#del tupla1
#print(tupla1)

#Convertendo tupla para lista
lista_t2 =list(tupla1)
print(lista_t2)

#Adiciona item
lista_t2.append("Chocolate")
print(lista_t2)

#Converte a lista novamente para uma tupla
tupla1 = lista_t2
print(tupla1)


