dicionario = {'nome': 'Julia', 'idade': 21, 'cidade': "Curitiba"}
print("Deseja apagar todos os dados do dicionario?")
resp = input("Resposta: ")
if resp == "Sim":
    dicionario.clear()
print(dicionario)
