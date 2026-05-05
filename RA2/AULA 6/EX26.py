# Inicializa a matriz
matriz = []

# Leitura da matriz 3x3
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Lista para armazenar a soma de cada coluna
soma_colunas = []

# Cálculo das somas das colunas
for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    soma_colunas.append(soma)

# Exibindo resultados
print("\nMatriz:")
for linha in matriz:
    print(linha)

print("\nSoma de cada coluna:")
print(soma_colunas)