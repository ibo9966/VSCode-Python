# region list_giris
"""
katilimciListesi = ["alperen","kübra","batu","umut"]
meyveler = ["karpuz", "üzüm"]
plakalar = [34, 35]
print(katilimciListesi)
print(meyveler)
print(plakalar)
"""
# endregion

# region bos_liste
"""
isimler = []
print(isimler)
print(type(isimler))
plakalar = []
print(isimler)
"""
# endregion

# region ornek_listeler
# duplicate??? evet
"""
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 15]
print(sayilar)
ogrenciListesi = ["ali", "mustafa", "ali"]
print(ogrenciListesi)
"""
# endregion

# region index
"""
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 12, 13]
print(sayilar[1])
print(sayilar[0])
print(sayilar[7]) # çok doğru yaklaşım değil
print(sayilar[-1])
print(sayilar[-2])
"""
# endregion

# region guncelleme_degistirme
"""
sayilar = [11, 15, 7, 12]
print(sayilar)
sayilar[1] = 34
print(sayilar)
"""

"""
sayilar = [11, 15, 7, 12]
print(sayilar)
sayilar[1] = sayilar[3]
print(sayilar)
"""
# endregion

# region listenin_uzunlugu_eleman_sayisi
"""
sayilar = [11, 15, 7, 12, 15, 25, 30]
print(len(sayilar))
print(sayilar[len(sayilar)-1])
print(sayilar[len(sayilar)//2])
"""
# endregion

# region del_talimati_instruction
"""
sayilar = [11, 15, 7, 12, 15]
print(sayilar)
del sayilar[1]
print(sayilar)
[11, 15, 7, 12, 15]
[11, 0, 7, 12, 15]
del sayilar #intellisense
print(sayilar)
"""
# endregion

# region for_loop_ile_oku
"""
sayilar = [12, 36, 9, 5, 3, 74]
print("30 dan büyük olan sayıların listesi")
for i in sayilar:
    if i>30:
        print(i)
"""
# endregion

# region for_loop_ile_liste_elemanlarını_topla
"""
toplam = 0
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 15]
for i in sayilar:
    toplam += i
print(f"listedeki elamanları toplamı → {toplam}")
"""
# endregion

# region for_loop_ile_listedeki_tek_sayi_adedi
"""
adet = 0
sayilar = [11, 15, 7, 12, 1, 15]
for i in sayilar:
    if i%2!=0:
        adet += 1
print(f"listedeki tek sayı adedi → {adet}")
"""
# endregion

# ad1="sena"
# ad2="furkan"
# ad3="ibrahim"
# s1=56
# s2=526
# s3=5
# ogrenciIsimleri=["sena", " furkan" , "ibrahim", "eda"]
# print(ogrenciIsimleri)
# ayakkabiKoleksiyonum=[]
# print(ayakkabiKoleksiyonum)
# meyveler=["elma", "muz" , "armut " , "elma"]
# print(meyveler)

# veriler=[3,56,4,8,19,56,5.8,55,4,53]
# # print(veriler)

# # result=veriler[3]
# # print(result)

# # result=veriler[-1]
# # print(result)

# veriler[2]="dört"
# result=veriler
# print(result)

# sayilar=[3,56,4,8,19,56,5.8,55,4,53]
# sayilar[2]=sayilar[3]
# print(sayilar)

# sayilar=[3,56,4,8,19,56,5.8,55,4,53]
# print(len(sayilar))
# print(f"listedeki eleman sayısı {len(sayilar)}")

# sayilar=[3,56,4,8,19,56,5.8,55,4,53]
# del sayilar[2]
# print(f"listedeki eleman sayısı {len(sayilar)}")
# print(sayilar)

# sayilar=[3,56,4,8,19,56,5.8,55,4,53]
# print("Listedeki float değerler")
# for i in sayilar:
#     if isinstance(i,float):
#         print(i)
    
# sayilar=[3,56,4,8,19,56,5.8,55,4,53]
# print("Listedeki tek sayıları yazınız..")
# for i in sayilar:
#     if i % 2 ==1:
#         print(f"{i}  tektir.")
#     else:
#         print(f"{i}  çifttir.")

# a,b=0,0
# sayilar=[3,56,4,8,19,56,55,4,53]
# for i in sayilar:
#     if i %2 ==0:
#         b+=1
#     else:
#         a+=1
# print(f"tek olanların adedi {a} çift olanların adedi {b}")
print("ibo")