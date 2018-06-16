import tkinter as tk
import random

okno =  tk.Tk()
##okno.overrideredirect(True)
okno.geometry("{0}x{1}+0+0".format(okno.winfo_screenwidth(), okno.winfo_screenheight()))
def zacetni_pozdrav():
   Label(okno, text="Vnesi svoje ime").grid(row=15, column = 30)
   vnos1 = Entry(master)
   vnos1.grid(row = 16, column = 31)
   print("Pozdravljena %s\n" % (vnos1.get()))
resitve = ['a','b','b','a']
nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]




    

okno.mainloop()
