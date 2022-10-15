# syntax->Söz dilimi demektir.
# compilation vs interpretation
# print("selam")
# tüm kodlar sol kenara dayalı olmalı → indentation

# ödev →
"""
şöyle bir çıktıyı tek bir print kullanarak ekrana yazınız;
kim    korkar
pythondan
"""

# print("kim\t\tkorkar")

# ödev →
"""
S.N     Ad      Soyad
---     ---     ---
1       yusuf   şahin
print("S.No\tAd\tSoyad\n---\t---\t---\n1\tEkin\tAkın")

"""

# print("Sayı Numarası\tAD\tSoyad\n1\t\tİbrahim\tKayatepe\n2\t\tFurkan\tYılmaz")

"""
raw string r string ile başlayınca içerideki komutları bu seferlik affet anlamına geliyor.
# print("C:\Windows\System32\networklist")
# print(r"C:\Windows\System32\networklist")
"""

"""
Hayatta En Hakiki 
İlim Mürşittir.     aralarına işaret koyarak yaz.
"""

# print("Hayatta", "En", "Hakiki", sep="*", end=" ")
# print("İlim", "Mürşittir",sep="+" , end=".")

# print("Hayatta", "En", "Hakiki", sep="*",)
# print("İlim", "Mürşittir",sep="+" , end=".")


"""
istanbul-teknopark
ecodation>>eğitim>>kurumları.
"""

# print("istanbul" , "TeknoPark", sep="-")
# print("ecodation", " eğitim", "kurumları", sep=">>>" ,end=".")

# region1
"""
Bnların arasına bir şeyler yazı yazıp kapatabiliriz.
"""
# endregion2

"""
Dünya'nın♥En♥Güzel♥Şehri→İstanbul.
"""
# print("Dünya'nın" , " En", "Güzel","Şehri" , sep="♥" ,end="→")
# print("istanbul", end=".")

"""
"Ege'nin"☼"İncisi"☼"İzmir"!
alt+15  ☼
"""

# print("Ege'nin", "İncisi" , "İzmir" ,sep="☼")

"""
okulNumarasi = 271
ad = "Emir"
soyad = "Besi"
sinavNotu = 99
print(okulNumarasi,ad, soyad, sinavNotu)
print("okul numarası", okulNumarasi," olan ", ad, soyad," isimli öğreninin snv notu ", sinavNotu)
"""

# okulNumarasi=input("Lütfen okul numaranızı giriniz:\t")

# ad=input("Lütfen adınızı giriniz:\t")
# soyad=input("Lütfen soyadınızı giriniz:\t")
# sinavNotu = int(input("Lütfen sınav notunuzu giriniz:\t"))
# print(f"{okulNumarasi} okul numaralı {ad} {soyad} isimli öğrencinin sınav notu {sinavNotu} 'dır.")

"""
programlamaDili = "c#"
os = "7"
ver = "8.0"
print("windows versiyonu " + os + " " + programlamaDili, " versiyonu " + ver)
"""

# programlamaDili=input("Lütfen program dilinizi giriniz:\t")
# os=int(input("Lütfen os giriniz:\t"))
# ver=float(input("Lütfen versiyon giriniz:\t"))

# print(f"{os} window versiyonu olan {programlamaDili} dilindeki versiyon {ver}'dir.")

"""
baslangic= "istanbul"
bitis = "danimarka"
mesafe = "2800"
print(baslangic + " ile " + bitis + " arası " + mesafe + " km.")
"""

# baslangic=input("Lütfen başlangıç noktası seçiniz:\t")
# bitiş=input("Lütfen bitiş nokasını seçiniz:\t")
# mesafe=int(input("Lütfen mesafe bilgisi giriniz:\t"))
# print(f"{baslangic} {bitiş} arası mesafe {mesafe}' km dir.")

"""
a = 15
b = 25
temp = a
a = b
b = temp
a, b = b, a
print("a değeri", a, " b değeri", b)
"""

