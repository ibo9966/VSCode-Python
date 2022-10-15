# region break_continue_neden_kullanilir
"""
break     → döngüyü sonlandırır
continue  → tepeye geri döndürecek
"""
# endregion

# region break
"""
i = 1
print("a")
while i<11:
    if i==15:
        print("b")
        break
    print(f"{i}. döngü")
    i += 1
print("c")
"""


# endregion

# region continue
"""
i = 1
print("a")
while i < 11:
    if i == 5:
        i += 1
        continue
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
# endregion

# region break_continue_mix
"""
i = 1
print("a")
while i < 100:
    if i % 7 == 0:
        i += 1
        continue
    elif i % 15 == 0:
        break
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
# endregion

# region ornek
"""
Kullanıcı istediği kadar sayı girsin. Çıkmak için -1 tuşlasın.
Döngü sonunda girilen en büyük sayıyı ekrana yazdıralım.
Adım sayısı belli olmadığı için sonsuz döngü içinde çözümleyeceğiz
eb, say = 0, 0
while True:
    sayi = int(input("lütfen sayı giriniz, çıkmak için -1 \t: "))
    if sayi == -1:
        break
    say += 1
    if sayi > eb:
        eb = sayi
if say:
    print(f"girdiğiniz listedeki en büyük sayı {eb}")
else:
    print("hiç bir sayı girmediniz")
"""
# endregion

# i=1
# while i <11:
#     if i ==5:
#         break
#     print(f"{i}. döngü")
#     i+=1

# i, j=0,0
# while i <5:
#     while j < 5:
#         print(f"{i}-{j}" , end="")
#         j+=1
#     i+=1
#     print()
#     j=0

# i=1
# while i <11:
#     if i ==5:
#         i+=1
#         continue
#     print(f"{i}. döngü")
#     i+=1

# i=1
# print("a")
# while i <100:
#     if i<100:
#         if i %7==0:
#             i+=1
#             continue
#         elif i % 15 ==0:
#             break
#         print(f"{i}")
#         i+=1
# print("c")

# eb = -99999999999
# sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
# while sayi != -1:
#     if sayi>eb:
#         eb = sayi
#     sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
# print(f"girdiğiniz sayılardan en büyüğü → {eb}")

# eb = -99999999999
# sayac=0
# while True:
#     sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
#     if sayi==-1:
#         break
#     sayac+=1
#     if sayi>eb:
#         eb=sayi
# if sayac==0:
#     print("Hiç bir sayı girmediniz.")
# else:
#     print(f"girdiğiniz sayılardan en büyüğü → {eb}")

"""
"Klavyeden sayı girilsin??? Kaç basamaklı"
"Tam sayıdan →Float"
"""

"""
Lütfen Tek Sayı giriniz, çıkmak için -1     :5
Lütfen Tek Sayı giriniz, çıkmak için -1     :7
Lütfen Tek Sayı giriniz, çıkmak için -1     :6
Sadece Tek sayı Girilmeli
Lütfen Tek Sayı giriniz, çıkmak için -1     :11
Lütfen Tek Sayı giriniz, çıkmak için -1     :-1
Girilen 3 adet tek sayının toplamı 23

"""

# tekAdet=0
# toplam=0
# while True:
#     sayi=int(input("Lüfen Tek Sayı giriniz, çıkmak için -1 basınız:\t"))
#     if sayi == -1:
#         break
#     if sayi % 2 !=1:
#         print("Sadece tek sayı girilmeliydi...!")
#         continue
#     tekAdet+=1
#     toplam+=sayi
# print(f"Girilen tek sayı adeti {tekAdet}")
# print(f"Girilen tek sayı toplamı {toplam}")
# print("Teşekkürler görüşmek üzere...")


menu="""
    [1] km → mil
    [2] mil→km
    [3] çık

 """
# while True:
#     print(menu)
#     secim=input("Lütfen seçim yapınız:\t")
#     if secim=="1":
#         km=int(input("Lütfen km bilgisini giriniz:\t"))
#         mil=km*0.62137
#         print(round(mil,2))
#     elif secim=="2":
#         mil=int(input("Lütfen mil bilgisini giriniz:\t"))
#         km=mil/(0.62137)
#         print(round(km,2))
#     elif secim=="3":
#         print("Çıkış yapıldı.")
#         break
#     else:
#         print("Hatalı  tuşlama yaptınız!")