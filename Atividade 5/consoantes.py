#Faça um Programa que leia em um vetor de 10 caracteres (letras)
#e diga quantas consoantes foram lidas.
#Mostre as consoantes.

print("Programa Contagem de Consoantes!")

vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    vetor[i] = input("Digite uma letra para cada posição: ")
print(vetor)

contador=0

for i in range(10):
    if not (vetor[i] == str("a") or vetor[i]=="e" or vetor[i]=="i" or vetor[i]=="o" or vetor[i]=="u"):
        print("consoante na posição " + str(i+1) + ": ", vetor[i])
        contador=contador+1

print("o número total de consoantes é", contador)

