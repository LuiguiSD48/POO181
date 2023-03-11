from tkinter import messagebox


class usuario:
    
 def __init__(self,cuen,nom,edad,saldo):
        #atributos
        self.__cuenta=cuen
        self.__nombre=nom
        self.__edad=edad
        self.__saldo=saldo
      
 def mostrarSaldo(self):
        messagebox.showinfo("Su saldo es", usuario.__saldo)
    
 def ingresarEfectivo(self,cantidad):
        usuario.__saldo=usuario.__saldo+cantidad
        messagebox.showinfo("Su nuevo saldo es", usuario.__saldo)   
        
 def retirarEfectivo(self,dispo):
        usuario.__saldo=usuario.__saldo-dispo
        messagebox.showinfo("Su nuevo saldo es", usuario.__saldo)           
        

        
 def getCuenta(self):
        return self.__especie
    
 def setCuenta(self,cuen):
        self.__cuenta=cuen
    
 def getTitular(self):
        return self.__nombre
    
 def setTitular(self,nom):
        self.__nombre=nom
        
 def getEdad(self):
        return self.__edad
    
 def setCuenta(self,edad):
        self.__edad=edad
        
 def getSaldo(self):
        return self.__saldo
    
 def setCuenta(self,saldo):
        self.__saldo=saldo
        
