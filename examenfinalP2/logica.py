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
        numerx=numero1
        romanos = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev = 0
        
        import re
        
        
        if ((bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",numerx)))==False):
            messagebox.showerror("Error","Numero invalido")
        else:
           

            for letra in numero1[::-1]:
                valor = romanos[letra]
                total += valor if valor >= prev else -valor
                prev = valor
      
            if(total>50):
                messagebox.showerror("Listo","El numero excede 50")
            else:
                messagebox.showinfo("Listo",str(total)) 
        
        
    