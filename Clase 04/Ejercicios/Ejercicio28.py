"""Ejercicio 28"""
"""Generar para cada provincia una tupla con el nombre de la provincia, su
capital, su población y su PBI. Armar un diccionario donde cada valor sea
la tupla de una provincia y la clave sea el nombre de la provincia. Mostrar
para cada provincia su PBI per capita."""

# Crear una lista de tuplas 
# Crear una lista de tuplas con la información de cada provincia
provincias = [
    ("Buenos Aires", "La Plata", 17541141, 460032),
    ("Córdoba", "Córdoba", 3797718, 120418),
    ("Santa Fe", "Santa Fe de la Vera Cruz", 3486207, 131555),
    ("Mendoza", "Mendoza", 2039374, 76912),
    ("Tucumán", "San Miguel de Tucumán", 1687305, 43054),
    ("Entre Ríos", "Paraná", 1385961, 45782),
    ("Salta", "Salta", 1412602, 38810),
    ("Chaco", "Resistencia", 1189446, 23710),
    ("Corrientes", "Corrientes", 992595, 25030),
    ("Santiago del Estero", "Santiago del Estero", 896461, 18738)
]

# Crear un diccionario donde cada clave sea el nombre de la provincia y el valor sea su tupla de información
provincias_dict = {p[0]: p[1:] for p in provincias}

# Calcular y mostrar el PBI per cápita de cada provincia
for provincia, info in provincias_dict.items():
    pbi_per_capita = info[2] / info[1]
    print(f"El PBI per cápita de {provincia} es de {pbi_per_capita:.2f}")
