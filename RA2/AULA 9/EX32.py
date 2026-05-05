lista = [1,2,3,4,5,6,7,8,9,10] #armazena os itens da lista
contador = 0 #inicia o contador
for num in lista: #percorre os itens da lista
    if num % 2 == 0: #verifica se o numero é par
        contador += 1 #incrementa o contador
print(contador) #printa o resultado do contador, ou seja, a quantidade de numeros pares na lista
