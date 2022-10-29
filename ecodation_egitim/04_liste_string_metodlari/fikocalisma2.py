"""
rakamlar = [6, 2, 7, 3, 5]
Çıktı:
["ALTI", "İKİ", "YEDİ", "ÜÇ, "BEŞ"]
"""

# i=0
# rakamlar=[6, 2, 7, 3, 5]
# yazi=[" ","BİR","İKİ","ÜÇ","DÖRT","BEŞ","ALTI","YEDİ","SEKİZ","DOKUZ"]
# for i in range(0,len(rakamlar)):
#     x=int(rakamlar[i])
#     print(f"{yazi[x%10]}",end=" ")
    
 
"""
Çözülen ticket adetini ve çözen kişileri  belirten uygulama yazınız.
"""

# cozulenAdet=[]
# calisanEkip=[]
# while True:
#     i=0
#     cozenKisi=input("Lütfen ad soyad giriniz: çıkmak için 00 yazınız:\t")
#     if cozenKisi=="00":
#         print("Çıkış yaptınız.Güle güle")
#         break
#     ticketAdet=int(input("Lütfen çözülen ticket sayısınız giriniz :\t"))
#     if ticketAdet>=34:
#         print(f"{cozenKisi} Tebrik ederiz.Ticket çözme adedinden 3 puan aldınız.Devam ediniz.")
#     elif ticketAdet>=21:
#         print(f"{cozenKisi} Tebrik ederiz.Ticket çözme adedinden 2 puan aldınız.Gayret gösteriniz.")
#     elif ticketAdet>=10:
#         print(f"{cozenKisi} Tebrik ederiz.Ticket çözme adedinden 1 puan aldınız.Daha çok çalışınız")
#     elif 0<=ticketAdet<=9:
#         print(f"{cozenKisi} .Ticket çözme adedinden 0 puan aldınız.Uyarı alacaksınız.")
#     else:
#         print("Hatalı sayı girdiniz tekrar giriniz.")
#     calisanEkip.append(cozenKisi)
#     cozulenAdet.append(ticketAdet)
#     i+=1  
# for i in range(0,len(calisanEkip)):
#     if int(cozulenAdet[i])>=34:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} Tebrik ederiz.Ticket çözme adedinden 3 puan aldınız.Devam ediniz")
#     elif int(cozulenAdet[i])>=21:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} Tebrik ederiz.Ticket çözme adedinden 2 puan aldınız.Gayret gösteriniz.")
#     elif int(cozulenAdet[i])>=10:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} Tebrik ederiz.Ticket çözme adedinden 1 puan aldınız.Daha çok çalışınız")
#     elif 0<=int(cozulenAdet[i])<=9:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} .Ticket çözme adedinden 0 puan aldınız.Uyarı alacaksınız.")
#     else:
#         print("Hatalı sayı girdiniz tekrar giriniz.")

"""
ÖDEV 2

"""

# sinif=[
#     [1,     "Ali Kemal",        80,     50,      80],
#     [2,     "Murat Çalışkan",   50,     30,      70],
#     [3,     "Efe Aydın",        50,     20,      100]

# ]
# for i in range(len(sinif)):
#     for j in range(len(sinif[i])):
#         print(sinif[i][j], end=" ")
#     print()
# print(f"{sinif[0][1]} isimli öğrencinin dönem ortalaması {((sinif[0][2])+(sinif[0][3])+(sinif[0][4]))/3}")
# print(f"{sinif[1][1]} isimli öğrencinin en yüksek notu {max(sinif[1][2],sinif[1][3],sinif[1][4])}")
# print(f"Matematik dersinin sınıf ortalaması {((sinif[0][2])+(sinif[1][2])+(sinif[2][2]))/3}")


"""
ÖDEV 3
meyveler = ["elma", "armut", "erik", "şeftali"]
Çıktı:
ismi e ile başlayan meyve elma
ismi e ile başlayan meyve erik
"""

# meyveler = ["elma", "armut", "erik", "şeftali"]
# for i in range (len(meyveler)):
#     if meyveler[i][0]=="e":
#         print(f"ismi e ile başlayan meyve {meyveler[i]} ")


# from colorama import Fore


# comment=["yusuf" , "ibo" , "fiko"]
# print(comment(Fore.RED[0],Fore.BLUE[1],Fore.GREEN[2]))

# print(bool("abc"))
# print(bool("0"))


"""
ÖRNEK 1
"""

