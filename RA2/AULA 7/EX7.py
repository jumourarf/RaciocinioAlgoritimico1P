nomes = input("Digite 3 nomes (separados por virgula): ").split(",")
dicionario = dict.fromkeys(nomes, 10)
print(dicionario)