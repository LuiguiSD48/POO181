
class Personaje:
    
    
    def __init__(self,esp,nom,alt):
        #atributos
        self.__especie=esp
        self.__nombre=nom
        self.__altura=alt
  
    
    #Metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.__nombre+" esta corriendo")
        else:
            print("El personaje "+self.__nombre+" se detuvo")
            
    def lanzarGranada(self):
        print("Se lanzo granada")
        
    def recargarArma(self,municiones):
        cargador=5
        cargador=cargador+municiones
        print("El arma tiene ahora "+ str(cargador)+" balas")
        
    def __pensar(selg):
        print("Toy pensanding........")
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie=esp
        

    