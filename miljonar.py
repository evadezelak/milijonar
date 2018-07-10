
import tkinter as tk
from tkinter import *
import random
import math
import time
import winsound
import os, sys
from PIL import Image, ImageTk


class podatki:
   nagrada = []
   stevilo_vprasanj = 0
   seznam_datotek = []

   def preveri_dolzino_stevk():
      dolzina = 0
      for znak in podatki.seznam_datotek[-1]:
         if znak.isdigit():
            dolzina = dolzina + 1
         else:
            return dolzina
      
   def dodaj_datoteke_v_seznam():
      mapa = os.listdir("vprasanja_in_odgovori/")
      for datoteka in mapa:
         podatki.seznam_datotek.append(datoteka)
      podatki.seznam_datotek.sort(key = lambda f : int(''.join(filter(str.isdigit, f))))
      dolzina_stevk = podatki.preveri_dolzino_stevk()
      zadnje_vprasanje = podatki.seznam_datotek[-1]
      indeks_zadnjega_vprasanja = zadnje_vprasanje[:dolzina_stevk]
      podatki.stevilo_vprasanj = int(indeks_zadnjega_vprasanja) + 1
      
    
   def __init__(self, stevilka_vprasanja, zasluzeni_denar, polovicka):
      podatki.seznam_datotek = []
      self.polovicka = polovicka
      self.stevilka_vprasanja = stevilka_vprasanja
      self.zasluzeni_denar = zasluzeni_denar
      podatki.nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]   
      podatki.dodaj_datoteke_v_seznam()
   
   

