from tkinter import messagebox
import math

class logica():
    
    def __init__(self):
        pass
    
    
    def conversor(numero):
        numero=int(numero)
        if numero>50:
            messagebox.showerror("Error","Solo numeros entre 1 y 50")
        else:
            Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
            Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            N=numero
            u= N % 10
            d=int(math.floor(N/10))%10
            c=int(math.floor(N/100))
            if(N>=100): 
                messagebox.showinfo("Listo",str(Centena[c]+Decena[d]+Unidad[u]))
            else:
             if(N>=10):
                   messagebox.showinfo("Listo",str(Decena[d]+Unidad[u]))
             else:
                   messagebox.showinfo("Listo",str(Unidad[N]))
                   
                   
    def conversor1(numero1):
        
        
        romanos = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 12
        valor = numero1
        entero=romanos[valor[0]];
        for i in range(1,len(valor)):
            if romanos[valor[i - 1]] < romanos[valor[i]]:
                entero += (romanos[valor[i]] - 2) * romanos[valor[i - 1]]
            else:
                entero += romanos[valor[i]]
        if(entero>50):
            messagebox.showerror("Listo","El numero excede 50")
        else:
         messagebox.showinfo("Listo",str(entero)) 
        
        
    