# Inicializa a matriz
matriz = []

# Leitura da matriz 4x4
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Soma da diagonal principal
soma = 0

for i in range(4):
    soma += matriz[i][i]

# Resultado
print(f"Soma da diagonal principal: {soma}")