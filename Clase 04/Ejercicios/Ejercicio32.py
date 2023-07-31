"""Ejercicio 32"""
"""Construya un generador que vaya recorriendo la suma de la serie
geométrica: 1, 3, 7, 15, 31, 63, 127 Imprima por pantalla los 10 primeros
valores."""
def suma_serie_geometrica():
    base = 1
    suma = 0
    while True:
        suma += base
        yield suma
        base = 2 * base + 1

s = suma_serie_geometrica()
for i in range(10):
    print(next(s))