"""
delta örneği
a = 1
b = 4
c = 2
delta = b**2 - 4*a*c
print("delta değeri " , delta)
"""
# a=int(input("Lütfen a değerinizi giriniz:\t"))
# b=int(input("Lütfen b değerinizi giriniz:\t"))
# c=int(input("Lütfen c değerinizi giriniz:\t"))
# delta=((b**2)-(4*a*c))
# print("delta değeri" , delta)

"""
ortalama
s1 = 2
s2 = 4
ort = (s1 + s2) / 2
print("oralama değeri ", ort)
"""

# s1=int(input("Lütfen s1 değerini giriniz:\t"))
# s2=int(input("Lütfen s2 değerini giriniz:\t"))
# ort=(s1+s2)/2
# print("ortalama değer" , ort)

"""
saat bilgisini saniyeye dönüştürsün
saat = 2
saniye = 3600
print("Saat: ", saat)
print("Ekrandaki saat biriminin saniye karşılığı →", saat*saniye, " sn.")
"""

# saat=float(input("Lütfen saat giriniz:\t"))
# dakika=saat*60
# saniye=dakika*60
# print(f"{saat} saat {dakika} dakika ve {saniye} saniye yapar.")

"""
sayi = 562
kalan = sayi % 10
birler = kalan // 1
kalan = sayi % 100
onlar = kalan // 10
kalan = sayi % 1000
yuzler = kalan //100
toplamDegeri = birler + onlar + yuzler
print(yuzler, onlar, birler)
print(sayi, " sayısının basamakları toplamı " , toplamDegeri)
"""

# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# kalan=sayi%10
# birler=kalan//1
# kalan=sayi%100
# onlar=kalan//10
# kalan = sayi % 1000
# yuzler = kalan //100
# kalan=sayi%10000
# binler=kalan//1000
# toplamDeger=birler+onlar+yuzler+binler
# print(binler,yuzler,onlar,birler)
# print(sayi, "sayısının basamak değerleri toplamı" , toplamDeger)

# ödev →
"""
boy bilgisi girilen değeri; metre ve santimetre cinsinden ekrana yazınız.
Örn. 165
1 metre 65 santim
"""

# boy=int(input("Lütfen boyunuzu santimetre cinsinden giriniz:\t"))
# m=boy//100
# cm=boy%100
# print(m , "metre" , cm ,"santimetre")

# kg=float(input("Lütfen ağırlığınızı kg cinsinden giriniz:\t"))
# boy=float(input("Lütfen boyunuzu metre cinsinden giriniz:\t"))
# vki=(kg/(boy**2))
# print(f"{kg} kilogram ve {boy} metre olan bireyin vücut kitle indeksi {round(vki,2)}'dir.")
# if vki <18.5:
#     print("Zayıf")
# elif 18.5<vki<24.9:
#     print("normal")
# elif 24.9<vki<29.9:
#     print("kilolu")
# else:
#     print("obez")

"""
dTarihi = int(input("Doğum Tarihi Giriniz\t: "))
#dTarihi = int(dTarihi)
yas = 2021 - dTarihi
print(dTarihi, "doğum tarihli üyemizin yaşı", yas)
"""
# dTarihi = int(input("Doğum Tarihi Giriniz\t: "))
# #dTarihi = int(dTarihi)
# yas = 2021 - dTarihi
# print(dTarihi, "doğum tarihli üyemizin yaşı", yas)

"""
km cinsinden girilen mesafe bilgisini mil'e çeviren programı yazınız.
mil =  km / 1.609344
"""

# km=int(input("Lütfen km bilgisi giriniz:\t"))
# mil =  km / 1.609344
# print(f"{km} km {round(mil,2)} mile eşittir.")

"""
- Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.
"""

# x1=int(input("Lütfen x1 sayısını giriniz:\t"))
# x2=int(input("Lütfen x2 sayısını giriniz:\t"))
# y1=int(input("Lütfen y1 sayısını giriniz:\t"))
# y2=int(input("Lütfen y2 sayısını giriniz:\t"))
# uzaklik=(((x1-x2)**2)+((y1-y2)**2))**(0.5)
# print(f"{x1,x2} ve {y1,y2} değerleri arasındaki uzaklık birimi {round(uzaklik,2)}")

