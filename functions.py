
import json 
import os

nombre_archivo = "mapa.json"
carpeta = "datos"
ruta_archivo = os.path.join(os.getcwd(), carpeta, nombre_archivo)

nombre_archivoPistas = "pistas.json"
ruta_archivoPistas = os.path.join(os.getcwd(), carpeta, nombre_archivoPistas)

with open(ruta_archivoPistas, 'r') as f:
    datos = json.load(f)
    
with open(ruta_archivo, 'r') as f:
    mapa = json.load(f)       


def select_all(event):
    event.widget.select_range(0, 'end')
    
def fncNuevaCoordenada(ejex, ejey, direccion):
    if direccion == "left":
        if ejex:
            ejex = int(ejex) - 2
        else:
            ejex=""
       
    elif direccion == "right":
        if ejex:
            ejex = int(ejex)  + 2
        else:
            ejex=""

    elif direccion == "top":
        if ejey:
            ejey = int(ejey) + 10
        else:
            ejey = ""
    elif direccion == "bot":
        if ejey:
            ejey = int(ejey) - 10
        else:
            ejey = ""
    return str(ejex), str(ejey)

def listadoBusquedaCoordenadas(CoordX,CoordY,direccion):
    nCoordX= int(CoordX)
    nCoordY= int(CoordY)
    arPistasEncontradas =[]
    
    for i in range(1,25):
        if direccion == "right":
            nCoordX= nCoordX+1
        if direccion == "left":
            nCoordX= nCoordX-1
        if direccion == "top":
            nCoordY= nCoordY-1
        if direccion == "bot":
            nCoordY= nCoordY+1
    
        for element in mapa["Coordenadas"][str(nCoordX)+","+str(nCoordY)]:
            if element not in arPistasEncontradas:
                arPistasEncontradas.append(element)
    
    return(arPistasEncontradas)

def busquedaCoordenadas(CoordX,CoordY,direccion,pista):
    nCoordX= int(CoordX)
    nCoordY= int(CoordY)
    for i in range(1,25):
        if direccion == "right":
            nCoordX= nCoordX+1
        if direccion == "left":
            nCoordX= nCoordX-1
        if direccion == "top":
            nCoordY= nCoordY-1
        if direccion == "bot":
            nCoordY= nCoordY+1

        coord_str = str(nCoordX) + "," + str(nCoordY)
        if coord_str not in mapa["Coordenadas"]:
            return "Coordenadas fuera del mapa"
        
        for element in mapa["Coordenadas"][coord_str]:
            if element == pista:
                nRestaX= int(CoordX)- int(nCoordX) 
                nRestaY= int(CoordY)- int(nCoordY) 
                                
                if nRestaX !=0:
                    print(nRestaX)
                    if int(nRestaX) < 0 :
                        nRestaX= nRestaX *(-1)
                    return coord_str,nRestaX
                if int(nRestaY) !=0:
                    print(nRestaY)
                    if nRestaY < 0 :
                        nRestaY= nRestaY *(-1)
                    return coord_str,nRestaY

    return "Pista no encontrada"

def nombrePistas(): 
    return(datos['pista'])

def agregarPista(CoordX,CoordY,pistaNueva):    
    if str(CoordX) == "0" and str(CoordY) == "0":
        return("No se puede agregar en el 0,0")
    else:
        if pistaNueva in mapa["Coordenadas"][str(CoordX)+","+str(CoordY)]:
            return("Pista ya Ingresada")
        else:
            mapa["Coordenadas"][str(CoordX)+","+str(CoordY)].append(pistaNueva)
            with open(ruta_archivo, 'w') as f:
                json.dump(mapa, f)
            return("Pista Agregada")
        
def pistasCoordenda(CoordX,CoordY): 
    with open(ruta_archivo, 'r') as f:
        mapa = json.load(f)
    if len(mapa["Coordenadas"][str(CoordX)+","+str(CoordY)])>0:  
        return(mapa["Coordenadas"][str(CoordX)+","+str(CoordY)])
    else:
        return("Sin Pistas")

def eliminarPista(CoordX, CoordY, indicePista):
    lista_pistas = mapa["Coordenadas"][str(CoordX)+","+str(CoordY)]
    if indicePista < len(lista_pistas):
        del lista_pistas[indicePista]
        mapa["Coordenadas"][str(CoordX)+","+str(CoordY)] = lista_pistas
        with open(ruta_archivo, 'w') as f:
            json.dump(mapa, f)
        return "Pista Eliminada"
    else:
        return "No se pudo eliminar la pista. El índice está fuera de rango."