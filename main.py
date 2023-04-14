import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import *
import funciont as fnc

#========Variables
nCoorX =0
nCoorY =0
#=====Funcion


# Crear una ventana
ventana = tk.Tk()
ventana.geometry("800x500")
ventana.configure(background="white")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Buscador de Objetos")
etiqueta.configure(background="white",font="arial")
etiqueta.place(x=5, y=10)

# Colocar la etiqueta en la posición (50, 100)

inCoordx = tk.Entry(ventana, width=20)
inCoordx.configure(font="arial")
inCoordx.pack()
inCoordx.place(x=150, y=60)

txtPuntoComa = tk.Label(ventana, text=";")
txtPuntoComa.configure(background="white",font=("arial",26))
txtPuntoComa.place(x=358, y=45)


inCoordy = tk.Entry(ventana, width=20)
inCoordy.configure(font="arial")
inCoordy.pack()
inCoordy.place(x=400, y=60)

txtDirecciones = tk.Label(ventana, text="Dirección y tipo de pista")
txtDirecciones.configure(background="white",font=("arial",10))
txtDirecciones.place(x=300, y=105)



# Crea el Canvas
canvas = Canvas(ventana, width=300, height=90)
# Crea el rectángulo
rect = canvas.create_rectangle(0, 0, 300, 90, fill="white")

# Agrega el texto al rectángulo
texto = canvas.create_text(150, 20, text=" ", fill="black")


canvas.pack()
canvas.place(x=230, y=300)

# Botones
def auxiliar(direccion):

    nCoorX,nCoorY = fnc.fncNuevaCoordenada(inCoordx.get(),inCoordy.get(),direccion)

    if str(nCoorX) == " " or str(nCoorY)== " ":
        canvas.itemconfigure(texto, text="--" + str(nCoorX) + ":" + str(nCoorY))
    else:
        canvas.itemconfigure(texto, text="")

    
# Cargar la imagen
btnNorte = tk.Button(ventana, font=("Arial",20),text="↟", relief="flat", borderwidth=0,command=auxiliar("top"))
btnNorte.place(x=350, y=130)
btnNorte.bind("<Button-1>", lambda event:auxiliar("top"))

btnSur = tk.Button(ventana,font=("Arial",20), text="↡", relief="flat", borderwidth=0)
btnSur.place(x=350, y=200)

btnEste = tk.Button(ventana,font=("Arial",20) ,text="↞", relief="flat", borderwidth=0,width=3)
btnEste.place(x=280, y=170)

btnOeste = tk.Button(ventana,font=("Arial",20), text="↠", relief="flat", borderwidth=0,width=3)
btnOeste.place(x=400, y=170)


#ComboBox
# Crea una lista de opciones para el combobox
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# Crea el combobox
combobox = ttk.Combobox(ventana, values=opciones,font=("Arial",13))

# Configura el valor predeterminado del combobox
combobox.set("Seleccione una opción")
combobox.place(x=270, y=270)
# Muestra el combobox



# Iniciar el bucle principal de la ventana
ventana.mainloop()




