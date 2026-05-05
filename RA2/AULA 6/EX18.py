# Criação da matriz 4x4 (pode ser fixa ou preenchida pelo usuário)
matriz = [
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
]

# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Variável de controle
encontrado = False

# Percorre a matriz
for i in range(4):
    for j in range(4):
        if matriz[i][j] == numero:
            encontrado = True

# Resultado
if encontrado:
    print("O número está na matriz!")
else:
    print("O número NÃO está na matriz.")