"""

Banka'da 10000 TL parası olan bir banka müşterisi para transferi yapmak istiyor.
Transfer yapılacak banka farklı ise %5 kesinti yapılacak.
Günün sonunda ekrana güncel bakiye yazılacaktır.
Lütfen bankanızın Kodunu giriniz:

"""


# bakiye = 10000
# bankaKodu = int(input("Lütfen banka kodunu giriniz\t: "))
# transferBanka = int(input("Lütfen transfer edilecek banka kodunu giriniz\t:"))
# transferToplamTutar = int(input("Lütfen transfer miktarını giriniz\t: "))
# kesinti = "%5"


# if bankaKodu == transferBanka:
#     bakiye -= transferToplamTutar
#     print(f"Bankamız bu işlem için sizden ücret almayacaktır. Yeni bakiyeniz {bakiye} TL dir.")
# if bankaKodu != transferBanka:
#     bakiye = bakiye - (transferToplamTutar*0.05) - transferToplamTutar
#     print(f"Bakmanız bu işlem için sizden {kesinti} ücret alacaktır. Yeni bakiyeniz {bakiye} TL dir.")


# TEK İFLE AŞAĞIDAKİ GİBİ YAPILIR


# bakiye = 10000
# bankaKodu = int(input("Lütfen banka kodunu giriniz\t: "))
# transferBanka = int(input("Lütfen transfer edilecek banka kodunu giriniz\t:"))
# transferToplamTutar = int(input("Lütfen transfer miktarını giriniz\t: "))
# kesinti = 0


# if bankaKodu != transferBanka:
#     kesinti = transferToplamTutar * 0.05
# print(f"Bankanız bu işlem için sizden {kesinti} ücret alacaktır. Yeni bakiyeniz {bakiye-transferToplamTutar-kesinti} TL dir")


"""
Y.İçi Uçuşlarda KDV %18'dir.
Kontuar Görevlisi Fiyat Girecek.
Bavul Ağırlığı 15kg. üzerinde her bir ağırlık için bilet fiyatına 5 TL. ek ücret güncellemesi yapacak.
Günün sonunda güncel fiyat ekrana yazılacak.
"""


# bilet_fiyati = int(input("Bilet fiyatını giriniz:\t→"))
# bavul_kg = int(input("Bavulunuzun kaç kg olduğunuz yazınız:\t→"))
# if bavul_kg > 15:
#     fark = bavul_kg-15
#     bilet_fiyati += fark*5
# print(f"Güncel fiyatıı {bilet_fiyati*1.18} TL'dir.")

"""
L. 1. Sınav Notu Giriniz    : 90
L. 2. Sınav Notu Giriniz    : 100
Yıl Sonu Notunuz 95, Başarı Durumu Pekiye
"""

# sinav1=int(input("Lütfen 1 .sınav notu giriniz:\t→"))
# sinav2=int(input("Lütfen 2 .sınav notu giriniz:\t→"))

# ort=(sinav1+sinav2)/2
# if ort>=85:
#     print(f"Yıl sonu notunuz {ort} Durumu pekiyi")
# elif ort>=70:
#     print(f"Yıl sonu notunuz {ort} Durumu iyi")
# elif ort>=55:
#     print(f"Yıl sonu notunuz {ort} Durumu orta")
# elif ort>=45:
#     print(f"Yıl sonu notunuz {ort} Durumu geçer not")
# else:
#     print(f"Yıl sonu notunuz {ort} Durumu geçer kaldı")


"""
Kullanıcı Adı : user
Parola  : 1234
Kullanıcı Adı Hatalı, Lütfen Tekrar Deneyin


Kullanıcı Adı : admin
Parola  : 1234
Parola Hatalı, Lütfen Tekrar Deneyin


Kullanıcı Adı : admin
Parola  : 123
Login Başarılı
"""



# id="admin"
# pw="123"

# keyid=input("TCKN veya e-posta adresinizi giriniz:\t→")
# keypw=input("Lütfen parolanızı giriniz:\t→")

