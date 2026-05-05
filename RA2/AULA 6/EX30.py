# Leitura das dimensões da matriz A
linhas_A = int(input("Digite o número de linhas da matriz A: "))
colunas_A = int(input("Digite o número de colunas da matriz A: "))

# Leitura da matriz A
A = []
for i in range(linhas_A):
    linha = []
    for j in range(colunas_A):
        valor = int(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

# Leitura das dimensões da matriz B
linhas_B = int(input("\nDigite o número de linhas da matriz B: "))
colunas_B = int(input("Digite o número de colunas da matriz B: "))

# Verificação da possibilidade de multiplicação
if colunas_A != linhas_B:
    print("Não é possível multiplicar as matrizes!")
else:
    # Leitura da matriz B
    B = []
    for i in range(linhas_B):
        linha = []
        for j in range(colunas_B):
            valor = int(input(f"B[{i}][{j}]: "))
            linha.append(valor)
        B.append(linha)

    # Inicializa matriz resultado (linhas_A x colunas_B)
    resultado = []
    for i in range(linhas_A):
        linha = []
        for j in range(colunas_B):
            linha.append(0)
        resultado.append(linha)

    # Multiplicação das matrizes
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    # Exibindo o resultado
    print("\nMatriz resultado (A x B):")
    for linha in resultado:
        print(linha)