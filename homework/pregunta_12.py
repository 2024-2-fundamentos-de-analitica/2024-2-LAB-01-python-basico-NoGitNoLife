"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            columnas = linea.strip().split()  # Usamos espacio como delimitador
            letra_columna_1 = columnas[0]  # Columna 1 (letra)
            columna_5 = columnas[4]  # Columna 5 (diccionario codificado como cadena)

            suma_columna_5 = 0
            for par in columna_5.split(','):
                _, valor = par.split(':')
                suma_columna_5 += int(valor)

            if letra_columna_1 in suma_por_letra:
                suma_por_letra[letra_columna_1] += suma_columna_5
            else:
                suma_por_letra[letra_columna_1] = suma_columna_5

    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada

print(pregunta_12())