preco = {"preco 1": 139, "preco 2": 154,"preco 3": 89}
atualizacao = input("Qual preço deseja atualizar? ")
if atualizacao in preco:
    novo = input("Qual sera o novo valor? ")
    preco[atualizacao] = novo
print (preco)
