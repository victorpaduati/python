#Crie um programa que receba um numero digitado pelo usuário, que será comparado se o numero digitado é maior que 10, igual a 10 ou menor que 10.

print("Programa adivinha número inteiro")
num1 = int(input("Digite um número inteiro: "))
#não será tratado erro de digitação de usuário
if num1 > 10:
    print("O número " + str(num1) + " digitado é maior que o número secreto!")
elif num1 < 10:
    print("O número ", num1, " digitado é menor que o número secreto!")
else:
    print(num1, "Acertou o número secreto!")