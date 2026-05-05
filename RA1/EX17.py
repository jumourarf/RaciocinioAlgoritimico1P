contador = 0
while True:
    num = float(input("Digite um número: "))
    if num % 2 == 0:
        contador += 1

    if num < 0:
        print("O número de pares é: ", contador)
        break
