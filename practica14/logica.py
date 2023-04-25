from tkinter import messagebox
import sqlite3


class usuario:
 
     def __init__(self):
        pass

     def conexionBD(self):
        try: 
                     conexion=sqlite3.connect("C:/Users/Luis/Documents/GitHub/POO181/practica14/CajaPopular.db")
                     print("Conectado a la base de datos")
                     return conexion
        
        except sqlite3.OperationalError:
                     print("No se pudo conectar")
         
     def guardarUsuario(self,tit,edad,saldo):
        #Importar conexion
        conx= self.conexionBD()
        
        #Validar campos
        if(tit=="" or edad=="" or saldo==""):
            messagebox.showwarning("Ojitooo!","Formulario incompleto")
        else:
            
            #Preparamos cursor,datos,querySQL
            cursor=conx.cursor()
         
            datos=(tit,edad,saldo)
            qrInsert= "insert into usuarios (Titular,Edad,Saldo) values (?,?,?)"
            
            #Ejrecutar insercion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Usuario Guardado")
    
    
     def consultarSaldo(self,cuenta):
         conx= self.conexionBD()
        
        #Validar campos
         if(cuenta==""):
                     messagebox.showwarning("Ojitooo!","Formulario incompleto")
         else:
            
                     #Preparamos cursor,datos,querySQL
                     cursor=conx.cursor()
         
                     selecQry = "SELECT saldo FROM usuarios WHERE Cuenta="+cuenta
            
                     cursor.execute(selecQry)
                     rsUsuario = cursor.fetchall()
                     conx.close()
                     messagebox.showinfo("Su saldo es",str(rsUsuario))   
        
     def retirarSaldo(self,cuenta,saldo):
         conx= self.conexionBD()
         if(cuenta==""):
                     messagebox.showwarning("Ojitooo!","Formulario incompleto")
         else:
            
                     #Preparamos cursor,datos,querySQL
                     cursor=conx.cursor()
         
                     selecQry = "SELECT saldo FROM usuarios WHERE Cuenta="+cuenta
            
                     cursor.execute(selecQry)
                     rsUsuario = cursor.fetchall()
                     conx.close()

                     cantidad=str(rsUsuario)
                     cantidad=int(cantidad)
                     nuevacan=cantidad-int(saldo) 
                     print(str(nuevacan))     
      
        

        

        
 

