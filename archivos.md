# Manejo de archivos en Python

## Recursos de interés
- Capítulo 7 del libro *Python for Everybody: Exploring data in Python 3*, de Charles Severance [PY4E - Python for Everybody - Chapter 7:Files](https://www.py4e.com/html3/07-files)

## Archivos
Los archivos proporcionan una forma para almacenar datos de manera persistente (i.e. no volátil) en medios como discos duros, discos compactos, DVD, dispositivos de almacenamiento USB y otros. Contrario a lo que sucede a las estructuras que residen en la memoria del computador, como las variables, la información almacenada en archivos permanece después de que finaliza la ejecución de un programa o se apaga el computador. En Python, los archivos se manejan como objetos de tipo [file](https://docs.python.org/3/glossary.html#term-file-object), los cuales tienen un conjunto de [métodos](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), entre las que están:

– Crear un archivo.  
– Abrir un archivo.  
– Leer datos de un archivo.  
– Escribir datos en un archivo.  
– Guardar (*salvar*) un archivo.  
– Cerrar un archivo.  

Las operaciones que se usan para manejar archivos se ilustran en la figura 1.

![Figura 1: Operaciones para manejo de archivos en Python. Imagen de Charles Severance (https://www.py4e.com/html3/07-files)](img/operaciones-archivos-python.png)


## Conda

### Ambientes

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
