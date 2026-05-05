acumulador = 0
while True:
    n = float(input("Digite algum numero (Se for 0 o programa irá parar): "))
    if n == 0:
        break
    elif n > 0 or n < 0:
        acumulador += n
print(acumulador)

