valor = int(input("Digite um valor: "))
if valor > 100:
    desconto = valor * 0.10
    total = valor - desconto
    print (total)
elif valor > 200:
    desconto1 = valor * 0.20
    total1 = valor - desconto1
    print (total1)
else:
    print(valor)
    print("Não há desconto!")
