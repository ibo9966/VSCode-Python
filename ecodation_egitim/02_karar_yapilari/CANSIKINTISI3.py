# İlk 5 günün tüm ödev ve örnekleri

# print("kim      korkar")

# print("Sayı Numarası\tAd\tSoyad\n1\tİbrahim\tKayatepe\n2\tFurkan\tYılmaz\n3\tDuygu\tSeçkin")

# İkiside aynı anlama gelmektedir. Birinde tırnak dışına "raw_string" anlamına gelen r yazarız . Birinde \ kaçma simgesi kullanılır.
# print("C:\Windows\System32\\networklist")
# print(r"C:\Windows\System32\networklist")

# Hayatta*en*hakiki mürşit*ilimdir.      yazdırınız.

# print("Hayatta", "en", "hakiki", sep="*", end=" ")
# print("mürşit", "ilimdir" , sep="*", end=".")

# istanbul-teknopark
# ecodation>>eğitim>>kurumları.   yazdırınız.

# print("istanbul" , "teknopark", sep="-",)
# print("ecodation" , " eğitim" , "kurumları", sep=">>" , end=".")

# Dünya'nın♥En♥Güzel♥Şehri→İstanbul.  yazınız..
# alt+3  ♥
# alt + 26 →

# print("Dünya'nın","En","Güzel","Şehri",sep="♥",end="→"
# print("istanbul", end=".")

# "Ege'nin"☼"İncisi"☼"İzmir"!         yazınız.
# alt+15  ☼

# print("Ege'nin", "İncisi", "İzmir", sep="☼", end="!")

# a=15
# c=15.5
# b="stringg"
# d=True
# print(type(d))

# print(2+2)
# print(4+4)
# print(9//2)
# print(9%3)

# print((3**2)+(1**2)+(3/1))

# github kayıt etmek için
# git add .
# git status(önemli değil ama yap)
# git commit -m 19092022-2058(kayıt etmek istediğin ad değişiebilir "tarih-saat")
# git push VSCode-Python master --force(klasör ismi değişebilir)

# from re import A

# a=1
# b=2
# a=b
# b=1
# print(a)

# a=1
# b=4
# c=2
# delta=?
# a = 1
# b = 4
# c = 2
# delta=(b**2)-(4*a*c)
# print("delta değeri" , delta)

# s1=2
# s2=4
# ort=(s1+s2)/2
# print("ortalama değeri" , ort)


# saat=int(input("kaç saat olduğunu giriniz."))
# dakika=saat*60
# saniye=saat*60*60
# print(f"{saat} saat {dakika} dakika {saniye} saniye yapar.")

# sayıların ondalık basamaklarını vs vs yazınız .----------#####ANLAMADIM#######------------
# sayi=int(input("Lütfen sayı giriniz:\t"))
# kalan = sayi % 10
# birler = kalan // 1
# kalan = sayi % 100
# onlar = kalan // 10
# kalan = sayi % 1000
# yuzler = kalan //100
# toplamDegeri=birler+onlar+yuzler
# print(yuzler, onlar , birler)
# print(sayi ," sayısının basamakları toplamı",toplamDegeri)

# boy bilgisi girilen değeri; metre ve santimetre cinsinden ekrana yazınız.
# boy=int(input("Lütfen boy bilgisi giriniz."))
# m=boy//100
# cm=boy%100
# print(f"{m} metre {cm} santimetre ")

# adimSayisi=int(input("Lütfen adım sayınızı giriniz:\t→"))
# günlükkalori=adimSayisi*0.09
# haftalikkalori=günlükkalori*7
# aylikkalori=haftalikkalori*4
# print(f"günlük ortalama {adimSayisi} atan biri günlük {günlükkalori} kalori , haftalık {haftalikkalori}, aylık {aylikkalori} kalori yakar.")

# name = "john"
# print(name)
# print(name)
# print(name)
# print(name)
# print(name)
# print(name)

# print(name*50)

# name = "john"
# i=0
# for i in range (i,6):
#     print(name)


# a=float(input("Girilecek sayı:\t"))
# print(round(a,2))

# i=1
# print(i)
# i=i+1
# print(i)
# sayi=10
# sayi=sayi-1
# sayi=sayi*2
# x=10
# x=x+1
# print(sayi)
# print(x)

