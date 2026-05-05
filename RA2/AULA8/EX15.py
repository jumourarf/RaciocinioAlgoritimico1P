def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Julia", idade = 21, cidade = "curitiba")