from tkinter import Tk,Frame,Button,Entry,Label,ttk,messagebox
from validacion import cUsuario

x="password"
y="usuario"

ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

labelU = Label(seccion1,text="Usuario: ")
labelU.pack()

entryU1 = Entry(seccion1)
entryU1.pack()
entryU=entryU1.get("1.0","end")

def im():
    messagebox.showinfo(entryU)


labelC = Label(seccion1,text="Contraseña: ")
labelC.pack()

entryC1 = ttk.Entry(seccion1)
entryC1.pack()
entryC=entryC1.get()
usu1="luisds"
con1="password"
usuario1=cUsuario(entryU,entryC)
usuario2=cUsuario(usu1,con1)
def validar():

    if cUsuario.validar1(usuario1,usuario2)==True:
        messagebox.showerror("InicioExitoso")

    else:
        messagebox.showerror("Error en el acceso")
  
    
botonVerde=Button(seccion1,text="Boton Verde",bg="green",command=im)
botonVerde.pack()   




ventana.mainloop()

