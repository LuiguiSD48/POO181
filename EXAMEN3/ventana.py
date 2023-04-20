from tkinter import *
from tkinter import ttk
import tkinter as tk
from logica import *

#Crear un objeto de la clase controlador
controlador=controladorBD()


#Funcion para el boton guardar
def ejecutaInsert():
    controlador.guardarUsuario(varMat.get(),varCan.get())
    
def muestra():
    tree.delete(*tree.get_children())
    datos=controlador.mostrarUsu()
    
    for row in datos:
        tree.insert("",0,text=row[0],values=(row[1],row[2]))
        
def ejecutaUpdate():
    controlador.actualizarUsuario(varMat4.get(),varCan4.get(),varId4.get())

ventana= Tk()
ventana.title("CRUD des materiales")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)

pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)


#Pestaña 1 Form de usu

titulo=Label(pestana1,text="Registro de Materiales",fg='blue',font=("Modern",18)).pack()

varMat=tk.StringVar()
lblMat=Label(pestana1,text="Material: ").pack()
txtMat=Entry(pestana1,textvariable=varMat).pack()

varCan=tk.StringVar()
lblCan=Label(pestana1,text="Cantidad: ").pack()
txtCan=Entry(pestana1,textvariable=varCan).pack()


btnGuardar=Button(pestana1,text="Guardar Material",command=ejecutaInsert).pack()


#pestaña3
btnMos=Button(pestana3,text="Mostrar Materiales",command=muestra).pack()

tree=ttk.Treeview(pestana3,height=10,columns=('#0','#1','#2'))
tree.heading('#0',text='Id')
tree.heading('#1',text='Material')
tree.heading('#2',text='Cantidad')
tree.pack()

#Pestaña 3 Form de usu

titulo=Label(pestana4,text="Actualizacion de Materiales",fg='blue',font=("Modern",18)).pack()

varMat4=tk.StringVar()
lblMat4=Label(pestana4,text="Material: ").pack()
txtMat4=Entry(pestana4,textvariable=varMat4).pack()

varCan4=tk.StringVar()
lblCan4=Label(pestana4,text="Cantidad: ").pack()
txtCan4=Entry(pestana4,textvariable=varCan4).pack()

varId4=tk.StringVar()
lblCon=Label(pestana4,text="ID: ").pack()
txtId4=Entry(pestana4,textvariable=varId4).pack()

btnGuardar=Button(pestana4,text="Actualizar Material",command=ejecutaUpdate).pack()



panel.add(pestana1,text='Formulario Materiales')
panel.add(pestana3,text='Consultar Materiales')
panel.add(pestana4,text='Actualizar Materiales')

#

ventana.mainloop()