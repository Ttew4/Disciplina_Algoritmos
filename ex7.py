idd = int(input("Digite sua idade: "))
atual = 2026
idade = (2026 - idd)

if(idd >= 18 and idd < 21):
    print("Você pode fazer a carteira de motorista AB")
elif(idd > 21):
     print("Você pode fazer a carteira motorista AB e D")
else:
    print("Você não tem idade suficiente.")

