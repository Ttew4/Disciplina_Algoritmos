aluguel = int(input("Digite a quantidade de dias da viagem: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))

clcdias = (aluguel * 220)
clc1 = (km * 0.85)
tt = (clcdias + clc1)
kmdia = (km / aluguel) 

print("=== RESUMO DA VIAGEM DE TRAILER ===")
print("Valor das diárias: R$",clcdias)
print("Valor pelos quilômetros percorridos: R$",clc1)
print("Total a pagar: R$",tt)
print("Média de km por dia: ",kmdia,"km")