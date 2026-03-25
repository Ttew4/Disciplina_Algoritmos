idd = int(input("Digite a sua idade: "))
aut = str(input("Tem autorização? (s/n): "))

if idd >= 18 or aut == "s":
          print("Entrada permitida")
else:
          print("Entrada negada")