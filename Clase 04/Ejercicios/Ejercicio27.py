"""Ejercicio 27"""

"""Generar una lista l1 con los números del 1 al 10. Generar una lista l2 que
tenga una lista con los números del uno al 10 en cada uno de sus 10
elementos. Recorrer l2 con un for anidado dentro de otro for mostrando el
producto de ambas coordenadas."""

l1 = list(range(1, 11))

# Crear la lista l2 con una lista de los números del 1 al 10 en cada uno de sus 10 elementos
l2 = [[i for i in range(1, 11)] for j in range(10)]

# Recorrer l2 con un for anidado dentro de otro for mostrando el producto de ambas coordenadas
for i in range(10):
    for j in range(10):
        print(l1[i] * l2[i][j])

