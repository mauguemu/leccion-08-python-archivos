# Recorrido e impresión de las líneas de un archivo de texto
subhilera = input("Ingrese la subhilera que se desea buscar:")
with open("maravillas_antiguas.csv", "r") as archivo:
    for linea in archivo:
        if(linea.find (subhilera)!=-1)
		print(linea, end='')