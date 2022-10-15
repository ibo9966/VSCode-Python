# region append→eleman_ekler_listenin_sonuna
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listemizin ilk hali")
meyveler.append("karpuz")
print(f"{meyveler} listemizin son hali")
"""
# endregion

# region insert→eleman_ekler_istediginiz_indekse
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
#meyveler.insert(2, "portakal")
meyveler.insert(44, "portakal")
#meyveler.insert("portakal", 3) # bu atama mümkün değil önce index
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region remove→listeden_siler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
# meyveler.remove("muz")
meyveler.remove("muzz")
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region pop→listeden_siler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
#print(meyveler.pop()) son elemanı
print(meyveler.pop(2)) #o indeksli elemanı siler
print(f"listemizin son hali → {meyveler}")
sebzeler = []
sebzeler.pop()
"""
# endregion

# region clear→listeyi_temizler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveler.clear()
print(meyveler)
del meyveler
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region copy→listeyi_kopyalar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveTabagi = meyveler.copy()
print(f"listemizin son hali → {meyveTabagi}")
"""
# endregion

# region count→elaman_sayisi
"""
listeRakamlar = [2, 5, 6, 1, 9, 7, 5, 9]
arananEleman = 9
elemanAdedi = listeRakamlar.count(arananEleman)
print(f"listemizdeki {arananEleman} elemanı adedi→ {elemanAdedi}")
meyveler = ["elma", "armut", "muz", "ayva", "muz", "üzüm"]
print(meyveler.count("muzz"))
"""
# endregion

# region ornek_1
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
arananMeyve = input("aramak istediğiniz meyve? : ")
elemanAdedi = meyveler.count(arananMeyve)
if elemanAdedi:   # elemanAdedi!=0
    print(f"aradığınız {arananMeyve} listede yer almaktadır.")
else:
    print(f"Aradığınız {arananMeyve} listede yer almamaktadır.")
"""
# endregion

# region sort_reverse→sirala_tersten_sirala
"""
listeRakamlar = [2, 5, 6, 1, 4, 9, 3, 8, 7]
print(f"listemizin ilk hali → {listeRakamlar}")
listeRakamlar.sort()
print(f"listemizin son hali → {listeRakamlar}")
listeRakamlar.reverse()
print(f"listemizin son hali → {listeRakamlar}")
"""
# endregion

# region index→arama_indeks_dondurme
"""
listeRakamlar = [2, 5, 6, 1, 9, 7]
print(listeRakamlar.index(10))
"""
# endregion

#biz kendimiz liste3dli eleman sayısını bulabiliriz.
#biz kendimiz son elemanı sil şeklinnde bir algoritma geliştirebiliriz.


# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe" , " nisa" ," tural"]
# ogrenciListesi.append("aziz")
# print(ogrenciListesi)
# print(len(ogrenciListesi)) 
# ogrenciListesi.insert(2,"mustafacan")
# print(ogrenciListesi)
# print(len(ogrenciListesi)) 
# ogrenciListesi.insert(100,"mustafacancan")
# print(ogrenciListesi)
# ogrenciListesi.remove("mustafacancan")
# print(ogrenciListesi)
# ogrenciListesi.remove("eda")
# print(ogrenciListesi)
# ogrenciListesi.pop(1)
# print(ogrenciListesi)



# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe" , " nisa" ," tural"]
# print(ogrenciListesi)
# gelmeyenlerListesi=ogrenciListesi.copy()
# print(type(ogrenciListesi))
# print(type(gelmeyenlerListesi))
# print(gelmeyenlerListesi)
# searcItem="furkan"
# result=ogrenciListesi.count(searcItem)
# print(f" aradığınız {searcItem} elamnından {result} adet bulundu.")
# sayiListesi=[3,6,7,8,9,3]
# items=["ahmet" , "sena", True, 3<9 , 5>10]
# print(items.count(True))

# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe" , " nisa" ," tural"]

# notListesi=[30,50,60,70,99]
# notListesi.sort(reverse=False)  #büyükten → küçüğe 
# notListesi.sort(reverse=True)  #küçükten → büyüğe 
# notListesi.reverse() # #büyükten → küçüğe 
# print(notListesi)

# notListesi=[30,50,60,70,99]
# result=notListesi.index(30)
# print(result)

# favoriFilm = []
# while True:
#     film = input("Eklenecek Film Adı Girin. Çıkmak için  -1 :  ")
#     if film == "-1" :
#         break
#     favoriFilm.append(film)
# print(favoriFilm)
# for i in range(0,len(favoriFilm)):
#     print(f"{i+1}. filmin adı {favoriFilm[i]}")
    
# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe" , " nisa" ," tural"]
# print(ogrenciListesi)
# gelmeyenlerListesi=ogrenciListesi.copy()
# print(type(ogrenciListesi))
# print(type(gelmeyenlerListesi))
# print(gelmeyenlerListesi)




# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe" , " nisa" ," tural"]
# for i in ogrenciListesi:
#     if i =="furkan":
#         result=ogrenciListesi.count(i)
#         break
# print(f"aradığınız {i} elemanından {result} adet bulundu.")



# ogrenciListesi=["ahmet", "sena" , "eda" , "furkan", "ibrahim" , "irem" , "mert" , "ramazan" , "şehnaz" ,"şakir" ,"ayşe" , " nisa" ," tural"]
# result=ogrenciListesi.count("furkan")
# if result==0:
#     print("bulamadım")
# else:
#     print("buldum")
#     print(result)

# notListesi=[30,50,60,70,99]
# notListesi.sort       #Küçükten → Büyüğe
# notListesi.sort(reverse=True)    #Büyükten → Küçüğe
# notListesi.sort(reverse=False)   #Küçükten → Büyüğe
# notListesi.reverse()      #Büyükten → Küçüğe
# print(notListesi)


# notListesi=[30,50,60,70,99]
# result=notListesi.index()
# print(result)

#extend SSS→FAQ




"""
olmasını istediği
a=[3,5,8,1,2,7]
b=[2,6,8,0,0,0]

"""

# a=[3 , 5 , 8 , 1 , 2 , 7]
# b=[2 , 6 , 8]
# lenA, lenB=len(a), len(b)
# diff=abs(lenA-lenB)
# if lenA<lenB:
#     a.extend([0]*diff)
# else:
#     b.extend([0]*diff)
# print(a)
# print(b)


# favoriFilm=[]
# while True:
#     film=input("Eklenecek film adı giriniz,çıkmak için -1 :\t")
#     if film=="-1":
#         break
#     favoriFilm.append(film)
# print(favoriFilm)
# for i in range(0,len(favoriFilm)):
#     print(f"{i+1}. film adı {favoriFilm[i]}")

