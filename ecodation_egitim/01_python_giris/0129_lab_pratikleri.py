print("""
        leylek uygulamasına hos geldiniz!!!!
        sürüş ücreti:1.99/dk
""")
s=int(input("lütfen sürüş süresini giriniz [saat]\t: "))
d=int(input("lütfen sürüş süresini giriniz [dakika]\t: "))
tDakika = s*60
tDakika += d
print(tDakika)
print(f"sürüşünüz süresi {s}:{d} - {tDakika} dk.da bitmiştir")
print(f"Kartınızdan {round (1.99*tDakika , 3)} TL. Tutar Çekilmiştir.")
#sürüşünüz süresi 1:15-75 dakikada bitmiştir.

# ödev →
"""
km cinsinden girilen mesafe bilgisini mil'e çeviren programı yazınız.
mil =  km / 1.609344
"""




# ödev →
"""
Lütfen Üçgenin A Kenarı Açısını Giriniz: 30
Lütfen Üçgenin B Kenarı Açısını Giriniz: 60
C Kenarı 90 Derecedir
"""


# ödev →
"""
- Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.
"""


# ödev 
"""
- Kısaltmalar;
    - at    aylık tüketim giriniz
    - aeb   aktif enerji bedeli
    - db    dağıtım bedeli
    - teb   toplam enerji bedeli
    - tp    trt payı
    - ef    enerji fonu
    - etv   elektrik tüketim vergisi
    - vt    vergiler toplamı
- elektrik faturamızı hesaplayalım
    - aylık tüketim giriniz ? [kWh]  : 500
    - aktif enerji bedeli = aylık tüketim x 0.39736
    - dağıtım bedeli = aktif enerji bedeli x 0,2474
    - toplam enerji bedeli = aktif enerji bedeli + dağıtım bedeli
    - trt payı = 3.97
    - enerji fonu = 1.39
    - elektrik tüketim vergisi = 9.92
    - KDV = (toplam enerji bedeli + trt payı + enerji fonu + elektrik tüketim vergisi) x 0.18
    - vergiler toplamı = trt payı + eerji fonu + elektrik tüketim vergisi + kdv
    - toplam fatura = vergiler toplamı + toplam enerji bedeli
"""

# ödev 
"""
Güncel Benzin Endeksini Giriniz                 : 7.09
Yakıt Tüketimini Giriniz [100 km. başına] )     : 4.08
Kaç Kilometre Yol Aldınız?                      : 50
Toplam Yakıt Tüketimi → 14.4636  
"""


# ödev 
"""
Lütfen Ürün Adı Giriniz                         : A4 Fotokopi
A4 Fotokopi - Satın Alınacak Adet               : 2
Lütfen Ürün Fiyatı Giriniz [KDV-Dahil]          : 130.00
Lütfen İndirim Oranını Giriniz [%]              : 5
Ürünlerin Toplam Tutarı 247.0 TL.
"""