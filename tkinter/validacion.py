

class cUsuario:

    
    def __init__(self,usu,con):
        #atributos
        self.__usuario=usu
        self.__contrasena=con
        
    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self,usu):
        self.__usuario=usu
        
    def getContrasena(self):
        return self.__contrasena
    
    def setContrasena(self,con):
        self.__contrasena=con
    

    def validar1(usuario11,usuario22):
        if usuario11.getUsuario==usuario22.getUsuario:
            if usuario11.getContrasena==usuario22.getContrasena:
                return True
            else :
                return False
        else:
            return False

         
 
            