"""
Güncel Benzin Endeksini Giriniz                 : 7.09
Yakıt Tüketimini Giriniz [100 km. başına] )     : 4.08
Kaç Kilometre Yol Aldınız?                      : 50
Toplam Yakıt Tüketimi → 14.4636  
"""

# güncelBenzin=float(input("Güncel Benzin Endeksini Giriniz:\t"))
# yakıtTüketimi=float(input("Yakıt Tüketimini Giriniz [100 km. başına]:\t )"))
# gidilenYol=float(input("Kaç Kilometre Yol Aldınız? :\t"))
# toplamTutar=(gidilenYol/100)*yakıtTüketimi*güncelBenzin
# print(f"Toplam Tutar={round(toplamTutar,2)}")

"""
ogrenciYas = int(input("Lütfen Öğrencinin Yaşını Giriniz: "))
print(ogrenciYas >= 18)
"""

# ogrenciYas=int(input("Lütfen öğrencinin yaşını giriniz:\t"))
# print(ogrenciYas>=18)

"""
Kullanıcı Adını Giriniz : admin     → True 
Kullanıcı Adını Giriniz : user      → False 
"""

# ad="admin"
# kullaniciAd=input("Lütfen kullanıcı adını giriniz:\t")
# print(kullaniciAd==ad)

"""
s = int(input("Lütfen sayı giriniz \t : "))
if s == 0:
    print("lütfen 0 değeri girmeyin")
"""

# s = int(input("Lütfen sayı giriniz \t : "))
# if s == 0:
#     print("lütfen 0 değeri girmeyin")
# else:
#     print(f"{s} girmiş olduğunuz sayıdır.")

"""
uName = input("lütfen kullanıcı adınızı giriniz : ")
if uName != "admin":
    print(f"{uName} admin paneline giriş yapamaz")
"""

# name=input("lütfen kullanıcı adınızı giriniz : ")
# if name!="admin":
#     print(f"{name} admin paneline giriş yapamaz.")
# else:
#     print("HOŞ GELDİNİZ...")

"""
bavulAgirligi = 16
biletFiyat  = float(input("lütfen bilet fiyatını giriniz: "))
if bavulAgirligi>15:
    fark = bavulAgirligi - 15
    biletFiyat += fark*5
print(f"güncel bilet fiyatı {round(biletFiyat*1.18, 2)} TL.")
fazla olan bavul kg ağırlığınında kdv sini alınız.

"""
# biletToplam=0
# ucusHat=input("Lütfen uçuş yapacağınız hattı seçiniz.")
# biletFiyati=float(input("Lütfen bilet fiyatını giriniz:\t"))
# bavulAgirligi=float(input("Lütfen bavul ağırlığını giriniz:\t"))
# if (ucusHat=="yurtiçi"):
#     if bavulAgirligi>15:
#         fark=bavulAgirligi-15
#         biletFiyati+=fark*5
#         biletToplam=((biletFiyati)*(1.18))
#         print(f"{bavulAgirligi} kg bavul ağırlığınız varken yurtiçinde  toplam tutarınız {biletToplam}")
#     else:
#         biletToplam=biletFiyati
#         print(f"{bavulAgirligi} kg bavul ağırlığınız varken yurtiçinde  toplam tutarınız {biletToplam}")
# elif (ucusHat=="yurtdışı"):
#     if bavulAgirligi>15:
#         fark=bavulAgirligi-15
#         biletFiyati+=fark*5
#         biletToplam=((biletFiyati)*(1.50))
#         print(f"{bavulAgirligi} kg bavul ağırlığınız varken yurtdışında  toplam tutarınız {biletToplam}")
#     else:
#         biletToplam=biletFiyati
#         print(f"{bavulAgirligi} kg bavul ağırlığınız varken yurtdışında  toplam tutarınız {biletToplam}")
# else:
#     print("Lütfen uçuş hattını doğru formatta yazınız..")

