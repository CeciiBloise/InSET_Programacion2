"""Ejercicio 11"""
"""Crear una lista l1 con todos los impares de 1 a 5. Insertar los pares en los
lugares correspondientes para que la lista quede ordenada Imprimir l1"""

impares=[1,3,5]
pares=[2,4]

lista=list(zip(impares,pares))

lista = [numero for tupla in lista for numero in tupla] #la tupla se utiliza como una estructura temporal para combinar los elementos de las listas

print(lista)
