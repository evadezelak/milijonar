import tkinter as tk
from tkinter import *
import random
import time
import winsound

nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

def preberi_datoteko(seznam, ime):
   with open(ime, "r", encoding = "utf-8") as file:
      for vrstica in file:
         seznam.append(vrstica.strip())
   return seznam

def ustvari_vprasanja():
   global vprasanja_prvi_nivo,vprasanja_drugi_nivo,vprasanja_tretji_nivo , odgovori_A_prvi, odgovori_B_prvi, odgovori_C_prvi, odgovori_D_prvi,odgovori_A_drugi,odgovori_B_drugi,odgovori_C_drugi,odgovori_D_drugi
   global odgovori_A_tretji, odgovori_B_tretji, odgovori_C_tretji, odgovori_D_tretji, resitve_prvi_nivo, resitve_drugi_nivo, resitve_tretji_nivo
   vprasanja_prvi_nivo = []
   vprasanja_drugi_nivo = []
   vprasanja_tretji_nivo = []
   odgovori_A_prvi = []
   odgovori_B_prvi = []
   odgovori_C_prvi = []
   odgovori_D_prvi = []
   odgovori_A_drugi = []
   odgovori_B_drugi = []
   odgovori_C_drugi = []
   odgovori_D_drugi = []
   odgovori_A_tretji = []
   odgovori_B_tretji = []
   odgovori_C_tretji = []
   odgovori_D_tretji = []
   resitve_prvi_nivo = []
   resitve_drugi_nivo = []
   resitve_tretji_nivo = []
   vprasanja_prvi_nivo = preberi_datoteko(vprasanja_prvi_nivo, "vprasanja_prvi_nivo.txt")
   vprasanja_drugi_nivo = preberi_datoteko(vprasanja_drugi_nivo, "vprasanja_drugi_nivo.txt")
   vprasanja_tretji_nivo = preberi_datoteko(vprasanja_tretji_nivo, "vprasanja_tretji_nivo.txt")
   odgovori_A_prvi = preberi_datoteko(odgovori_A_prvi, "odgovori_A_prvi_nivo.txt")
   odgovori_B_prvi = preberi_datoteko(odgovori_B_prvi, "odgovori_B_prvi_nivo.txt")
   odgovori_C_prvi = preberi_datoteko(odgovori_C_prvi, "odgovori_C_prvi_nivo.txt")
   odgovori_D_prvi = preberi_datoteko(odgovori_D_prvi, "odgovori_D_prvi_nivo.txt")
   odgovori_A_drugi = preberi_datoteko(odgovori_A_drugi, "odgovori_A_drugi_nivo.txt")
   odgovori_B_drugi = preberi_datoteko(odgovori_B_drugi, "odgovori_B_drugi_nivo.txt")
   odgovori_C_drugi = preberi_datoteko(odgovori_C_drugi, "odgovori_C_drugi_nivo.txt")
   odgovori_D_drugi = preberi_datoteko(odgovori_D_drugi, "odgovori_D_drugi_nivo.txt")
   odgovori_A_tretji = preberi_datoteko(odgovori_A_tretji, "odgovori_A_drugi_nivo.txt")
   odgovori_B_tretji = preberi_datoteko(odgovori_B_tretji, "odgovori_B_drugi_nivo.txt")
   odgovori_C_tretji = preberi_datoteko(odgovori_C_tretji, "odgovori_C_drugi_nivo.txt")
   odgovori_D_tretji = preberi_datoteko(odgovori_D_tretji, "odgovori_D_drugi_nivo.txt")
   resitve_prvi_nivo = preberi_datoteko(resitve_prvi_nivo, "resitve_prvi_nivo.txt")
   resitve_drugi_nivo = preberi_datoteko(resitve_drugi_nivo, "resitve_drugi_nivo.txt")
   resitve_tretji_nivo = preberi_datoteko(resitve_tretji_nivo, "resitve_tretji_nivo.txt")

def izhod__(x):
   x.destroy()

def zmagovalno_okno(zacetek):
   zmagovalno = tk.Tk()
   zacetek.destroy()
   zmagovalno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   ozadje = tk.PhotoImage(file = "zmaga.gif")
   ozadje_s_sliko = tk.Label(zmagovalno, image = ozadje)
   ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
   zmagovalno.mainloop()
def poraz(zacetek):
   zakljucno = tk.Tk()
   zacetek.destroy()
   zakljucno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   zakljucno.configure(background = "deep sky blue")
   koncaj = tk.Label(zakljucno, text = "Ostali ste brez nagrade, več sreče prihodnjič!", fg = "navy", font = ("Comic Sans MS", 30))
   koncaj.place(relx = .5, rely = .4, anchor = "center")
   izhod1 = tk.Button(zakljucno, text = "Izhod", fg = "navy", font = ("Comic Sans MS", 25), command = lambda: izhod__(zakljucno))
   izhod1.place(relx = .5, rely = .5, anchor = "center")
   ponovna_igra = tk.Button(zakljucno, text = "Poskusi znova", fg = "navy", font = ("Comic Sans MS", 25), command = lambda : ponovna_igra_fun(zakljucno))
   ponovna_igra.place(relx = .5, rely = .6, anchor = "center")
   zakljucno.mainloop()

