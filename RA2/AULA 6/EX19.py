# Criação da matriz 2x2
matriz = [
    [1, 2],
    [3, 4]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

# Troca das linhas
for j in range(2):
    temp = matriz[0][j]
    matriz[0][j] = matriz[1][j]
    matriz[1][j] = temp

print("\nMatriz após trocar as linhas:")
for linha in matriz:
    print(linha)