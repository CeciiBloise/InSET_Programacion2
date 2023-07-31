"""Crear 2 matrices y realizar la multiplicación entre ambas"""
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

import numpy as np

#Realizo la multliplicacion
matriz_resultado = np.dot(matriz1, matriz2)

print(matriz_resultado)