# sayi=5
# toplam=0
# toplam=toplam+sayi
# sayi=10
# sayi=sayi+1
# toplam=toplam+sayi
# print(toplam)

# sayi=10
# sayi+=1
# print(sayi)

# sayi=15
# sayi-=1
# print(sayi)

# sayi=16
# sayi*=2
# print(sayi)

# sayi=16
# sayi/=2
# print(sayi)

# skor=0
# can=3
# #engeli geçtiğinde skor 1 artar.
# skor+=1

# #engele çarptığında can  1 azalır.
# can-=1
# print("anlık skorunuz", skor)
# print("kalan canınız", can)

# dTarihi=input("Lütfen Doğum Tarihinizi Giriniz:\t→")
# print(dTarihi)
# yas=2022-dTarihi
# print(f"{dTarihi} yılında doğan birisi 2022 yılında {yas} yaşındadır.")

# STRİNGTEN İNT ÇIKMAZ
# İNTTEN STRİNG ÇIKMAZ
# ----------------------------------------BİR KAÇ YOL VAR DÜZELTMEK İÇİN---------------

# dTarihi=int(input("Lütfen Doğum Tarihinizi Giriniz:\t→"))
# print(dTarihi)
# yas=2022-dTarihi
# print(f"{dTarihi} yılında doğan birisi 2022 yılında {yas} yaşındadır.")

# dTarihi=input("Lütfen Doğum Tarihinizi Giriniz:\t→")
# print(dTarihi)
# yas=2022-int(dTarihi)
# print(f"{dTarihi} yılında doğan birisi 2022 yılında {yas} yaşındadır.")


# GÜNÜN TARİHİNİ YAZMAK İÇİN GOOGLEDAN ARAŞTIR.

# dTarihi=int(input("Doğum tarihinizi giriniz:\t"))
# import datetime
# tarih = datetime.datetime.now()
# buYil=tarih.year
# yas=buYil-dTarihi
# print(f"{dTarihi} yılında doğan birisi {buYil} yılında  {yas} yaşında olur. ")

# a = int(input("lütfen dörtgenin a kenarını giriniz : "))
# b = int(input("lütfen dörtgenin b kenarını giriniz : "))
# alan=a*b
# print(f"diktörgenin alanı{alan} metre karedir.")

# concatenation
# replication

# okulTuru="Anadolu"
# seviye=12
# print(okulTuru+ "         \n\n\n\t   " + str(seviye))

# rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
# print("girdiğiniz rakamın bir fazlası {}".format(rakam , (rakam+1)))
# print("girdiğiniz {} rakamın bir fazlası {}".format(rakam, (rakam+1)))


# rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
# print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")
# a = int(input("l. a. de. giriniz: "))
# b = int(input("l. b. de. giriniz: "))
# print(f"{a} değeri ile {b} değerinin toplamı {a+b}")

# km=float(input("Girmek istediğiniz mesafeyi giriniz:\t"))
# mil=km/1.609344
# print(f"girmiş olduğunuz {km} kilometre {round(mil,3)} mile eşittir.")

# a=int(input("Lütfen Üçgenin A Kenarı Açısını Giriniz:\t"))
# b=int(input("Lütfen Üçgenin B Kenarı Açısını Giriniz:\t"))
# c=180-(a+b)
# print(f"A kenarının açısı {a} B kenarının açısı {b} bundan dolayı C kenarının açısı {c} dır.")

# x1=int(input("x1 sayısını giriniz:\t"))
# x2=int(input("x2 sayısını giriniz:\t"))
# y1=int(input("y1 sayısını giriniz:\t"))
# y2=int(input("y2 sayısını giriniz:\t"))
# uzaklik=(((x1-x2)**2)+((y1-y2)**2))**(0.5)
# print(f"x1,x2 ve y1,y2 noktaları arasındaki uzaklık {round(uzaklik,2)} birimdir.")


