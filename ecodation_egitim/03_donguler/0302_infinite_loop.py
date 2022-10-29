"""
lütfen sayı giriniz, çıkmak için 0... : 3
lütfen sayı giriniz, çıkmak için 0... : 6
lütfen sayı giriniz, çıkmak için 0... : 12
lütfen sayı giriniz, çıkmak için 0... : 10
lütfen sayı giriniz, çıkmak için 0... : 11
lütfen sayı giriniz, çıkmak için 0... : 0
girdiğiniz tek sayıların toplamı 14
"""


# tekSayiTop=0
# sayi=int(input("Lütfen sayı giriniz, çıkmak için 0 yazınız.."))
# while sayi !=0:
#     if sayi % 2 ==1:
#        tekSayiTop+=sayi
#     sayi=int(input("Lütfen sayı giriniz, çıkmak için 0 yazınız.."))
# print(f"Girdiğiniz sayıların toplamı: {tekSayiTop}")

"""
lütfen sayı giriniz, çıkmak için 0... : 3
lütfen sayı giriniz, çıkmak için 0... : 6
lütfen sayı giriniz, çıkmak için 0... : 12
lütfen sayı giriniz, çıkmak için 0... : 10
lütfen sayı giriniz, çıkmak için 0... : 11
lütfen sayı giriniz, çıkmak için 0... : 0
2 adet tek sayı, 3 adet çift sayı girdiniz
"""
# tekSayiAdeti=0
# ciftSayiAdeti=0
# sayi=int(input("Lütfen sayı giriniz, çıkmak için 0 yazınız.."))
# while sayi !=0:
#     if sayi % 2 ==1:
#         tekSayiAdeti+=1
#     else:
#         ciftSayiAdeti+=1
#     sayi=int(input("Lütfen sayı giriniz, çıkmak için 0 yazınız.."))
# print(f"{tekSayiAdeti} adet tek sayı vardır. {ciftSayiAdeti} adet çift sayı vardır.")

# region infinite_looop→sonsuz_dongu
"""
eb = -99999999999
sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
while sayi != -1:
    if sayi>eb:
        eb = sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
print(f"girdiğiniz sayılardan en büyüğü → {eb}")
"""
# endregion


# region infinite_looop_ornek_1
"""
tekSayilarinAdedi, ciftSayilarinAdedi = 0, 0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
while sayi != 0:
    if sayi % 2 == 0:
        ciftSayilarinAdedi += 1
    else:
        tekSayilarinAdedi += 1
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
print(f"girdiğiniz sayılar içinde {tekSayilarinAdedi} adet tek sayı var")
print(f"girdiğiniz sayılar içinde {ciftSayilarinAdedi} adet çift sayı var")
"""
# endregion


# region infinite_looop_ornek_1
"""
tekSayilarinToplami, ciftSayilarinToplami = 0, 0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
while sayi != 0:
    if sayi % 2 == 0:
        ciftSayilarinToplami += sayi
    else:
        tekSayilarinToplami += sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
print(f"girdiğiniz sayılar içinde tek olanların toplamı →  {tekSayilarinToplami}")
print(f"girdiğiniz sayılar içinde çift olanların toplamı →  {ciftSayilarinToplami}")
"""
# endregion



"""
lütfen sayı giriniz, çıkmak için 0... : 3
lütfen sayı giriniz, çıkmak için 0... : 6
lütfen sayı giriniz, çıkmak için 0... : 12
lütfen sayı giriniz, çıkmak için 0... : 10
lütfen sayı giriniz, çıkmak için 0... : 11
lütfen sayı giriniz, çıkmak için 0... : 0
girdiğiniz tek sayıların toplamı 14
"""


# tekSayiTop=0
# sayi=int(input("Lütfen bir sayı giriniz, çıkmak için 0 yazınız:\t"))
# while sayi!=0:
#     if sayi%2==1:
#         tekSayiTop+=sayi
#     sayi=int(input("Lütfen bir sayı giriniz, çıkmak için 0 yazınız:\t"))
# print(f"Girdiğiniz sayıların toplamı : {tekSayiTop}")


"""
lütfen sayı giriniz, çıkmak için 0... : 3
lütfen sayı giriniz, çıkmak için 0... : 6
lütfen sayı giriniz, çıkmak için 0... : 12
lütfen sayı giriniz, çıkmak için 0... : 10
lütfen sayı giriniz, çıkmak için 0... : 11
lütfen sayı giriniz, çıkmak için 0... : 0
2 adet tek sayı, 3 adet çift sayı giriniz.
"""

# adetT=0
# adetCift=0
# sayi=int(input("Lütfen bir sayı giriniz, çıkmak için 0 yazınız:\t"))
# while sayi!=0:
#     if sayi%2==1:
#         adetT+=1
#     else:
#         adetCift+=1
#     sayi=int(input("Lütfen bir sayı giriniz, çıkmak için 0 yazınız:\t"))
# print(f"{adetT} adet tek sayı vardır. {adetCift} adet çift sayı vardır.")
