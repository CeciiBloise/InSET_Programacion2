""" Obtener el número Mínimo de la matriz creada en el ejercicio 1 """
import numpy as np

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(matriz)

num_minimo = matriz.min()

print("El número mínimo de la matriz es:", num_minimo)