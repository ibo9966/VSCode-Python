# region ornek_1
"""
kg = float(input("kilonuz: "))
mt = float(input("boyunuz [mt] : "))
vki =round(kg/mt**2, 2)
if vki<18.49:
    print("ideal kilonun altı")
elif vki>18.5 and vki<24.99:
    print("ideal kilo")
elif vki>25 and vki<29.99:
    print("ideal kilo üzeri")
elif vki>30:
    print("ideal kilonun çok üzeri")
"""
# endregion


# region ornek_2
"""
yg = float(input("yıllık geliriniz: "))
if yg<22000:
    ygv = yg * 0.15
elif yg>22000 and yg<49000:
    ygv = yg * 0.20
elif yg>49000 and yg<180000:
    ygv = yg * 0.27
elif yg>180000 and yg<600000:
    ygv = yg * 0.35
elif yg>600000:
    ygv = yg * 0.40
print(f"yıllık gelir verginiz {ygv}")
"""
# endregion





# ödev →
"""
    - lütfen boyunuzu giriniz: 1.60
    - lütfen kilonuzu giriniz: 80
    - ideal kilo için 17 kilo vermelisiniz
"""

# ödev →
"""
    - Youtube izlenme oranı son ek ekleme ile ilgili örneği yapınız.
    - izlenme 18000         → 18 B
    - izlenme 1800000       → 1.8 Mn
    - izlenme 1800000000    → 1.8 Ml
"""


# a, b =0,0
# sayilar = [3, 56, 4 , 8, 19, 56, 55, 4, 53]
# for i in sayilar :
#     if i % 2 == 1:
#         a+=1
#     else:
#         b+=1
# print(f"{a} adet tek sayı vardır. {b} adet çift sayı vardır.")

# a=10
# b=20
# a=b
# b=30
# print(a)

"""
istenilen->Aradığınız 55 değeri, 6. indeksli elemandır
"""


# sayilar = [3, 56, 4, 8, 19, 56, 55, 4, 53]
# a = 55
# nokta = 0
# for i in sayilar:
#     if a == i:
#        break
#     else:
#         nokta +=1
# print(f"Aradığınız {i} değeri, {nokta}. indeksli elemandır.")

"""
ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]
aradığınız öğrenci : furkan
furkan isimli öğrenci listemizde mevcut


aradığınız öğrenci : murat
murat isimli öğrenci bulunamadı
"""


ogrenciListesi = ["ahmet", "sena", "eda", "furkan", "ibrahim", "irem", "mert", "ramazan", "şehnaz", "şakir", "ayşe", "nisa","tural"]

while True:
    ogrenci=input("aradığınız öğrenci, çıkmak istediğiniz zaman ç'ye basınız:\t ")
    if ogrenci=="ç":
        break
    for i in ogrenciListesi:
        if ogrenci==i:
            print(f"{ogrenci} isimli öğrenci listemizde mevcut")
            break
    else : 
        print(f"{ogrenci}isimli öğrenci bulunamadı")


