
#Loops Alinhados
"""
for i in range (0,5):
    for a in range (0,5):
        print(a)
"""

#Operando os valores de uma lista com loop for
"""
ListaB = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
soma = 0

for i in ListaB:
    double_i = i * 1
    soma += double_i

print(soma)
"""

#Loops em lista de listas
"""
listas = [1,2,3], [10,15,14], [10.1,8.7,2.3]
for valor in listas:
    print(valor)
"""

#Contando os itens de uma lista
"""
listas1 = [1, 4, 5, 6, 7, 8, 8, 9, 4, 3]
count = 0

for item in listas1:
    count += 1
    print(count)
    
"""

#Contando o numero de colunas
"""
lista3 = [1, 2, 3, 4, 5, 6], [1, 5, 6], [7, 8, 9]

primeira_linha = lista3[0]
count = 0

for column in primeira_linha:
    count = count + 1

print(count)
"""

#Pesquisando em listas
""""
listaC = [5, 6, 7, 10, 50]

#Loop através da lista
for item in listaC:
     if item == 5:
         print("Numero encontrado na lista")
"""

#Listando as chaves de um dicionario
"""
dict = {'k1':"Python", 'k2':"R", 'k3':"Scala" }

for item in dict:
    print(item)
"""
#Imprimindo chave e valor do dicionário. Usando o metodo items () para retornar
#os itens de um dicionário

dict = {'k1':"Python", 'k2':"R", 'k3':"Scala" }
for k,v in dict.items():
    print(k,v)



