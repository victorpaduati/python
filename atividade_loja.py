# Crie um programa receba 5 produtos em variáveis constantes, iPhone, Samsung, Tablet, PS5, notebook , com valores respectivos de R$ 2980, R$ 2540, R$ 1950, R$ 2100, R$ 2350.
# O usuário deverá informar a quantidade de cada produto que ele deseja comprar em sua loja, caso não queira nenhum produto deverá informar o valor 0 (zero) de quantidade.
# OBS: Preferência não usar estrutura condicional

print("Programa venda de produtos")
iPhone = 2980
samsumg = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

print("O valor do iPhone é R$: ", iPhone)
totalIphone = iPhone + float((input("Deseja comprar quantos? ")))
print("O valor do Samsumg é R$: ", samsumg)
totalSamsumg = samsumg + float((input("Deseja comprar quantos? ")))
print("O valor do Tablet é R$: ", tablet)
totalTablet = tablet + float((input("Deseja comprar quantos? ")))
print("O valor do PS5 é R$: ", ps5)
totalPs5 = ps5 + float((input("Deseja comprar quantos? ")))
print("O valor do notebook é R$: ", notebook)
totalNotebook = notebook + float((input("Deseja comprar quantos? ")))
totalgeral = totalIphone + totalSamsumg + totalTablet + totalPs5 + totalNotebook
# Ao final da compra mostre o valor total de todos os produtos.
print("Valor total da venda dos produtos: R$", totalgeral)
# O valor da parcela dividido em 3X sem juros.
print("Valor da parcela dividido em 3x sem juros: R$", totalgeral/3)
# O valor da parcela dividido em 6X com acréscimo de 5%.
print("Valor da parcela divido em 6x com juros de 5%: R$", (((totalgeral/100)*5)+totalgeral)/6)
# E um valor com 10% de desconto para pagamento à vista.
print("O valor com desconto de 10% à vista: R$", (totalgeral-(totalgeral/100)*10))











