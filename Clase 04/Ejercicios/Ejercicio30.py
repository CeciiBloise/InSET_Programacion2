"""Ejercicio 30"""
"""Construya un generador que vaya recorriendo la serie que va sumando la
sucesión aritmética: 1, 2, 3, 6, 10, 15, 21 ... Imprima por pantalla los 10
primeros valores"""

def sucesion_suma_aritmetica():
    n = 1
    suma = 0
    while True:
        yield suma
        suma += n
        n += 1

s = sucesion_suma_aritmetica()
for i in range(10):
    print(next(s))
