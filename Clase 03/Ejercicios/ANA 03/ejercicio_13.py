#EJERCICIO 13
"""
Pidan el ingreso de dos datos a y b por teclado. Convierta a y b a enteros usando la
función int. Muestren por pantalla el contenido de a<=b.
"""

print("Ingese los datos:\n")
a=input("Ingrese un numero para a: ")
b=input("Ingrese un numero para b: ")

a=int(a)
b=int(b)

print("a es menor o igual que b?: ", a<=b)