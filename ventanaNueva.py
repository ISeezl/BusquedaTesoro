import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import *
import functions as fnc

ventana2 = tk.Tk()
ventana2.title("Agregar Pista")
#ventana2.lift()
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
btnAgregar.bind("<Button-1>", lambda event:fnc.agregarPista(inCoordx.get(),inCoordy.get(),combobox.get()))

btnAgregar.pack()
btnAgregar.place(x=130, y=180)
ventana2.mainloop()

