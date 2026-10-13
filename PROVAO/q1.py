contador = 0
while contador != 3:
    print("=== SISTEMA DE ACESSO ===")
    usuario = str(input("Digite o usuário: "))
    senha = str(input("Digite a senha: "))
    autoriz = str(input("Possui autorização especial? (S/N): ").capitalize())
    
    if (usuario == "admin" and senha == "monster123" or autoriz == "S"):
        print("Acesso liberado. \n Bem-vindo ao sistema!")
        break
    else:
        print("Acesso Negado. \n Tente Novamente")
        contador += 1
        continue
    