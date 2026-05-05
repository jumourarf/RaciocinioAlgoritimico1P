lista = [1,2,3,4,5,6,7,8,9,10] 
lista2 = []
for num in lista:
  if num % 2 != 0:
    lista2.append(num) 
print(sum(lista2)) #percorre a lista original, verifica se cada número é ímpar e, se for, adiciona à nova lista e printa a soma dos números ímpares encontrados até o momento.