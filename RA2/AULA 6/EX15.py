# Solicita o valor de n
n = int(input("Digite o valor de n: "))

# Inicializa a matriz vazia
matriz = []

i = 0
while i < n:
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
    i += 1

# Exibe a matriz identidade
print("Matriz Identidade:")
for linha in matriz:
    print(linha)