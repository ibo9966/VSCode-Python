# region ornek_1
"""
sayı dizisi tanımlanacak
for loop içinde arama yaparak
aradığınız ... indisli eleman bulundu
mesajı verilecek
sayilar = [11, 5, 36, 78, 99, 2]
n = 0
for i in sayilar:
    if i == 99:
        break
    n += 1
print(f"aradığınız {n} indisli eleman bulundu")
"""
# endregion

# region ornek_2
"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet isimli öğrenci bulundu
Aradığınız Öğrenci: murat
murat isimli öğrenci bulunamadı
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
while True:
    ogrenciAdi = input("Aradığınız Öğrenci Giriniz, Çıkmak İçin ç : ")
    if ogrenciAdi == "ç":
        break
    for i in ogrenciListesi:
        if i == ogrenciAdi:
            print(f"{ogrenciAdi} isimli öğrenci bulundu")
            break
    else:
        print(f"{ogrenciAdi} isimli öğrenci bulunamadı")
"""
# endregion

# region ornek_3

"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet listenin 3. sırasındaki öğrencidir
Aradığınız Öğrenci: murat
sınıfta murat isimli öğrenci yoktur
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa", "önder"]
print(len(ogrenciListesi))
listem = range(len(ogrenciListesi))
print(listem)
while True:
    ogrenciAdi = input("Aradığınız Öğrenci Giriniz, Çıkmak İçin ç : ")
    if ogrenciAdi == "ç":
        break
    for i in range(len(ogrenciListesi)):
        if ogrenciListesi[i] == ogrenciAdi:
            print(f"{ogrenciAdi} listenin {i+1}. sırasındaki öğrencidir")
            break
    else:
        print(f"sınıfta {ogrenciAdi} isimli öğrenci yoktur")
"""
# endregion

# region ornek_4
"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa", "önder"]
for i in range(len(ogrenciListesi)):
    print(ogrenciListesi[i])
"""    
# endregion



# ödev →
"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet listenin 3. sırasındaki öğrencidir
Aradığınız Öğrenci: murat
sınıfta murat isimli öğrenci yoktur
"""


# ödev →
"""
rakamlar = [6, 2, 7, 3, 5]
Çıktı:
["ALTI", "İKİ", "YEDİ", "ÜÇ, "BEŞ"]
"""


# ödev →
"""
rakamlar = ["elma", "armut", "erik", "şeftali"]
Çıktı:
ismi e ile başlayan meyve elma
ismi e ile başlayan meyve erik
"""


"""
istenilden >Aradığnız 55 değeri 6 indeksli elemandır.

"""
# sayilar=[3,56,4,8,19,56,55,4,53]
# a=55
# nokta=0
# for i in sayilar:
#     if a==i:
#         break
#     else:
#         nokta+=1
# print(f"Aradığınız {i} değeri {nokta}. indeksli elemandır.")

"""
ad="ramazan"

verilen ismi ters şekilde yazdırın
"""

# ad="ramazan"


# for i in range(len(ad)-1,-1,-1):
#     print(ad[i])

# print(ad[::-1])
"""

ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe"]
aradığınız öğrenci: furkan
furkan isimli öğrenci listemizde mevcut

aradığını öğrenci:murat
murat isimli öğrenci bulunamadı.
"""
# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe"]
# ogrenci=input("aradığınız öğrenci:  ")
# for i in ogrenciListesi:
#     if ogrenci==i:
#         print(f"{ogrenci} isimli öğrenci listemizde mevcuttur.")
#         break
# else:
#     print(f"{ogrenci} isimli öğrenci listemizde mevcut değildir.")

"""
baş harfi a ile başlayan öğrenciler yazdır.

"""
# sayac=0
# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe"]
# for i in ogrenciListesi:
#     if i[0]=="a":
#         print(i)
#         sayac+=1
# print(f"a harfi ile başlayan kişi sayısı {sayac} 'tir.")

"""
baş harfi a ve ş  ile başlayan öğrenciler yazdır.

"""

# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe"]
# sayac=0
# arananHarfler=["a","ş"]
# for i in arananHarfler:
#     for j in ogrenciListesi:
#         if j[0]==i:
#             sayac+=1
#     print(f"{i} harfi ile başlayan kişi sayısı {sayac} 'tir.")
#     sayac=0

"""
sesli harfleri sayan uygulama yazınız.
"""

# ad="ibrahim"
# harfler=["a","e","i","ı","o","ö","u","ü"]
# say=0
# for i in harfler:
#     for j in ad:
#         if j in ad:
#             if i==j:
#                 say+=1
#     print(f"{i} karekterlerinden {say} adet vardır.")
#     say=0