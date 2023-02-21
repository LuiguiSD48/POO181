
class Personaje:
    
    #atributos
    especie="Humano"
    nombre="Marcus Fenix"
    altura=1.90
    
    #Metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" se detuvo")
            
    def lanzarGranada(self):
        print("Se lanzo granada")
        
    def recargarArma(self,municiones):
        cargador=5
        cargador=cargador+municiones
        print("El arma tiene ahora "+ str(cargador)+" balas")