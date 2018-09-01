
import tkinter as tk
from tkinter import *
import random
import math
import time
import winsound
import os, sys
from PIL import Image, ImageTk
from tkinter import messagebox



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
      
    
   def __init__(self, stevilka_vprasanja, zasluzeni_denar, polovicka, glas_ljudstva):
      podatki.seznam_datotek = []
      self.polovicka = polovicka
      self.glas_ljudstva = glas_ljudstva
      self.stevilka_vprasanja = stevilka_vprasanja
      self.zasluzeni_denar = zasluzeni_denar
      podatki.nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]   
      podatki.dodaj_datoteke_v_seznam()
      
   
   

class grafika:
   stevilka_vprasanja = -1
   sirina_okna = -1
   visina_okna = -1
   seznam_gumbov = []

   def __init__(self, sirina_okna, visina_okna, podatki, okno, glasba, stevilka_vprasanja, ozadje, ozadje_s_sliko, seznam_widgetov):
      self.sirina_okna = sirina_okna
      self.visina_okna = visina_okna
      self.podatki = podatki
      self.okno = okno
      self.glasba = glasba
      grafika.stevilka_vprasanja = stevilka_vprasanja
      self.ozadje = ozadje
      self.ozadje_s_sliko = ozadje_s_sliko
      self.seznam_widgetov = seznam_widgetov

   def izhod__(self,x):
      winsound.PlaySound(None, winsound.SND_PURGE) ##da izklopimo glasbo ob izhodu iz aplikacije
      x.destroy()

   def pozdravno_okno(self, zacetek, glasba):
      ozadje = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      self.ozadje = ozadje
      ozadje_s_sliko = tk.Label(zacetek, image = ozadje)
      ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      pozdrav = tk.Label(zacetek, wraplength = 1000, text = "Pozdravljeni v igri Lepo je biti Milijonar! Igra je sestavljena iz treh nivojev težavnosti. Po vsakem doseženem nivoju, se lahko odločite, ali boste denar vzeli, ali igrali naprej.Veliko sreče!!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30) )
      pozdrav.grid(row = 0, sticky = N, pady = 50, rowspan = 2)
      začni = tk.Button(zacetek, text = "Začni!",fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacetek__nastavi_ozadje(self,zacetek, glasba))
      začni.grid(row = 1, sticky = S,  pady = 100)
      self.dodaj_na_seznam_widgetov(ozadje_s_sliko, pozdrav, začni)
      zacetek.mainloop()
      
   def zmagovalno_okno(self,zmagovalno, glasba, okvir_za_gumbe):
      self.uniči_gumbe(self.seznam_widgetov)
      okvir_za_gumbe.destroy()
      ozadjeozadja = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_slikoozadja = tk.Label(zmagovalno, image = ozadjeozadja)
      ozadje_s_slikoozadja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      izhod1 = tk.Button(zmagovalno, text = "Izhod", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.izhod__(self, zmagovalno))
      izhod1.grid(sticky = S+W+E, row = 1, pady = 100)
      ponovna_igra = tk.Button(zmagovalno, text = "Igraj ponovno", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.pred_ponovno_igro_uniči_prejšne_widgete(self, zmagovalno))
      ponovna_igra.grid(row = 0, sticky = N+W+E, pady = 300)
      self.dodaj_na_seznam_widgetov(ozadje_s_slikoozadja, izhod1, ponovna_igra)
      zmagovalno.mainloop()

   def vzemi_okno(self, vzemi, glasba, dobiček, okvir_za_gumbe):
      self.uniči_gumbe(self.seznam_widgetov)
      okvir_za_gumbe.destroy()
      ozadjeozadja = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_slikoozadja = tk.Label(vzemi, image = ozadjeozadja)
      ozadje_s_slikoozadja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      predčasno = tk.Label(vzemi, text = "Odločili ste se, da predčasno končate z igro.\nOsvojili ste " + str(dobiček) + "€, čestitke!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
      predčasno.grid(sticky = N , pady = 100, columnspan = 2)
      izhod1 = tk.Button(vzemi, text = "Izhod", fg = "white", bg = "grey6",  width = 15, height = 2, font = ("Comic Sans MS", 30), command = lambda: grafika.izhod__(self, vzemi))
      izhod1.grid(sticky = W, row = 0,  padx = 500)
      ponovna_igra = tk.Button(vzemi, text = "Igraj ponovno", fg = "white", width = 15, height = 2,  bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.pred_ponovno_igro_uniči_prejšne_widgete(self, vzemi))
      ponovna_igra.grid(sticky = E, row = 0,    padx = 500)
      self.dodaj_na_seznam_widgetov(ozadje_s_slikoozadja, predčasno, izhod1, ponovna_igra)
      vzemi.mainloop()
      
   def poraz(self,zacetek, okvir_za_gumbe):
      
      Grid.columnconfigure(zacetek,1, weight = 0)
      okvir_za_gumbe.destroy()
      self.uniči_gumbe(self.seznam_widgetov)
      ozadje = tk.PhotoImage(file = "ozadja/drugo_ozadje.gif")
      ozadje_s_sliko = tk.Label(zacetek, image = ozadje)
      ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      koncaj = tk.Label(zacetek, text = "Ostali ste brez nagrade, več sreče prihodnjič!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
      koncaj.grid(sticky = N, row = 0, columnspan = 2, pady = 50 )
      izhod1 = tk.Button(zacetek, text = "Izhod", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.izhod__(self, zacetek), width = 15, height = 2)
      izhod1.grid( row = 0, column = 0, padx = 300)
      ponovna_igra = tk.Button(zacetek, wraplength = 200 , text = "Poskusi znova", fg = "white", bg = "grey6", width = 15 ,height = 2,  font = ("Comic Sans MS", 30), command = lambda : grafika.pred_ponovno_igro_uniči_prejšne_widgete(self, zacetek))
      ponovna_igra.grid(   row = 0, column = 1, padx = 300)
      self.dodaj_na_seznam_widgetov(ozadje_s_sliko, koncaj, izhod1, ponovna_igra)
      zacetek.mainloop()

   def pred_ponovno_igro_uniči_prejšne_widgete(self, zacetek):
      self.uniči_gumbe(self.seznam_widgetov)
      #Grid.columnconfigure(zacetek,0, weight = 1)
      prva(zacetek)

   def vrni_pravilni_odgovor(self, vprasanje_in_odgovori):
      for odgovor in vprasanje_in_odgovori:
         if "***" in odgovor:
            return odgovor.strip('***\n')
   
   
   def uniči_gumbe(self, seznam):
      dolzina_seznama = len(seznam)
      for i in range(0,dolzina_seznama):
         try:
            seznam[i].destroy()
         except:
            pass
      for i in range(0, dolzina_seznama):
         del seznam[dolzina_seznama - i - 1]

   def dodaj_na_seznam_widgetov(self, prvo, drugo, tretje = None, cetrto = None ):
      self.seznam_widgetov.append(prvo)
      self.seznam_widgetov.append(drugo)
      if(tretje != None):
         self.seznam_widgetov.append(tretje)
      if(cetrto != None):
         self.seznam_widgetov.append(cetrto)

   def preveri_odgovor(self, vprasanje_in_odgovori, zacetek, izbira, okvir_za_gumbe, gumb):
      pravilni_odgovor = grafika.vrni_pravilni_odgovor(self, vprasanje_in_odgovori)
      odgovor = vprasanje_in_odgovori[izbira].strip('***\n')
      if(odgovor != pravilni_odgovor):
         gumb.config(relief = SUNKEN, bg = "red", command = winsound.PlaySound("glasba/napacen", winsound.SND_ASYNC) )
         zacetek.after(1500, lambda : grafika.nepravilni_odgovor(self,pravilni_odgovor, vprasanje_in_odgovori, zacetek, izbira, okvir_za_gumbe))
      else:
         gumb.config(relief = SUNKEN, bg = "green", command = winsound.PlaySound("glasba/pravilen", winsound.SND_ASYNC))
         zacetek.after(1500, lambda : grafika.pravilni_odgovor(self, vprasanje_in_odgovori, zacetek, izbira, okvir_za_gumbe))

   def nepravilni_odgovor(self,pravilni_odgovor,  vprasanje_in_odgovori, zacetek, izbira, okvir_za_gumbe):
      self.uniči_gumbe(grafika.seznam_gumbov)
      self.uniči_gumbe(self.seznam_widgetov)
      napacno = tk.Label(zacetek, text = "Žal je vaš odgovor napačen, pravilen odgovor je:\n" + pravilni_odgovor, fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
      napacno.place(relx = .5 , rely = .4, anchor = "center")
      zakljuci = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comis Sans MS", 30), command = lambda : grafika.poraz(self, zacetek, okvir_za_gumbe) )
      zakljuci.place(relx = .5 , rely = .6, anchor = "center")
      self.dodaj_na_seznam_widgetov( napacno, zakljuci)
      grafika.stevilka_vprasanja = grafika.stevilka_vprasanja +1

   def pravilni_odgovor(self, vprasanje_in_odgovori,zacetek, izbira, okvir_za_gumbe):
      self.uniči_gumbe(grafika.seznam_gumbov)
      self.uniči_gumbe(self.seznam_widgetov)
      self.podatki.zasluzeni_denar = self.podatki.nagrada[grafika.stevilka_vprasanja-1]
      if(grafika.stevilka_vprasanja >= 5 and grafika.stevilka_vprasanja < 10 ):
         pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(self.podatki.zasluzeni_denar) + " Eurov", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
         pravilno.place(relx = .5 , rely = .3, anchor = "center")
         naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self, zacetek, self.glasba, okvir_za_gumbe) )
         naprej.place(relx = .4 , rely = .5, anchor = "center")
         vzemi = tk.Button(zacetek, text = "Vzemi 1000 €", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.vzemi_okno(self, zacetek, self.glasba,1000, okvir_za_gumbe) )
         vzemi.place(relx = .6 , rely = .5, anchor = "center")
         self.dodaj_na_seznam_widgetov( pravilno, naprej, vzemi)
         if(grafika.stevilka_vprasanja == 5):
            opomba = tk.Label(zacetek, text = "Prva stopnja opravljena!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40) )
            opomba.place(relx = .5, rely = .7, anchor = "center")
            self.seznam_widgetov.append(opomba)
      elif(grafika.stevilka_vprasanja >= 10 and grafika.stevilka_vprasanja < 15 ):
         pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(self.podatki.zasluzeni_denar) + " Eurov", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
         pravilno.place(relx = .5 , rely = .3, anchor = "center")
         naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self, zacetek, self.glasba, okvir_za_gumbe) )
         naprej.place(relx = .4 , rely = .5, anchor = "center")
         vzemi = tk.Button(zacetek, text = "Vzemi 32000 €", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.vzemi_okno(self, zacetek, self.glasba,32000, okvir_za_gumbe) )
         vzemi.place(relx = .6 , rely = .5, anchor = "center")
         self.dodaj_na_seznam_widgetov( pravilno, naprej, vzemi)
         if(grafika.stevilka_vprasanja == 10):
            opomba = tk.Label(zacetek, text = "Druga stopnja opravljena!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40) )
            opomba.place(relx = .5, rely = .7, anchor = "center")
            self.seznam_widgetov.append(opomba)
      elif(grafika.stevilka_vprasanja == 15):
         naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zmagovalno_okno(self, zacetek, self.glasba, okvir_za_gumbe) )
         naprej.place(relx = .5 , rely = .7, anchor = "center")
         opomba = tk.Label(zacetek, text = "Čestitke postali ste milijonar!!!", fg = "white", bg = "grey6", font = ("Comic Sans MS", 50) )
         opomba.place(relx = .5, rely = .5, anchor = "center")
         self.dodaj_na_seznam_widgetov( naprej, opomba)
      else:
         pravilno = tk.Label(zacetek, text = "Vaš odgovor je pravilen!\nZaslužili ste " + str(self.podatki.zasluzeni_denar) + " Eurov", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
         pravilno.place(relx = .5 , rely = .3, anchor = "center")
         naprej = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda : grafika.zacni(self, zacetek, self.glasba, okvir_za_gumbe) )
         naprej.place(relx = .5 , rely = .5, anchor = "center")
         self.dodaj_na_seznam_widgetov( pravilno, naprej)

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
         grafika.seznam_gumbov[nakljucna_prva].destroy()
         grafika.seznam_gumbov[nakljucna_druga].destroy()
      else:
         grafika.pokrij(pravilni_odgovor, vprasanje_in_odgovori)

   def izkoristi_polovicko(self,vprasanje_in_odgovori, gumb, glas_ljudstva):
      pravilni_odgovor = grafika.vrni_pravilni_odgovor(self, vprasanje_in_odgovori)
      grafika.pokrij(pravilni_odgovor, vprasanje_in_odgovori)
      glas_ljudstva.grid_forget()
      self.podatki.polovicka = False
      gumb.config(state = "disabled")

   def poisci_pravi_gumb( pravilni_odgovor):
      for gumb in grafika.seznam_gumbov:
         if(pravilni_odgovor in gumb['text']):
            odgovor = gumb['text']
      pravilna_crka = odgovor[0]
      return pravilna_crka
   
   def izdelaj_seznam_parov(seznam_vseh, pravilen_par):
      prejsnja_vrednost = -1
      indeks_para = 0
      for par in seznam_vseh:
         if(par[0] == pravilen_par[0]):
            prejsnja_vrednost = par[1]
            novi_par =(pravilen_par[0], pravilen_par[1])
            seznam_vseh[indeks_para] = novi_par
         indeks_para+=1
      indeks_para = 0
      for par in seznam_vseh:
         if(par[1] == pravilen_par[1] and par[0] != pravilen_par[0]):
            novi_par =(par[0], prejsnja_vrednost)
            seznam_vseh[indeks_para] = novi_par
            return seznam_vseh
         indeks_para+=1
      return seznam_vseh
   
   def poracunaj_procente(pravilni_odgovor):
      prvi_odstotek = random.randint( 0, 100 )
      drugi_odstotek = 100 - random.randint( prvi_odstotek, 100)
      tretji_odstotek = 100 - random.randint( prvi_odstotek + drugi_odstotek , 100 )
      cetrti_odstotek = 100 - (prvi_odstotek + drugi_odstotek + tretji_odstotek)
      seznam_vseh = [('A', prvi_odstotek), ('B', drugi_odstotek), ('C', tretji_odstotek), ('D', cetrti_odstotek)]
      najvisji_procent = max(prvi_odstotek, drugi_odstotek, tretji_odstotek, cetrti_odstotek)
      pravilni_odgovor = grafika.poisci_pravi_gumb(pravilni_odgovor)
      pravilen_par = (pravilni_odgovor, najvisji_procent)
      print(prvi_odstotek, drugi_odstotek, tretji_odstotek, cetrti_odstotek, najvisji_procent, pravilni_odgovor)
      seznam_parov = grafika.izdelaj_seznam_parov(seznam_vseh, pravilen_par)
      print(seznam_parov)
      return seznam_parov

   def izrisi_graf(self, seznam_parov, gumb):
      glas_ljudstva_okno = tk.Tk()
      glas_ljudstva_okno.title("Glas ljudstva")
      glas_ljudstva_okno.geometry('%dx%d+%d+%d' % (700, 500, self.sirina_okna/2 - 700/2, self.visina_okna/2 - 500/2))
      sirina_podlage = 700
      visina_podlage = 500
      platno = tk.Canvas(glas_ljudstva_okno, width = sirina_podlage, height = visina_podlage)
      platno.pack(fill ='both', expand = 'yes')
      ozadje = tk.PhotoImage(master = platno, file = "ozadja/drugo_ozadje.gif")
      platno.create_image(0,0 ,image = ozadje, anchor = 'center')
      y_razteg = 4
      y_razmak = 50
      x_sirina = 25
      x_razteg = sirina_podlage/4 - x_sirina
      x_razmak= 20

      for x, par in enumerate(seznam_parov):
         x0 = x * x_razteg + x * x_sirina + x_razteg
         y0 = visina_podlage - (par[1] * y_razteg + y_razmak)
         x1 = x * x_razteg + x * x_sirina + x_sirina + x_razmak
         y1 = visina_podlage - y_razmak
         platno.create_rectangle(x0, y0, x1, y1, fill = "grey6", outline = "silver")
         platno.create_text(x0 - 55, y0 - 40, anchor = tk.N ,text =  str(par[1])+ " %", font = ("Comic Sans MS", 20), fill = "white")
         platno.create_text(x0 - 55, y1 + 40, anchor = tk.S ,text =  str(par[0])+ ")", font = ("Comic Sans MS", 20), fill = "white")
         platno.create_line(0, visina_podlage - 48, sirina_podlage, visina_podlage - 48, fill = "silver", width = 1.5)
      gumb.config(state = "disabled")
      self.podatki.glas_ljudstva = False
      self.seznam_widgetov.append(glas_ljudstva_okno)
      glas_ljudstva_okno.mainloop()
      
      
   
   def izkoristi_glas_ljudstva(self, vprasanje_in_odgovori, gumb):
      pravilni_odgovor = grafika.vrni_pravilni_odgovor(self, vprasanje_in_odgovori)
      seznam_parov = grafika.poracunaj_procente(pravilni_odgovor)
      grafika.izrisi_graf(self, seznam_parov, gumb)
     
      
      
   def naredi_gumb(self, st_odgovora, vprasanje_in_odgovori,   zacetek, okvir_za_gumbe):
         crke = ['A', 'B', 'C', 'D']
         gumb = tk.Button(okvir_za_gumbe)
         besedilo = vprasanje_in_odgovori[st_odgovora].strip('***\n')
         ukaz = lambda: grafika.preveri_odgovor(self, vprasanje_in_odgovori,zacetek, st_odgovora, okvir_za_gumbe, gumb)
         gumb.config(wraplength = 200,  text = crke[st_odgovora - 2] + ")   " + besedilo, fg = "white", bg = "grey6",font = ("Comic Sans MS", 20), command = ukaz, height = 30, width = 30)   
         return gumb

   
   def zacetek__nastavi_ozadje(self, zacetek, glasba):
      self.uniči_gumbe(self.seznam_widgetov)
      ozadje_okvirja = Image.open("ozadja/drugo_ozadje.gif")
      slika_okvirja = ImageTk.PhotoImage(ozadje_okvirja)
      stalno_ozadje = tk.Label(zacetek, image = slika_okvirja)
      stalno_ozadje.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      okvir_za_gumbe = tk.Frame(zacetek, width = grafika.sirina_okna, height = grafika.visina_okna)
      okvir_za_gumbe.grid(sticky = N+S+E+W)
      ozadje_s_sliko_okvirja = tk.Label(okvir_za_gumbe, image = slika_okvirja)
      ozadje_s_sliko_okvirja.place(x = 0, y = 0, relwidth = 1, relheight = 1)
      grafika.zacni(self, zacetek, glasba, okvir_za_gumbe)

  
   def vprasanje_stirje_odgovori(self, vprasanje_in_odgovori, zacetek, okvir_za_gumbe, vprasanje):
      novo = tk.Label(okvir_za_gumbe, wraplength = 1000, text = vprasanje, fg = "white", bg = "grey6", font = ("Comic Sans MS", 30))
      novo.grid(sticky = N+W, row = 0, columnspan = 3,  pady = 60, padx = 200)
      self.seznam_widgetov.append(novo)
      st_odgovora = 2
      for vrstica in range(1, 3):
            Grid.rowconfigure(okvir_za_gumbe, vrstica, weight = 1)
            for stolpec in range(0, 2):
               Grid.columnconfigure(okvir_za_gumbe, stolpec, weight = 1)
               gumb = grafika.naredi_gumb(self, st_odgovora, vprasanje_in_odgovori, zacetek, okvir_za_gumbe)
               gumb.grid(row = vrstica, column = stolpec, sticky = W , pady = 80, padx = 50)
               grafika.seznam_gumbov.append(gumb)
               st_odgovora += 1
   
   
   def zacni(self, zacetek, glasba, okvir_za_gumbe):
      winsound.PlaySound("glasba/Who Wants", winsound.SND_ALIAS | winsound.SND_ASYNC)
      self.uniči_gumbe(self.seznam_widgetov)
      vprasanje_in_odgovori = grafika.izberi_novo_vprasanje(self)
      vprasanje = vprasanje_in_odgovori[1].strip('\n')

      if (self.podatki.glas_ljudstva == True):
         gumb_glas_ljudstva = tk.Button(okvir_za_gumbe, command = lambda : grafika.izkoristi_glas_ljudstva(self, vprasanje_in_odgovori, gumb_glas_ljudstva))
         gumb_glas_ljudstva.grid(sticky = E, row = 2, column = 2, padx = 200, pady = 80)
         glas_ljudstva_slika = tk.PhotoImage(file = "ozadja/glas_ljudstva.gif")
         gumb_glas_ljudstva.config(image = glas_ljudstva_slika)
         self.seznam_widgetov.append(gumb_glas_ljudstva)
      else:
         neglas_ljudstva_slika = tk.PhotoImage(file = "ozadja/ne_glas_ljudstva.gif")
         neglas_ljudstva = tk.Label(okvir_za_gumbe, image = neglas_ljudstva_slika)
         neglas_ljudstva.grid(sticky = E, row = 2, column = 2, padx = 200, pady = 80)
         self.seznam_widgetov.append(neglas_ljudstva)
         
      if (self.podatki.polovicka == True):
         gumb_polovicka = tk.Button(okvir_za_gumbe,command = lambda : grafika.izkoristi_polovicko(self,vprasanje_in_odgovori, gumb_polovicka, gumb_glas_ljudstva))
         gumb_polovicka.grid(sticky = E, row = 1, column = 2, padx = 200, pady = 80)
         polovic = tk.PhotoImage(file = "ozadja/polovicka.gif")
         gumb_polovicka.config(image = polovic)
         self.seznam_widgetov.append(gumb_polovicka)
      else:
         nepolovic = tk.PhotoImage(file = "ozadja/nepolovicka.gif")
         nepol = tk.Label(okvir_za_gumbe, image = nepolovic)
         nepol.grid(sticky = E, row = 1, column = 2, pady = 80, padx = 200)
         self.seznam_widgetov.append(nepol)
      

      grafika.vprasanje_stirje_odgovori(self,vprasanje_in_odgovori, zacetek, okvir_za_gumbe, vprasanje)  
      zacetek.mainloop()

def prva(okno):
   Grid.rowconfigure(okno,0, weight = 1)
   Grid.columnconfigure(okno,0, weight = 1)
   zazeni_glasbo = True
   glasba = "glasba/Who - Wants.wav"
   winsound.PlaySound(glasba, winsound.SND_ALIAS | winsound.SND_ASYNC)
   sirina_okna = okno.winfo_screenwidth()
   visina_okna = okno.winfo_screenheight()
   okno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   zasluzeni_denar = 0
   stevilka_vprasanja = 15
   polovicka = True
   glas_ljudstva = True
   ozadje = Image.open("ozadja/mil.gif")
   kopija = ozadje.copy()
   ozadje2 = kopija.resize((sirina_okna, visina_okna))
   photo = ImageTk.PhotoImage(ozadje2)
   ozadje_s_sliko = tk.Label(okno, image = photo)
   ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
   vsebina = podatki(stevilka_vprasanja,zasluzeni_denar, polovicka, glas_ljudstva)
   vmesnik = grafika(sirina_okna, visina_okna, vsebina, okno, glasba, stevilka_vprasanja, kopija, ozadje_s_sliko, [])
   gumb_za_zacetek = tk.Button(okno, text = "Začni z igro",fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: vmesnik.pozdravno_okno(okno, zazeni_glasbo))
   gumb_za_zacetek.grid(row = 0, sticky = W)
   izhod = tk.Button(okno, text = "Ne upam :(", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: vmesnik.izhod__(okno))
   izhod.grid(row = 0, sticky = E)
   vmesnik.dodaj_na_seznam_widgetov(gumb_za_zacetek, izhod)
   okno.mainloop()



okno = tk.Tk()
okno.title("Milijonar")
prva(okno)
