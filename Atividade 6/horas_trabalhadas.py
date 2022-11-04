#Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do seu
#salário no referido mês, sabendo-se que são descontados 11% para o
#Imposto de Renda, 8% para o INSS e 5% para o sindicato, mostre
#todos os descontos, mostre o salário bruto e o líquido.

valor = float(input("Digite o valor de horas trabalhadas: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))

salarioBruto = valor + horas
inss = salarioBruto + 0.08
ir = salarioBruto + 0.11
sindicato = salarioBruto + 0.05

salarioLiquido = salarioBruto - inss - ir - sindicato

print("Salário Bruto: ", round(salarioBruto, 2))
print ("Desconto INSS: ", round (inss, 2) )