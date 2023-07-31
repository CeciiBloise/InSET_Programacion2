"""Ejercicio 12"""
"""Crear una lista l1 con todos los días de la semana Imprimir la longitud de
l1. Extender l1 con si misma Imprimir la longitud de l1."""

l1=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

# Imprimir la longitud de l1
print("Longitud de la lista original:", len(l1))

# Extender l1 con si misma
l1.extend(l1)

# Imprimir la longitud de l1
print("Longitud de la lista extendida:", len(l1))