# print("ARAMA SAYISI HESAPLAMAYA HOŞ GELDİNİZ")
# print("ÇIKMAK İÇİN 00 YAZINIZ \n\n")
# calisanEkip=[]
# calanTel=[]
# acanTel=[]
# oran=[]
# while True:
#     i=0
#     ad=input("Lütfen çalışan adı soyadı giriniz, çıkmak için 00 basınız.\t")
#     if ad=="00":
#         print("Çıkış  yaptınız.")
#         break
#     arananSayi=int(input("Lütfen aranılan sayıyı giriniz:\t"))
#     ulasilanSayi=int(input("Lütfen ulaşılan sayıyı giriniz:\t"))
#     i+=1
#     yuzdeHesap=((ulasilanSayi*100)/arananSayi)
#     calisanEkip.append(ad)
#     calanTel.append(arananSayi)
#     acanTel.append(ulasilanSayi)
#     oran.append(yuzdeHesap)
# for i in range(0,len(calisanEkip)):
#     print(f"{calisanEkip[i]} adlı çalışanın aradığı kişi sayısı {calanTel[i]} ve ulaştığı kişi sayısı {acanTel[i]} % {oran[i]} kullanıcıya ulaşma oranına sahiptir.")



# print("ŞAHİN GALERİYE HOŞ GELDİNİZ")
# print("Çıkmak İçin '00' Yaz: \n\n ")

# guncelYil=2022
# aracListe = []
# aracMotor = []
# aracYıl = []
# aracFiyat = []
# aracFiyat2 = []
# kar = []

# while True:
#     i = 0
#     arabaMarka = input("Lütfen araba markasını giriniz : \t")
#     if arabaMarka == "00":
#         print("ŞAHİN GALERİ İYİ GÜNLER DİLER.")
#         break
#     arabaMotor = float(input("Lütfen araba motor hacmini giriniz : \t"))
#     arabaModel = int(input("Lütfen araba yılını giriniz : \t"))
#     arabaFiyat = int(input("Lütfen arabayı aldığınız ilk fiyatını giriniz : \t"))
#     arabaFiyat2 = int(input("Lütfen arabanını şu anki fiyatını giriniz : \t"))
#     i += 1
#     karOran = ((arabaFiyat2 - arabaFiyat) / arabaFiyat) * 100
#     aracListe.append(arabaMarka)
#     aracMotor.append(arabaMotor)
#     aracYıl.append(arabaModel)
#     aracFiyat.append(arabaFiyat)
#     aracFiyat2.append(arabaFiyat2)
#     kar.append(karOran)

# for i in range(0, len(aracListe)):
#     print(f"{aracListe[i]} marka, {aracMotor[i]} motor ve {guncelYil-aracYıl[i]} yaşında olan ilk alınan fiyatı {aracFiyat[i]} TL ve güncel fiyatı {aracFiyat2[i]} TL dir. Eğer arabatı şimdi satarsanız % {kar[i]} kar edersiniz.")





# print("Fikobİ diyetetik ve Beslenme A.Ş")
# print("Çıkmak için 00'a basınız.")

# hastaListesi=[]
# hastaKilo=[]
# hastaBoy=[]
# hastaVki=[]
# hastaKategori=[]
# while True:
#     i=0
#     hastaAd=input("Lütfen hasta ad soyad giriniz:\t")
#     if hastaAd=="00":
#         print("Tekrar bekleriz.")
#         break
#     kilo=float(input("Lütfen kilogram bilginizi giriniz(kg cinsinden):\t"))
#     boy=float(input("Lütfen boy bilginizi giriniz(metre cinsinden):\t"))
#     vki=(kilo/(boy**2))
#     if vki<=18:
#         print("zayıf")
#         hastaKategori.append("zayıf")
#     elif 18.6<=vki<=24.9:
#         print("normal")
#         hastaKategori.append("normal")
#     elif 25<=vki<=29.9:
#         print("kilolu")
#         hastaKategori.append("kilolu")
#     elif 30<=vki<=34.9:
#         print("obez")
#         hastaKategori.append("obez")
#     else:
#         print("ciddi obez")
#         hastaKategori.append("ciddi obez")
#     i+=1
#     hastaListesi.append(hastaAd)
#     hastaKilo.append(kilo)
#     hastaBoy.append(boy)
#     hastaVki.append(vki)
# for i in range(0,len(hastaListesi)):
#     if float(hastaVki[i])<=18.0:
#         print(f"{hastaListesi[i]} isimli hastanın kilosu →{hastaKilo[i]} boyu → {hastaBoy[i]} ve vücut kitle indeksi → {round(hastaVki[i],2)} ve girmiş olduğu kategori→ {hastaKategori[i]}")
#     elif 18.6<=float(hastaVki[i])<=24.9:
#         print(f"{hastaListesi[i]} isimli hastanın kilosu →{hastaKilo[i]} boyu → {hastaBoy[i]} ve vücut kitle indeksi → {round(hastaVki[i],2)} ve girmiş olduğu kategori→ {hastaKategori[i]}")
#     elif 25.0<=float(hastaVki[i])<=29.9:
#         print(f"{hastaListesi[i]} isimli hastanın kilosu →{hastaKilo[i]} boyu → {hastaBoy[i]} ve vücut kitle indeksi → {round(hastaVki[i],2)} ve girmiş olduğu kategori→ {hastaKategori[i]}")
#     elif 30.0<=float(hastaVki[i])<=34.9:
#         print(f"{hastaListesi[i]} isimli hastanın kilosu →{hastaKilo[i]} boyu → {hastaBoy[i]} ve vücut kitle indeksi → {round(hastaVki[i],2)} ve girmiş olduğu kategori→ {hastaKategori[i]}")
#     else:
#         print(f"{hastaListesi[i]} isimli hastanın kilosu →{hastaKilo[i]} boyu → {hastaBoy[i]} ve vücut kitle indeksi → {round(hastaVki[i],2)} ve girmiş olduğu kategori→ {hastaKategori[i]}")



