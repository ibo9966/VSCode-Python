# i, j= 0,  0
# while i<3:
#     while j<3:
#         print(f"{i} x {j}", end= " ")
#         j += 1
#     j = 0
#     i += 1
#     print()




# x , y = 0 , 0
# while x<10 :
#     while y<10:
#         print(" . ", end= " ")
#         y +=1
#     x +=1
#     y=0
#     print()

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

# i=0
# j=0
# while i<3:
#     while j<3:
#         print(f"{i} x {j}" , end=" ")
#         j+=1
#     j=0
#     i+=1
#     print()

"""
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .

"""

x=0
y=0
while x<10:
    while y<10:
        print(" . ", end="")
        y+=1
    y=0
    x+=1
    print()