# güncelBenzin=float(input("Güncel Benzin Endeksini Giriniz:\t"))
# yakitTüketimi=float(input("Yakıt Tüketiminiz Giriniz [100 km. başına]:\t"))
# alinanKm=float(input("Kaç Kilometre Yol Aldığınızı Giriniz:\t"))
# toplamYakit=(alinanKm/100)*yakitTüketimi*güncelBenzin
# print(f"Yakıt tüketimi 100 km'de {yakitTüketimi} olan bir araç güncel benzin fiyatı {güncelBenzin} ise {alinanKm} km yol gidince {round(toplamYakit,2)} TL yakıt yakar.")

# ürünAdi=input("Lütfen ürün adı giriniz:\t")
# adet=int(input("Lütfen alınacak adet sayısını yazınız:\t"))
# ürünFiyati=float(input("Lütfen ürün fiyatı giriniz:\t"))
# indirim=float(input("Lütfen indirim oranını giriniz:\t"))
# ürünToplam=(100-indirim)*ürünFiyati*adet
# print(f"% {indirim} indirim ile fiyatı {ürünFiyati}  TL olan {ürünAdi}'lerden {adet} adet  alındığına göre toplam {ürünToplam} TL ödenmiştir.")

# bavulAgirligi=float(input("Bavulun ağırlığını giriniz:\t"))
# biletFiyati=float(input("Lütfen bilet fiyatını giriniz:\t"))
# if bavulAgirligi>15:
#     fark=bavulAgirligi-15
#     biletFiyati+=fark*5
# print(f"bilet fiyatı bavulun ekstraları ile birlikte {biletFiyati} TL'ye gelmektedir.")

# hatSeçimi=input("Lütfen hat seçiniz:\t")
# biletFiyati=float(input("Lütfen bilet fiyatını giriniz:\t"))
# if hatSeçimi=="yurtiçi":
#     print(f"Bilet fiyatı yurtiçi olduğu için %18 KDV+FAİZ ile {biletFiyati*1.18} TL dir.")
# elif hatSeçimi=="yurtdışı":
#     print(f"Bilet fiyatı yurtdışı olduğu için %50 KDV+FAİZ ile {biletFiyati*1.50} TL dir.")
# else:
#     print("Geçersiz hat lütfen hat seçimini 'yurtiçi' veya 'yurtdışı' olarak yapınız.")


# bavulAgirligi = float(input("Lütfen bavul ağırlığını giriniz:\t"))
# hatSeçimi = input("Lütfen hat seçiniz:\t")
# biletFiyati = float(input("Lütfen bilet fiyatını giriniz:\t"))
# if bavulAgirligi > 15:
#     fark = bavulAgirligi-15
#     if hatSeçimi == "yurtiçi":
#         biletFiyati *= 1.18
#     elif hatSeçimi == "yurtdışı":
#         biletFiyati *= 1.50
#     else:
#         print("Hat seçimini doğru yazınız.")
#     biletFiyati += (fark*5)

# if hatSeçimi == "yurtiçi":
#     print(f"Bilet fiyatı yurtiçi olduğu için %18 KDV+FAİZ+Ekstra Bavul ağırlığı {biletFiyati} TL dir.")
# elif hatSeçimi == "yurtdışı":
#     print(f"Bilet fiyatı yurtdışı olduğu için %50 KDV+FAİZ+Ekstra Bavul ağırlı ile {biletFiyati} TL dir.")
# else:
#     print("Geçersiz hat lütfen hat seçimini 'yurtiçi' veya 'yurtdışı' olarak yapınız.")


# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi<0:
#     sayi*=-1
# print(f"sayısının mutlak değeri {sayi} 'dir.")


# a=int(input("Lütfen sayı giriniz:\t"))
# if a<0:
#     b=a*-1
# print(f"{a} sayısının mutlak değeri {b} 'dir.")


# Kullanıcının bankadaki bakiyesi 10,000 TL dir. Kullanıcı aynı bankalar arasında EFT yaparsa komisyon ödememektedir. Kullanıcı farklı bankalar arasında EFT yaparsa
# %5 komisyon ödemektedir. Kalan bakiyeyi en son not almayı unutmayınız.

