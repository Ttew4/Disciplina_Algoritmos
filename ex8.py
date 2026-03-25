preço = int(input("Digite o preço do item desejado: "))
forma = str(input("Digite a forma de pagamento: "))

av = "a vista"
tr = "3x"
ms = "mais de 3x"

desconto = preço * 0.12
juros = preço * 0.15

print (av)

if(forma == av):
    print(preço - desconto)

elif(forma == tr):
    print(preço / 3)

elif(forma == ms):
    print(preço + juros)
    