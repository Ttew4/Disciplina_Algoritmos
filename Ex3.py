nt1 = float(input("Digite sua primeira nota: "))
nt2 = float(input("Digite sua segunda nota: "))
prc = int(input("Digite sua frequência (%): "))
md = (nt1 + nt2) / 2
print("Média =", md)

if prc < 75:
    print("Você está reprovado")
elif prc > 75 and md >= 7:
    print("Você está aprovado!")
elif prc > 75 and md >= 3 and md < 7:
    print("Você está de exame")
elif prc > 75 and md < 3:
    print("Você está reprovado")
else:
    print("Erro")