# bakiye=10000
# bankaKodu=1001
# eftBankaKodu=1001
# bankaKodu=input("Lütfen banka kodunuzu giriniz:\t→")
# eftBankaKodu=input("Lütfen Eft Banka kodunuzu giriniz:\t→")
# kesinti=0
# transferTutari=float(input("Lütfen EFT yapmak istediğiniz tutarı giriniz:\t"))
# if bankaKodu!=eftBankaKodu:
#     kesinti=transferTutari*(0.05)
# print(f"yapılan transferi ücreti:→ {transferTutari}, kesilen komisyon:→ {kesinti}, kalan bakiyeniz:→{bakiye-transferTutari-kesinti}'dir.  ")

# 3 sayı girilecek en büyük ekrana yazılacak

# eb = 0
# s = int(input("Lütfen Sayı Giriniz \t : "))
# if s > eb:
#     eb = s
# s = int(input("Lütfen Sayı Giriniz \t : "))
# if s > eb:
#     eb = s
# s = int(input("Lütfen Sayı Giriniz \t : "))
# if s > eb:
#     eb = s
# print(f"Girilen Sayıların En Büyüğü {eb}")

# eb=0
# sayi=int(input("Lütfen sayı giriniz:\t→"))
# if sayi>eb:
#     eb=sayi
# sayi=int(input("Lütfen sayı giriniz:\t→"))
# if sayi>eb:
#     eb=sayi
# sayi=int(input("Lütfen sayı giriniz:\t→"))
# if sayi>eb:
#     eb=sayi
# print(f"Girilen sayının en büyüğü {sayi}")


# sayi1=int(input("Lütfen 1.sayı giriniz:\t→"))
# sayi2=int(input("Lütfen 2.sayı giriniz:\t→"))
# sayi3=int(input("Lütfen 3.sayı giriniz:\t→"))
# eb=0
# if sayi1>eb:
#     eb=sayi1
# if sayi2>eb:
#     eb=sayi2
# if sayi3>eb:
#     eb=sayi3
# print(f"Girilen sayının en büyüğü {eb}")


# s1=int(input("Lütfen 1. Sayı Giriniz \t : "))
# s2=int(input("Lütfen 2. Sayı Giriniz \t : "))
# if s1>s2:
#     print(f"{s1}>{s2}")
# print("sayı 1 sayı 2 den büyük değil")

# kargoBedeli=7.5
# ürünFiyatı1=int(input("Lütfen 1. ürünün fiyatını giriniz:\t"))
# ürünFiyatı2=int(input("Lütfen 2. ürünün fiyatını giriniz:\t"))
# ürünFiyatı3=int(input("Lütfen 3. ürünün fiyatını giriniz:\t"))
# ürünToplami=ürünFiyatı1+ürünFiyatı2+ürünFiyatı3
# if ürünToplami<=250:
#     print(f"Ürünlerin toplam fiyatı {ürünToplami} kargo dahil {ürünToplami+kargoBedeli} dir.")
# print(f"Ürünlerin toplam fiyatı {ürünToplami} kargo dahil {ürünToplami} ")

# sayi = int(input("Lütfen sayı giriniz:\t→"))
# if sayi % 2 == 1:
#     print(f"{sayi} sayısı tektir..")
# else:
#     print(f"{sayi} sayısı çifttir..")

# sayi=int(input("Lütfen sayı giriniz:\t→"))
# if sayi>0:
#     print(f"{sayi} sayısı pozitftir..")
# elif sayi<0:
#     print(f"{sayi} sayısı negatiftir..")
# else:
#     print(f"{sayi} sayısı sıfırdır..")


# sayi=int(input("Lütfen sayı giriniz:\t→"))
# if sayi>0:
#     if sayi<100:
#         print(f"{sayi} sayısı 0 ile 100 arasındadır ve pozitiftir.")
#     elif sayi>100:
#         print(f"{sayi} sayısı 100 den büyük ve pozitiftir.")
#     else :
#         print(f"{sayi} sayısı 100 e eşittir.")
# else:
#     print("lütfen 0 ve ya negatif sayı girmeyiniz.")

# Öğrencinin aldığı notların ortalamasını 0-45, 45-55, 55-70, 70-85, 85-100 arasında durum ve notu belirterek yapınız.

