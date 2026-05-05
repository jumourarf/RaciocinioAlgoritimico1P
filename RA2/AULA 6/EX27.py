# Leitura da ordem da matriz
n = int(input("Digite a ordem da matriz (n): "))

# Leitura da matriz nxn
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Verificação de simetria
simetrica = True

for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False

# Resultado
if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz NÃO é simétrica.")