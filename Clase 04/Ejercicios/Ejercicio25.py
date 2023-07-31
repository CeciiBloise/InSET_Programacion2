"""Ejercicio 25"""
"""Crear una tupla con los siete días de la semana. Recorrer los 365 días del
año 2023. Para cada día del año imprimir el nombre del día de la semana."""

dias_semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado','Domingo')

# Recorrer los días del año 2023 e imprimir el día de la semana correspondiente
for dia in range(1, 366):
    dia_semana = dias_semana[(dia + 5) % 7]  # Sumar 5 días para ajustar el calendario a partir del 1 de enero de 2023
    print(f"El día {dia} de 2023 es un {dia_semana}.")
