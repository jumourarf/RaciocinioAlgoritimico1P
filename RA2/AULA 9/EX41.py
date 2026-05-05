lista = [1,2,3,4,5,2,7,8,9]
target = 2
contador = 0
for num in lista:
  if num == target:
    contador += 1
print(f"O número {target} aparecem {contador} vezes na lista.") 