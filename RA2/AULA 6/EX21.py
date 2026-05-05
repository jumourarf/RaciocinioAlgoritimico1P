# Inicializa a matriz
matriz = []

# Leitura da matriz 3x4
for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Contador de números pares
pares = 0

# Percorre a matriz
for i in range(3):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares += 1

# Resultado
print(f"Quantidade de números pares: {pares}")