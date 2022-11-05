#Faça um programa para imprimir igual abaixo:
# 1
# 2 2
# 3 3 3
# n n n n
# "n" para um "numero" (range) informado pelo usuario.
# Use uma função que receba um valor n inteiro e imprima até a "n-linha" informado pelo usuário.

numero = int(input("Digite um número inteiro 1 - 10 para exibir for alinhado: "))

for i in range(numero):
    for j in range(i+1):
        print(i+1, end= " ")
    print("")






















