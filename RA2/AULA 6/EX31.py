# Leitura da ordem da matriz
n = int(input("Digite a ordem da matriz (n): "))

# Leitura da matriz
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Criando a matriz rotacionada
rotacionada = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    rotacionada.append(linha)

# Rotação 90 graus horário
for i in range(n):
    for j in range(n):
        rotacionada[j][n - 1 - i] = matriz[i][j]

# Exibindo resultados
print("\nMatriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz rotacionada (90° horário):")
for linha in rotacionada:
    print(linha)