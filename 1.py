alg = int(input("Quanto tempo o carro ficou alugado? "))
km = float(input("Quantos Km foram rodados? "))

clc = (alg * 60)
clc1 = (km * 0.15)
tt = (clc + clc1)

print("-------------------------------------")
print("Valor gasto com diária do carro: ",clc)
print("Valor gasto com Km rodado: ",clc1)
print("Valor total a pagar: ",tt)