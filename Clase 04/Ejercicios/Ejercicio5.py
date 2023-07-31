"""Ejercicio 5"""
"""Ingresar por teclado una edad. Mostrar por los años todos los cumpleaños
que la persona tuvo hasta ahora: Cumpleaños 1 Cumpleaños 2."""

print("Ingrese su edad\n")
edad=int(input("Edad: "))

def cumpleaños():
    for i in range(1, edad+1):
        print("Cumpleaños ",i)
        
cumpleaños()