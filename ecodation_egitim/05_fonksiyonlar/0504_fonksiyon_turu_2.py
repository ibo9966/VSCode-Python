# region fonksiyon_turu_2_parametre_alan_deger_dondurmeyen
"""
Fonksiyon tanımlama anında argüman alır, değer döndürmez
"""
# endregion

# region ornek1
"""
def yas(dTarihi):
    print(f"Yaşınız, {2021-dTarihi}")
yas(int(input("lütfen d.tarihi giriniz: ")))
"""
# endregion

# region ornek2
# def tekcift(s):
#     if str(s).isdigit():
#         s=int(s)
#         if s%2==0:
#             print(f"{s } çift")
#         else:
#             print(f"{s } tek")
#     else:
#         print("lutfen sayi giriniz")

# listem = [3, 6, 45, 98, 66, 45 , 65]
# for i in listem:
#     tekcift(i)
# endregion



# from curses.ascii import isdigit


# def isValid(dTarihi):
#     if str(dTarihi).isdigit():   
#         yas=2022-dTarihi
#         if yas>=19:
#             print("askere gidebilirsiniz.")
#         else:
#             print("12 yıllık kesintisiz eğitimine devam et, askerlik senin için biraz beklesin")
#     else:
#         hataKodu100()

# def hataKodu100():
#     print("lütfen sayısal değer giriniz.")

# isValid("ağustos")






# def selamlama(ad:str):
#     import datetime
#     saat=datetime.datetime.now().hour
#     if saat<12:
#         print(f"Günaydın {ad}")
#     else:
#         print(f"Merhaba {ad}")

# selamlama("ibrahim")


# def yas(dTarihi):
#     print(f"yaşınız, {2021-dTarihi}")
# yas(int(input("Lütfen doğum tarihinizi giriniz:")))

from curses.ascii import isdigit


def tekcift(s):
    if str(s).isdigit():
        s=int(s)
        if s%2==0:
            print(f"{s} çift")
        else:
            print(f"{s} tek")
    else:
        print("Lütfen sayı giriniz!")
listem = [3, 6, 45, 98, 66, 45 , 65]
for i in listem:
    tekcift(i)