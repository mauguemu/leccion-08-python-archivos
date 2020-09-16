# Manejo de archivos en Python

## Recursos de interés
- Capítulo 7 del libro *Python for Everybody: Exploring data in Python 3*, de Charles Severance [PY4E - Python for Everybody - Chapter 7:Files](https://www.py4e.com/html3/07-files)

## Archivos
Los archivos proporcionan una forma de almacenar datos de manera persistente (i.e. no volátil) en medios como discos duros, discos compactos, DVD, dispositivos de almacenamiento USB y otros. Contrario a lo que sucede a las estructuras que residen en la memoria del computador, como las variables, la información almacenada en archivos permanece después de que finaliza la ejecución de un programa o se apaga el computador. En Python, los archivos se manejan como objetos de tipo [file](https://docs.python.org/3/glossary.html#term-file-object), los cuales tienen un conjunto de [métodos](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), entre las que están:

* Abrir un archivo.  
* Leer datos de un archivo.  
* Escribir datos en un archivo.  
* Cerrar un archivo.  

Las operaciones que se usan para manejar archivos se ilustran en la figura 1.

![Figura 1: Operaciones para manejo de archivos en Python. Imagen de Charles Severance (https://www.py4e.com/html3/07-files)](img/operaciones-archivos-python.png)

Figura 1: Operaciones para manejo de archivos en Python. Imagen de Charles Severance ([https://www.py4e.com/html3/07-files](https://www.py4e.com/html3/07-files))

Estas operaciones se realizan a través de una variable llamada "manejador de archivo" (*file handle*).

## La sentencia ```with```
La sentencia [with](https://docs.python.org/3/reference/compound_stmts.html#with) se utiliza para ejecutar un bloque con métodos definidos por un [administrador de contexto (*context manager*)](https://docs.python.org/3/reference/datamodel.html#context-managers). Permite recorrer un archivo y cerrarlo automáticamente cuando se finaliza.

```python
# Recorrido e impresión de las líneas de un archivo de texto
with open("maravillas_antiguas.csv") as archivo:
    for linea in archivo:
        print(linea, end='')
```

## Archivos CSV
Los archivos CSV (*comma separated values*, valores separados por comas) son de los más empleados para intercambiar datos en formato tabular (i.e. en columnas). Pueden llamarse de otras formas, como por ejemplo “archivos de texto delimitado”. Son ampliamente utilizados para importar y exportar datos desde y hacia hojas electrónicas, bases de datos y otros sistemas de manejo de información. Consisten de líneas de texto en las cuales hay datos separados por comas. Cada dato corresponde a una columna. Por ejemplo, el siguiente es el contenido de un archivo CSV con cuatro columnas:

```
nombre,ubicacion,longitud,latitud
Taj Mahal,India,78.042111,27.174799
Chichen Itza,México,-88.56865,20.6829
La estatua de Cristo Redentor,Brasil,-43.210556,-22.951944
```


### El módulo ```csv```


#### Ejemplos de creación y uso de ambientes

##### Ambiente para utilitarios de línea de comandos de GDAL

A continuación, se crea un ambiente Conda en el que se instalan los utilitarios de línea de comandos de GDAL y se presentan varios ejemplos de su uso.

**Creación del ambiente**
```shell
# Actualización de Conda
conda update -n base -c defaults conda

# Creación de un ambiente de nombre "gdal"
conda create -n gdal

# Activación del ambiente
conda activate gdal

# Instalación de paquetes
# Binarios de GDAL desde el canal conda-forge
conda install -c conda-forge gdal

# Desactivación del ambiente
$ conda deactivate
```

**Uso del ambiente**
```shell
# Activación del ambiente
conda activate gdal

# Descarga de la capa de cantones de Costa Rica desde el servicio WFS del IGN en el SNIT
ogr2ogr -f "GeoJSON" -s_srs EPSG:5367 -t_srs EPSG:4326 -makevalid cantones.geojson WFS:"http://geos.snitcr.go.cr/be/IGN_5/wfs" "IGN_5:limitecantonal_5k"

# Información sobre la capa descargada
ogrinfo -al -so cantones.geojson

# Extracción de los cantones de la provincia de Heredia
ogr2ogr -where "provincia = 'Heredia'" cantones-heredia.geojson cantones.geojson

# Extracción de los cantones con área >= 2000 km2
ogr2ogr -where "area >= 2000" cantones-grandes.geojson cantones.geojson

# Extracción de los cantones con área >= 2000 km2 de la provincia de Limón
ogr2ogr -where "area >= 2000 AND provincia = 'Limón'" cantones-grandes-limon.geojson cantones.geojson

# EJERCICIO: Extracción de los cantones con área <= 20 km2 de la provincia de Heredia

# Extracción de los campos de provincia, cantón y área de los cantones de la provincia de Alajuela
ogr2ogr -select "provincia, canton, area" -where "provincia = 'Alajuela'" cantones-alajuela.geojson cantones.geojson

# Información sobre la capa de cantones de Alajuela
ogrinfo -al -so cantones-alajuela.geojson

# EJERCICIO: Extracción de los campos de provincia, cantón y área de los cantones con área <= 20 km2 de la provincia de San José

# Desactivación del ambiente
$ conda deactivate
```

Puede encontrar la referencia de todos los comandos para manejo de ambientes de Conda en [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
