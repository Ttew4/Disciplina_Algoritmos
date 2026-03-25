import random
print("Adivinhe o número!")

num = random.randint(1,10)
dig = int(input("Digite algum número de 1 a 10: "))

if dig < 1 or dig > 10 :
    print("Número inválido")
elif dig == num:
    print("Você acertou!")
elif dig != num:
    print("Número secreto:", num)
    print("Tente outra vez...")