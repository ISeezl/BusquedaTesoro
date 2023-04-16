import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import *
import functions as fnc
#========Variables
nCoorX =0
nCoorY =0
sTextoAgregado=""
sCoordNueva=""
sNroMov=""
#=====Funcion


# Crear una ventana
ventana = tk.Tk()
ventana.title("--Busqueda de Tesoro")
ventana.geometry("800x500")
ventana.attributes("-toolwindow", True)
ventana.configure(background="white")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Buscador de Objetos")
etiqueta.configure(background="white",font="arial")
etiqueta.place(x=5, y=10)

# Colocar la etiqueta en la posición (50, 100)

inCoordx = tk.Entry(ventana, width=20)
inCoordx.configure(font="arial")
inCoordx.insert(0,0)
inCoordx.pack()
inCoordx.place(x=150, y=60)
inCoordx.bind('<FocusIn>', fnc.select_all)

lblPuntoComa = tk.Label(ventana, text=";")
lblPuntoComa.configure(background="white",font=("arial",26))
lblPuntoComa.place(x=358, y=45)


inCoordy = tk.Entry(ventana, width=20)
inCoordy.configure(font="arial")
inCoordy.insert(0,0)
inCoordy.pack()
inCoordy.place(x=400, y=60)
inCoordy.bind('<FocusIn>', fnc.select_all)

txtDirecciones = tk.Label(ventana, text="Dirección y tipo de pista")
txtDirecciones.configure(background="white",font=("arial",10))
txtDirecciones.place(x=300, y=105)

#ComboBox
# Crea el combobox
combobox = ttk.Combobox(ventana,font=("Arial",13))
combobox.set("Seleccione una opción")
combobox.place(x=270, y=270)


# Crea el Canvas
canvas = Canvas(ventana, width=300, height=90)
# Crea el rectángulo
rect = canvas.create_rectangle(0, 0, 300, 90, fill="white")
# Agrega el texto al rectángulo
texto = canvas.create_text(150, 20, text=" ", fill="black")
texto2 = canvas.create_text(150, 30, text=" ", fill="black")
canvas.pack()
canvas.place(x=230, y=300)

# Botones
def destellar_rectangulo(tiempo):
    if tiempo % 200 == 0:
        canvas.itemconfigure(rect, fill="red")
    else:
        canvas.itemconfigure(rect, fill="white")
    if tiempo < 200:
        ventana.after(500, destellar_rectangulo, tiempo+500)

def auxiliar(direccion):
    if inCoordx.get() == "0" and inCoordy.get() == "0":
        ventana.after(200, destellar_rectangulo(0))
    else:
        global sDireccion
        sDireccion=direccion
       
        arLista =fnc.listadoBusquedaCoordenadas(inCoordx.get(), inCoordy.get(), direccion)
        if len(arLista)>0:
            combobox.delete(0,"end")
            combobox["values"] = arLista
        else:
            combobox.delete(0,"end")
            canvas.itemconfig(texto, text="Pistas no encontradas") 

        
def auxiliar_pisaElegida(event):
    # Obtener el valor seleccionado en el combobox
   #  selected_value = combobox.get()
   global sDireccion
   sCoordNueva,sNroMov=fnc.busquedaCoordenadas(inCoordx.get(),inCoordy.get(),sDireccion, combobox.get())
   canvas.itemconfig(texto, text=sCoordNueva)
   canvas.itemconfig(texto2, text=sNroMov) 


    
combobox.bind("<<ComboboxSelected>>", auxiliar_pisaElegida)

# Cargar la imagen
btnNorte = tk.Button(ventana, font=("Arial",20),text="↟", relief="flat", borderwidth=0)
btnNorte.place(x=350, y=130)
btnNorte.bind("<Button-1>", lambda event:auxiliar("top"))

btnSur = tk.Button(ventana,font=("Arial",20), text="↡", relief="flat", borderwidth=0)
btnSur.place(x=350, y=200)
btnSur.bind("<Button-1>", lambda event:auxiliar("bot"))

