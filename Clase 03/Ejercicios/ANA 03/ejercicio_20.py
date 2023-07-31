#EJERCICIO 20
"""
Pidan el ingreso de un dato a por teclado indicando que es la parte real. Convierta a
a real (flotante). Pidan el ingreso de un dato b por teclado indicando que es la parte
imaginaria. Convierta b a real (flotante). Guarde en la variable complejo
completándola con los datos ingresados por teclado. Muestre por pantalla el
contenido de a, b y complejo. Muestra por pantalla los tipos de a, b y complejo.
"""

a = float(input("Ingrese la parte real: "))
b = float(input("Ingrese la parte imaginaria: "))

complejo = complex(a, b)

print("a =", a)
print("b =", b)
print("complejo =", complejo)

print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de complejo:", type(complejo))
