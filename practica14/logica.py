from tkinter import messagebox


class usuario:
 
 def __init__(self,nom,edad,saldo,cuenta):
        #atributos

        self.__nombre=nom
        self.__edad=edad
        self.__saldo=saldo
        self.__cuenta=cuenta
      
 def mostrarSaldo(self):
        messagebox.showinfo("Su saldo es",self.__saldo)
    
 def ingresarEfectivo(self,cantidad):
        usuario.__saldo=usuario.__saldo+int(cantidad)
        messagebox.showinfo("Su nuevo saldo es", usuario.__saldo)   
        
 def retirarEfectivo(self,dispo):
        usuario.__saldo=usuario.__saldo-int(dispo)
        messagebox.showinfo("Su nuevo saldo es", usuario.__saldo)           
        

        
 def getCuenta(self):
        return self.__cuenta
    
 def setCuenta(self,cuenta):
        self.__cuenta=cuenta
    
 def getNombre(self):
        return self.__nombre
    
 def setNombre(self,nom):
        self.__nombre=nom
        
 def getEdad(self):
        return self.__edad
    
 def setEdad(self,edad):
        self.__edad=edad
        
 def getSaldo(self):
        return self.__saldo
    
 def setCuenta(self,saldo):
        self.__saldo=saldo
        
