ano = int(input("Digite seu ano de nascimento: "))
atual = 2026
idade = (2026 - ano)

if (idade >=16):
    print("Pode votar já")
elif (idade < 4):
    print("você é um bebê?")
else:
    print("Não pode votar mano")