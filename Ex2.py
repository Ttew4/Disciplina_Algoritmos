rnd = int(input("Digite sua renda: "))
nm = str(input("Seu nome está limpo? (s/n):"))
         
if rnd >= 3500 and nm == "s":
    print("Crédito aprovado!")
elif rnd >=2500 and rnd < 3500 and nm == "s":
    print("Crédito parcialmente aprovado")
else:
    print("Crédito negado")