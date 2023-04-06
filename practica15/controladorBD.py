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
    
    #Metodo para buscar un usuario
    def consultarUsuario(self,id):
        #1 preparar conexion
        conx=self.conexionBD()
        #2 verificar si id tiene algo 
        if(id==""):
            messagebox.showwarning("Cuidado","Id vacio, escribe un id valido")
        else:
            try:
                
                #3 preparar cursor y query
                cursor=conx.cursor()
                selecQry = "SELECT * FROM TBregistrados WHERE id="+id
                
                #4 ejecutar y guardar la consulta
                cursor.execute(selecQry)
                rsUsuario = cursor.fetchall()
                conx.close()
                messagebox.showinfo("Listo","Usuario Encontrado")
                return rsUsuario
                
            except sqlite3.OperationalError:
             print("Error Consulta")
             conx.close()
    
    def mostrarUsu(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        qrMostrar= "SELECT * FROM TBregistrados"
        
        cursor.execute(qrMostrar)
        msUsuario=cursor.fetchall()
        return msUsuario
    
    #Metodo para eliminar un usuario
    def eliminarUsuario(self,id):
        #1 preparar conexion
        conx=self.conexionBD()
        #2 verificar si id tiene algo 
        if(id==""):
            messagebox.showwarning("Cuidado","Id vacio, escribe un id valido")
        else:
            try:
                
                #3 preparar cursor y query
                cursor=conx.cursor()
                selecQry = "DELETE FROM TBregistrados WHERE id="+id
                
                #4 ejecutar y guardar la consulta
                cursor.execute(selecQry)
                conx.commit()
                conx.close()
                messagebox.showinfo("Listo","Usuario Eliminado")
                
                
                
            except sqlite3.OperationalError:
             messagebox.showerror("Error","Usuario no existe")
             conx.close()     
               
    #Metodo para actualizar usuarios
    def actualizarUsuario(self,nom,cor,con,id):
        #Importar conexion
        conx= self.conexionBD()
        
        #Validar campos
        if(nom=="" or con=="" or cor=="" or id==""):
            messagebox.showwarning("Ojitooo!","Formulario incompleto")
        else:
            
            #Preparamos cursor,datos,querySQL
            cursor=conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert= "UPDATE TBregistrados SET nombre=?, correo=?, contra=? WHERE ID="+id
            
            #Ejrecutar insercion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Usuario Actualizado")

    
   
 