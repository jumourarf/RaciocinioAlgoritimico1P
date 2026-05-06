lista = [1,15,-3,6,22,-4,0,-7,9]
lista2 = [] #cria uma nova lista vazia para armazenar os números positivos
for num in lista:
  if num >= 0:
    lista2.append(num) #adiciona os números positivos da lista original à nova lista
print(lista2) #printa a nova lista com os números positivos