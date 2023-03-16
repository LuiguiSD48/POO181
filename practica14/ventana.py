from tkinter import *
import tkinter as tk
from logica import *


ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="green")
seccion2.pack(expand=True,fill='both')

entryNU = tk.StringVar()
labelN= Label(seccion1,text="Titular: ").pack()
EntryNU1= Entry(seccion1,textvariable=entryNU).pack()

entryNT = tk.StringVar()
labelT= Label(seccion1,text="Numero de caracteres: ").pack()
EntryNT1= Entry(seccion1,textvariable=entryNT).pack()

entryET = tk.StringVar()
labelE= Label(seccion1,text="Numero de caracteres: ").pack()
EntryET1= Entry(seccion1,textvariable=entryET).pack()

entryST = tk.StringVar()
labelS= Label(seccion1,text="Numero de caracteres: ").pack()
EntryST1= Entry(seccion1,textvariable=entryST).pack()


NuevoU=usuario(entryNT.get(),entryET.get(),entryST.get())




botonVerde=Button(seccion1,text="Guardar datos ",bg="gray")
botonVerde.pack()  

def mostrarS():
   print(usuario.mostrarSaldo(NuevoU.getSaldo())) 

botonVerde1=Button(seccion1,text="Guardar datos ",bg="gray",command=mostrarS)
botonVerde1.pack()  
ventana.mainloop()
