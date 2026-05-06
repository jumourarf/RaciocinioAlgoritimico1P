lista = []
while True:
  nome = input("Digite um nome: ")
  if nome == "fim":
    break
  lista.append(nome) #adiciona o nome digitado à lista
print(lista) #printa a lista com os nomes digitados pelo usuário, exceto "fim" que é a palavra de parada para o loop.