def vrni_pravilni_odgovor_prvi_nivo(vprasanje, izbira):
   pravilni_odgovor = ''
   if(izbira == 'a'):
         pravilni_odgovor = odgovori_A_prvi[vprasanje]
   elif(izbira == 'b'):
         pravilni_odgovor = odgovori_B_prvi[vprasanje]
   elif(izbira == 'c'):
         pravilni_odgovor = odgovori_C_prvi[vprasanje]
   elif(izbira == 'd'):
         pravilni_odgovor = odgovori_D_prvi[vprasanje]
   del odgovori_A_prvi[vprasanje]
   del odgovori_B_prvi[vprasanje]
   del odgovori_C_prvi[vprasanje]
   del odgovori_D_prvi[vprasanje]
   return pravilni_odgovor

def vrni_pravilni_odgovor_drugi_nivo(vprasanje, izbira):
   pravilni_odgovor = ''
   if(izbira == 'a'):
         pravilni_odgovor = odgovori_A_drugi[vprasanje]
   elif(izbira == 'b'):
         pravilni_odgovor = odgovori_B_drugi[vprasanje]
   elif(izbira == 'c'):
         pravilni_odgovor = odgovori_C_drugi[vprasanje]
   elif(izbira == 'd'):
         pravilni_odgovor = odgovori_D_drugi[vprasanje]
   del odgovori_A_drugi[vprasanje]
   del odgovori_B_drugi[vprasanje]
   del odgovori_C_drugi[vprasanje]
   del odgovori_D_drugi[vprasanje]
   return pravilni_odgovor

def vrni_pravilni_odgovor_tretji_nivo(vprasanje, izbira):
   pravilni_odgovor = ''
   if(izbira == 'a'):
         pravilni_odgovor = odgovori_A_tretji[vprasanje]
   elif(izbira == 'b'):
         pravilni_odgovor = odgovori_B_tretji[vprasanje]
   elif(izbira == 'c'):
         pravilni_odgovor = odgovori_C_tretji[vprasanje]
   elif(izbira == 'd'):
         pravilni_odgovor = odgovori_D_tretji[vprasanje]
   del odgovori_A_tretji[vprasanje]
   del odgovori_B_tretji[vprasanje]
   del odgovori_C_tretji[vprasanje]
   del odgovori_D_tretji[vprasanje]
   return pravilni_odgovor

