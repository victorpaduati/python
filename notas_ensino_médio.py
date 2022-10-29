#Crie um programa para calcular as notas obtidas pelo aluno do ensino médio,
#deverá mostrar mensagem para ser digitado a nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
#Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º bimestre
#E depois o total informado se o aluno foi aprovado,
#esta em recuperação ou foi reprovado sem recuperação.

print("Notas Ensino Médio!")

nota1p = float(input("Digite a nota da Primeira Prova: "))
nota1t = float(input("Digite a nota do Primeiro Trabalho: "))
resultado1b = nota1t + nota1t
print("A nota obtida pelo aluno no Primeiro Bimestre foi: ", resultado1b)

nota2p = float(input("Digite a nota da Segunda Prova: "))
nota2t = float(input("Digite a nota do Segundo Trabalho: "))
resultado2b = nota2t + nota2t
print("A nota obtida pelo aluno no Primeiro Bimestre foi: ", resultado2b)

nota3p = float(input("Digite a nota da Terceira Prova: "))
nota3t = float(input("Digite a nota do Terceiro Trabalho: "))
resultado3b = nota3t + nota3t
print("A nota obtida pelo aluno no Primeiro Bimestre foi: ", resultado3b)

nota4p = float(input("Digite a nota da Quarta Prova: "))
nota4t = float(input("Digite a nota do Quarto Trabalho: "))
resultado4b = nota4t + nota4t
print("A nota obtida pelo aluno no Primeiro Bimestre foi: ", resultado4b)

resultadofinal = resultado1b + resultado2b + resultado3b + resultado4b

print ( "O resultado final obtido pelo aluno foi: " , resultadofinal )

#CÓDIGO EM ANDAMENTO...
