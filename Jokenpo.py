import random

jogador = str(input(" Jokenpo! \n Escolha entre, Pedra, Papel ou Tesoura: ").capitalize())
opcoes = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(opcoes)

a = "Você venceu! \n"
b = "Empate! \n"
c = "Você perdeu! \n"

if jogador == "Pedra" and pc == "Papel" :
    print(a, jogador, "Ganha de", pc)
    
elif jogador == "Tesoura" and pc == "Papel" :
    print(a, jogador, "Ganha de", pc)

elif jogador == "Pedra" and pc == "Tesoura" :
    print(c, jogador, "Ganhou de", pc)
    
elif jogador == "Papel" and pc == "Pedra" :
    print(a, jogador, "Ganha de", pc)


elif jogador == "Pedra" and pc == "Pedra" :
    print(b, jogador, "E", pc)
    
elif jogador == "Tesoura" and pc == "Tesoura" :
    print(b, jogador, "E", pc)
    
elif jogador == "Papel" and pc == "Papel" :
    print(b, jogador, "E", pc)
    
    
elif jogador == "Papel" and pc == "Pedra" :
    print(c, pc, "Ganhou de", jogador)
    
elif jogador == "Papel" and pc == "Tesoura" :
    print(c, pc, "Ganhou de", jogador)

elif jogador == "Tesoura" and pc == "Pedra" :
    print(c, pc, "Ganhou de", jogador)
    
elif jogador == "Pedra" and pc == "Papel" :
    print(c, pc, "Ganhou de", jogador)




