from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
        
        
    #Metodo para crear conexion a la base de datos
    def conexionBD(self):
    
     try: 
         conexion=sqlite3.connect("C:/Users/Luis/Documents/GitHub/POO181/EXAMEN3/Ferreteria.db")
         print("Conectado a la base de datos")
         return conexion
        
     except sqlite3.OperationalError:
         print("No se pudo conectar")
         
    #Metodo para guardar usuarios
    def guardarUsuario(self,nom,can):
        #Importar conexion
        conx= self.conexionBD()
        
        #Validar campos
        if(nom=="" or can==""):
            messagebox.showwarning("Ojitooo!","Formulario incompleto")
        else:
            
            #Preparamos cursor,datos,querySQL
            cursor=conx.cursor()
           
            datos=(nom,can)
            qrInsert= "insert into MatConstruccion(Material,Cantidad) values (?,?)"
            
            #Ejrecutar insercion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Material Guardado")
    
    
    
    def mostrarUsu(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        qrMostrar= "SELECT * FROM MatConstruccion"
        
        cursor.execute(qrMostrar)
        msUsuario=cursor.fetchall()
        return msUsuario
    
    

    #Metodo para actualizar usuarios
    def actualizarUsuario(self,nom,can,id):
        #Importar conexion
        conx= self.conexionBD()
        
        #Validar campos
        if(nom=="" or can=="" or id==""):
            messagebox.showwarning("Ojitooo!","Formulario incompleto")
        else:
            
            #Preparamos cursor,datos,querySQL
            cursor=conx.cursor()
     
            datos=(nom,can)
            qrInsert= "UPDATE MatConstruccion SET Material=?, Cantidad=? WHERE IDMat="+id
            
            #Ejrecutar insercion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Material Actualizado")
