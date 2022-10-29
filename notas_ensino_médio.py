#Crie um programa para calcular as notas obtidas pelo aluno do ensino médio,
#deverá mostrar mensagem para ser digitado a nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
#Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º bimestre
#E depois o total informado se o aluno foi aprovado,
#esta em recuperação ou foi reprovado sem recuperação.

print("Notas Escola!")

nota1 = float(input("Digite a nota do Primeiro Bimestre do aluno (0 à 25): "))
nota2 = float(input("Digite a nota do Segundo Bimestre do aluno (0 à 25): "))
nota3 = float(input("Digite a nota do Terceiro Bimestre do aluno (0 à 25): "))
nota4 = float(input("Digite a nota do Quarto Bimestre do aluno (0 à 25): "))

resultado = nota1 + nota2 + nota3 + nota4

print("A nota obtida pelo aluno durante o ano foi (0 à 100): ", resultado)

if (resultado >= 60):
    print ("O aluno está Aprovado!")
elif (resultado < 40):
    print("O aluno está Reprovado!")
elif (resultado < 60 or resultado >= 40):
    print ("O aluno está de Recuperação!")
