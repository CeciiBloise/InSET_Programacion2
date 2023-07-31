"""Ejercicio 3"""
"""Ingresar por teclado una edad. Devolver por pantalla un mensaje
proporcionado a la edad: Menor a 15: edad de crecer De 15 a 40: edad
del amor De 40 a 65: edad de los amigos De 65 en adelante: edad de los
médicos."""

print("Ingrese su edad:\n")
edad=input("Edad:")
edad=int(edad)

if edad < 0:
    print("La edad ingresada es incorrecta. Debe ser un numero positivo")
elif edad in range(0,15):
    print("\nEdad de crecer")
elif edad in range(15,40):
    print("\nEdad del amor")
elif edad in range(40,65):
    print("\nEdad de los amigos")
else:
    print("edad de medicos")