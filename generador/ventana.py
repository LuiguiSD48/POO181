from tkinter import *
import tkinter as tk
from logica import *

ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

entryUN = tk.StringVar()
labelN= Label(seccion1,text="Numero de caracteres: ").pack()
EntryN= Entry(seccion1,textvariable=entryUN).pack()

checkbox_value = tk.BooleanVar()
checkbox = tk.Checkbutton(seccion1,text="Mayus", variable=checkbox_value).pack()

checkbox_value1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(seccion1,text="Caracter Especial", variable=checkbox_value1).pack()

def generar():
    logica().generarContra(EntryN,checkbox_value,checkbox_value1)

botonVerde=Button(seccion1,text="Generar Contraseña",bg="gray",command=generar)
botonVerde.pack()  

entryGC = tk.StringVar()
EntryGC= Entry(seccion1,textvariable=entryGC).pack()

ventana.mainloop()

