import tkinter as tk
from tkinter import *
import random
import time
import winsound

class podatki:
   nagrada = []
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
   stevilo_vprasanj = 0
   

   def ustvari_datoteko():
      for index in range(0, 20):
         
         ime = str(index+40) + "_vprasanje_in_odgovori.txt"
         with open(ime, 'a', encoding = "utf-8") as file:
            file.write('Tretji nivo\n')
            file.write(podatki.vprasanja_tretji_nivo[index]+'\n')
            if(podatki.resitve_tretji_nivo[index] == 'a'):
               file.write('***' + podatki.odgovori_A_tretji[index]+ '\n')
            else:
               file.write(podatki.odgovori_A_tretji[index]+ '\n')
            if(podatki.resitve_tretji_nivo[index] == 'b'):
               file.write('***' + podatki.odgovori_B_tretji[index]+ '\n')
            else:
               file.write(podatki.odgovori_B_tretji[index]+ '\n')
            if(podatki.resitve_tretji_nivo[index] == 'c'):
               file.write('***' + podatki.odgovori_C_tretji[index]+ '\n')
            else:
               file.write(podatki.odgovori_C_tretji[index]+ '\n')
            if(podatki.resitve_tretji_nivo[index] == 'd'):
               file.write('***' + podatki.odgovori_D_tretji[index])
            else:
               file.write(podatki.odgovori_D_tretji[index])
            
            
   
   def prepisi_v_seznam(datoteka,vprasanja, odgovoriA, odgovoriB, odgovoriC, odgovoriD, resitve):
     
      for i, vrstica in enumerate(datoteka):
         
         if i == 0:
            vprasanja.append(vrstica.strip())
         elif i == 1:
            if '***' in vrstica:
               resitve.append('a')
            odgovoriA.append(vrstica.strip('***''\n'))
         elif i == 2:
            if '***' in vrstica:
              resitve.append('b')
            odgovoriB.append(vrstica.strip('***''\n'))
         elif i == 3:
            if '***' in vrstica:
               resitve.append('c')
            odgovoriC.append(vrstica.strip('***''\n'))
         elif i == 4:
            if '***' in vrstica:
               resitve.append('d')
            odgovoriD.append(vrstica.strip('***'))

      
      

   
   def preberi_datoteko(self):
      for index_vprasanja in range(0, podatki.stevilo_vprasanj):
         ime_datoteke = str(index_vprasanja) + '_vprasanje_in_odgovori.txt'
         file = open("vprasanja_in_odgovori/"+ime_datoteke, "r", encoding = "utf-8")
      
         prva_vrstica = file.readline().strip()

         if prva_vrstica == "Prvi nivo":
            podatki.prepisi_v_seznam(file, podatki.vprasanja_prvi_nivo, podatki.odgovori_A_prvi, podatki.odgovori_B_prvi, podatki.odgovori_C_prvi, podatki.odgovori_D_prvi, podatki.resitve_prvi_nivo)
         elif prva_vrstica == "Drugi nivo":
            podatki.prepisi_v_seznam(file, podatki.vprasanja_drugi_nivo, podatki.odgovori_A_drugi, podatki.odgovori_B_drugi, podatki.odgovori_C_drugi, podatki.odgovori_D_drugi, podatki.resitve_drugi_nivo)
         elif prva_vrstica == "Tretji nivo":
            podatki.prepisi_v_seznam(file, podatki.vprasanja_tretji_nivo, podatki.odgovori_A_tretji, podatki.odgovori_B_tretji, podatki.odgovori_C_tretji, podatki.odgovori_D_tretji, podatki.resitve_tretji_nivo)
         file.close()          
               
      
   
   def __init__(self, stevilka_vprasanja, zasluzeni_denar, polovicka, stevilo_vprasanj):
      podatki.stevilo_vprasanj = stevilo_vprasanj
      self.polovicka = polovicka
      self.stevilka_vprasanja = stevilka_vprasanja
      self.zasluzeni_denar = zasluzeni_denar
      podatki.nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
      podatki.preberi_datoteko(self)     # podatki.ustvari_datoteko()
   
   def vrni_pravilni_odgovor_prvi_nivo(self, vprasanje, izbira):
      pravilni_odgovor = ''
      if(izbira == 'a'):
            pravilni_odgovor = podatki.odgovori_A_prvi[vprasanje]
      elif(izbira == 'b'):
            pravilni_odgovor = podatki.odgovori_B_prvi[vprasanje]
      elif(izbira == 'c'):
            pravilni_odgovor = podatki.odgovori_C_prvi[vprasanje]
      elif(izbira == 'd'):
            pravilni_odgovor = podatki.odgovori_D_prvi[vprasanje]
      del podatki.odgovori_A_prvi[vprasanje]
      del podatki.odgovori_B_prvi[vprasanje]
      del podatki.odgovori_C_prvi[vprasanje]
      del podatki.odgovori_D_prvi[vprasanje]
      return pravilni_odgovor

   def vrni_pravilni_odgovor_drugi_nivo(self, vprasanje, izbira):
      pravilni_odgovor = ''
      if(izbira == 'a'):
            pravilni_odgovor = podatki.odgovori_A_drugi[vprasanje]
      elif(izbira == 'b'):
            pravilni_odgovor = podatki.odgovori_B_drugi[vprasanje]
      elif(izbira == 'c'):
            pravilni_odgovor = podatki.odgovori_C_drugi[vprasanje]
      elif(izbira == 'd'):
            pravilni_odgovor = podatki.odgovori_D_drugi[vprasanje]
      del podatki.odgovori_A_drugi[vprasanje]
      del podatki.odgovori_B_drugi[vprasanje]
      del podatki.odgovori_C_drugi[vprasanje]
      del podatki.odgovori_D_drugi[vprasanje]
      return pravilni_odgovor

   def vrni_pravilni_odgovor_tretji_nivo(self,vprasanje, izbira):
      pravilni_odgovor = ''
      if(izbira == 'a'):
            pravilni_odgovor = podatki.odgovori_A_tretji[vprasanje]
      elif(izbira == 'b'):
            pravilni_odgovor = podatki.odgovori_B_tretji[vprasanje]
      elif(izbira == 'c'):
            pravilni_odgovor = podatki.odgovori_C_tretji[vprasanje]
      elif(izbira == 'd'):
            pravilni_odgovor = podatki.odgovori_D_tretji[vprasanje]
      del podatki.odgovori_A_tretji[vprasanje]
      del podatki.odgovori_B_tretji[vprasanje]
      del podatki.odgovori_C_tretji[vprasanje]
      del podatki.odgovori_D_tretji[vprasanje]
      return pravilni_odgovor
   

            
      

