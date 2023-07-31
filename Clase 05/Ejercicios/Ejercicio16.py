""" Para la matriz creada en el Ejercicio 15 obtener su traspuesta"""
import numpy as np

matriz = np.array([[1, 2], [3, 4]])

#Convierto la matriz en un vector utilizando la función flatten()
vector = matriz.flatten()

#Obtengo la traspuesta de la matriz utilizando la función transpose()
matriz_traspuesta = matriz.transpose()

print("Matriz original:\n", matriz)
print("Vector resultante:\n", vector)
print("Matriz traspuesta:\n", matriz_traspuesta)
