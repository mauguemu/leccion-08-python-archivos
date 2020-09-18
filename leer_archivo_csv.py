import csv

# Recorrido e impresión de las líneas de un archivo de texto
with open("maravillas_nuevas.csv") as archivo:
    # Se crea el objeto reader
    lector = csv.reader(archivo)
    
    # Se recorren las líneas
    for linea in lector:
        print('Línea: ', linea)
        
        # Se recorren las columnas de la línea
        for columna in linea:
            print ('Columna: ', columna)