"""
sayi = int(input("lütfen sayı giriniz "))
if sayi<0:
    sayi *= -1
print(f"sayının mutlak değeri {sayi}")
"""

# sayi = int(input("lütfen sayı giriniz "))
# if sayi < 0:
#     sayiasli = sayi
#     sayi *= -1
#     print(f" {sayiasli} sayınının mutlak değeri {sayi}")
# else:
#     print(f"{sayi} sayısının mutlak değeri de {sayi} ")

"""
bakiye = 5000
bankaKodu = 101
eftBankaKodu = 101
kesinti = 0
transfer = float(input("lütfen eft tutarını giriniz : "))
if bankaKodu != eftBankaKodu:
    kesinti = transfer*0.05
print(f"güncel bakiyeniz {bakiye - transfer - kesinti} TL.")
"""

# bakiye=5000
# kesinti = 0
# bankaKodu=int(input("Lütfen Banka Kodunuz Giriniz:\t"))
# eftKodu=int(input("Lütfen EFT Kodunuz Giriniz:\t"))
# transfer=float(input("Lütfen EFT tutarını giriniz:\t"))
# if bankaKodu!=eftKodu:
#     kesinti=(transfer*0.05)
# print(f"güncel bakiyeniz {bakiye - transfer - kesinti} TL.")

"""
3 sayı girilecek en büyük ekrana yazılacak
"""
# eb=0
# sayi1=int(input("Lütfen sayi giriniz:\t"))
# if sayi1>eb:
#     eb=sayi1
# sayi2=int(input("Lütfen sayi giriniz:\t"))
# if sayi2>eb:
#     eb=sayi2
# sayi3=int(input("Lütfen sayi giriniz:\t"))
# if sayi3>eb:
#     eb=sayi3
# print(f"Girilen sayıların en büyüğü {eb}'dir.")

"""
3 sayının ortalamasını alınız.
"""
# s1 = int(input("Lütfen 1. Sayı Giriniz \t : "))
# s2 = int(input("Lütfen 2. Sayı Giriniz \t : "))
# s3 = int(input("Lütfen 3. Sayı Giriniz \t : "))
# ort = (s1+s2+s3) / 3
# if ort >= 50:
#     print(f"GEÇTİNİZ, ORTALAMANIZ {round(ort,2)}")
# else:
#     print(f"KALDINIZ, ORTALAMANIZ {round(ort,2)}")

"""
Kargo Bedeli 7.5 TL.’dir
Satın Alınan Ürünlerin Toplam Fiyatı 250 TL üzeri olduğunda kargo bedavadır.
Kullanıcıdan fiyat bilgisi alıp ekrana ödenecek tutarı yazan prog.?
"""

# kargoBedeli=7.5
# urunFiyat=int(input("Lütfen ürün fiyatını giriniz:\t"))
# if urunFiyat>=250:
#     print(f"ürün fiyatınız {urunFiyat} 'dir. Yani 250 TL den fazla olduğunu için toplam tutarınız {urunFiyat}'dir.")
# else:
#     print(f"ürün fiyatınız {urunFiyat} 'dir. Yani 250 TL den az olduğunu için toplam tutarınız {urunFiyat+kargoBedeli}'dir.")

"""
sayı alınsın tek mi çift mi yazdırılsın.
"""

# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi %2 == 1 :
#     print(f"{sayi} sayısı tektir.")
# else:
#     print(f"{sayi} sayısı çifttir..")

"""
sayı alınsın negatif pozitif sıfır mı kontrol edilsin.
"""

# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi>0 :
#     print(f"{sayi} sayısı pozitiftir..")
# elif sayi<0:
#     print(f"{sayi} sayısı negatiftir.")
# else:
#     print("Sayı sıfırdır.")

"""
Sayı alınsın 0-100 arasında pozitif yada 100 + olup olmadığı kontrol edilsin.
"""
# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi > 0 :
#     if sayi<100:
#         print(f"{sayi} sayısı 100 den küçük ve pozitiftir.")
#     else:
#         print(f"{sayi} sayısı 100 den büyük ve pozitiftir.")
# else:
#     print("Lütfen 0 ya da negatif sayı girmeyiniz.")

