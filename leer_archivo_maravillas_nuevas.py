# Recorrido e impresión de las líneas de un archivo de texto
with open("maravillas_nuevas.csv", "r") as archivo:
    for linea in archivo:
        print(linea, end='')