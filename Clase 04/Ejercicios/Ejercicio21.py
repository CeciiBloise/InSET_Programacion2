"""Ejercicio 21"""
"""Tomar el diccionario generado en el ejercicio 19 y cambiar cada valor
letras mayúsculas. Imprimir el resultado."""
#Diccionario 
d = {'a': 'Lunes', 'b': 'Martes', 'c': 'Miércoles', 'd': 'Jueves', 'e': 'Viernes', 'f': 'Sábado', 'g': 'Domingo'}

for key in d.keys():
    d[key] = d[key].upper()

print(d)