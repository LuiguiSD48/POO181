from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

#Crear un objeto de la clase controlador

controlador=controladorBD()

#Funcion para el boton guardar

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())


def ejecutaSelectU():
    textEnc.delete("1.0","end")
    usuario=controlador.consultarUsuario(varBus.get())
    
    for usu in usuario:
        var1= "ID: "+str(usu[0])+" Nombre: "+usu[1]+" Correo: "+str(usu[2])+" Contraseña: "+str(usu[3])
                
    textEnc.insert(1.0,[var1])
    
    
def muestra():
    tree.delete(*tree.get_children())
    datos=controlador.mostrarUsu()
    
    for row in datos:
        tree.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        
def eliminar():
    controlador.eliminarUsuario(idelete.get())
    
def ejecutaUpdate():
    controlador.actualizarUsuario(varNom4.get(),varCor4.get(),varCon4.get(),varId4.get())
   
   

ventana= Tk()
ventana.title("CRUD des usuarios")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)

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

#Pestaña 2 Buscar usuario

titulo2=Label(pestana2,text="Buscar Usuario",fg='blue',font=("Modern",18)).pack()

varBus=tk.StringVar()
lblID=Label(pestana2,text="Id usuario: ").pack()
txtID=Entry(pestana2,textvariable=varBus).pack()

btnBus=Button(pestana2,text="Buscar Usuario",command=ejecutaSelectU).pack()

subBus=Label(pestana2,text="Encontrado",fg='blue',font=("Modern",18)).pack()


textEnc=tk.Text(pestana2,height=5,width=52)
textEnc.pack()

#pestaña3
btnMos=Button(pestana3,text="Mostrar Usuarios",command=muestra).pack()

tree=ttk.Treeview(pestana3,height=10,columns=('#0','#1','#2','#3'))
tree.heading('#0',text='Id')
tree.heading('#1',text='Nombre')
tree.heading('#2',text='Correo')
tree.heading('#3',text='Contraseña')
tree.pack()

#Pestaña 3 Form de usu

titulo=Label(pestana4,text="Actualizacion de Uusarios",fg='blue',font=("Modern",18)).pack()

varNom4=tk.StringVar()
lblNom=Label(pestana4,text="Nombre: ").pack()
txtNom4=Entry(pestana4,textvariable=varNom4).pack()

varCor4=tk.StringVar()
lblCor=Label(pestana4,text="Correo: ").pack()
txtCor4=Entry(pestana4,textvariable=varCor4).pack()

varCon4=tk.StringVar()
lblCon=Label(pestana4,text="Contraseña: ").pack()
txtCon4=Entry(pestana4,textvariable=varCon4).pack()

varId4=tk.StringVar()
lblCon=Label(pestana4,text="ID: ").pack()
txtId4=Entry(pestana4,textvariable=varId4).pack()

btnGuardar=Button(pestana4,text="Actualizar Uusuario",command=ejecutaUpdate).pack()

#Pestaña 5 Eliminar usuario

titulo5=Label(pestana5,text="Eliminar Usuario",fg='blue',font=("Modern",18)).pack()

idelete=tk.StringVar()
lblID5=Label(pestana5,text="Id usuario: ").pack()
txtID5=Entry(pestana5,textvariable=idelete).pack()

btnDel=Button(pestana5,text="Eliminar Usuario",command=eliminar).pack()

panel.add(pestana1,text='Formulario Usuarios')
panel.add(pestana2,text='Buscar Usuario')
panel.add(pestana3,text='Consultar Usuario')
panel.add(pestana4,text='Actualizar Usuario')
panel.add(pestana5,text='Eliminar Usuario')

#

ventana.mainloop()