"""
2 ayrı sınav notu giriniz. Ortalamasını alınız.85/70/55/45/ olarak kategorilere ayırınız.
"""

# sinavNotu1 = int(input("Lütfen 1.sınav notunu giriniz:\t"))
# sinavNotu2 = int(input("Lütfen 2.sınav notunu giriniz:\t"))
# ort = (sinavNotu1+sinavNotu2)/2
# if ort >= 85:
#     print(f"{ort}, sınıf ortalamanızdır. ÇOK İYİ")
# elif ort >= 70:
#     print(f"{ort}, sınıf ortalamanızdır. İYİ")
# elif ort >= 55:
#     print(f"{ort}, sınıf ortalamanızdır. ORTA")
# elif ort >= 45:
#     print(f"{ort}, sınıf ortalamanızdır. GEÇER")
# else:
#     print(f"{ort}, sınıf ortalamanızdır. KALDI")

"""
3 sayı giriniz aralarında büyükten küçükü sırlayınız.
"""
# s1 = int(input("l. s1. giriniz : "))
# s2 = int(input("l. s2. giriniz : "))
# s3 = int(input("l. s3. giriniz : "))

# if s1<s2:
#     s1,s2=s2,s1
# if s1<s3:
#     s1,s3=s3,s1
# if s2<s3:
#     s2,s3=s3,s2
# print(f"{s1}>{s2}>{s3}")

"""
2 değer int değer alınız. oluşan dikdörtgen veya karenin alanını hesaplayınız.
"""

# a = int(input("lütfen a kenarını giriniz \t : "))
# b = int(input("lütfen b kenarını giriniz \t : "))
# if a==b:
#      print(f"karenin alanı {a*b}")
# else:
#      print(f"diktörtgenin alanı {a*b}")

"""
2 kenar uzunluğu verisi alınız . kısa kenar uzun kenardan büyük değer alamaz. Dikdörtgenin çevresini hesaplayınız.
"""

# kisaKenar = int(input("lütfen kısa kenarını giriniz \t : "))
# uzunKenar = int(input("lütfen uzun kenarını giriniz \t : "))
# if kisaKenar>=uzunKenar:
#     print("Kısa kenar daha uzun ve ya eşit girilemez.")
# else:
#     print(f"Dikdörtgenin çevresi {2*(kisaKenar+uzunKenar)}")

"""
2 sayı alınız. a sayısı b sayısında ta bölünür mü bölünmez mi belirtiniz.
"""

# a = int(input("lütfen 1. s giriniz \t : "))
# b = int(input("lütfen 2. s giriniz \t : "))
# if a%b==0:
#     print(f"{a} sayısı {b} sayısına tam bölünür.")
# else:
#     print(f"{a} sayısı {b} sayısına tam bölünmez.")

"""
    - Kullanıcıdan bir sayı alınır.
        - Pozitifse karesini yazdırın.
        - Negatifse karekökünü yazdırın.
        - 0'sa sıfır yazsın
"""

# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi>0:
#     print(f"{sayi} sayısı pozitif olduğu için {sayi**2}")
# elif sayi<0:
#     print(f"{sayi} sayısı negatif olduğu için {sayi**(0.5)}")
# else:
#     print("0")

"""
    - Klavyeden iki tane fiyat verisi alınır.
    - Eğer bu fiyat verileri düzgünse;
        - Eğer ödenecek tutar 200TL den fazlaysa, ikinci ürüne
            %25 indirim yapılacaktır.
        - Değilse bişey yapılmayacak.
    - 150,300 -> Ürünlerin fiyatı .. TL ve .. TL'dir. İkinci ürüne
     .. TL indirim yapılmıştır. Borcunuz : ..TL'dir.
"""

