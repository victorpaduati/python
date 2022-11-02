#Crie um programa para calcular as notas obtidas pelo aluno do ensino médio,
#deverá mostrar mensagem para ser digitado a nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
#Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º bimestre
#E depois o total informado se o aluno foi aprovado,
#esta em recuperação ou foi reprovado sem recuperação.

print("Programa para calcular notas bimestrais!")

p1 = float(input("Digite a nota da prova no Primeiro Bimestre: "))
p2 = float(input("Digite a nota da prova no Segundo Bimestre): "))
p3 = float(input("Digite a nota da prova no Terceiro Bimestre: "))
p4 = float(input("Digite a nota da prova no Quarto Bimestre: "))

t1 = float(input("Digite a nota do trabalho no Primeiro Bimestre: "))
t2 = float(input("Digite a nota do trabalho no Segundo Bimestre: "))
t3 = float(input("Digite a nota do trabalho no Terceiro Bimestre: "))
t4 = float(input("Digite a nota do trabalho no Quarto Bimestre: "))

b1 = (p1+t1)/2
b2 = (p2+t2)/2
b3 = (p3+t3)/2
b4 = (p4+t4)/2

print("A nota do Primeiro Bimestre é:", b1)
print("A nota do Segundo Bimestre é:", b2)
print("A nota do Terceiro Bimestre é:", b3)
print("A nota do Quarto Bimestre é:", b4)

resultado = b1 + b2 + b3 + b4
print ("O resultado final do aluno foi: ", resultado)

if (resultado >= 60 and resultado <= 100):
    print ("O aluno está Aprovado!")
elif (resultado >= 40 and resultado < 60):
    print("O aluno está em Recuperação!")
elif (resultado < 40 and resultado >= 0):
    print ("O aluno está Reprovado!")
else:
    print("Confirme os valores digitados, valor inválido!")