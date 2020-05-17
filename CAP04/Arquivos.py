# ********************* Arquivos *********************

# Abrindo arquivo para leitura
arq1 = open("../Arquivos/arquivo1.txt", "r")

#Lendo o arquivo
print(arq1.read())

#Contar o número de caracteres
print(arq1.tell())

#Retornar para o inicio do arquivo
print(arq1.seek(0.0))

#Ler os primeiros 10 caracteres do arquivo
print(arq1.read(10))

#************************** GRAVANDO ARQUIVOS **************************

#Abrindo arquivo para gravação
arq2 = open("../Arquivos/arquivo1.txt", "w")

#Gravando arquivo
arq2.write("Testando gravação de arquivos em Python")

#Fechando arquivo
arq2.close()

#Abrindo arquivo gravado
arq2 = open("../Arquivos/arquivo1.txt", "r")

print(arq2.read())

#Acrescentando conteúdo -  (modo append)
arq2 = open("../Arquivos/arquivo1.txt", "a")
arq2.write("\nAcrescentando conteúdo")
arq2.close()

#Abrindo arquivo gravado
arq2 = open("../Arquivos/arquivo1.txt", "r")
print(arq2.read())


#Retornando ao ínicio do arquivo para leitura
arq2.seek(0.0)
print(arq2.read())