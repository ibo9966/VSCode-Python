# ödev →
"""
km cinsinden girilen mesafe bilgisini mil'e çeviren programı yazınız.
mil =  km / 1.609344
"""

# km=int(input("uzunluk bilgisini giriniz:\t→"))
# mil=km/1.609344
# print(f"{km} kilometre {mil} mile karşılık gelmektedir.")

# ödev →
"""
Lütfen Üçgenin A Kenarı Açısını Giriniz: 30
Lütfen Üçgenin B Kenarı Açısını Giriniz: 60
C Kenarı 90 Derecedir
"""

# A=int(input("Lütfen üçgenin A kenar açısını giriniz:\t→"))
# B=int(input("Lütfen üçgenin B kenar açısını giriniz:\t→"))
# C=180-(A+B)
# print(f"A kenarının açısı {A}, B kenarının açısı {B} ve kalan C açısının kenar {C}")


# ödev →
"""
- Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.
"""

# x1=int(input("x1 değerini giriniz:\t→"))
# x2=int(input("x2 değerini giriniz:\t→"))
# y1=int(input("y1 değerini giriniz:\t→"))
# y2=int(input("y2 değerini giriniz:\t→"))
# uzaklık=(((x1-x2)**2)+((y1-y2)**2))**(0.5)
# print(f"({x1,x2} ve {y1,y2} noktaları arasındaki uzaklık {round(uzaklık,2)} birimidir.")

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
# # """
#                                                                                                  ---------- BU SORUYU ANLAMADIM SORMAYI UNUTMA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# at=int(input("aylık tüketim giriniz:\t→"))
# aeb=float(input("aktif enerji bedeli:\t→"))
# db=float(input("dağıtım bedeli:\t\t→"))
# teb=float(input("toplam enerji bedeli:\t→"))
# tp=float(input("trt payı:\t\t→"))
# ef=float(input(" enerji fonu\t\t→"))
# etv=float(input("elektrik tüketim vergisi:→"))
# vt=float(input("vergiler toplamı:\t→"))


# aeb=at*0.39736
# db=aeb*0.2474
# teb=aeb+db
# tp=3.97
# ef=1.39
# etv=9.92
# KDV=(teb+tp+ef+etv)*0.18
# vt=(tp+ef+etv+KDV)
# toplam_fatura=vt+teb


# ödev 
"""
Güncel Benzin Endeksini Giriniz                 : 7.09
Yakıt Tüketimini Giriniz [100 km. başına] )     : 4.08
Kaç Kilometre Yol Aldınız?                      : 50
Toplam Yakıt Tüketimi → 14.4636  
"""
# güncel_b=float(input("Güncel Benzin Endeksini Giriniz :\t→"))
# yakıt_t=float(input("Yakıt Tüketimini Giriniz [100 km. başına]:\t→"))
# alinan_yol=float(input(" Kaç Kilometre Yol Aldınız?:\t→"))
# hesapla=(alinan_yol/100)*yakıt_t*güncel_b
# print(f"güncel benzin endeksi {güncel_b} ile {alinan_yol} km yol gidildiğinde 100 km başına {yakıt_t} yakan bir araç {hesapla} tutar öder")

# ödev 
"""
Lütfen Ürün Adı Giriniz                         : A4 Fotokopi
A4 Fotokopi - Satın Alınacak Adet               : 2
Lütfen Ürün Fiyatı Giriniz [KDV-Dahil]          : 130.00
Lütfen İndirim Oranını Giriniz [%]              : 5
Ürünlerin Toplam Tutarı 247.0 TL.
"""

# ürün_adi=input("Lütfen Ürün Adı Giriniz\t→")
# adet=int(input("Lütfen Satın alınacak adet sayısı giriniz.\t"))
# ürün_fiyat=int(input("Lütfen Ürün Fiyatı Giriniz [KDV-Dahil]\t→"))
# indirim=int(input("Lütfen İndirim Oranını Giriniz [%]\t→ "))
# hesapla=(ürün_fiyat*(100-indirim)/100)*adet
# print(f"% {indirim} indirim ile alınan {adet} adet {ürün_adi} toplam {hesapla} TL tutmuştur.")



