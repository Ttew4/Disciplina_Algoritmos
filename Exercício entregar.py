sal = int(input("Digite seu salário: ")) #reajuste de acordo com salario
tempo = float(input("Digite seu tempo de serviço (anos): ")) # bonus de acordo com tempo
#Reajuste salarial

if sal > 500 and sal < 1000:
    calc = sal + (sal * 0.25)
    print("Reajuste =", calc)
    
elif sal > 1000 * 0.20 and sal < 1500:
    calc = sal + (sal * 0.20)
    print("Salário =", calc)

elif sal > 1500 * 0.15 and sal < 2000:
    calc = sal + (sal * 0.15)
    print("Salário =", calc)
    
elif sal > 2000 * 0.10 and sal < 3000:
    calc = sal + (sal * 0.10)
    print("Salário =", calc)

#bonus tempo
    
if tempo > 0 and tempo < 1:
    print("Sem bônus")

elif tempo >= 1 and tempo <= 3:
    print("Bônus de R$100,00")
    
elif tempo >= 4 and tempo <= 6:
    print("Bônus de R$200,00")
    
elif tempo >= 7 and tempo <= 10:
    print("Bônus de R$300,00")
    
elif tempo >= 10:
    print("R$500 de bônus")
    
else:
    print("Erro")