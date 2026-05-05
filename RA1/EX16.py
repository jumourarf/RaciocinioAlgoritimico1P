contador = 0
for i in range(10):
    num = int(input("Digite um numero: "))
    if num > 5:
        contador += 1
print(f"A quantidade de números maiores que 5 é: {contador}")
print("A quantidade de números maiores que 5 é: ", contador)