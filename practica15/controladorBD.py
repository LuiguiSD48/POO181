from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
        
        
    #Metodo para crear conexion a la base de datos
    def conexionBD(self):
    
     try: 
         conexion=sqlite3.connect("C:/Users/Luis/Documents/GitHub/POO181/practica15/DBusuarios.db")
         print("Conectado a la base de datos")
         return conexion
        
     except sqlite3.OperationalError:
         print("No se pudo conectar")
         
    #Metodo para guardar usuarios
    def guardarUsuario(self,nom,cor,con):
        #Importar conexion
        conx= self.conexionBD()
        
        #Validar campos
        if(nom=="" or con=="" or cor==""):
            messagebox.showwarning("Ojitooo!","Formulario incompleto")
        else:
            
            #Preparamos cursor,datos,querySQL
            cursor=conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,conH,cor)
            qrInsert= "insert into TBregistrados(nombre,contra,correo) values (?,?,?)"
            
            #Ejrecutar insercion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Usuario Guardado")
    
    def encriptarCon(self,con):
        conPlana=con
        conplana=conPlana.encode() #convertimos con a bytes
        sal=bcrypt.gensalt()
        conHa= bcrypt.hashpw(conplana,sal)
        print(conHa)
        return conHa

    
   
 