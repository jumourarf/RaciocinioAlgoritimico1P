# Inicializa a matriz
matriz = []

# Leitura da matriz 3x3
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Cálculo da média de cada linha
for i in range(3):
    soma = 0
    for j in range(3):
        soma += matriz[i][j]

    media = soma / 3
    print(f"Média da linha {i}: {media:.2f}")