# import tkinter as tk
# arayüz = tk.Tk()
# arayüz.title("LOGİN SAYFASI")
# arayüz.geometry("400x200")
# a1 = "ibrahim"
# a2 = "kayatepe"

# kullanici = tk.Label(text="KULLANICI ADI:")
# kullanici.place(x=20,y=10)

# y= tk.StringVar()
# kullanici_girisi = tk.Entry(textvariable=y)
# kullanici_girisi.place(x=130,y=10)

# kullanici = tk.Label(text="ŞİFRE:")
# kullanici.place(x=74,y=35)

# x= tk.StringVar()
# kullanici_girisi = tk.Entry(textvariable=x)
# kullanici_girisi.place(x=130,y=30)

# doğru_yanlis = tk.Label(text="", font="Verdana 10 bold")
# doğru_yanlis.place(x=100,y=95)
# def giris_komut():
#  kullan = y.get()
#  sif = x.get()
#  if kullan == a1 and sif == a2:
#   print("doğru")
#   doğru_yanlis.config(text="DOĞRU",fg="green")
#  else:
#   doğru_yanlis.config(text="YANLIŞ",fg="red") 
# giris = tk.Button(text="Giris",command=giris_komut)
# giris.place(x=150,y=55)

# arayüz.mainloop()


# print("Fikobİ diyetetik ve Beslenme A.Ş")
# print("Çıkmak için 00'a basınız.")

# hastaListesi=[]

# while True:
#     hastaBilgileri={
# }
#     hastaBilgileri["ad"]=input("Lütfen hasta ad soyad giriniz:\t")
#     if hastaBilgileri["ad"]=="00":
#         print("Tekrar bekleriz.")
#         break
#     kilo=float(input("Lütfen kilogram bilginizi giriniz(kg cinsinden):\t"))
#     boy=float(input("Lütfen boy bilginizi giriniz(metre cinsinden):\t"))
#     hastaBilgileri["boy"]=boy
#     hastaBilgileri["kilo"]=kilo
#     hastaBilgileri["vki"]=round(kilo/(boy**2))
#     if hastaBilgileri["vki"]<=18:
#         print("zayıf")
#         hastaBilgileri['kategori'] = "zayif"
#     elif 18.6<=hastaBilgileri["vki"]<=24.9:
#         print("normal")
#         hastaBilgileri['kategori'] = "normal"
#     elif 25<=hastaBilgileri["vki"]<=29.9:
#         print("kilolu")
#         hastaBilgileri['kategori'] = "kilolu"
#     elif 30<=hastaBilgileri["vki"]<=34.9:
#         print("obez")
#         hastaBilgileri['kategori'] = "obez"
#     else:
#         print("ciddi obez")
#         hastaBilgileri['kategori'] = "ciddi obez"
#     hastaListesi.append(hastaBilgileri)
# for hasta in hastaListesi:
#     print(hasta["ad"]+" isimli hastanın kilosu " + str(hasta["kilo"]) + "  boyu " + str(hasta["boy"]) + " ve vücut kitle indeksi " + str(hasta["vki"])+ " ve girmiş olduğu kategori " + hasta["kategori"] )


