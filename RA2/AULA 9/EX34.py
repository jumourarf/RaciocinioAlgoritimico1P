lista = [1,2,3,4,5,6,7,8,9,10] #armazena os itens da lista
num = int(input("Digite um número: ")) #solicita ao usuário que digite um número e armazena na variável num
if num in lista:
  print("O número está na lista.") #verifica se o número digitado pelo usuário está na lista e printa a mensagem correspondente
else:
  print("O número não está na lista.") #printa a mensagem caso o número digitado pelo usuário não esteja na lista
