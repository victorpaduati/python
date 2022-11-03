#Crie um programa com uma função para multiplicar dois números
# e o algoritmo mostrar o resultado.

def multiplica(n1, n2):
    result = n1 * n2
    return result

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("O resultado da multiplicação é: ", multiplica(n1, n2))