# if id == keyid:
#     if pw == keypw:
#         print("Login Başarılı")
#     else:
#         print("Parola Hatalı, Lütfen Tekrar Deneyin")
# else:
#     print("Kullanıcı Adı Hatalı, Lütfen Tekrar Deneyin")

"""
Lütfen 1. Sayı Giriniz  : 63
Lütfen 2. Sayı Giriniz  : 2
Lütfen 3. Sayı Giriniz  : 25
63 > 25 > 2
"""

# s1 = int(input("Lütfen 1. Sayı Giriniz  :"))
# s2 = int(input("Lütfen 2. Sayı Giriniz  :"))
# s3 = int(input("Lütfen 3. Sayı Giriniz  :"))

# #s1,s2 = s2,s1

# if s1 < s2 :
#     s1,s2 = s2,s1

# if s2 < s3 :
#     s2,s3 = s3,s2

# if s1 < s3 :
#     s1, s3 = s3,s1

# print(f"Sıralama : {s1} > {s2} > {s3}  ")


# s1 = 30
# s2 = 10
# print("""
#         Lütfen Cevaplamak İstediğiniz Soruyu Giriniz
#         [1-4]
# """)
# soru = int(input())
# if soru==1:
#     cevap = int(input(f"{s1}+{s2} = "))
#     if cevap==40:
#         print("Doğru")
#     else:
#         print("hatalı")
# elif soru==2:
#     cevap = int(input(f"{s1}-{s2} = "))
#     if cevap==20:
#         print("Doğru")
#     else:
#         print("hatalı")
# elif soru==3:
#     cevap = int(input(f"{s1}*{s2} = "))
#     if cevap==300:
#         print("Doğru")
#     else:
#         print("hatalı")
# elif soru==4:
#     cevap = int(input(f"{s1}/{s2} = "))
#     if cevap==3:
#         print("Doğru")
#     else:
#         print("hatalı")
# else:
#     print("hatalı seçim")


"""
A Kenarı Giriniz : 10
B Kenarı Giriniz : 20
Dikdörtgenin alanı 200 metre kare.


A Kenarı Giriniz : 10
B Kenarı Giriniz : 10
Karenin alanı 100 metre kare.
"""

# aKenari=int(input("Lütfen A kenarını giriniz:\t→"))
# bKenari=int(input("Lütfen B kenarını giriniz:\t→"))

# aKenari = int(input("Lütfen A Kenarını Giriniz\t: "))
# bKenari = int(input("Lütfen B Kenarını Giriniz\t: "))

# if aKenari == bKenari:
#     print(f"Karenin alanı {aKenari*bKenari} metre karedir")
# else:
#     print(f"Diktörgenin alanı {aKenari * bKenari} metre karedir")

"""
Lütfen Kısa Kenarı Giriniz : 25
Lütfen Uzun Kenarı Giriniz : 15
Uzun Kenar, Kısa Girilemez
"""

# uzunKenar = int(input("Lütfen uzun kenarı giriniz: "))
# kısaKenar = int(input("Lütfen kısa kenarı giriniz: "))

# if uzunKenar < kısaKenar:
#     print("Uzun Kenar, Kısa Girilemez")
# else:
#     cevre = 2*(uzunKenar+kısaKenar)
#     print(f"Şeklin çevresi {cevre} ")

"""
Klavyeden Sırayla 2 sayı girilir,
Tam Bölünüp/Bölünmediğini Bularak Ekrana Mesaj Verir
"""

# s1 = int(input("1.sayıyı giriniz:"))
# s2 = int(input("2.sayıyı giriniz:"))

# if s2 == 0:
#     print("Payda 0 olamaz.")
# else:
#     if s1 % s2 == 0:
#         print(f"{s1}, {s2} sayısına tam bölünür. ")
#     else:
#         print(f"{s1}, {s2} sayısına tam bölünmez. ")

