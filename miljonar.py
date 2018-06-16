import tkinter as tk
from tkinter import *
import random
import time

resitve = ['a','b','b','a']
nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

def ustvari_vprasanja():
   global vprasanja, odgovoriA, odgovoriB, odgovoriC, odgovoriD
   vprasanja = []
   odgovoriA = []
   odgovoriB = []
   odgovoriC = []
   odgovoriD = []
   v = open('vprasanja.txt', 'r', encoding = "utf-8")
   a = open('odgovori A.txt', 'r', encoding = "utf-8")
   b = open('odgovori B.txt', 'r', encoding = "utf-8")
   c = open('odgovori C.txt', 'r', encoding = "utf-8")
   d = open('odgovori D.txt', 'r', encoding = "utf-8")
   for vrstica in v:
      vprasanja.append(vrstica.strip())
   for vrstica in a:
      odgovoriA.append(vrstica.strip())
   for vrstica in b:
      odgovoriB.append(vrstica.strip())
   for vrstica in c:
     odgovoriC.append(vrstica.strip())
   for vrstica in d:
      odgovoriD.append(vrstica.strip())

def izhod(okno):
   okno.destroy()
   
def poraz(zacetek):
   zakljucno = tk.Tk()
   zacetek.destroy()
   zakljucno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   zakljucno.configure(background = "deep sky blue")
   koncaj = tk.Label(zakljucno, text = "Ostali ste brez nagrade, več sreče prihodnjič!", fg = "navy", font = ("Comic Sans MS", 30))
   koncaj.place(relx = .5, rely = .5, anchor = "center")
   izhod = tk.Button(zacetek, text = "Izhod", fg = "navy", font = ("Comic Sans MS", 25), command = lambda: izhod(zakljucno))
   izhod.pack()
   zakljucno.mainloop()

def preveri_odgovor(vprasanje,zacetek, izbira):
   pravilni_odgovor = ''
   if(izbira == 'a'):
      pravilni_odgovor = odgovoriA[vprasanje]
   elif(izbira == 'b'):
      pravilni_odgovor = odgovoriB[vprasanje]
   elif(izbira == 'c'):
      pravilni_odgovor = odgovoriC[vprasanje]
   elif(izbira == 'd'):
      pravilni_odgovor = odgovoriD[vprasanje]
   if(izbira != resitve[vprasanje]):
      #novo vprasanje 
      napacno = tk.Label(zacetek, text = "Žal je vaš odgovor napačen, pravilen odgovor je\n" + pravilni_odgovor, fg = "navy", font = ("Comic Sans MS", 20))
      napacno.place(relx = .5 , rely = .6, anchor = "center")
      time.sleep(5)
      poraz(zacetek)
                        
   
def zacni(stevilka_vprasanja):
   
   zacetek = tk.Tk()
   okno.destroy()
   zacetek.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   zacetek.configure(background = "deep sky blue")
   ustvari_vprasanja()
   okvir = tk.Frame(zacetek)
   okvir.pack()
   stevlika_v = stevilka_vprasanja +1   
   vprasanje = random.randint(0, len(vprasanja)-1)
   novo = tk.Label(okvir, text = vprasanja[vprasanje], fg = "navy",  font = ("Comic Sans MS", 20  ))
   novo.pack()
   A = tk.Button(zacetek, text = odgovoriA[vprasanje], fg ="blue", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(vprasanje,zacetek, 'a'))
   B = tk.Button(zacetek, text = odgovoriB[vprasanje], fg ="blue", font = ("Comic Sans MS", 30),command = lambda: preveri_odgovor(vprasanje,zacetek, 'b'))
   C = tk.Button(zacetek, text = odgovoriC[vprasanje], fg ="blue", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(vprasanje,zacetek, 'c'))
   D = tk.Button(zacetek, text = odgovoriD[vprasanje], fg ="blue", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(vprasanje,zacetek, 'd'))
   A.place(relx = .4, rely = .4, anchor = "center")
   B.place(relx = .6, rely = .4, anchor = "center")
   C.place(relx = .4, rely = .5, anchor = "center")
   D.place(relx = .6, rely = .5, anchor = "center")
   #del vprasanja[vprasanje]
   zacetek.mainloop()



okno =  tk.Tk()
sirina_okna = okno.winfo_screenwidth()
visina_okna = okno.winfo_screenheight()
stevilka_vprasanja = 0
okno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
okno.configure(background = "blue")
tk.Label(okno, text = "Milijonar", font = ("Comic Sans MS", 120)).place(relx = .5 , rely = .4, anchor = "center")
gumb_za_zacetek = tk.Button(okno, text = "Začni z igro", font = ("Comic Sans MS", 20  ), command = lambda: zacni(stevilka_vprasanja))
gumb_za_zacetek.place(relx = .5, rely = .6 , anchor = "center")
izhod = tk.Button(okno, text = "Neupam :(", font = ("Comic Sans MS", 20  ), command = izhod)
izhod.place(relx = .5, rely = .7 , anchor = "center")

#print("Pozdravljena %s\n" % (vnos1.get())).grid( row = y - 1, column = x - 1)
### ozadje to be
#photo = tk.PhotoImage(file = "milijonarlogo")
#slika = tk.Label(okno, image = photo)
##ozadje = tk.PhotoImage(data = b64_ozadja)
##oznaka_ozadja = tk.Label(parent, image = ozadje)
##oznaka_ozadja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
###

okno.mainloop()
