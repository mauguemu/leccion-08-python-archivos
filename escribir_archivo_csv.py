import csv

# Recorrido de las líneas de un archivo de texto y escritura en un nuevo archivo de las líneas que cumplen con una condición
with open("maravillas_antiguas.csv") as archivo_entrada:
    lector = csv.reader(archivo_entrada)

    with open("maravillas_antiguas_irak_egipto.csv", "w") as archivo_salida:
        escritor = csv.writer(archivo_salida, delimiter=',')
        i = 0
        for linea in lector:
            if i == 0:
                # Línea del encabezado
                escritor.writerow(linea)
                print(linea)
            elif linea[1] == "Irak" or linea[1] == "Egipto":
                 # La ubicación es Egipto o Irak
                escritor.writerow(linea)
                print(linea)
            i = i + 1