def preveri_odgovor(vprasanje,zacetek, izbira):
   
   global stevilka_vprasanja
   pravilna_izbira = ''
   if(stevilka_vprasanja <= 5):
      pravilna_izbira = resitve_prvi_nivo[vprasanje]
      del resitve_prvi_nivo[vprasanje]
   elif(stevilka_vprasanja > 5 and stevilka_vprasanja <= 10):
      pravilna_izbira = resitve_drugi_nivo[vprasanje]
      del resitve_drugi_nivo[vprasanje]
   elif(stevilka_vprasanja > 10):
      pravilna_izbira = resitve_tretji_nivo[vprasanje]
      del resitve_tretji_nivo[vprasanje]
   elif(stevilka_vprasanja == 15):
       pravilna_izbira = resitve_tretji_nivo[vprasanje]
       del resitve_tretji_nivo[vprasanje]

   pravilni_odgovor = ''
   if(stevilka_vprasanja <= 5):
      pravilni_odgovor = vrni_pravilni_odgovor_prvi_nivo(vprasanje, pravilna_izbira)
   elif(stevilka_vprasanja > 5 and stevilka_vprasanja <= 10):
      pravilni_odgovor = vrni_pravilni_odgovor_drugi_nivo(vprasanje, pravilna_izbira)
   elif(stevilka_vprasanja > 10):
      pravilni_odgovor = vrni_pravilni_odgovor_tretji_nivo(vprasanje, pravilna_izbira)
   elif(stevilka_vprasanja == 15):
      pravilni_odgovor = vrni_pravilni_odgovor_tretji_nivo(vprasanje, pravilna_izbira)

   if(izbira != pravilna_izbira):
      A.destroy()
      B.destroy()
      C.destroy()
      D.destroy()
      napacno = tk.Label(zacetek, text = "Žal je vaš odgovor napačen, pravilen odgovor je\n" + pravilni_odgovor, fg = "navy", font = ("Comic Sans MS", 20))
      napacno.place(relx = .5 , rely = .3, anchor = "center")
      zakljuci = tk.Button(zacetek, text = "Naprej", fg = "navy", font = ("Comis Sans MS", 20), command = lambda : poraz(zacetek) )
      zakljuci.place(relx = .5 , rely = .4, anchor = "center")
      
   elif(izbira == pravilna_izbira):
      A.destroy()
      B.destroy()
      C.destroy()
      D.destroy()
      zasluzeni_denar = nagrada[stevilka_vprasanja-1]
      if(stevilka_vprasanja == 5):
         pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(zasluzeni_denar) + " Eurov", fg = "navy", font = ("Comic Sans MS", 20))
         pravilno.place(relx = .5 , rely = .3, anchor = "center")
         naprej = tk.Button(zacetek, text = "Naprej", fg = "navy", font = ("Comis Sans MS", 20), command = lambda : zacni(zacetek) )
         naprej.place(relx = .5 , rely = .4, anchor = "center")
         opomba = tk.Label(zacetek, text = "Prva stopnja opravljena!", fg = "navy",font = ("Comic Sans MS", 20) )
         opomba.place(relx = .2, rely = .4, anchor = "center")
      elif(stevilka_vprasanja == 10):
         pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(zasluzeni_denar) + " Eurov", fg = "navy", font = ("Comic Sans MS", 20))
         pravilno.place(relx = .5 , rely = .3, anchor = "center")
         naprej = tk.Button(zacetek, text = "Naprej", fg = "navy", font = ("Comis Sans MS", 20), command = lambda : zacni(zacetek) )
         naprej.place(relx = .5 , rely = .4, anchor = "center")
         opomba = tk.Label(zacetek, text = "Druga stopnja opravljena!", fg = "navy",font = ("Comic Sans MS", 20) )
         opomba.place(relx = .2, rely = .4, anchor = "center")
      elif(stevilka_vprasanja == 15):
         naprej = tk.Button(zacetek, text = "Naprej", fg = "navy", font = ("Comis Sans MS", 20), command = lambda : zmagovalno_okno(zacetek) )
         naprej.place(relx = .5 , rely = .7, anchor = "center")
         opomba = tk.Label(zacetek, text = "Čestitke postali ste milijonar!!!", fg = "navy",font = ("Comic Sans MS", 40) )
         opomba.place(relx = .5, rely = .5, anchor = "center")
      else:
         pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(zasluzeni_denar) + " Eurov", fg = "navy", font = ("Comic Sans MS", 20))
         pravilno.place(relx = .5 , rely = .3, anchor = "center")
         naprej = tk.Button(zacetek, text = "Naprej", fg = "navy", font = ("Comis Sans MS", 20), command = lambda : zacni(zacetek) )
         naprej.place(relx = .5 , rely = .4, anchor = "center")
      stevilka_vprasanja = stevilka_vprasanja +1
      
         
   
def izberi_novo_vprasanje():
   novo = ''
   vprasanje = ''
   seznam = ['','']
   if(stevilka_vprasanja <= 5):
      novo = random.randint(0, len(vprasanja_prvi_nivo)-1)
      vprasanje = vprasanja_prvi_nivo[novo]
      seznam[0] = novo;
      seznam[1] = vprasanje;
   elif(stevilka_vprasanja > 5 and stevilka_vprasanja <= 10):
      novo = random.randint(0, len(vprasanja_drugi_nivo)-1)
      vprasanje = vprasanja_drugi_nivo[novo]
      seznam[0] = novo;
      seznam[1] = vprasanje;
   elif(stevilka_vprasanja > 10):
      novo = random.randint(0, len(vprasanja_tretji_nivo)-1)
      vprasanje = vprasanja_tretji_nivo[novo]
      seznam[0] = novo;
      seznam[1] = vprasanje;
   return seznam

