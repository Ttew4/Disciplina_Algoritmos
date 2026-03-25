comp = float(input("Digite o valor da compra: "))
reg = str(input("Digite sua região (sul/sudeste/norte/nordeste/centro-oeste): "))
cup = str(input("Cupom? (s/n): "))
loj = str(input("Retirar na loja? (s/n): "))

if comp >= 220 or cup == "s" and loj == "n":
    print("Frete grátis")

elif loj == "s" and cup == "n":
    print("Venha buscar em nosso endereço! \n Rua... Nº... Cidade...")  
    
elif comp > 0 and reg == "sul" or reg == "sudeste" and cup == "n":
    print("Valor total do frete: R$10")
    
elif comp > 0 and reg == "norte" or reg == "nordeste" or reg == "centro-oeste" and cup == "n":
    print("Valor total do frete: R$20")
      
else:
    print("Erro")