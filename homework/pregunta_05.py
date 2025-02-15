"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    datos_por_letra = {}

    with open("files/input/data.csv", "r") as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            columnas = linea.strip().split()  # Usamos espacio como delimitador
            letra = columnas[0]  # Letra en la columna 1
            valor = int(columnas[1])  # Convertimos a entero la segunda columna

            if letra in datos_por_letra:
                datos_por_letra[letra].append(valor)
            else:
                datos_por_letra[letra] = [valor]

    resultado = []
    for letra, valores in datos_por_letra.items():
        maximo = max(valores)  # Valor máximo para esa letra
        minimo = min(valores)  # Valor mínimo para esa letra
        resultado.append((letra, maximo, minimo))

    resultado.sort()

    return resultado

print(pregunta_05())
