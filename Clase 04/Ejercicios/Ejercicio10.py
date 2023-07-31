"""Ejercicio 10"""
"""Crear una lista l1 con todos los días de la semana. Crear una lista l2 con
los días hábiles de la semana. Recorrer l1 e indicar para cada elemento
si se encuentra o no en l2."""

l1=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
l2=['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

dias_comunes=[]
dias_unicos=[]

for dias in l1:
    if dias in l2:
        dias_comunes.append(dias)
    else:
        dias_unicos.append(dias)
        
print("Los siguinetes dias estan en lista l2: \n", dias_comunes)
print("Y estos dias no estan en la lista l1: \n", dias_unicos)