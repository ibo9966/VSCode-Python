# region for_giris
"""
for i in range(15):
    print(i, end= " ")
"""
# endregion

# region range
"""
sayiDizisi = list(range(15, 5, -1))
print(sayiDizisi)
"""

# endregion

# region ornek_1
"""
for i in range(1, 11): # 1 2 3 4 5 6 7 8 9 10
    if i !=5:
        print(f"{i}. Öğrenci")
"""
# endregion

# region ornek_2
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(" * ", end= "")
    print()
[1 x 1 = 1]     [1 x 2 = 2]     [1 x 3 = 3]     [1 x 4 = 4]     [1 x 5 = 5]
[2 x 1 = 1]     [2 x 2 = 2]     [2 x 3 = 3]     [2 x 4 = 4]     [2 x 5 = 5]
[3 x 1 = 1]     [3 x 2 = 2]     [3 x 3 = 3]     [3 x 4 = 4]     [3 x 5 = 5]
for i in range(1, 6):
    for j in range(1, 6):
        print(f"[ {i}x{j} = {i*j} ]\t", end= "")
    print()
    """
# endregion  

# region pass
"""
for i in range(1,6):
    for j in range(1,6):
        pass
"""
# endregion 

# sDizisi=list(range(2,20))
# print(sDizisi)

# sDizisi=list(range(2,20,2))
# print(sDizisi)

# sDizisi=list(range(20,2,-1))
# print(sDizisi)

# sDizisi=list(range(5))
# print(sDizisi)

"""
1. öğrenci
2. öğrenci
3. öğrenci
4. öğrenci
...
9. öğrenci
10. öğrenci
"""

# x=10
# if x>5:
#     for i in range (1,11):
#         if i !=5:
#             print(f"{i}. öğrenci")


# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i}-{j}" , end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         pass


"""
Lütfen Bir sayı giriniz:\t
1 2 3 5 6 10 15 

"""

# adet=0
# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# for i in range (1, sayi+1):
#     if sayi%i==0:
#         print(f"{i}", end=" ")
#         adet+=1
# print(f"\n {adet} adet tam böleni vardır", end="")

"""

# ek, obeb=0, 0
# sayi1=int(input("Lütfen sayı giriniz:\t"))
# sayi2=int(input("Lütfen sayı giriniz:\t"))
# if sayi1<sayi2:
#     ek=sayi1
# else:
#     ek=sayi2
# for i in range(1, ek+1):
#     if sayi1 % i ==0 and sayi2 % i ==0:
#         obeb=i
# print(f"{obeb}")

---########farklı bir şekilde aşağıdaki gibi yazılır hiç ek(en küçük) ve ya eb (en büyük) kullanmadan####-----


# obeb=0
# sayi1=int(input("Lütfen sayı giriniz:\t"))
# sayi2=int(input("Lütfen sayı giriniz:\t"))
# for i in range(1, min(sayi1, sayi2)+1):
#     if sayi1 % i ==0 and sayi2 % i ==0:
#         obeb=i
# print(f"{obeb}")

"""

"""
alınan sayı tau sayısı mı kontrol ediniz.
"""
# sayac=0
# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# for i in range(1, sayi+1):
#     if sayi % i ==0:
#         sayac+=1
# if sayi % sayac==0:
#     print(f"{sayi} sayısı TAU sayısıdır.")
# else:
#     print(f"{sayi} sayısı TAU sayı değidir.")
    

# toplam=0
# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# for i in range(1, sayi):
#     if sayi % i ==0:
#         toplam+=i
# if sayi == toplam:
#     print(f"{sayi} sayısı mükkemmel sayıdır.")
# else:
#     print(f"{sayi} sayısı mükemmel sayı değidir.")
    
# sayi1=int(input("Lütfen 1.sayıyı giriniz:\t"))
# sayi2=int(input("Lütfen 2.sayıyı giriniz:\t"))
# ek,obeb=0,0
# if sayi1<sayi2:
#     ek=sayi1
# else:
#     ek=sayi2
# for i in range (1,ek+1):
#     if sayi1 % i==0:
#         if sayi2 % i ==0:
#             obeb=i
# print(f"{sayi1} ve {sayi2} sayılarının obebi → {obeb}'dir")


#-########farklı bir şekilde aşağıdaki gibi yazılır hiç ek(en küçük) ve ya eb (en büyük) kullanmadan####-----
"""
OBEB 
"""
# obeb=0
# sayi1=int(input("Lütfen sayı giriniz:\t"))
# sayi2=int(input("Lütfen sayı giriniz:\t"))
# for i in range(1, min(sayi1, sayi2)+1):
#     if sayi1 % i ==0 and sayi2 % i ==0:
#         obeb=i
# print(f"{obeb}")
 
"""
TAU SAYISIDIR.
"""
# sayac=0
# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# for i in range(1,sayi+1):
#     if sayi % i ==0:
#         sayac+=1
# if sayi%sayac==0:
#     print(f"{sayi} sayısı TAU sayısıdır.")
# else:
#     print(f"{sayi} sayısı TAU sayısı değildir..")

"MUKKEMMEL SAYII"

# toplam=0
# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# for i in range(1,sayi):
#     if sayi % i ==0:
#         toplam+=i
# if sayi==toplam:
#     print(f"{sayi} sayısı mükemmel sayıdır.")
# else:
#     print(f"{sayi} sayısı mükemmel sayı değildir..")

"""
Aşağıdaki üsttekinin ufak dokunulmuş hali
"""

# toplam=0
# sayi=int(input("Lütfen bir sayı giriniz:\t"))
# for i in range(1,int(sayi/2)+1):
#     if sayi % i ==0:
#         toplam+=i
# if sayi==toplam:
#     print(f"{sayi} sayısı mükemmel sayıdır.")
# else:
#     print(f"{sayi} sayısı mükemmel sayı değildir..")

