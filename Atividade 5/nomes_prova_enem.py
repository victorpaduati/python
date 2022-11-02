#Crie um programa que leia um conjunto de nomes de 20 estudantes
#inscritos na prova do ENEM. Com esses nomes, realizar uma
#ordenação crescente usando uma função para facilitar a localização
#do nome na lista que será afixada no quadro de avisos da escola.

print("Programa Nomes Inscritos no ENEM!")

lista_nomes= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(20):
    lista_nomes[i]=str(input("digite o nome do aluno: "))

sorted(str(lista_nomes))

print(sorted(lista_nomes))