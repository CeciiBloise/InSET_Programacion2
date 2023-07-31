#EJERCICIO 19
"""
Pidan el ingreso de un dato a por teclado. Guarde en b el valor de a convertido en
real (flotante). Guarde en c el valor de a convertido a string. Muestre por pantalla el
contenido de a, b y c Muestra por pantalla los tipos de a, b y c
"""
print("Ingrese los datos:\n")
a = input("Ingrese un valor: ")

# Convierto a en flotante 
b = float(a)

# Convierto a en string
c = str(a)

# Imprimo por pantalla
print("a:", a)
print("b:", b)
print("c:", c)

# Imprimo por pantalla los tipos de a, b y c
print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de c:", type(c))
