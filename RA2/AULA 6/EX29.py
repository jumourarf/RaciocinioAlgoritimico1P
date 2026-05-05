# Inicializa a matriz
matriz = []

# Leitura da matriz 5x5
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a diagonal secundária
print("\nElementos da diagonal secundária:")

for i in range(5):
    for j in range(5):
        if i + j == 4:  # condição da diagonal secundária
            print(matriz[i][j], end=" ")