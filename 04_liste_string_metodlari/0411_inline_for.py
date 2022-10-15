# region inline_for_giris
# tek satırda for yazmak mümkün inline for
"""
liste =[]
for i in range(1, 9):
    liste.append(i)
print(liste)
liste = [i for i in range(1, 9)]
print(liste)
row = ["piyon" for i in range(8)]
print(row)
"""
# endregion

# region ornek
"""
Haftanın 1. Günü Pazartesi  Haftanın 2. Günü Salı ...
"""
# hafaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# liste = [f"Haftanın {i}. Günü {hafaninGunleri[i]}" for i in range(1, 8) if i<=3]
# print(liste)
# # endregion


# liste=[" piyon " for i in range(1,9) if i >=3]
# print(liste)


hafaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba",
                  "Perşembe", "Cuma", "Cumartesi", "Pazar"]
# hafaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]


listem = [f"Haftanın {i}.günü {hafaninGunleri[i]}" for i in range(1, 8)]
print(listem)


"""
fav.mevsim,çıkmak için -1 :yaz
fav.mevsim,çıkmak için -1 :sohbahar
fav.mevsim,çıkmak için -1 :yaz
daha önce eklediniz.
fav.mevsim,çıkmak için -1 :ilkbahar
fav.mevsim,çıkmak için -1-1
fav.mevsim,çıkmak için -1 :yaz,sonbahar,ilk bahar

"""

# mevsimler=[]
# while True:
#     favoriMevsim=input("Lütfen favori mevsim giriniz,çıkmak için -1 giriniz:\t")
#     if favoriMevsim=="-1":
#         print("Çıkış yaptınız.")
#         break
#     if favoriMevsim in mevsimler:
#         print("Daha önce eklediniz.")
#         continue
#     mevsimler.append(favoriMevsim)
# print(f"Favori mevsimleriniz:{mevsimler}")

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# # 1,2,3,4,5,6,7,8
# tekilListe = list1.copy()
# for i in list2:
#     if i not in tekilListe:
#         tekilListe.append(i)
# print(tekilListe)    


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# # 4,5
# ortakElemanlar=[]
# for i in list1:
#     if i in list2:
#         ortakElemanlar.append(i)
# print(ortakElemanlar)


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# listem1=[i for i in range (1,6)]
# listem2=[i for i in range (4,9)]
# ortakElemanlar=[]
# for i in listem1:
#     if i in listem2:
#         ortakElemanlar.append(i)
# print(ortakElemanlar)


