#Crie um programa com uma função para multiplicar dois números
# e o algoritmo mostrar o resultado.

print("Algoritmo para Multiplicação")

nx = float(input("Digite os números a serem multiplicados: "))
ny = float(input("* "))

def multiplica(n1,n2):
    resultado=n1*n2
    return print("O resultado da multiplicação é: ",resultado)

multiplica(nx,ny)