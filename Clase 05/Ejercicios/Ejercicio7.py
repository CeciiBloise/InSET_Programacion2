"""Probar de acceder a una porción de la columna para la matriz creada en
el Ejercicio 1."""
import numpy as np

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Matriz original:")
print(matriz)

columna = matriz[0:2, 1]
print("Porción de la segunda columna:")
print(columna)
