# region python_arama_metodları
"""
→ List index metodu: Liste elemanlarında arama yapar. 
Bulduğu anda index’i geriye döndürür. Ancak bulamadığı anda value error fırlatılır. 
→ List count medodu: Tam olarak arama özelinde bir metod değildir. 
Parametre ile gönderilen değerin, listede kaç adet olduğunu geriye döndürdüğü için 
dolaylı şekilde arama sürecine dahil edilebilir. Geriye sıfır döndüğünde bulamadığı anlaşılır.
→ In / Not In : bir diğer arama metodudur. Kullanımı oldukça basittir.
"""
# endregion

# region index
"""
kurumAdi="ecodation"
print(kurumAdi.index("i"))
"""

# endregion

# region index_ornek
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz: ")
if  meyveler.index(arananMeyve) >= 0:
    print("var")
"""
# endregion

# region count
"""
kurum= "ecodation"
print(kurum.count("z"))
"""
# endregion

# region count_ornek
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz: ")
if meyveler.count(arananMeyve)!=0:
    print("var")
else:
    print("yok")
"""
# endregion

# region in_notin
"""
kurum= "ecodation"
if "z" in kurum:
    print("var")
else:
    print("yok")
"""
# endregion

# region in_notin_ornek
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz: ")
if arananMeyve in meyveler:
    print(f"{arananMeyve} liste elemanları içinde mevcut")
else:
    print(f"{arananMeyve} liste elemanları içinde yok")
"""
# endregion

# region tekrarsiz_liste
"""
listede tekrar eden elemanlar var. tekrarsız liste oluşturan pratik yapalım
meyveler = ["elma", "armut", "üzüm", "muz", "ayva", "üzüm", "elma"]
yeniListe = []
for i in meyveler:
    if i not in yeniListe:
        yeniListe.append(i)
print(yeniListe)
"""
# endregion


# ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]
# result=ogrenciListesi.index("şehnaz")
# if result>=0:
#     print("buldum")


# ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]
# result=ogrenciListesi.count("şehnaz")
# if result==0:
#     print("bulamadım")
# else:
#     print("buldum")


# ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]
# if "şehnaz" in ogrenciListesi:
#     print("buldum")
# else:
#     print("bulamadım")


# ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]
# sName="şehnaz"
# if "şehnaz"  not in ogrenciListesi:
#     print("bulamadım")
# else:
#     result=ogrenciListesi.index("şehnaz")
#     print(result)
#     print(f"{sName} listenin {result+1}.sırasındadır.")



# stokKodlari = [1002, 1008, 1009, 1005, 1002, 1008, 1007]
# tekrarsizStoklar=[]
# for i in stokKodlari:
#     if i not in tekrarsizStoklar:
#         tekrarsizStoklar.append(i)
# print(tekrarsizStoklar)

# import random
# mylist=["apple", "banana", "cherry"]
# print(random.choice(mylist))

