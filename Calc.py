a = 0
while a == 0:
    print("=== Calculadora ==")
    print(" 1 - Soma \n 2- Subtração \n 3 - Divisão \n 4- Multiplicação \n 0 - Sair \n ---------------")
    i = int(input())
    
    if i > 4 or i < 0:
        print("Opção inválida")
        continue
        
    if i == 0:
        print("Você escolheu sair.")
        break

    else:
        v1 = float(input("Digite o primeiro número: "))
        v2 = float(input("Digite o segundo número: "))

        if i == 1:
            soma = v1 + v2
            print("O valor da soma é: ", soma)
        if i == 2:
            sub = v1 - v2
            print("O valor da subtração é: ", sub)
        if i == 3:
            div = v1 / v2
            print("O valor da divisão é: ", div)
        if i == 4:
            mlt = v1 * v2
            print("O valor da multiplicação é: ", mlt)