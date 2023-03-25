from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

#Crear un objeto de la clase controlador

controlador=controladorBD()

#Funcion para el biotin guardar

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

ventana= Tk()
ventana.title("CRUD des usuarios")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#Pestaña 1 Form de usu

titulo=Label(pestana1,text="Registro de Uusarios",fg='blue',font=("Modern",18)).pack()

varNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varCor=tk.StringVar()
lblCor=Label(pestana1,text="Correo: ").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()

varCon=tk.StringVar()
lblCon=Label(pestana1,text="Contraseña: ").pack()
txtCon=Entry(pestana1,textvariable=varCon).pack()

btnGuardar=Button(pestana1,text="Guardar Uusuario",command=ejecutaInsert).pack()

panel.add(pestana1,text='Formulario Usuarios')
panel.add(pestana2,text='Buscar Usuario')
panel.add(pestana3,text='Consultar Usuario')
panel.add(pestana4,text='Actualizar Usuario')

#

ventana.mainloop()