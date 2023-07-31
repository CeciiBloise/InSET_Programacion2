"""Ejercicio 26"""
"""Crear una tupla con las longitudes de los meses del año 2023. Recorrer
el año mostrando por pantalla el número de día dentro del año y el número
del día dentro del mes."""

# Tupla con las longitudes de los meses del año 2023
longitudes_meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# Contadores 
dia_anio = 1
dia_mes = 1

# Recorrer el año 2023 e imprimir el número de día dentro del año y el número de día dentro del mes correspondiente
for mes, longitud in enumerate(longitudes_meses, start=1):
    for dia in range(1, longitud+1):
        print(f"Día {dia_anio}: {dia} de {mes}")
        dia_mes += 1
        dia_anio += 1

print("Fin del año 2023.")
