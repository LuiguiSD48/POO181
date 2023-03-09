from tkinter import *
import random, string
class logica():
    def generarContra(lon,mayus,carac):
        if lon=="":
            if mayus==True:
                if carac==True:
                    number_of_strings=1
                    length_of_string = 8
                    for x in range(number_of_strings): print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
                    
                    
        