"""Sustituir la fila 0 de la matriz creada en el Ejercicio 1 por los valores (10,
20, 30, 40)"""
import numpy as np

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("Matriz original:")
print(matriz)

# Reemplazo la primera fila con los valores (10, 20, 30, 40)
matriz[0] = [10, 20, 30, 40]

print("Matriz actualizada:")
print(matriz)
