client = str(input("Digite seu nome: "))
item =  str(input("Digite o nome do produto: "))
valor = float(input("Digite o valor do produto: "))
parc = float(input("Em quantas parcelas pretende pagar: "))

valorParcela = valor / parc

print("Cliente:",client,"Produto:",item,"Valor:",valor,"Parcela",parc,"Valor por parcela:",valorParcela)