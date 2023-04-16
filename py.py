import json 
import os

nombre_archivo = "mapa.json"
carpeta = "datos"
ruta_archivo = os.path.join(os.getcwd(), carpeta, nombre_archivo)
with open(ruta_archivo, 'r') as f:
    mapa = json.load(f)

# Agregar nuevos datos a CoordenadasX -93 -> 50
print (mapa["Coordenadas"]["-93,-100"])
