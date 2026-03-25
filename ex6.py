notas1 = float(input("Digite sua primeira nota: "))
notas2 = float(input("Digite sua segunda nota: "))
notas3 = float(input("Digite sua terceira nota: "))
notas4 = float(input("Digite sua quarta nota: "))

media = (notas1 + notas2 + notas3 + notas4) / 4

if (media >= 7):
    print("A média requisitada é 7" "\n" "Você está aprovado")
else:
    print("A média requisitada é 7" "\n" "Você está reprovado")
