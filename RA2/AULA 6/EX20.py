# Inicializa a matriz vazia
matriz = []

# Leitura da matriz 3x3
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Leitura do número real
numero = float(input("Digite um número real para multiplicar a matriz: "))

# Multiplicação e exibição da nova matriz
print("\nMatriz resultante:")
for i in range(3):
    for j in range(3):
        resultado = matriz[i][j] * numero
        print(f"{resultado:.2f}", end=" ")
    print()