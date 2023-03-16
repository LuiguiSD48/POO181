from tkinter import *
import tkinter as tk
from logica import *

ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

entryNU = tk.StringVar()
labelN= Label(seccion1,text="Nombre: ").pack()
EntryNU1= Entry(seccion1,textvariable=entryNU).pack()

entryAP = tk.StringVar()
labelT= Label(seccion1,text="Apeido Paterno: ").pack()
EntryNT1= Entry(seccion1,textvariable=entryAP).pack()

entryAM = tk.StringVar()
labelE= Label(seccion1,text="Apeido Materno: ").pack()
EntryET1= Entry(seccion1,textvariable=entryAM).pack()

entryAN = tk.StringVar()
labelS= Label(seccion1,text="Año de nacimiento: ").pack()
EntryST1= Entry(seccion1,textvariable=entryAN).pack()

entryAC = tk.StringVar()
labelS= Label(seccion1,text="Año de curso: ").pack()
EntryST1= Entry(seccion1,textvariable=entryAC).pack()

entryCU = tk.StringVar()
labelS= Label(seccion1,text="Carrera: ").pack()
EntryST1= Entry(seccion1,textvariable=entryCU).pack()


def generarMat():
 nuevou=usuario(entryNU.get(),entryAP.get(),entryAM.get(),entryAN.get(),entryAC.get(),entryCU.get())
 nuevou.CrearM()

botonVerde=Button(seccion1,text="GENERAR MATRICULA ",bg="gray",command=generarMat)
botonVerde.pack()  
 
ventana.mainloop()