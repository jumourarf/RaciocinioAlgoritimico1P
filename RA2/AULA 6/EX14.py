# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Soma todos os elementos com while e for
soma = 0
linha = 0

while linha < 3:
    for coluna in range(3):
        soma = soma + matriz[linha][coluna]
    linha = linha + 1

# Exibe o resultado
if soma > 0:
    print("A soma dos elementos é:", soma)
else:
    print("A soma é zero ou negativa:", soma)