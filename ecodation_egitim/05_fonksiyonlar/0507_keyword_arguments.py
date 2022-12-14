# region keyword_arguments_isimli_argumanlar
"""
Fonksiyonu çağırırken argümana değer atar isek, sırasına bakmak zorunda kalmaz
Fonksiyonda parametre hangi sırada ise, fonksiyonu çağırırken de o sırada çağırmak zorundayız.
Bu dez avantajı keyword kullanımı ile aşarız.
def hastaKart(ad, soyad):
    print(f"sağlıklı günler dileriz {ad} {soyad}")
hastaKart(soyad = "Kemal", ad = "Ali")
"""
# endregion

# region ornek
"""
Ürün Kodu - Ürün Adı - Fiyat - Satıştamı
şeklinde dört argüman, değişken pozisyonda da olsa fonksiyonun çağırılmasına izin verelim
def urunSatistaMi(urunKodu, urunAdi, fiyat, satistaMi):
    if satistaMi:
        print(f"ürün kodu {urunKodu} olan {urunAdi} isimli ürünümüz {fiyat} TL. fiyat ile satıştadır")
    else:
        print(f"ürün kodu {urunKodu} olan {urunAdi} isimli ürünümüz satışta değildir")
urunSatistaMi(satistaMi=True,fiyat=80.75, urunAdi="Filtre Kahve", urunKodu="v60")
"""
# endregion

def urunSatistaMi(uKodu, uAdi, fiyat, satistaMi):
    if satistaMi:
        print(f"ürün kodu {uKodu} nolu {uAdi}, {fiyat}  fiyatı ile satıştadır.")
    else:
        print(f"ürün kodu {uKodu} nolu {uAdi} satışta değil")

# urunSatistaMi(1001, "kuru kahve", 25 , True)
# urunSatistaMi(1001, "kuru kahve", True , 25)                     ///////////# sırasına dikkat et///////
urunSatistaMi(satistaMi=False, uAdi="nescafe" , uKodu=1001, fiyat=55)