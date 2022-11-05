#A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um programa
#para coletar quantos habitantes tem na cidade e os dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:
#Média de salário da população
#Média do número de filhos
#Maior salário dos habitantes
#Percentual de pessoas com salário menor que R$ 1200,00

print("Pesquisa Prefeitura!")

filhos = 0
contador_pessoas = 0
contador_pessoas_1200 = 0
salario = 0
media_salario = 0
media_filhos = 0
porcentagem_salario = 0
maior_salario = 0
a = 'SIM'
while a == 'SIM':
    if salario >= 0:
        salario = float(input("Digite o seu salário: "))
        media_salario = media_salario + salario
        contador_pessoas += 1

        if (salario < 1200):
            contador_pessoas_1200 += 1
            porcentagem_salario = (contador_pessoas_1200 * 100) / contador_pessoas

        if (salario > maior_salario):
            maior_salario = salario
        filhos = int(input("Digite o número de filhos: "))
        media_filhos = media_filhos + filhos
    a = input("Você deseja continuar? (Sim) Caso errou e deseja alterar o salário ou N° de Filhos - (Não) Para ver os resultados da média da população. ")
    a = a.upper()
    if a != 'SIM':
        break

print(f"A média do salário da população é R$ {media_salario / contador_pessoas}")
print(f"A média do número de filhos da população é: {media_filhos / contador_pessoas}")
print(f"O maior salário é R$ {maior_salario}")
print(f"A porcentagem de pessoas com salário de até R$1.200 é: {porcentagem_salario}%")