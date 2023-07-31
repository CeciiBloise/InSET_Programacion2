"""Ejercicio 1"""

"""Pidan el ingreso de dos datos a por teclado. Convierta los datos a flotantes.
Si el primer dato es mayor que el segundo muestre por pantalla el cartel: mayor."""

print("Ingese dos numeros:\n")
a=input("\nIngrese el primer numero, a: ")
b=input("\nIngrese el segundo numero, b: ")
a=float(a)
b=float(b)

if a>b:
    print("\nEl numero a es mayor que b")
else:
    print("\nEl numero a es menor que b")