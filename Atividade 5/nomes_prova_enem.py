#Crie um programa que leia um conjunto de nomes de 20 estudantes
#inscritos na prova do ENEM. Com esses nomes, realizar uma
#ordenação crescente usando uma função para facilitar a localização
#do nome na lista que será afixada no quadro de avisos da escola.

def ordenacao(vetor):
    for i in range(len(vetor)):
        for j in range(i+1,len(vetor)):
            if vetor [i] > vetor[j]:
                x = vetor[i]
                vetor [i] = vetor [j]
                vetor [j] = x

    return vetor

vetor = []
for i in range (20):
    vetor.append(input("Digite um nome do aluno do Enem: ").capitalize())

vetorOrdenacao = ordenacao(vetor)
print(vetorOrdenacao)