print("=== CONTROLE DE ESTACIONAMENTO ===")
estacionamento = 0
vagas = 4
while True:
    esc = int(input(" 1- Registrar entrada de veículo. \n 2- Registrar saída de veículo. \n 3- Exibir vagas ocupadas e disponíveis. \n 4- Encerrar programa. \n Escolha uma opção: "))
    if esc == 1:
        if estacionamento < 4 and estacionamento >= 0:
            estacionamento += 1
            print("Entrada registrada com sucesso.")
            vagas -=1
        else:
            print("Estacionamento cheio")

    elif esc == 2:
        if estacionamento <= 4 and estacionamento >= 1:
            estacionamento -= 1
            print("Saída registrada com sucesso.")
            vagas +=1
        else:
            print("Estacionamento vazio")

    elif esc == 3:
        print("Vagas ocupadas: ", estacionamento)
        print("Vagas disponíveis: ", vagas)
   
    elif esc == 4:
        print("Você escolheu sair.")
        break
