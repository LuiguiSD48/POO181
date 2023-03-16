from tkinter import messagebox


class usuario:
 
 def init(self,nom,app,apm,nac,cur,car):
        #atributos

       nombre=nom
       apeidop=app
       apeidom=apm
       fnacimiento=nac
       fcurso=cur
       carrera=car
      
 def CrearM():
        messagebox.showinfo("cadena",usuario.nombre+usuario.apeidop+usuario.apeidom)  
    