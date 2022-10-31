#Crie um programa para calcular as notas obtidas pelo aluno do
#ensino médio, deverá mostrar mensagem para ser digitado a
#nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado,
#se está em recuperação ou foi reprovado sem chance de recuperação.
#Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Programa para calcular notas bimestrais!")

b1 = float(input("Digite a nota do Primeiro Bimestre do aluno (0 à 25): "))
b2 = float(input("Digite a nota do Segundo Bimestre do aluno (0 à 25): "))
b3 = float(input("Digite a nota do Terceiro Bimestre do aluno (0 à 25): "))
b4 = float(input("Digite a nota do Quarto Bimestre do aluno (0 à 25): "))

resultado = b1 + b2 + b3 + b4

print("A nota obtida pelo aluno durante o ano foi (0 à 100): ", resultado)

if (resultado >= 60 and resultado <= 100):
    print ("O aluno está Aprovado!")
elif (resultado >= 40 and resultado < 60):
    print("O aluno está em Recuperação!")
elif (resultado < 40 and resultado >= 0):
    print ("O aluno está Reprovado!")
else:
    print("Confirme os valores digitados, valor inválido!")

