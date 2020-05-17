#Calculadora em Python

def soma() :
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digte o segundo número: "))
    result = num1 + num2
    print(result)

def subtracao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    result = num1 - num2
    print(result)

def multiplicacao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    result = num1 * num2
    print(result)

def divisao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    result = num1 / num2
    print(result)

print("********* Calculadora em Python *********  ")

print("Escola uma opção:")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão\n")

a = int(input("Qual operação deseja realizar? "))

if a == 1:
    soma()

elif a == 2:
    subtracao()

elif a == 3:
    multiplicacao()

elif a == 4:
    divisao()

else:
    print("Opção inválida!")
