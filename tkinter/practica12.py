from tkinter import *
from tkinter import ttk
import tkinter as tk
from validacion import *

val=Usuario()

ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

varUsu=tk.StringVar()
lblUsu=Label(seccion1,text="Usuario: ").pack()
txtUsu=Entry(seccion1,textvariable=varUsu).pack()


varCon=tk.StringVar()
lblCon=Label(seccion1,text="Contraseña: ").pack()
txtCon=Entry(seccion1,show="**",textvariable=varCon).pack()


def validar():
    val.validar1(varUsu.get(),varCon.get())


    
botonVerde=Button(seccion1,text="Boton Verde",bg="green",command=validar)
botonVerde.pack()   




ventana.mainloop()

