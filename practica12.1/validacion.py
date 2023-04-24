from tkinter import messagebox

class Usuario:

    
    def __init__(self):
        #atributos
        self.__usuario="luissandoval"
        self.__contrasena="121041263"
        
    

    def validar1(self,usu,contra):
        if (usu=="" or contra==""):
            messagebox.showwarning("Error","Faltan datos en el formulario")
        else:
            if(self.__usuario==usu and self.__contrasena==contra):
                messagebox.showinfo("Exito","Bienvenido al sistema")
            else:
                messagebox.showerror("Error","Usuario o contyraseña incorrecta")


         
 
            