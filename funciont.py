
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