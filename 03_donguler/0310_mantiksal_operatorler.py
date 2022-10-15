# mantıksal operatörler → logical operatörler
# koşul ifadelerini birleştirmek için kullanılır
"""
1→ ve       and
2→ veya     or
3→ değil    not
"""


# region and
"""
print(5 == 5 and 15 > 5)
print(5 == 5 and 15 < 5)
print(5 == 15 and 15 > 5)
print(5 == 15 and 15 < 15)
"""
# endregion


# region or
"""
print(5 == 5 or 15 > 5)
print(5 == 5 or 15 < 5)
print(5 == 15 or 15 > 5)
print(5 == 15 or 15 < 15)
"""
# endregion


# region not
"""
print(not 5 == 5)
print(5 != 5)
"""
# endregion


# region ornek_1
"""
iç içe if ile yaptığımız pratiğimizi tekrar edelim
0<sayı<100 arasında pozitiftir
a = int(input("a değeri giriniz: "))
# if a>0 and a<100:
#    print(f"{a} sayısı 100 den küçük pozitif")
#if 0 < a < 100:
    #print(f"{a} sayısı 100 den küçük pozitif")
  """  
# endregion


# region ornek_2
"""
code.org sitesine giriş yapacak olan kullanıcı
4,5,6 yaşları için kurs 1'e hoş geldin
dışında yaşı olanlar ise kurs 1'e uygun değilsin mesajı verelim
yas = int(input("lütfen yaş giriniz: "))
if yas>6 or yas<4:
    print("kurs 1 e uygun değilsin")
else:
    print("kurs 1 e hoş geldiniz")
"""    
# endregion


# region ornek_3
"""
toplam = 0
while True:
    sayi = int(input("lütfen sayı giriniz. Çıkmak için 0 tuşuna basınız. \t"))
    if sayi == 0:
        break
    if sayi<0 or sayi %2 == 1:
        print("Negatif ve tek sayı giremezsin")
        continue
    toplam += sayi
print(toplam)
"""
# endregion

# yas=int(input("Lütfen yaşınızı giriniz:\t"))
# if yas<7 and yas>3:
#     print(f"{yas} yaş kurs için uygundur." ) 
# else:
#     print(f"{yas} yaş kurs için uygun değildir." ) 



# while True:
#     yillikGelir=(input("Lütfen Yıllık gelirinizi yazınız, çıkmak için 0'a basınız."))
#     if yillikGelir==0:
#         print("bb")
#         break
#     if yillikGelir<32000:
#         vergi=yillikGelir*0.15
#         print(f" verginiz →{vergi} TL dir.")
#     elif yillikGelir<70000 or yillikGelir>32000:
#         vergi=yillikGelir*0.20
#         print(f" verginiz →{vergi} TL dir.")
#     elif yillikGelir<250000 or yillikGelir>70000:
#         vergi=yillikGelir*0.27
#         print(f" verginiz →{vergi} TL dir.")
#     elif yillikGelir<880000 or yillikGelir>61000:
#         vergi=yillikGelir*0.35
#         print(f" verginiz →{vergi} TL dir.")
#     else:
#         vergi=yillikGelir*0.40
#         print(f" verginiz →{vergi} TL dir.")




# kg=float(input("Lütfen kilogram bilginizi yazınız:\t"))
# boy=float(input("Lütfen boy bilginizi metre olarak giriniz:\t"))
# vki=kg/(boy**2)
# durum=True
# while durum:
#     if vki<=18.5:
#         print(f"vki →{round(vki,2)} olduğundan dolayı zayıfsınız.")
#     elif 18.6<=vki<=24.9:
#         print(f"vki →{round(vki,2)} olduğundan dolayı idealsiniz.")
#     elif 25<=vki<=29.9:
#         print(f"vki →{round(vki,2)} olduğundan dolayı şişmansınız.")
#     elif 30<=vki<=34.9:
#         print(f"vki →{round(vki,2)} olduğundan dolayı obezsiniz.")
#     else:
#         print(f"vki →{round(vki,2)} olduğundan dolayı aşırı obenzsiniz.")
#     print(f"Vücut kitle indeksiniz kilo {kg} - boy :{boy}: \t {vki}")
#     devam=input("Devam edecek misinix:[e/E]\t")
#     if devam not in "e":
#         durum=False

"""
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,asal sayıları belirten bir uygulama yapınız.
"""

# for i in range (2,19+1):
#     for j in range (2,i):
#         if i % i==0:
#             print(f"{i} sayısı asal değildir.")
#             break
#     else:
#         print(f"{i} sayısı asal değildir.")

"""
ekok uygulaması yapınız.
"""

# ekok=1
# s1=int(input("Lütfen sayı giriniz:\t"))
# s2=int(input("Lütfen sayı giriniz:\t"))
# liste =[2,3,5]
# for i in liste:
#     while True:
#         if s1 %i==0 and s2%i==0:
#             ekok*=i
#             s1=int(s1/i)
#             s2=int(s2/i)
#         elif s1%i==0:
#             ekok*=i
#             s1=int(s1/i)
#         elif s2%i==0:
#             ekok*=i
#             s2=int(s2/i)
#         else:
#             break
# ekok=ekok*s1*s2
# print(ekok)