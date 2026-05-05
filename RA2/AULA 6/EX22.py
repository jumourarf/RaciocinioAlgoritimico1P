# Definindo tamanho da matriz (3x3)
linhas = 3
colunas = 3

matriz = []

# Leitura da matriz
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a matriz
print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

# Encontrando o maior valor
maior = matriz[0][0]

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

# Resultado
print(f"\nMaior valor da matriz: {maior}")