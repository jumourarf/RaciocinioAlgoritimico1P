inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o ultimo número: "))
soma = 0
for i in range(inicio, fim+1):
  soma += i
  print("A soma é: ", soma)