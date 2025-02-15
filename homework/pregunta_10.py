"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    resultado = []

    with open("files/input/data.csv", "r") as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            columnas = linea.strip().split()  # Usamos espacio como delimitador
            letra = columnas[0]  # Primera columna (letra)
            
            columna_4 = columnas[3]  # Cuarta columna
            cantidad_columna_4 = len(columna_4.split(',')) if columna_4 else 0

            columna_5 = columnas[4]  # Quinta columna
            cantidad_columna_5 = len(columna_5.split(',')) if columna_5 else 0

            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))

    return resultado

print(pregunta_10())
