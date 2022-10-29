# region fonksiyon_turu_1_parametre_almayan_deger_dondurmeyen
"""
Fonksiyon tanımlama anında argüman almaz, değer döndürmez
def kullaniciGiris():
    kAd = input("Kullanıcı Adınız : ")
    print(f"hoşgeldiniz {kAd}")
kullaniciGiris()
"""
# endregion

# region ornek
"""
def topla():
    s1, s2 = input("lütfen s1 giriniz : "), input("lütfen s2 giriniz : ")
    if s1.isdigit() and s2.isdigit():
        s1, s2 = int(s1), int(s2)
        print(f"{s1} + {s2} = {s1+s2}")
    else:
        print("lütfen sayı giriniz")
topla()
"""
# endregion



def kullaniciGiris():
    kAd=input("Lütfen kullanıcı adı giriniz:\t")
    print(f"hoşgeldiniz {kAd}")    
kullaniciGiris()


def toplam():
    deger1=int(input("Lütfen sayı giriniz:\t"))
    deger2=int(input("Lütfen sayı giriniz:\t"))
    print(f"{deger1}+{deger2}={deger1+deger2}")
toplam()


from curses.ascii import isdigit


def topla():
    s1,s2 = input("Lütfen s1 değerini giriniz:"),input("Lütfen s2 değerini giriniz:")
    if s1.isdigit() and s2.isdigit():
        s1,s2=int(s1),int(s2)
        print(f"{s1}+{s2}={s1+s2}")
    else:
        print("Lütfen sayı giriniz.")

topla()