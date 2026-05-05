import numpy as np
#Dimensoes
linhas = 2
colunas = 4

#inicializando a matriz vazia
matriz = []

#preenchendo com entrada do usuario
for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = float(input(f"Digite o elemento para a posicao ({i}, {j}): "))
        linha.append(elemento)
    matriz.append(linha)

#Convertendo a lista de listas em matriz NumPy
matriz_np = np.array(matriz)
print(matriz_np)