class grafika:
   stevilka_vprasanja = -1
   sirina_okna = -1
   visina_okna = -1
   seznam_gumbov = []

   def __init__(self, sirina_okna, visina_okna, podatki, okno, glasba, stevilka_vprasanja, ozadje, ozadje_s_sliko):
      self.sirina_okna = sirina_okna
      self.visina_okna = visina_okna
      self.podatki = podatki
      self.okno = okno
      self.glasba = glasba
      grafika.stevilka_vprasanja = stevilka_vprasanja
      self.ozadje = ozadje
      self.ozadje_s_sliko = ozadje_s_sliko

   def izhod__(self,x):
      winsound.PlaySound(None, winsound.SND_PURGE) ##da izklopimo glasbo ob izhodu iz aplikacije
      x.destroy()

   def pozdravno_okno(self, zacetek, glasba):
      ozadje = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_sliko = tk.Label(zacetek, image = ozadje)
      ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      pozdrav = tk.Label(zacetek, text = "Pozdravljeni v igri Lepo je biti Milijonar!\nIgra je sestavljena iz treh nivojev težavnosti.\nPo vsakem doseženem nivoju, se lahko odločite,\n ali boste denar vzeli, ali igrali naprej.\nVeliko sreče!!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30) )
      pozdrav.place(relx = .5, rely = .4, anchor = "center")
      začni = tk.Button(zacetek, text = "Začni!",fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self,zacetek, pozdrav, začni, glasba))
      začni.place(relx = .5, rely = .7, anchor = "center")
      zacetek.mainloop()
      
   def zmagovalno_okno(self,zmagovalno, opomba, naprej, glasba):
      opomba.destroy()
      naprej.destroy()
      ozadjeozadja = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_slikoozadja = tk.Label(zmagovalno, image = ozadjeozadja)
      ozadje_s_slikoozadja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      izhod1 = tk.Button(ozadje_s_slikoozadja, text = "Izhod", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.izhod__(self, zmagovalno))
      izhod1.place(relx = .5, rely = .5, anchor = "center")
      ponovna_igra = tk.Button(ozadje_s_slikoozadja, text = "Poskusi znova", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : prva(zmagovalno))
      ponovna_igra.place(relx = .5, rely = .6, anchor = "center")
      zmagovalno.mainloop()

   def vzemi_okno(self, vzemi, opomba, naprej, glasba, dobiček):
      opomba.destroy()
      naprej.destroy()
      ozadjeozadja = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_slikoozadja = tk.Label(vzemi, image = ozadjeozadja)
      ozadje_s_slikoozadja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      predčasno = tk.Label(vzemi, text = "Odločili ste se, da predčasno končate z igro.\nOsvojili ste " + str(dobiček) + "€, čestitke!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
      predčasno.place(relx = .5, rely = .4, anchor = "center")
      izhod1 = tk.Button(vzemi, text = "Izhod", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.izhod__(self, vzemi))
      izhod1.place(relx = .4, rely = .6, anchor = "center")
      ponovna_igra = tk.Button(vzemi, text = "Igraj ponovno", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : prva(vzemi))
      ponovna_igra.place(relx = .6, rely = .6, anchor = "center")
      vzemi.mainloop()
      
   def poraz(self,zacetek, napacno, zakljuci):
      napacno.destroy()
      zakljuci.destroy()
      ozadje = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_sliko = tk.Label(zacetek, image = ozadje)
      ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      koncaj = tk.Label(zacetek, text = "Ostali ste brez nagrade, več sreče prihodnjič!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
      koncaj.place(relx = .5, rely = .4, anchor = "center")
      izhod1 = tk.Button(zacetek, text = "Izhod", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.izhod__(self, zacetek))
      izhod1.place(relx = .5, rely = .5, anchor = "center")
      ponovna_igra = tk.Button(zacetek, text = "Poskusi znova", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : prva(zacetek))
      ponovna_igra.place(relx = .5, rely = .6, anchor = "center")
      zacetek.mainloop()


   def vrni_pravilni_odgovor(self, vprasanje_in_odgovori):
      for odgovor in vprasanje_in_odgovori:
         if "***" in odgovor:
            return odgovor.strip('***\n')
   

   def uniči_gumbe():
      for i in range(0,4):
         grafika.seznam_gumbov[i].destroy()
      for i in range(0,4):
         del grafika.seznam_gumbov[3-i]

   def preveri_odgovor(self, vprasanje_in_odgovori,zacetek, izbira, prejsni_napis):
      pravilni_odgovor = grafika.vrni_pravilni_odgovor(self, vprasanje_in_odgovori)
      grafika.uniči_gumbe()
      odgovor = vprasanje_in_odgovori[izbira].strip('***\n')
      prejsni_napis.destroy()
     

      if(odgovor != pravilni_odgovor):
         
         napacno = tk.Label(zacetek, text = "Žal je vaš odgovor napačen, pravilen odgovor je:\n" + pravilni_odgovor, fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
         napacno.place(relx = .5 , rely = .4, anchor = "center")
         zakljuci = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comis Sans MS", 30), command = lambda : grafika.poraz(self, zacetek, napacno, zakljuci) )
         zakljuci.place(relx = .5 , rely = .6, anchor = "center")
         
      elif(odgovor == pravilni_odgovor):
         print(grafika.stevilka_vprasanja)
         print(self.podatki.nagrada)
         self.podatki.zasluzeni_denar = self.podatki.nagrada[grafika.stevilka_vprasanja-1]
         if(grafika.stevilka_vprasanja >= 5 and grafika.stevilka_vprasanja < 10 ):
            pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(self.podatki.zasluzeni_denar) + " Eurov", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
            pravilno.place(relx = .5 , rely = .3, anchor = "center")
            naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self, zacetek,pravilno,naprej, self.glasba) )
            naprej.place(relx = .4 , rely = .5, anchor = "center")
            vzemi = tk.Button(zacetek, text = "Vzemi 1000 € in končaj", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.vzemi_okno(self, zacetek,pravilno,naprej, self.glasba,1000) )
            vzemi.place(relx = .6 , rely = .5, anchor = "center")
            if(grafika.stevilka_vprasanja == 5):
               opomba = tk.Label(zacetek, text = "Prva stopnja opravljena!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40) )
               opomba.place(relx = .5, rely = .7, anchor = "center")
         elif(grafika.stevilka_vprasanja >= 10 and grafika.stevilka_vprasanja < 15 ):
            pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(self.podatki.zasluzeni_denar) + " Eurov", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
            pravilno.place(relx = .5 , rely = .3, anchor = "center")
            naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self, zacetek,pravilno,naprej, self.glasba) )
            naprej.place(relx = .4 , rely = .5, anchor = "center")
            vzemi = tk.Button(zacetek, text = "Vzemi 32000 € in končaj", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.vzemi_okno(self, zacetek,pravilno,naprej, self.glasba,32000) )
            vzemi.place(relx = .6 , rely = .5, anchor = "center")
            if(grafika.stevilka_vprasanja == 10):
               opomba = tk.Label(zacetek, text = "Druga stopnja opravljena!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40) )
               opomba.place(relx = .5, rely = .7, anchor = "center")
         elif(grafika.stevilka_vprasanja == 15):
            naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zmagovalno_okno(self, zacetek,opomba,naprej, self.glasba) )
            naprej.place(relx = .5 , rely = .7, anchor = "center")
            opomba = tk.Label(zacetek, text = "Čestitke postali ste milijonar!!!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 50) )
            opomba.place(relx = .5, rely = .5, anchor = "center")
         else:
            pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(self.podatki.zasluzeni_denar) + " Eurov", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
            pravilno.place(relx = .5 , rely = .3, anchor = "center")
            naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self, zacetek,pravilno,naprej, self.glasba) )
            naprej.place(relx = .5 , rely = .5, anchor = "center")
         grafika.stevilka_vprasanja = grafika.stevilka_vprasanja +1
         
            
   def izberi_ustrezno_vprasanje(self, nivo):
      indeks_vprasanja = random.randint(0, self.podatki.stevilo_vprasanj-1)
      if(self.podatki.seznam_datotek[indeks_vprasanja] == 'X'):
         return grafika.izberi_ustrezno_vprasanje(self, nivo)
      ime = str(indeks_vprasanja) + "_vprasanje_in_odgovori.txt"
      nivo_vprasanja = ''
      with open("vprasanja_in_odgovori/" + ime, 'r', encoding = "utf-8") as file:
         vrstice = file.readlines()
         nivo_vprasanja = vrstice[0].strip()
         if(nivo_vprasanja != nivo):
            
            return grafika.izberi_ustrezno_vprasanje(self, nivo)
         else:
            
            self.podatki.seznam_datotek[indeks_vprasanja] = 'X'
            return vrstice
      
   def izberi_novo_vprasanje(self):
      vprasanje_in_odgovori = []
      if(grafika.stevilka_vprasanja <= 5):
         vprasanje_in_odgovori = grafika.izberi_ustrezno_vprasanje(self, "Prvi nivo")
      elif(grafika.stevilka_vprasanja > 5 and grafika.stevilka_vprasanja <= 10):
         vprasanje_in_odgovori = grafika.izberi_ustrezno_vprasanje(self, "Drugi nivo")
      elif(grafika.stevilka_vprasanja > 10):
         vprasanje_in_odgovori = grafika.izberi_ustrezno_vprasanje(self, "Tretji nivo")
      return vprasanje_in_odgovori

   def pokrij(pravilni_odgovor, vprasanje_in_odgovori):
      nakljucna_prva = random.randint(0,3)
      nakljucna_druga = random.randint(0,3)
      odgovor_prva = vprasanje_in_odgovori[nakljucna_prva+2].strip('***\n')
      odgovor_druga = vprasanje_in_odgovori[nakljucna_druga+2].strip('***\n')
      if(nakljucna_prva != nakljucna_druga and odgovor_prva != pravilni_odgovor and odgovor_druga != pravilni_odgovor):
         grafika.seznam_gumbov[nakljucna_prva].place_forget()
         grafika.seznam_gumbov[nakljucna_druga].place_forget()
      else:
         grafika.pokrij(pravilni_odgovor, vprasanje_in_odgovori)

   def izkoristi_polovicko(self,vprasanje_in_odgovori, gumb):
      gumb['state'] = 'disabled'
      pravilni_odgovor = grafika.vrni_pravilni_odgovor(self, vprasanje_in_odgovori)
      grafika.pokrij(pravilni_odgovor, vprasanje_in_odgovori)
      self.podatki.polovicka = False
      
   
   def naredi_gumb(self, st_odgovora, vprasanje_in_odgovori, zacetek, novo):
         besedilo = vprasanje_in_odgovori[st_odgovora].strip('***\n')
         ukaz = lambda: grafika.preveri_odgovor(self, vprasanje_in_odgovori,zacetek, st_odgovora,novo)
         gumb = tk.Button(zacetek, text = besedilo, fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = ukaz)
         polozaj = {2 : (0.4, 0.4), 3 : (0.6, 0.4), 4: (0.4, 0.5), 5: (0.6, 0.5)}
         gumb.place(relx = polozaj[st_odgovora][0], rely = polozaj[st_odgovora][1], anchor = "center")
         return gumb

   
   
   def zacni(self, zacetek,pozdrav,zacni, glasba):
      if (glasba == True):
         winsound.PlaySound("glasba/Who Wants", winsound.SND_ALIAS | winsound.SND_ASYNC)
         glasba = False
 
      pozdrav.destroy()
      zacni.destroy()
      ozadje = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_sliko = tk.Label(zacetek, image = ozadje)
      ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      lestvica = tk.PhotoImage(file = "ozadja/Zajeta slika.gif")
      ozadje_z_lestvico = tk.Label(ozadje_s_sliko, image = lestvica)
      ozadje_z_lestvico.place(x = 50, y = 250)
      vprasanje_in_odgovori = grafika.izberi_novo_vprasanje(self)
      vprasanje = vprasanje_in_odgovori[1]
      gumb = tk.Button(zacetek, command = lambda : grafika.izkoristi_polovicko(self,vprasanje_in_odgovori, gumb))
      gumb.place(relx = .1, rely = .1, anchor = "center")
      nepolovic = tk.Label(zacetek)
      if (self.podatki.polovicka == True):
         polovic = tk.PhotoImage(file = "ozadja/polovicka.gif")
         gumb.config(image = polovic)
      else:
         nepolovic = tk.PhotoImage(file = "ozadja/nepolovicka.gif")
         nepol = tk.Label(zacetek, image = nepolovic)
         nepol.place(relx = .1, rely = .1, anchor = "center")
      
      
      novo = tk.Label(zacetek, text = vprasanje, fg = "white", bg = "grey6", font = ("Comic Sans MS", 30))
      novo.place(relx = .5, rely = .2, anchor = "center")
      grafika.seznam_gumbov = [grafika.naredi_gumb(self, st, vprasanje_in_odgovori, zacetek, novo) for st in [2, 3, 4, 5]]
      zacetek.mainloop()

   def nastavi_ozadje(self, event):
      nova_sirina = event.width
      nova_visina = event.height
      slika = self.ozadje.resize((nova_sirina, nova_visina))
      photo = ImageTk.PhotoImage(slika)
      self.ozadje_s_sliko.config(image = photo)
      self.ozadje_s_sliko.image = photo