class grafika:
   stevilka_vprasanja = -1
   sirina_okna = -1
   visina_okna = -1
   seznam_gumbov = []

   def __init__(self, sirina_okna, visina_okna, podatki, okno, glasba, stevilka_vprasanja):
      self.sirina_okna = sirina_okna
      self.visina_okna = visina_okna
      self.podatki = podatki
      self.okno = okno
      self.glasba = glasba
      grafika.stevilka_vprasanja = stevilka_vprasanja

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



   def preveri_odgovor(self, vprasanje,zacetek, izbira, prejsni_napis):
      
      pravilna_izbira = ''
      if(grafika.stevilka_vprasanja <= 5):
         pravilna_izbira = self.podatki.resitve_prvi_nivo[vprasanje]
         del self.podatki.resitve_prvi_nivo[vprasanje]
      elif(grafika.stevilka_vprasanja > 5 and grafika.stevilka_vprasanja <= 10):
         pravilna_izbira = self.podatki.resitve_drugi_nivo[vprasanje]
         del self.podatki.resitve_drugi_nivo[vprasanje]
      elif(grafika.stevilka_vprasanja > 10):
         pravilna_izbira = self.podatki.resitve_tretji_nivo[vprasanje]
         del self.podatki.resitve_tretji_nivo[vprasanje]
      elif(grafika.stevilka_vprasanja == 15):
          pravilna_izbira = self.podatki.resitve_tretji_nivo[vprasanje]
          del self.podatki.resitve_tretji_nivo[vprasanje]

      pravilni_odgovor = ''
      if(grafika.stevilka_vprasanja <= 5):
         pravilni_odgovor = self.podatki.vrni_pravilni_odgovor_prvi_nivo(vprasanje, pravilna_izbira)
      elif(grafika.stevilka_vprasanja > 5 and grafika.stevilka_vprasanja <= 10):
         pravilni_odgovor = self.podatki.vrni_pravilni_odgovor_drugi_nivo(vprasanje, pravilna_izbira)
      elif(grafika.stevilka_vprasanja > 10):
         pravilni_odgovor = self.podatki.vrni_pravilni_odgovor_tretji_nivo(vprasanje, pravilna_izbira)
      elif(grafika.stevilka_vprasanja == 15):
         pravilni_odgovor = self.podatki.vrni_pravilni_odgovor_tretji_nivo(vprasanje, pravilna_izbira)

      grafika.seznam_gumbov[0].destroy()
      grafika.seznam_gumbov[1].destroy()
      grafika.seznam_gumbov[2].destroy()
      grafika.seznam_gumbov[3].destroy()
      prejsni_napis.destroy()
      del grafika.seznam_gumbov[3]
      del grafika.seznam_gumbov[2]
      del grafika.seznam_gumbov[1]
      del grafika.seznam_gumbov[0]

      if(izbira != pravilna_izbira):
         
         napacno = tk.Label(zacetek, text = "Žal je vaš odgovor napačen, pravilen odgovor je:\n" + pravilni_odgovor, fg = "white", bg = "grey6", font = ("Comic Sans MS", 40))
         napacno.place(relx = .5 , rely = .4, anchor = "center")
         zakljuci = tk.Button(zacetek, text = "Naprej", fg = "white", bg = "grey6", font = ("Comis Sans MS", 30), command = lambda : grafika.poraz(self, zacetek, napacno, zakljuci) )
         zakljuci.place(relx = .5 , rely = .6, anchor = "center")
         
      elif(izbira == pravilna_izbira):
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
         
            
      
   def izberi_novo_vprasanje(self):
      novo = ''
      vprasanje = ''
      seznam = ['','']
      if(grafika.stevilka_vprasanja <= 5):
         novo = random.randint(0, len(self.podatki.vprasanja_prvi_nivo)-1)
         vprasanje = self.podatki.vprasanja_prvi_nivo[novo]
         seznam[0] = novo;
         seznam[1] = vprasanje;
      elif(grafika.stevilka_vprasanja > 5 and grafika.stevilka_vprasanja <= 10):
         novo = random.randint(0, len(self.podatki.vprasanja_drugi_nivo)-1)
         vprasanje = self.podatki.vprasanja_drugi_nivo[novo]
         seznam[0] = novo;
         seznam[1] = vprasanje;
      elif(grafika.stevilka_vprasanja > 10):
         novo = random.randint(0, len(self.podatki.vprasanja_tretji_nivo)-1)
         vprasanje = self.podatki.vprasanja_tretji_nivo[novo]
         seznam[0] = novo;
         seznam[1] = vprasanje;
      return seznam

   def pokrij(pravilna_izbira):
      odkrita=['','']
      izberi = random.randint(1,3)
      if (pravilna_izbira == 'a'): 
         if (izberi == 1):
            odkrita = ['a','b']
            grafika.seznam_gumbov[2].place_forget()
            grafika.seznam_gumbov[3].place_forget()
         elif (izberi == 2):
            odkrita = ['a','c']
            grafika.seznam_gumbov[1].place_forget()
            grafika.seznam_gumbov[3].place_forget()
         elif (izberi == 3):
            odkrita = ['a','d']
            grafika.seznam_gumbov[1].place_forget()
            grafika.seznam_gumbov[2].place_forget()
      elif (pravilna_izbira == 'b'): 
         if (izberi == 1):
            odkrita = ['b','a']
            grafika.seznam_gumbov[2].place_forget()
            grafika.seznam_gumbov[3].place_forget()
         elif (izberi == 2):
            odkrita = ['b','c']
            grafika.seznam_gumbov[0].place_forget()
            grafika.seznam_gumbov[3].place_forget()
         elif (izberi == 3):
            odkrita = ['b','d']
            grafika.seznam_gumbov[0].place_forget()
            grafika.seznam_gumbov[2].place_forget()
      elif (pravilna_izbira == 'c'): 
         if (izberi == 1):
            odkrita = ['c','a']
            grafika.seznam_gumbov[1].place_forget()
            grafika.seznam_gumbov[3].place_forget()
         elif (izberi == 2):
            odkrita = ['c','b']
            grafika.seznam_gumbov[0].place_forget()
            grafika.seznam_gumbov[3].place_forget()
         elif (izberi == 3):
            odkrita = ['c','d']
            grafika.seznam_gumbov[0].place_forget()
            grafika.seznam_gumbov[1].place_forget()
      elif (pravilna_izbira == 'd'): 
         if (izberi == 1):
            odkrita = ['d','a']
            grafika.seznam_gumbov[1].place_forget()
            grafika.seznam_gumbov[2].place_forget()
         elif (izberi == 2):
            odkrita = ['d','b']
            grafika.seznam_gumbov[0].place_forget()
            grafika.seznam_gumbov[2].place_forget()
         elif (izberi == 3):
            odkrita = ['d','c']
            grafika.seznam_gumbov[0].place_forget()
            grafika.seznam_gumbov[1].place_forget()

      return odkrita
      

   def izkoristi_polovicko(self,vprasanje):
      pravilna_izbira = ''
      if(grafika.stevilka_vprasanja <= 5):
         pravilna_izbira = self.podatki.resitve_prvi_nivo[vprasanje]
      elif(grafika.stevilka_vprasanja > 5 and grafika.stevilka_vprasanja <= 10):
         pravilna_izbira = self.podatki.resitve_drugi_nivo[vprasanje]
      elif(grafika.stevilka_vprasanja > 10):
         pravilna_izbira = self.podatki.resitve_tretji_nivo[vprasanje]
      
      odkriti_par = grafika.pokrij(pravilna_izbira)
      self.podatki.polovicka = False
      
      
   

      

   
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
      vprasanje_indeks = grafika.izberi_novo_vprasanje(self)
      vprasanje = vprasanje_indeks[1]
      indeks = int(vprasanje_indeks[0])
      gumb = tk.Button(zacetek, command = lambda : grafika.izkoristi_polovicko(self,indeks))
      gumb.place(relx = .1, rely = .1, anchor = "center")
      nepolovic = tk.Label(zacetek)
      if (self.podatki.polovicka == True):
         polovic = tk.PhotoImage(file = "ozadja/polovicka.gif")
         gumb.config(image = polovic)
      else:
         nepolovic = tk.PhotoImage(file = "ozadja/nepolovicka.gif")
         nepol = tk.Label(zacetek, image = nepolovic)
         nepol.place(relx = .1, rely = .1, anchor = "center")
      print(grafika.stevilka_vprasanja)
      
      
      novo = tk.Label(zacetek, text = vprasanje, fg = "white", bg = "grey6", font = ("Comic Sans MS", 30))
      novo.place(relx = .5, rely = .2, anchor = "center")
      if(grafika.stevilka_vprasanja <= 5):
         A = tk.Button(zacetek, text = self.podatki.odgovori_A_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'a',novo))
         B = tk.Button(zacetek, text = self.podatki.odgovori_B_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30),command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'b',novo))
         C = tk.Button(zacetek, text = self.podatki.odgovori_C_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'c',novo))
         D = tk.Button(zacetek, text = self.podatki.odgovori_D_prvi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'd',novo))
         grafika.seznam_gumbov.append(A)
         grafika.seznam_gumbov.append(B)
         grafika.seznam_gumbov.append(C)
         grafika.seznam_gumbov.append(D)
      elif(grafika.stevilka_vprasanja > 5 and self.stevilka_vprasanja <= 10):
         A = tk.Button(zacetek, text = self.podatki.odgovori_A_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'a',novo))
         B = tk.Button(zacetek, text = self.podatki.odgovori_B_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30),command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'b',novo))
         C = tk.Button(zacetek, text = self.podatki.odgovori_C_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'c', novo))
         D = tk.Button(zacetek, text = self.podatki.odgovori_D_drugi[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'd', novo))
         grafika.seznam_gumbov.append(A)
         grafika.seznam_gumbov.append(B)
         grafika.seznam_gumbov.append(C)
         grafika.seznam_gumbov.append(D)
      elif(grafika.stevilka_vprasanja > 10):
         A = tk.Button(zacetek, text = self.podatki.odgovori_A_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'a', novo))
         B = tk.Button(zacetek, text = self.podatki.odgovori_B_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'b', novo))
         C = tk.Button(zacetek, text = self.podatki.odgovori_C_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self,indeks,zacetek, 'c', novo))
         D = tk.Button(zacetek, text = self.podatki.odgovori_D_tretji[indeks], fg = "white", bg = "grey6", font = ("Comic Sans MS", 30), command = lambda: grafika.preveri_odgovor(self, indeks,zacetek, 'd', novo))
         grafika.seznam_gumbov.append(A)
         grafika.seznam_gumbov.append(B)
         grafika.seznam_gumbov.append(C)
         grafika.seznam_gumbov.append(D)
      grafika.seznam_gumbov[0].place(relx = .4, rely = .4, anchor = "center")
      grafika.seznam_gumbov[1].place(relx = .6, rely = .4, anchor = "center")
      grafika.seznam_gumbov[2].place(relx = .4, rely = .5, anchor = "center")
      grafika.seznam_gumbov[3].place(relx = .6, rely = .5, anchor = "center")
      if(grafika.stevilka_vprasanja <= 5):
         del self.podatki.vprasanja_prvi_nivo[indeks]
         
      elif(grafika.stevilka_vprasanja > 5 and grafika.stevilka_vprasanja <= 10):
         del self.podatki.vprasanja_drugi_nivo[indeks]
         
      elif(grafika.stevilka_vprasanja > 10):
         del self.podatki.vprasanja_tretji_nivo[indeks]
       
      zacetek.mainloop()



