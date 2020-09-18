import csv

# Recorrido e impresión de las líneas de un archivo de texto
with open("maravillas_nuevas.csv") as archivo:
    # Se crea el objeto reader
    lector = csv.reader(archivo)
    
    # Se recorren las líneas
    i = 0
    for linea in lector:
        if (i != 0): 
            if float(linea [2]) < 0:
                print('Línea: ', linea)
        i += 1
        
        # Se recorren las columnas de la línea
        #for columna in linea:
        #    print ('Columna: ', columna)