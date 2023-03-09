
from tkinter import Tk,Frame,Button,messagebox

def mostrarMensaje():
    messagebox.showinfo("Aviso","Este mensaje es para informar")
    messagebox.showerror("Error","Este mensaje fallo con exito")
    messagebox.askokcancel("Pregunta","El o ella jugo con tu corazon?")
  

def agregarBoton():
    botonVerde.config(text="+",bg="green",fg="white")
    botonNuevo= Button(seccion3,text="Boton Nuevo")
    botonNuevo.pack()
    

#1 Instanciamos el objeto ventana
ventana=Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry('600x400')

#2 Definimos secciones de la ventana
seccion1=Frame(ventana,bg="#00e6e6")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="#99ff99")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="#cc99ff")
seccion3.pack(expand=True,fill='both')

#3 Botones
botonAzul=Button(seccion1,text="Boton Azul",fg="blue",command=mostrarMensaje)
botonAzul.place(x=60,y=60)

botonAmarillo=Button(seccion2,text="Boton Amarillo",bg="yellow")
botonAmarillo.grid(row=0,column=0)

botonNegro=Button(seccion2,text="Boton Negro",bg="black",fg="white")
botonNegro.grid(row=1,column=1)

botonVerde=Button(seccion3,text="Boton Verde",bg="green", command=agregarBoton)
botonVerde.pack()   

#Iniciamos la ventana
ventana.mainloop()