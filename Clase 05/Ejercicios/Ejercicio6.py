"""Probar de acceder a una porción de la fila para la Matriz creada en el
Ejercicio 1."""
import numpy as np

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Matriz completa:\n", matriz)

porcion1 = matriz[0, 0:3]
print("Primera porción:", porcion1)

porcion2 = matriz[1, 0:2]
print("Segunda porción:", porcion2)
