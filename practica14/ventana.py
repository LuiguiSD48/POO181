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

entryET = tk.StringVar()
labelE= Label(seccion1,text="Edad: ").pack()
EntryET1= Entry(seccion1,textvariable=entryET).pack()

entryST = tk.StringVar()
labelS= Label(seccion1,text="Saldo: ").pack()
EntryST1= Entry(seccion1,textvariable=entryST).pack()


entryNT = tk.StringVar()
labelT= Label(seccion1,text="Numero de cuenta: ").pack()
EntryNT1= Entry(seccion1,textvariable=entryNT).pack()


def NuevoUsu():
   
 NuevoU=usuario(entryNU.get(),entryET.get(),entryST.get(),entryNT.get())
 print(NuevoU.getSaldo())
 nuecoU=NuevoU
 
 

 



botonVerde=Button(seccion1,text="Guardar datos ",bg="gray",command=NuevoU)
botonVerde.pack()  

def mostrarS():
   print(usuario.mostrarSaldo(nuevo1.getSaldo())) 

botonVerde1=Button(seccion1,text="Guardar datos ",bg="gray",command=mostrarS)
botonVerde1.pack()  
ventana.mainloop()