# sinav1=int(input("1.Sınav notunu giriniz:\t→"))
# sinav2=int(input("2.Sınav notunu giriniz:\t→"))
# sinav3=int(input("3.Sınav notunu giriniz:\t→"))
# ort=(sinav1+sinav2+sinav3)/3
# if ort>=85:
#     print(f"Yıl sonu notunuz {ort}→ çok iyi")
# if ort>=70:
#     print(f"Yıl sonu notunuz {ort}→ iyi")
# if ort>=55:
#     print(f"Yıl sonu notunuz {ort}→ orta")
# if ort>=45:
#     print(f"Yıl sonu notunuz {ort}→ geçer")
# else:
#     print(f"Yıl sonu notunuz {ort}→ kaldı")

# s1 = int(input("lütfen s1. giriniz : "))
# s2 = int(input("lütfen s2. giriniz : "))
# s3 = int(input("lütfen s3. giriniz : "))
# if s1<s2:
#     s1, s2 = s2, s1
# if s1<s3:
#     s1, s3 = s3, s1
# if s2<s3:
#     s2, s3 = s3, s2
# print(f"{s1}>{s2}>{s3}")

# a = int(input("lütfen a kenarını giriniz \t : "))
# b = int(input("lütfen b kenarını giriniz \t : "))
# if a==b:
#     print(f"karenin alanı {a*b}")
# else:
#     print(f"diktörgenin alanı {a*b}")

# kisaKenar = int(input("lütfen kısa kenarını giriniz \t : "))
# uzunKenar = int(input("lütfen uzun kenarını giriniz \t : "))
# if kisaKenar>uzunKenar:
#     print("kısa kenar uzun kenardan uzun veya eşit olamaz lütfen kontrol ediniz.")
# else:
#     print(f"diktörgenin alanı:\t {kisaKenar*uzunKenar}")
#     print(f"diktörgenin çevresi:\t {(kisaKenar+uzunKenar)*2}")

# a = int(input("lütfen 1. s giriniz \t : "))
# b = int(input("lütfen 2. s giriniz \t : "))
# if a%b==0:
#     print(f"{a} sayısı {b} sayısına tam bölünür.")
# else:
#     print(f"{a} sayısı {b} sayısına tam bölünemez.")

# a = int(input("lütfen sayı giriniz \t : "))
# if a>0:
#     print(f"{a} sayısı pozitif olduğunu için karesi\t→ {(a**2)}")
# elif a<0:
#     print(f"{a} sayısı negatif olduğunu için karekökü\t→ {(a**(0.5))}")
# else :
#     print("sayı sıfırdır.")

# ürün1=int(input("1.ürün fiyatını giriniz:\t"))
# ürün2=int(input("2.ürün fiyatını giriniz:\t"))
# ürünToplam=ürün1+ürün2
# if ürünToplam>200:
#     print(f"Ürün Toplamı 200 TL yi geçtiği için toplam tutar :→{ürün1+(ürün2*75/100)}")
# else:
#     print(f"Ürün Toplam Fiyatı 200 TL yi geçmediği için toplam tutar:→{ürünToplam}")

# a = int(input("lütfen  a sayısını giriniz \t : "))
# b = int(input("lütfen  b sayısını giriniz \t : "))
# c = int(input("lütfen  c sayısını giriniz \t : "))
# delta=(b**2-(4*a*c))
# if delta>0:
#     print(f"iki kök vardır.")
#     print(f"1.kök→ {(((-1*b)+((delta)**(0.5)))/2*a)}")
#     print(f"2.kök→ {(((-1*b)-((delta)**(0.5)))/2*a)}")
# elif delta==0:
#     print("iki kök vardır.")
#     print(f"kökler→ {-b/(2*a)}")
# else:
#     print("Kök Yoktur...")


# vize=int(input("Lütfen vize notunuzu giriniz:\t"))
# final=int(input("Lütfen final notunuzu giriniz:\t"))5
# if 0<=vize<=100:
#     if 0<=final<=100:
#         dönemSonuNotu:(vize*40/100)+(final*60/100)
#         print(f"vize notunun %40 'ı {vize*40/100} final notunun %60'ı {final*60/100} olduğuna göre dönem sonu notun:→ {dönemSonuNotu}")
# if 90<=dönemSonuNotu<=100:
#     print(f"Dönem sonu notun {dönemSonuNotu} ve harfin {AA}")
# if 75<=dönemSonuNotu<=89:
#     print(f"Dönem sonu notun {dönemSonuNotu} ve harfin {BB}")
# if 60<=dönemSonuNotu<=74:
#     print(f"Dönem sonu notun {dönemSonuNotu} ve harfin {CC}")
# if 50<=dönemSonuNotu<=59:
#     print(f"Dönem sonu notun {dönemSonuNotu} ve harfin {DD}")
# else:
#     print(f"Dönem sonu notun {dönemSonuNotu} ve harfin {FF}")