def prva(okno):
   zazeni_glasbo = True
   glasba = "glasba/Who - Wants.wav"
   winsound.PlaySound(glasba, winsound.SND_ALIAS | winsound.SND_ASYNC)
   sirina_okna = okno.winfo_screenwidth()
   visina_okna = okno.winfo_screenheight()
   zasluzeni_denar = 0
   stevilka_vprasanja = 1
   polovicka = True
   vsebina = podatki(stevilka_vprasanja,zasluzeni_denar, polovicka, 60)
   print(vsebina.odgovori_A_prvi, vsebina.odgovori_B_prvi, vsebina.odgovori_C_prvi, vsebina.odgovori_D_prvi)
   vmesnik = grafika(sirina_okna, visina_okna, vsebina, okno, glasba, stevilka_vprasanja)
   okno.geometry("{0}x{1}+0+0".format(sirina_okna,visina_okna ))
   ozadje = tk.PhotoImage(file = "ozadja/mil.gif")
   ozadje_s_sliko = tk.Label(okno, image = ozadje)
   ozadje_s_sliko.place(x = 0, y = 0, relwidth = 1, relheight = 1)
   gumb_za_zacetek = tk.Button(okno, text = "Začni z igro",fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: vmesnik.pozdravno_okno(okno, zazeni_glasbo))
   gumb_za_zacetek.place(relx = .1, rely = .5 , anchor = "center")
   izhod = tk.Button(okno, text = "Ne upam :(", fg = "white", bg = "grey6", font = ("Comic Sans MS", 40  ), command = lambda: vmesnik.izhod__(okno))
   izhod.place(relx = .9, rely = .5 , anchor = "center")
   okno.mainloop()

okno = tk.Tk()
prva(okno)
