from tkinter import messagebox
import random, string
class logica():
    def generarContra(lon,mayus,carac):
        lon=int(lon)
        if mayus==1:
            if carac==1:
                length_of_string = lon

                messagebox.showinfo("Contraseña generada",''.join(random.choice(string.ascii_letters+str('+*-%/&#!?¿')+string.digits) for _ in range(length_of_string)))
            
            else:
                length_of_string = lon

                messagebox.showinfo("Contraseña generada",''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length_of_string)))
                        
        else:
            if carac==1:
                length_of_string = lon

                messagebox.showinfo("Contraseña generada",''.join(random.choice(string.ascii_lowercase+str('+*-%/&#!?¿')+string.digits) for _ in range(length_of_string)))
            
            else:
                
                length_of_string = lon

                messagebox.showinfo("Contraseña generada",''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(length_of_string)))