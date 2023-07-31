"""Ejercicio 8"""
"""Crear una lista con los días de la semana. Eliminar de la lista el sábado y
el domingo. Mostrar el contenido de la lista con un único print."""

lista_dias=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

"""Utilizo remover() para eliminar un elemento de la lista"""
lista_dias.remove('Sabado')
lista_dias.remove('Domingo')

print(lista_dias)