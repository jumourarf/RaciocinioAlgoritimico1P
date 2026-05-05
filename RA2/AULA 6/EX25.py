# Leitura das dimensões
m = int(input("Digite o número de linhas (M): "))
n = int(input("Digite o número de colunas (N): "))

# Leitura da matriz MxN
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Gerando a matriz transposta (NxM)
transposta = []
for j in range(n):
    nova_linha = []
    for i in range(m):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

# Exibindo a matriz original
print("\nMatriz original:")
for linha in matriz:
    print(linha)

# Exibindo a matriz transposta
print("\nMatriz transposta:")
for linha in transposta:
    print(linha)