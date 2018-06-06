senha = "54321"
leitura = ()

while(leitura != senha):
    leitura = input("Digite a senha: ")
    if leitura == senha:
        print("Acesso liberado!")
    else:
        print("Senha incorreta. Tente novamente.")
