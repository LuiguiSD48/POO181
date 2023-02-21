#Importar pj
from Personaje import *

#Instanciar un objeto
Heroe= Personaje()

#Acceder a sus atributos
print("ATRIBUTOS DE PJ")
print("El personaje pertenece a la raza: "+Heroe.especie)
print("Se llama: "+Heroe.nombre)
print("Mide: "+str(Heroe.altura)+" mts")

#Acceder a sus metodos
print("METODOS DE PJ")
Heroe.lanzarGranada()
Heroe.correr(True)
Heroe.recargarArma(16)
