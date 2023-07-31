"""Ejercicio 29"""
"""Construya un generador que vaya recorriendo la sucesión aritmética: 1,
2, 3, 4, 5 ... Imprima por pantalla los 10 primeros valores."""

def sucesion_aritmetica():
    n = 1
    while True:
        yield n
        n += 1

s = sucesion_aritmetica()
for i in range(10):
    print(next(s))
