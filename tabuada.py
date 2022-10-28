#Crie um programa para realizar as operações de uma tabuada de
#multiplicação,onde será solicitado ao usuário digitar qual
#numero será a tabuada e qual intervalo do inicio e fim da tabuada,
#e exibir na tela o resultado conforme intervalo.
#REPETIÇÃO USANDO "PARA"

print("Tabuada do número desejado!")

tabuada = int(input("Digite o número da tabuada:"))
inicio = int(input("Digite o início do intervalo da tabuada: "))
fim = int(input("Digite o fim do intervalo da tabuada: "))

for i in range(fim +1):
    print("Tabuada do número ", tabuada, " resultado ", tabuada, " * ", i, "= ", tabuada + inicio)
    #print("Tabuada resultado: ", tabuada + inicio)
    inicio = inicio + 1










































print("PROGRAMA TABUADA MULTIPLICAÇÃO")
numero = int(input("Qual número você deseja saber a tabuada? "))
inicio = int(input("Digite o início do intervalo da tabuada: "))
fim = int(input("Digite o fim do intervalo da tabuada: "))

print("Tabuada de", numero, "de", inicio, "até", fim)
for i in range(inicio,fim):
    print(numero, '*', 1 , "=", (numero*(1)))