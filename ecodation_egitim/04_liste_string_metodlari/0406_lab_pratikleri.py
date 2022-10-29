# region ornek_1
"""
Listeye 
sonsuz döngü içinde öğrenci ekleyeceğiz
ogrenciListesi= []
while True:
    ogrenci = input("listeye eklenecek öğrenci, çıkmak için -1 : ")
    if ogrenci == "-1":
        break
    ogrenciListesi.append(ogrenci)
for i in ogrenciListesi:
    print(i)
"""
# endregion


# region ornek_2
"""
Benzer örneği bu kez
Ekle-Sil-Listele menüsü ile genişletelim
ogrenciListesi = []
print("""
# [1]     Ekle
# [2]     Sil
# [3]     Listele
# [4]     Çık
""")
while True:
    secim = int(input("lütfen seçiminizi giriniz... : "))
    if secim == 1:
        ogrenci = input("listeye eklenecek öğrenci,")
        ogrenciListesi.append(ogrenci)
    elif secim == 2:
        ogrenci = input("listeden silinecek öğrenci,")
        ogrenciListesi.remove(ogrenci)
    elif secim == 3:
        for i in ogrenciListesi:
            print(i)
    elif secim == 4:
        break
    else:
        print("hatalı seçim")
   
"""
# endregion


# region ornek_3
"""
Ad-Soyad-Not1-Not2 
Sonsuz döngü içinde girilecek, not ortalamaları baz alınarak
en düşük, en yüksek not listelenecek
notOrtalamalari = []
while True:
    ogrenciAdSoyad = input("lütfen ad soyad giriniz, çıkmak için -1 : ")
    if ogrenciAdSoyad=="-1":
        break
    n1 = int(input("lütfen n1 notu giriniz: "))
    n2 = int(input("lütfen n2 notu giriniz: "))
    if not 0<=n1<=100 or not 0<=n2<=100:
        print("lütfen [0-100] arası değer giririniz")
        continue
    notOrtalamalari.append((n1+n2)/2)
for i in notOrtalamalari:
    print(i)
minimum,maksimum = 9999999999, 0
for i in notOrtalamalari:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i
print(f"en düşük not → {minimum} - en yüksek not {maksimum}")
"""
# endregion


# region ornek_4
"""
Benzer örneği bu kez
Çan eğrisi mantığı ile ortalamanın altında kalan notları listeleyelim
notOrtalamalari = []
while True:
    ogrenciAdSoyad = input("lütfen ad soyad giriniz, çıkmak için -1 : ")
    if ogrenciAdSoyad=="-1":
        break
    n1 = int(input("lütfen n1 notu giriniz: "))
    n2 = int(input("lütfen n2 notu giriniz: "))
    if not 0<=n1<=100 or not 0<=n2<=100:
        print("lütfen [0-100] arası değer giririniz")
        continue
    notOrtalamalari.append((n1+n2)/2)
genelOrtalama = sum(notOrtalamalari)/len(notOrtalamalari)
for i in notOrtalamalari:
    print(i)
minimum,maksimum = 9999999999, 0
for i in notOrtalamalari:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i
print(f"en düşük not → {minimum} - en yüksek not {maksimum}")
for i in notOrtalamalari:
    if i<genelOrtalama:
        print(f"dönem tekrar yapacak öğrencinin notu {i}")
"""
# endregion


# region ornek_5
"""
İki basamaklı sayıyı → metne dönüştüren uygulama yapalım
Örn; 95
doksan beş
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
sayi = 95
print(f"{onlar[sayi//10]} {birler[sayi%10]}")
"""
# endregion

# birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
# onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "atmış", "yetmiş", "seksen", "doksan"]
# sayi = int(input("lütfen sayı giriniz: "))
# print(f"{onlar[sayi//10]} {birler[sayi%10]}")

"""
9,7,6,3,4,1,5,2,8
7,9
7,6,9
7,6,3,9
7,6,3,4,9
7,6,3,4,1,5,9
7,6,3,4,1,5,2,9
7,6,3,4,1,5,2,8,9
sıralama= yer değiştirme
"""


# listem = [9,7,6,3,4,1,5,2,8]
# while True:
#     siraliMi = True
#     for i in range(len(listem)-1):  #→ Hata vermesin diye -1 verdik.
#         if listem[i]>listem[i+1]:
#             listem[i], listem[i+1] = listem[i+1], listem[i]
#             siraliMi=False
#     if siraliMi:
#         break
# print(listem)


# ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]
# sName = "şehnaz"
# if sName not in ogrenciListesi:
#     print("bulamadım")
# else:
#     result = ogrenciListesi.index(sName)
#     print(result)
#     print(f"{sName} listenin {result+1}. sırasındadır")


"""
stokKodlari = [1002, 1008, 1009, 1005, 1002, 1008, 1007]

"""

