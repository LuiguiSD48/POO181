from logica import *
from tkinter import *
from tkinter import ttk
import tkinter as tk


controlador=usuario()

def ejecutaInsert():
   controlador.guardarUsuario(entryNU.get(),entryET.get(),entryST.get())

def consulta():
   controlador.consultarSaldo(entryNT.get())
   
def retirar():
   controlador.retirarSaldo(entryNT2.get(),entryST2.get())

ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')
pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)

titulo=Label(pestana1,text="Registro de Usarios",fg='blue',font=("Modern",18)).pack()

entryNU = tk.StringVar()
labelN= Label(pestana1,text="Titular: ").pack()
EntryNU1= Entry(pestana1,textvariable=entryNU).pack()

entryET = tk.StringVar()
labelE= Label(pestana1,text="Edad: ").pack()
EntryET1= Entry(pestana1,textvariable=entryET).pack()

entryST = tk.StringVar()
labelS= Label(pestana1,text="Saldo: ").pack()
EntryST1= Entry(pestana1,textvariable=entryST).pack()


botonVerde=Button(pestana1,text="Guardar datos ",bg="gray",command=ejecutaInsert)
botonVerde.pack()  

titulo2=Label(pestana2,text="Consultar",fg='blue',font=("Modern",18)).pack()

entryNT = tk.StringVar()
labelT= Label(pestana2,text="Numero de cuenta: ").pack()
EntryNT1= Entry(pestana2,textvariable=entryNT).pack()

botonVerde=Button(pestana2,text="Mostrar saldo ",bg="gray",command=consulta)
botonVerde.pack()  

titulo3=Label(pestana3,text="Operaciones",fg='blue',font=("Modern",18)).pack()

entryNT2 = tk.StringVar()
labelT2= Label(pestana3,text="Numero de cuenta: ").pack()
EntryNT12= Entry(pestana3,textvariable=entryNT2).pack()

entryST2 = tk.StringVar()
labelS2= Label(pestana3,text="Saldo: ").pack()
EntryST2= Entry(pestana3,textvariable=entryST2).pack()

botonVerde=Button(pestana3,text="Mostrar saldo ",bg="gray",command=retirar)
botonVerde.pack()  


panel.add(pestana1,text='Formulario Usuarios')
panel.add(pestana2,text='Buscar Usuario')
panel.add(pestana3,text='operaciones')
ventana.mainloop()