# urunFiyati1=int(input("Lütfen 1.ürünün fiyatını giriniz:\t"))
# urunFiyati2=int(input("Lütfen 2.ürünün fiyatını giriniz:\t"))
# urunToplam=urunFiyati1+urunFiyati2
# if urunToplam>200:
#     print(f"Toplam tutar {urunToplam}'dır. 200 TL den fazla olduğu için 2.ürüne %25 indirim hakkı kazandınız. Ödeyeceğiniz tutar→{urunFiyati1+(urunFiyati2*75/100)}'TL'dir.")
# else:
#     print(f"Toplam tutar {urunToplam}'dır. Kampyadan faydalanmak için ürün toplam tutarınız 200 TL yi geçmelidir. {200-urunToplam} TL daha alışveriş yapınız.")

"""
    - ax2+bx+c = 0
    - Kullanıcıdan a,b,c değerleri alınır. Bu degerler uygunsa ;
        - delta = b2 - 4ac
        - delta>0. iki kök : (-b+kök(delta))/2a,(-b-kök(delta))/2a
        - delta=0. iki kök : k1=k2=-b/2a
        - delta<0. kök yoktur.
"""

# a=int(input("Lüten a sayısını giriniz:\t"))
# b=int(input("Lüten b sayısını giriniz:\t"))
# c=int(input("Lüten c sayısını giriniz:\t"))
# delta=(b**2)-(4*a*c)
# if delta>0:
#     print(f"delta 0'dan büyük olduğu için iki kök vardır.")
#     print(f"{(((-b)+(delta)**(0.5)))/(2*a)}")
#     print(f"{(((-b)-(delta)**(0.5)))/(2*a)}")
# elif delta==0:
#     print(f"Delta 0'a eşitse 2 eşik kök vardır.")
#     print(f"{(-b)/(2*a)}")
#     print(f"{(-b)/(2*a)}")
# else:
#     print("Delta 0 dan küçük olduğu için kök yoktur.")

# yakitTuru=input("Lütfen yakıt türünüzü giriniz:\t")
# yakitTuketimi=float(input("Aracınızın 100 km.'deki ortalama yakıt tütekimi kullanıcıdan alınacak "))
# yakitKuru=float(input("Güncel yakıt bilgisi giriniz."))
# gidilenYol=float(input("Gidelen km bilgisini giriniz:\t"))
# toplamTutar=(((gidilenYol/100)*yakitTuketimi)*yakitKuru)
# print((f" Yakıt türü {yakitTuru} olan bir araç 100 km'de {yakitTuketimi} yakıt yakıyorsa ve yakit kuru {yakitKuru} ise {gidilenYol} gittiğinde {toplamTutar} TL para harcar."))


"""
print("24 saatte kargoda")
alt alta 12 kez yazdırmak için while kullanırız.

"""
# print("24 saatte kargoda")
# print("24 saatte kargoda")
# print("24 saatte kargoda")
# print("24 saatte kargoda")
# print("24 saatte kargoda")
# print("24 saatte kargoda")

# i=0
# while i<12:
#     print("24 saatte kargoda")
#     i+=2


"""
while True:
    print("şu an while döngüsü içindeyim")

"""
# while True:
#     print("şu an while döngüsü içindeyim")

"""
1 → BAŞLANGIÇ
2 → BİTİŞ
3 → ARTIŞ MİKTARI
 
i = 0
print("a")
while i<=3:
    i +=1
    print("b")
print("c")
""" 
"""
i = 1
while i<3:   # i büyük 3 olduğu sürece DÖN   
    print("sponsorlu ürün")
"""

"""
2 sayı al.
başlangıc ve bitiş sayıları olsun
başlangıc ve bitiş sayıları arasındaki sayı kadar 2 şer 2 şer 
--Bizim seninle el ele vererek sikemeceğimiz adam yok-- yazdır.
"""

# a=int(input("Lütfen a sayı giriniz:\t"))
# b=int(input("Lütfen b sayı giriniz:\t"))
# i=a
# while i<b:
#     print("Bizim seninle el ele vererek sikemeceğimiz adam yok")
#     i+=2
"""
sayac = 1
while sayac<=5:
    print(sayac)
    sayac += 1
"""

"ekrana bir metin girin 5 kere yazdırı"