# yakitTürü=input("Yakıt türünüzü yazınız:\t")
# aracinYakitTüketimi=float(input("Aracının 100 km'deki ortalama yakıt tüketimini yazınız:\t"))
# anlikYakitKuru=float(input("Anlık yakit kurunu yazını:\t"))
# gidilenYol=float(input("Kaç km yol gittiğinizi yazınız:\t"))
# toplamTutar=(gidilenYol/100)*aracinYakitTüketimi*anlikYakitKuru
# print(f" yakıt türü {yakitTürü} olan aracımızla {gidilenYol} km yol gittiğimiz taktirde anlık yakıt kuru {anlikYakitKuru} ise {round(toplamTutar)} TL harcamış oluruz. "  )

# import datetime

# isim=input("İsminizi Giriniz:\t")
# soyİsim=input("Soyisminizi Giriniz:\t")
# eğitim=input("Eğitim durumunuzu giriniz:\t")
# dTarihi=int(input("Doğum tarihinizi giriniz:\t"))
# tarih= datetime.datetime.now()
# buYil=tarih.year
# yas=buYil-dTarihi
# if yas>18:
#     if eğitim=="lise" or eğitim=="üniversite":
#         print(f"{isim} yaşın {yas} olduğu için ve eğitim durumun {eğitim} mezunu izin verdiği için ehliyet alabilirsin.")
#     else:
#         print(f"{isim} yaşın {yas} fakat eğitim durumun {eğitim} mezunu  olduğun için ehliyet alamazsın.")
# else:
#         print(f"Yaşınız {yas} 'dir. {18-yas} yıl sonra tekrar deneyiniz.")


# yazili1=float(input("Lütfen 1.Sınav Notunu Giriniz:"))
# yazili2=float(input("Lütfen 2.Sınav Notunu Giriniz:"))
# sözlü=float(input("Lütfen Sözlü Notunu Giriniz:"))
# ort=(yazili1*40/100)+(yazili2*40/100)+(sözlü*20/100)
# if 85<=ort<=100:
#     print(f"ortalamanız {ort}, notunuz 5")
# if 70<=ort<=84:
#     print(f"ortalamanız {ort}, notunuz 4")
# if 55<=ort<=69:
#     print(f"ortalamanız {ort}, notunuz 3")
# if 44<=ort<=54:
#     print(f"ortalamanız {ort}, notunuz 2")
# if 25<=ort<=44:
#     print(f"ortalamanız {ort}, notunuz 1")
# else:
#     print(f"ortalamanız {ort}, notunuz 0")


# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi>0:
#     print(f"{sayi} sayısı pozitiftir.")
# elif sayi<0:
#     print(f"{sayi} sayısı negatiftir.")
# else:
#     print(f"{sayi} sayısı sıfırdır.")



# email = "ibrahim@gmail.com"
# password = "abc12"

# girilenEmail = input("Mail adresinizi giriniz:\t")
# girilenPassword = input("Password giriniz:\t")

# if girilenEmail == "ibrahim@gmail.com":
#     if girilenPassword == "abc12":
#         print("uygulamaya giriş başarılı.")
#     else:
#         print("paralonız yanlış")
# else:
#     print("Email bilginiz yanlış")

# a=int(input("a sayısını giriniz:\t"))
# b=int(input("b sayısını giriniz:\t"))
# c=int(input("c sayısını giriniz:\t"))
# eb=0
# if a>eb:
#     eb=a
# if b>eb:
#     eb=b
# if c>eb:
#     eb=c
# print(f"en büyük sayı{eb}")

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if (a > b) and (a > c):
#     print(f'a en büyük sayıdır.')
# elif (b > a) and (b > c):
#     print(f'b en büyük sayıdır.')
# elif (c > a) and (c > b):
#     print(f'c en büyük sayıdır.')