#ejercicio 18
"""
Pidan el ingreso de cuatro datos a,b,c y d por teclado. Convierta a, b, c y d a enteros
usando la función int. Muestren por pantalla el contenido de a==b OR NOT c==d.
"""

print("Ingese los datos:\n")
a=input("Ingrese un numero para a: ")
b=input("Ingrese un numero para b: ")
c=input("Ingrese un numero para c: ")
d=input("Ingrese un numero para d: ")

a=int(a)
b=int(b)
c=int(c)
d=int(d)

print(a==b or not c==d)