from tkinter import *
import tkinter as tk
from logica import *


def conver():
    logica.conversor(entryAR.get())
    
def conver1():
    logica.conversor1(entryRA.get())
    
ventana=Tk()
ventana.title("Examen final")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="#00e6e6")
seccion2.pack(expand=True,fill='both')

titulo=Label(seccion1,text="Arabigos a Romanos",fg='blue',font=("Modern",18)).pack()

entryAR = tk.StringVar()
labelAR= Label(seccion1,text="Numero: ").pack()
EntryAR= Entry(seccion1,textvariable=entryAR).pack()

boton1=Button(seccion1,text="Convertir ",bg="gray",command=conver)
boton1.pack()  

titulo=Label(seccion2,text="Romanos a arabigos",fg='blue',font=("Modern",18)).pack()

entryRA = tk.StringVar()
labelRA= Label(seccion2,text="Numero: ").pack()
EntryRA= Entry(seccion2,textvariable=entryRA).pack()

boton1=Button(seccion2,text="Convertir ",bg="gray",command=conver1)
boton1.pack()  

ventana.mainloop()