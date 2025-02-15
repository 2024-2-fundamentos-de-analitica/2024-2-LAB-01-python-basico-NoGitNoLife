"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    valores_claves = {}

    with open("files/input/data.csv", "r") as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            columnas = linea.strip().split()  # Usamos espacio como delimitador
            columna_5 = columnas[4]  # La columna 5 contiene el diccionario codificado

            diccionario = {}
            for par in columna_5.split(','):
                clave, valor = par.split(':')
                diccionario[clave] = int(valor)  # Convertimos el valor a entero

            for clave, valor in diccionario.items():
                if clave not in valores_claves:
                    valores_claves[clave] = [valor, valor]  # [minimo, maximo]
                else:
                    valores_claves[clave][0] = min(valores_claves[clave][0], valor)
                    valores_claves[clave][1] = max(valores_claves[clave][1], valor)

    resultado = [(clave, valores[0], valores[1]) for clave, valores in valores_claves.items()]

    resultado.sort()

    return resultado

print(pregunta_06())