def prva(okno):
   #okno.resizable(width= False, height = False)
   zazeni_glasbo = True
   glasba = "glasba/Who - Wants.wav"
   winsound.PlaySound(glasba, winsound.SND_ALIAS | winsound.SND_ASYNC)
   sirina_okna = okno.winfo_screenwidth()
   visina_okna = okno.winfo_screenheight()
   okno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   zasluzeni_denar = 0
   stevilka_vprasanja = 1
   polovicka = True
   ozadje = Image.open("ozadja/mil.gif")
   kopija = ozadje.copy()
   photo = ImageTk.PhotoImage(ozadje)
   ozadje_s_sliko = tk.Label(okno, image = photo)
   vsebina = podatki(stevilka_vprasanja,zasluzeni_denar, polovicka)
   vmesnik = grafika(sirina_okna, visina_okna, vsebina, okno, glasba, stevilka_vprasanja, kopija, ozadje_s_sliko)
   ozadje_s_sliko.bind('<Configure>', vmesnik.nastavi_ozadje)
   ozadje_s_sliko.pack(fill = BOTH, expand = YES)
   gumb_za_zacetek = tk.Button(okno, text = "Začni z igro",fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: vmesnik.pozdravno_okno(okno, zazeni_glasbo))
   gumb_za_zacetek.place(relx = .1, rely = .5 , anchor = "center")
   izhod = tk.Button(okno, text = "Ne upam :(", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: vmesnik.izhod__(okno))
   izhod.place(relx = .9, rely = .5 , anchor = "center")
   okno.mainloop()

okno = tk.Tk()
prva(okno)
