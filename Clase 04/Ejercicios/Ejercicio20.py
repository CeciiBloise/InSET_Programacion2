"""Ejercicio 20"""
"""Crear una tupla con la siete primeras letras del alfabeto. Recorrer la tupla
y usarla como clave para imprimir los valores del diccionario construido
en el ejercicio 19."""

#Diccionario 
d = {'a': 'Lunes', 'b': 'Martes', 'c': 'Miércoles', 'd': 'Jueves', 'e': 'Viernes', 'f': 'Sábado', 'g': 'Domingo'}

tupla_letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

for letra in tupla_letras:
    print(d[letra])