btnEste = tk.Button(ventana,font=("Arial",20) ,text="↞", relief="flat", borderwidth=0,width=3)
btnEste.place(x=280, y=170)
btnEste.bind("<Button-1>", lambda event:auxiliar("left"))

btnOeste = tk.Button(ventana,font=("Arial",20), text="↠", relief="flat", borderwidth=0,width=3)
btnOeste.place(x=400, y=170)
btnOeste.bind("<Button-1>", lambda event:auxiliar("right"))



def abrir_ventana():
    #Ventana 2 Buscador Pistas
    ventana2 = tk.Toplevel()
    ventana2.title("Agregar Pista")
    ventana2.lift()
    ventana2.geometry("400x400")
    ventana2.configure(background="white")

    inCoordx = tk.Entry(ventana2, width=10)
    inCoordx.configure(font="arial")
    inCoordx.insert(0,0)
    inCoordx.pack()
    inCoordx.place(x=70, y=60)
    inCoordx.bind('<FocusIn>', fnc.select_all)

    txtPuntoComa = tk.Label(ventana2, text=";")
    txtPuntoComa.configure(background="white",font=("arial",26))
    txtPuntoComa.place(x=180, y=45)


    inCoordy = tk.Entry(ventana2, width=10)
    inCoordy.configure(font="arial")
    inCoordy.insert(0,0)
    inCoordy.pack()
    inCoordy.place(x=210, y=60)

    

    inCoordy.bind('<FocusIn>', fnc.select_all)
    
    # Crea el combobox
    combobox = ttk.Combobox(ventana2, values=fnc.nombrePistas(),font=("Arial",13))

    # Configura el valor predeterminado del combobox
    combobox.set("Seleccione una opción")
    combobox.place(x=80, y=130)

    btnAgregar = tk.Button(ventana2, text="Agregar Pista")
    btnAgregar.bind("<Button-1>", lambda event:auxiliar_ingreso())

    btnAgregar.pack()
    btnAgregar.place(x=130, y=180)
    
    btnVerPistas = tk.Button(ventana2, text="Ver Pista")
    btnVerPistas.bind("<Button-1>", lambda event:auxiliar_listadoPistas())

    btnVerPistas.pack()
    btnVerPistas.place(x=300, y=180)
    
    btnEliminarPista = tk.Button(ventana2, text="Eliminar Pista")
    btnEliminarPista.bind("<Button-1>", lambda event:auxiliar_eliminarPista())

    btnEliminarPista.pack()
    btnEliminarPista.place(x=300, y=200)
    
    lblMensaje = tk.Label(ventana2, text="")
    lblMensaje.configure(background="white",font=("arial",10))
    lblMensaje.place(x=70, y=250)
    
    
    listbox = tk.Listbox(ventana2, height=3)
    listbox.grid_rowconfigure(0, minsize=3)
    # Agregar las filas como elementos de la lista
    # Mostrar la lista en la ventana principal
    listbox.pack()
    
    def auxiliar_listadoPistas():
        
        listado=fnc.pistasCoordenda(inCoordx.get(),inCoordy.get())
        listbox.delete(0,"end")
        if listado == "Sin Pistas":
            lblMensaje.config(text=listado)
        else:
           
            for elemento in (listado):
                listbox.insert(listado.index(elemento),elemento.upper())

    def auxiliar_eliminarPista():
       print(listbox.curselection()[0])
       lblMensaje.config(text=fnc.eliminarPista(inCoordx.get(),inCoordy.get(),listbox.curselection()[0]))
       auxiliar_listadoPistas()
        
    def auxiliar_ingreso():
        lblMensaje.config(text=fnc.agregarPista(inCoordx.get(),inCoordy.get(),combobox.get()))
        auxiliar_listadoPistas()


# Mostrar tabla


boton = tk.Button(ventana, text="Abrir ventana")
boton.bind("<Button-1>", lambda event:abrir_ventana())
boton.pack()

# Iniciar el bucle principal de la ventana


ventana.mainloop()




