"""Ejercicio 31"""
"""Construya un generador que vaya recorriendo la serie geométrica: 1, 2, 4,
8, 16, 32, 64 ... Imprima por pantalla los 10 primeros valores."""

def sucesion_geometrica():
    base = 1
    while True:
        yield base
        base *= 2

s = sucesion_geometrica()
for i in range(10):
    print(next(s))
