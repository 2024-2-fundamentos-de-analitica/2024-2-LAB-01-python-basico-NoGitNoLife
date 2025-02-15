"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    conteo_claves = {}

    # Abrir el archivo y leer sus líneas
    with open("files/input/data.csv", "r") as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            columnas = linea.strip().split()  # Usamos espacio como delimitador
            columna_5 = columnas[4]  # Columna 5 (el diccionario codificado)

            for par in columna_5.split(','):
                clave, _ = par.split(':')  # Extraemos solo la clave

                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1

    conteo_claves_ordenado = dict(sorted(conteo_claves.items()))

    return conteo_claves_ordenado

print(pregunta_09())