def zacni(okno):
   winsound.PlaySound("Who Wants", winsound.SND_ALIAS | winsound.SND_ASYNC)
   okno.destroy()
   zacetek = tk.Tk()
   zacetek.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   ozadje = tk.PhotoImage(file = "drugo_ozadje.gif")
   ozadje_s_sliko = tk.Label(zacetek, image = ozadje)
   ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)  
   okvir = tk.Frame(zacetek)
   okvir.pack()
   global stevilka_vprasanja
   print(stevilka_vprasanja)
   
   vprasanje_indeks = izberi_novo_vprasanje()
   
   vprasanje = vprasanje_indeks[1]
   indeks = int(vprasanje_indeks[0])
   novo = tk.Label(okvir, text = vprasanje, fg = "navy",  font = ("Comic Sans MS", 20  ))
   novo.pack()
   global A, B, C, D
   if(stevilka_vprasanja <= 5):
      A = tk.Button(zacetek, text = odgovori_A_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'a'))
      B = tk.Button(zacetek, text = odgovori_B_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30),command = lambda: preveri_odgovor(indeks,zacetek, 'b'))
      C = tk.Button(zacetek, text = odgovori_C_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'c'))
      D = tk.Button(zacetek, text = odgovori_D_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'd'))
   elif(stevilka_vprasanja > 5 and stevilka_vprasanja <= 10):
      A = tk.Button(zacetek, text = odgovori_A_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'a'))
      B = tk.Button(zacetek, text = odgovori_B_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30),command = lambda: preveri_odgovor(indeks,zacetek, 'b'))
      C = tk.Button(zacetek, text = odgovori_C_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'c'))
      D = tk.Button(zacetek, text = odgovori_D_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'd'))
   elif(stevilka_vprasanja > 10):
      A = tk.Button(zacetek, text = odgovori_A_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'a'))
      B = tk.Button(zacetek, text = odgovori_B_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30),command = lambda: preveri_odgovor(indeks,zacetek, 'b'))
      C = tk.Button(zacetek, text = odgovori_C_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'c'))
      D = tk.Button(zacetek, text = odgovori_D_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: preveri_odgovor(indeks,zacetek, 'd'))
   A.place(relx = .4, rely = .4, anchor = "center")
   B.place(relx = .6, rely = .4, anchor = "center")
   C.place(relx = .4, rely = .5, anchor = "center")
   D.place(relx = .6, rely = .5, anchor = "center")
   if(stevilka_vprasanja <= 5):
      del vprasanja_prvi_nivo[indeks]
      
   elif(stevilka_vprasanja > 5 and stevilka_vprasanja <= 10):
      del vprasanja_drugi_nivo[indeks]
      
   elif(stevilka_vprasanja > 10):
      del vprasanja_tretji_nivo[indeks]
    
   zacetek.mainloop()

def ponovna_igra_fun(zakljucna):
   zakljucna.destroy()
   okno =  tk.Tk()
   glasba = "Who - Wants.wav"
   winsound.PlaySound(glasba, winsound.SND_ALIAS | winsound.SND_ASYNC)
   global stevilka_vprasanja, zasluzeni_denar, sirina_okna, visina_okna
   sirina_okna = okno.winfo_screenwidth()
   visina_okna = okno.winfo_screenheight()
   ustvari_vprasanja()
   zasluzeni_denar = 0
   stevilka_vprasanja = 15
   okno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   ozadje = tk.PhotoImage(file = "milijonar_ozadje.jpg")
   ozadje_s_sliko = tk.Label(okno, image = ozadje)
   ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
   #okno.configure(background = "blue")
   #tk.Label(okno, text = "Milijonar", font = ("Comic Sans MS", 120)).place(relx = .5 , rely = .4, anchor = "center")
   gumb_za_zacetek = tk.Button(okno, text = "Začni z igro", font = ("Comic Sans MS", 20  ), command = lambda: zacni(okno))
   gumb_za_zacetek.place(relx = .5, rely = .6 , anchor = "center")
   izhod = tk.Button(okno, text = "Neupam :(", font = ("Comic Sans MS", 20  ), command = lambda: izhod__(okno))
   izhod.place(relx = .5, rely = .7 , anchor = "center")
def prva():
   okno =  tk.Tk()
   glasba = "Who - Wants.wav"
   winsound.PlaySound(glasba, winsound.SND_ALIAS | winsound.SND_ASYNC)
   global stevilka_vprasanja, zasluzeni_denar, sirina_okna, visina_okna
   sirina_okna = okno.winfo_screenwidth()
   visina_okna = okno.winfo_screenheight()
   ustvari_vprasanja()
   zasluzeni_denar = 0
   stevilka_vprasanja = 15
   okno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   ozadje = tk.PhotoImage(file = "mil.gif")
   ozadje_s_sliko = tk.Label(okno, image = ozadje)
   ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
   #okno.configure(background = "blue")
   #tk.Label(okno, text = "Milijonar", font = ("Comic Sans MS", 120)).place(relx = .5 , rely = .4, anchor = "center")
   gumb_za_zacetek = tk.Button(okno, text = "Začni z igro",fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: zacni(okno))
   gumb_za_zacetek.place(relx = .1, rely = .5 , anchor = "center")
   izhod = tk.Button(okno, text = "Neupam :(", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: izhod__(okno))
   izhod.place(relx = .9, rely = .5 , anchor = "center")

   #print("Pozdravljena %s\n" % (vnos1.get())).grid( row = y - 1, column = x - 1)
   ### ozadje to be
   #photo = tk.PhotoImage(file = "milijonarlogo")
   #slika = tk.Label(okno, image = photo)
   ##ozadje = tk.PhotoImage(data = b64_ozadja)
   ##oznaka_ozadja = tk.Label(parent, image = ozadje)
   ##oznaka_ozadja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
   ###

   okno.mainloop()

prva()
