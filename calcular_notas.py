#Crie um programa para calcular as notas obtidas pelo aluno do
#ensino médio, deverá mostrar mensagem para ser digitado a
#nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado,
#se está em recuperação ou foi reprovado sem chance de recuperação.
#Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Notas Escola!")

nota1 = float(input("Digite a nota do Primeiro Bimestre do aluno (0 à 25): "))
nota2 = float(input("Digite a nota do Segundo Bimestre do aluno (0 à 25): "))
nota3 = float(input("Digite a nota do Terceiro Bimestre do aluno (0 à 25): "))
nota4 = float(input("Digite a nota do Quarto Bimestre do aluno (0 à 25): "))

resultado = nota1 + nota2 + nota3 + nota4

print("A nota obtida pelo aluno durante o ano foi (0 à 100): ", resultado)

if (resultado >= 60):
    print ("O aluno está Aprovado!")
elif (resultado < 60 or resultado >= 40):
    print ("O aluno está de Recuperação!")
elif (resultado < 40):
    print ("O aluno está Reprovado!")