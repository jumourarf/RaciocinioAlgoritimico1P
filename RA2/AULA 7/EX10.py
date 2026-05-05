dados = {'nome': 'Julia', 'idade': 21, 'cidade': "Curitiba"}
print("Dados iniciais: ", dados)

chave = input("Chave que deseja remover: ")
dados.pop(chave, "Chave não encontrada!")

dados.popitem()
print("Após remoções: ", dados)

nova_chave = input("Nova chave: ")
novo_valor = input("Novo valor: ")

dados.update({nova_chave: novo_valor})

print("Dados finais: ", dados)