contador = 0
while True:
    num = float(input("Digite um número: "))
    if num < 0:
        contador += 1
        print(f"Quantidade de numeros negativos: {contador}")