# stokKodlari = [1002, 1008, 1009, 1005, 1002, 1008, 1007]
# tekrarsizStoklar=[]
# for i in stokKodlari:
#     if i not in tekrarsizStoklar:
#         tekrarsizStoklar.append(i)
# print(tekrarsizStoklar)


# trKarakterler="şçğü"
# sehir="lüleburgaz"
# for i in trKarakterler:
#     print("ingilizce klavyesi ile yazamazsın")
#     break
# else:
#     print("sorun yok")


# # PS C:\VSCode-Ecodation-Eylul> pip install keyboard
# import keyboard  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed
#             print('You Pressed A Key!')
#             break  # finishing the loop
#     except:
#         break  # if user pressed a key other than the given key the loop will break


# haftaninGunleri = ["","Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# listem = [f"Haftanın {i}. günü {haftaninGunleri[i]}" for i in range(1, 8)]
# print(listem)

"""
fav. mevsim, çıkmak için -1 : yaz
fav. mevsim, çıkmak için -1 : sonbahar
fav. mevsim, çıkmak için -1 : yaz
daha önce eklediniz
fav. mevsim, çıkmak için -1 : ilkbahar
fav. mevsim, çıkmak için -1 : -1
favori mevsimlerimiz yaz, sonbahar, ilkbahar
"""

# mevsimler=[]
# while True:
#     mevsim=input("Lütfen fav mevsim yazınız, çıkmak için -1  yazınız:\t")
#     if mevsim=="1":
#         break
#     if mevsim in mevsimler:
#         print("Daha önce eklediniz. Tekrar veri giriniz.")
#         continue
#     mevsimler.append(mevsim)
# print(f"Favori mevsimleriniz {mevsimler}")


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# 1,2,3,4,5,6,7,8
# tekilListe = list1.copy()
# for i in list2:
#     if i not in tekilListe:
#         tekilListe.append(i)
# print(tekilListe)


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# ortakElemanlar = []
# for i in list1:
#     if i in list2:
#         ortakElemanlar.append(i)
# print(ortakElemanlar)


# cihazListesi = [
#     [1, "Desktop_Test", 56, "chrome.exe"],
#     [2, "Guest101", 60, "excel.exe"],
#     [3, "Kat-1_Laptop", 90, "camtasia.exe, chrome.exe"]
# ]
# for i in range(len(cihazListesi)):
#     for j in range(len(cihazListesi[i])):
#         if j == 2:
#             print(f"%{cihazListesi[i][j]}", end=" ")
#         else:
#             print(cihazListesi[i][j], end=" ")
#     print()


# for i in range(8):
#     row=["piyon"for j in range(8)]
#     print(row)


# for i in range(8):
#     row = ["piyon" for j in range(8)]
#     print(row)


# row = [["piyon" for j in range(8)] for i in range(8)]
# print(row)

# row = [[f"{i}{j}" for j in range(24)] for i in range(7)]
# print(row[6][23])


# iftaarListesi = []
# for i in ogrenciler:
#     if i[3] == 100:
#         iftaarListesi.append(i)
# print(iftaarListesi)

# notlar=[]
# while True:
#     oAdSoyad=input("Ad-Soyad girin, çıkmak için -1 :\t ")
#     if oAdSoyad =="-1":
#         break
#     n1=int(input(f"{oAdSoyad} isimli öğrencinin 1.notu:\t"))
#     n2=int(input(f"{oAdSoyad} isimlü öğrencinin 2.notu:\t"))
#     ort=(n1+n2)/2
#     notlar.append(ort)
# for i in notlar:
#     print(i)
# print(f"en düşük not{min(notlar)}- en yüksek not {max(notlar)}")

# sayi=int(input("Sayı giriniz:\t"))
# birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
# onlar=["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"]
# print(f"{onlar[sayi//10]} {birler[sayi%10]}")


"""
listem = [9, 7, 6, 3, 4, 1, 5, 2, 8]
"""



# listem = [9, 7, 6, 3, 4, 1, 5, 2, 8]
# while True:
#     siraliMi=True
#     for i in range(len(listem)-1):
#         if listem[i]>listem[i+1]:
#             listem[i],listem[i+1]=listem[i+1],listem[i]
#             siraliMi=False
#     if siraliMi:
#         break
# print(listem)

################################### kaç kere döndüğünü aşağısı gösteriyor.

# say=0
# listem = [9, 7, 6, 3, 4, 1, 5, 2, 8]
# while True:
#     siraliMi=True
#     for i in range(len(listem)-1):
#         if listem[i]>listem[i+1]:
#             listem[i],listem[i+1]=listem[i+1],listem[i]
#             siraliMi=False
#         say+=1
#     if siraliMi:
#         break
# print(listem)
# print(say)