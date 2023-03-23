from tkinter import messagebox
import random

class usuario:
 
 def __init__(self,nom,app,apm,nac,cur,car):
        #atributos

       self.__nombre=nom
       self.__apeidop=app
       self.__apeidom=apm
       self.__fnacimiento=nac
       self.__fcurso=cur
       self.__carrera=car
      
 def CrearM(self):
       x= self.__nombre[0]+self.__apeidop[0]+self.__apeidop[1]+self.__apeidom[0]+self.__apeidom[1]+self.__fnacimiento[2]+self.__fnacimiento[3]+self.__fcurso[2]+self.__fcurso[3]+self.__carrera[0]+self.__carrera[1]+self.__carrera[2]
             
       messagebox.showinfo("cadena",x)  
        
 def getNombre(self):
        return self.__nombre
 def getapp(self):
        return self.__apeidop
 def getapm(self):
        return self.__apeidom
 def getnac(self):
        return self.__fnacimiento
 def getcur(self):
        return self.__fcurso
 def getcar(self):
        return self.__carrera

        

    