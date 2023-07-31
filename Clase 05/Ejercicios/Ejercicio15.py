"""Crear una nueva matriz de 2X2 y luego convertir la matriz en un vector
utilizando la función flatten()."""
import numpy as np

matriz = np.array([[1, 2], [3, 4]])

#Convierto la matriz en un vector utilizando la función flatten()
vector = matriz.flatten()

print("Matriz original:\n", matriz)
print("Vector resultante:\n", vector)
