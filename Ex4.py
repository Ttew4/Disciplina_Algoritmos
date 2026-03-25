userd = str(input("Digite seu usuário: "))
passw = str(input("Digite sua senha: "))

if userd == "admin" and passw == "123":
    print("Acesso total")
elif userd == "professor" and passw == "123":
    print("Acesso intermediário")
elif userd == "aluno" and passw == "123":
    print("Acesso básico")
else:
    print("Acesso Negado")