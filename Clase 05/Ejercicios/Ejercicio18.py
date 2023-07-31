"""Crear dos matrices y realizar la suma entre ambas"""
"""Crear dos matrices y realizar la suma entre ambas."""
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matriz_resultado = []

for i in range(len(matriz1)):
    fila = []
    for j in range(len(matriz1[0])):
        fila.append(matriz1[i][j] + matriz2[i][j])
    matriz_resultado.append(fila)


for fila in matriz_resultado:
    print(fila)
