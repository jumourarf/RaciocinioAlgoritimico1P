login = str(input("Digite seu login: "))
login_correto = "jumourarf"
senha = int(input("Digite sua senha: "))
senha_correta = 1234
if login == login_correto and senha == senha_correta:
    print("Acesso liberado!")
else:
    print ("Acesso negado!")