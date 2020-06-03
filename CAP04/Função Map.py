"""
Função built in - MAP

map(Função, Sequencia)

Aplica a função a cada elemento da sequencia, e retorna uma nova lista

"""

def quadrado_map(x):
    return x**2

lista_map = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

#Aplicando a função map
print(list(map(quadrado_map,lista_map)))
