from tkinter import *
import tkinter as tk
from logica import *
from tkinter import ttk

ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

entryUN = tk.StringVar()
labelN= Label(seccion1,text="Numero de caracteres: ").pack()
EntryN= Entry(seccion1,textvariable=entryUN)
EntryN.insert(0,"8")
EntryN.pack()

'''
entryMa = tk.StringVar()
labelMa= Label(seccion1,text="Contraseña con mayusculas: ").pack()
EntryMa= Entry(seccion1,textvariable=entryMa)
EntryMa.insert(0,"Si")
EntryMa.pack()

entryCa = tk.StringVar()
labelCa= Label(seccion1,text="Contraseña con caracteres especiales: ").pack()
EntryCa= Entry(seccion1,textvariable=entryCa)
EntryCa.insert(0,"Si")
EntryCa.pack()
'''


checkbox_value = tk.IntVar()
checkbox = ttk.Checkbutton(seccion1,text="Mayus",variable=checkbox_value)
checkbox.pack()

checkbox_value1 = tk.IntVar()
checkbox1 = ttk.Checkbutton(seccion1,text="Caracter Especial",variable=checkbox_value1)
checkbox1.pack()


def generar():
    logica.generarContra(entryUN.get(),checkbox_value.get(),checkbox_value1.get())
    




botonVerde=Button(seccion1,text="Generar Contraseña",bg="gray",command=generar).pack()



ventana.mainloop()

