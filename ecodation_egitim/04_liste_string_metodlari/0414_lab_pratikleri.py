
"""
#random
#built-in
#seed

"""
# import random as rnd
# print(rnd.random())

# for i in range(5):
#     print(rnd.random() , end="")


# from random import randrange
# print(randrange(3)) #min<= x < max 0,1,2
# print(randrange(3,6)) #min<= x < max 3,4,5



# for i in range(25):
#     print(randrange(3,6+1), end=",")

# from random import randrange
# print(randrange(10,50,10))

# from random import randrange, randint
# for i in range(10):
#     print(randint(3,6), end=",")

# import random
# random.seed()
# print(f"1.sayı {random.randint(25,75)}")
# random.seed()
# print(f"2.sayı {random.randint(25,75)}")
# random.seed()
# print(f"3.sayı {random.randint(25,75)}")

# from random import sample,choice,randrange
# oListesi = ["ahmet" , "sena" , "furkan" , "ibrahim"]
# i=randrange(0,4)
# print(oListesi[i])
# _1, _2, _3, _4=0,0,0,0
# for i in range(100):
#     i= randrange(0,4)
#     if i ==0:
#         _1+=1
#     elif i==1:
#         _2+=1
#     elif i==2:
#         _3+=1
#     elif i==3:
#         _4+=1
# print(f"irem {_1} kez")
# print(f"mert {_2} kez")
# print(f"furkan {_3} kez")
# print(f"ibrahim {_4} kez")

# from random import sample,choice,randrange
# oListesi = ["ahmet" , "sena" , "furkan" , "ibrahim"]
# # print(choice(oListesi))
# result=(sample(oListesi,2))
# print(result)
# print(type(result))

# from random import sample,choice,randrange
# oListesi = ["irem" , "mert" , "furkan" , "ibrahim"]
# kListesi  =[
#     ["irem" , 0],
#     ["mert" , 0],
#     ["furkan" , 0],
#     ["ibrahim" , 0]
# ]
# # result=sample(oListesi,2)
# # print(result)
# # print(type(result))

# _1, _2, _3, _4=0,0,0,0
# for i in range(100):
#     o=choice(oListesi)
#     if o =="irem":
#         _1+=1
#     elif o=="mert":
#         _2+=1
#     elif o=="furkan":
#         _3+=1
#     elif o=="ibrahim":
#         _4+=1
# kListesi[0][1]=_1
# kListesi[1][1]=_2
# kListesi[2][1]=_3
# kListesi[3][1]=_4

# print(kListesi)


"""
zar oyunu yapalım
"""

# import random as rnd
# z1=int(input("zar 1 : "))
# z2=int(input("zar 2 : "))
# sayac=0
# if 0<z1<7 and 0<z2<7:
#     while True:
#         zar1=rnd.randint(1,6)
#         zar2=rnd.randint(1,6)
#         sayac+=1
#         if (zar1==z1 and zar2==z2) or (zar1==z2 and zar2==z1):
#             print(f"{sayac} . seferde bulundu. {zar1}-{zar2} ")
#             break
# else:
#     print("hatalı giriş")

# region ornek_1
"""
ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,	90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]
for i in ogrenciler:
    if (i[2]+i[3])/2<50:
        print(f"{i[0]} {i[1]} → KALDI")
    else:
        print(f"{i[0]} {i[1]} → GEÇTİ")
"""
# endregion

# region ornek_2
""""""
ogrenci1 = [
    "Alp",
    "Besi",
    90,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    1997
]
ogrenci2 = [
    "Batu",
    "Koçhan",
    10,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    1998
]
ogrenci3 = [
    "Emir",
    "Besi",
    100,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    2008
]
ogrenci4 = [
    "Umut",
    "Ahmet",
    95,
    80,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    2000
]
ogrenci5 = [
    "Aziz",
    "Bektaş",
    15,
    10,
    "Kısa CV",
    1980
]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]
i = 1
for item in ogrenciler:
    if len(item[4]) > 30:
        cv = f"{item[4][:30]}..."
    else:
        cv = item[4]
    if (item[2]+item[3])/2 < 50:
        print(f"{i} {(2021-(item[-1]))} {item[0]} {item[1]} {cv}→ KALDI")
    else:
        print(f"{i} {(2021-(item[-1]))} {item[0]} {item[1]} {cv} → GEÇTİ")
    i += 1

# endregion
