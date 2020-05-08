#dict = {chave1: valor1, chave2: valor 2}

dict = {"Rafael": 36, "Jolise": 36, "Amora": 3}
print(dict)

print(dict["Rafael"])

#Adicionando argumento ao dicionário
dict["Pedro"] = 32
print(dict)

#Imprime o tamanho do dicionário
print("O tamanho do dicionário é {}".format(len(dict)))


#Deletando argumento do dicionário
del(dict["Pedro"])

print(dict)

#Imprime somente as chaves do dicionário
print("A chave dos dicionários são {}".format(dict.keys()))

#Imprime somente os valores dos dicionários
print("Os valores contido no dicionário é {}".format(dict.values()))

#Imprime os itens contidos no dicionário
print("Os itens contidos no dicionário são {}".format(dict.items()))



#Limpando dicionário
dict.clear()
print(dict)

