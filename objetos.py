#Importar pj
from Personaje import *

#ISolicitar atributos para el obj
print("")
print("###Solicitud de datpos de heroe###")
espH=input("Escribe la especie del heroe: ")
nomH=input("Escribe el nombre del heroe: ")
altH=float(input("Escribe la altura del heroe: "))
cargaH=int(input("Escribe la carga del heroe: "))

print("")
print("###Solicitud de datos de villano###")
espV=input("Escribe la especie del villano: ")
nomV=input("Escribe el nombre del villanio: ")
altV=float(input("Escribe la altura del villano: "))
cargaV=int(input("Escribe la carga del villano: "))

#3
Heroe= Personaje(espH,nomH,altH)
Villano= Personaje(espV,nomV,altV)



#Acceder a sus atributos
print("ATRIBUTOS DE Heroe")
print("El personaje pertenece a la raza: "+Heroe.especie)
print("Se llama: "+Heroe.nombre)
print("Mide: "+str(Heroe.altura)+" mts")

#Acceder a sus metodos
print("METODOS DE PJ")
Heroe.lanzarGranada()
Heroe.correr(True)
Heroe.recargarArma(cargaH)

print("ATRIBUTOS DE Villano")
print("El personaje pertenece a la raza: "+Villano.especie)
print("Se llama: "+Villano.nombre)
print("Mide: "+str(Villano.altura)+" mts")


print("METODOS DE PJ")
Villano.lanzarGranada()
Villano.correr(False)
Villano.recargarArma(cargaV)
