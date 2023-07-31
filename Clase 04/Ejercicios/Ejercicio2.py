"""Ejercicio 2"""
"""Pidan el ingreso de dos datos a por teclado.
Convierta los datos a flotantes.
Muestre por pantalla los datos ordenados de menor a mayor."""

print("Ingrese los datos:\n")
a=input("\nIngrese el primer numero, a:")
a=float(a)
b=input("\nIngrese el segundo numero, b:")
b=float(b)

if a<b:
    print(a,b)
else:
    print(b,a)