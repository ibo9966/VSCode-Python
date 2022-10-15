# region ornek_1
"""
Ekrana Yazılacak Metni Giriniz: Ecodation
Ecodation
Ecodation
Ecodation
Ecodation
Ecodation
metin = input("Ekrana Yazılacak Metni Giriniz: ")
i = 1
while i<=5:
    print(metin)
    i += 1
"""
# endregion

# region ornek_2
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * * * * * * * * * *
i = 0
while i<10:
    print(" * ", end= "")
    i += 1
"""
# endregion

# region ornek_3
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * $ * $ * $ * $ * $
i = 0
while i<10:
    if i%2==0:
        print(" * ", end= "")
    else:
        print(" $ ", end= "")
    i += 1
"""
# endregion

# region ornek_4
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
"""
"""i, j = 0, 0
while i<10:
    while j<10:
        if i%2 ==0:
            print(" * ", end= "")
        else:
            print(" $ ", end= "")
        j += 1
    i +=1
    j = 0
    print()
"""
# endregion

# region ornek_5
"""
1→  [1-99] arası tek sayıları yan yana yazdıralım
2→  Her bir 10 adet sayıda alt satıra alalım
i = 1
s = 0
while i < 100:
    if s % 10 == 0:
        print()
    print(i, end=" ")
    s += 1
    i += 2
"""
# endregion

# region ornek_6
"""
1→  [1-99] arası tek sayıların toplamını yazdıralım
i = 1
toplam = 0
while i < 100:
    toplam += i
    i += 2
print(f"[1-99] arası tek sayıların toplamı → {toplam}")
"""
# endregion

# region ornek_7
"""
Lütfen Sayı Giriniz:    5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
i = 1
sayi = int(input("Lütfen Sayı Giriniz: "))
while i <= 10:
    print(f"{sayi } x {i} = {sayi*i}")
    i += 1
"""
# endregion

# region ornek_8
"""
Kırk Haramilerin hazine dolu mağarasından çıkmak için, gizli kelime olan
susamı bulmaya çalışan kahramanımızın hikayesini python ile yazalım
1→  kullanıcı gizli kelime girecek
2→  sonsuz döngü içinde kelimeyi bulmaya çalışırken, bulduğu anda döngüden çıkacak
gizliKelime = input("açıl .... açıl!!! lütfen boşluğu doldurun: \t")
while gizliKelime != "susam":
    print("hahahahahah ne oldu bilemedin ama :-)")
    gizliKelime = input("açıl .... açıl!!! lütfen boşluğu doldurun: \t")
print("başardın!!!")
"""
# endregion

# region ornek_9
"""
Kullanıcıdan sonsuz döngü içinde sayı girmesi istenir. 0 girdiğinde döngüden çıkılacak.
1→  döngü sonunda girilen sayıların ortalaması hesaplanacak
adet, toplam = 0, 0
sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
while sayi:
    toplam += sayi
    adet += 1
    sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
print(f"girdiğiniz sayıların ortalaması → {toplam/adet}")
"""
# endregion

# region ornek_10
"""
Kullanıcının girdiği rakama göre aşağıdaki gibi bir seri ekrana yazılacak
x - 2x - 3x - 4x - 5x
1→  kullanıcı rakam girecek
2→  int dönüşümü yapılacak
3→  döngü 5 kez tekrar ederek ekrandaki gibi bir çıktı yazılacak
Lütfen [1-9] arası rakam giriniz:  4
4  8  12  16  20
i = 1
rakam = int(input("lütfen [1-9] arası rakam giriniz: "))
while i<6:
    print(f"{rakam * i}", end=" ")
    i += 1
"""
# endregion

# region ornek_11
"""
1→  sayıların faktoriyelini bulacağız: [1-5] arası
2→  döngü 5 kez tekrar edecek
Çıktı:
1   1
2   2
3   6
4   24
5   120
i = 1
sonuc = 1
while i<6:
    sonuc *= i
    print(f"{i} \t {sonuc}")
    i += 1
"""
# endregion

# region ornek_12_algoritmalar_kitabından
"""
100-999
haneleri toplamı, hane sayısına eşit olanları ekrana yazalım
KOŞULU SAĞLAYAN SAYILAR:
102 (3 haneli, haneleri toplamı 3)
111 (3 haneli, haneleri toplamı 3)
120 (3 haneli, haneleri toplamı 3)
201 (3 haneli, haneleri toplamı 3)
210 (3 haneli, haneleri toplamı 3)
300 (3 haneli, haneleri toplamı 3)
i = 100
while i<1000:
    kalan = i % 10
    birler = kalan // 1
    kalan = i % 100
    onlar = kalan // 10
    kalan = i % 1000
    yuzler = kalan //100
    haneleriToplami = birler + onlar + yuzler
    if haneleriToplami == 3:
        print(f"{i} (3 haneli, haneleri toplamı 3)")
    i += 1
"""
# endregion

# region ornek_13
"""
rasgele sayı üreteceğiz [1, 99]
kullanıcı 3 kez sayı girecek, en yakın tahmin ekrana basılacak
örn →  54
34
50
99
en yakın sayı 50
örn →  54
51
4
99
en yakın sayı 51
import random   # random modülünü ekle
uretilenSayi = random.randint(1, 99)   # [1-99] arası sayı üretir
print(uretilenSayi)
i = 0
enKucukFark=99999999999
while i<3:
    tahmin = int(input("lütfen [1-99] arası tahmininizi giriniz: \t"))    
    fark = uretilenSayi - tahmin
    if fark<0:
        fark *= -1
    if fark<enKucukFark:
        enKucukFark = fark
        enYakinTahmin = tahmin
    i += 1
print(enYakinTahmin)
"""


# endregion

# region ornek_14
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
* * * * * * * * * *
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * *
* * *
* *
*
*
* * 
* * *
* * * *
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * *
* * * * * * * * * 
* * * * * * * * * * 
i, j = 0, 10
while i<10:
    while j>0:
        print(" * ", end= "")
        j -= 1
    i += 1
    j = 10 -i
    print()
i, j = 0, 0
while i < 10:
    while j < i:
        print(" * ", end="")
        j += 1
    i += 1
    j = 0
    print()
"""
# endregion

# region ornek_15
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
* * * *
  * * *
    * *
      *
i, j = 0, 4
n = 0
while i<4:
    while n>0:
        print("   ", end= "")
        n -=1
    while j>0:
        print(" * ", end="")
        j -=1
    i +=1
    n = i
    j = 4-i
    print()
i, j, n = 0, 0, 0
while i<4:
    while j<4:
        if n<i:
            print("   ", end="")
        else:
            print(" * ", end="")
        j +=1
        n +=1
    i +=1
    j = 0
    n = 0
    print()
"""
# endregion

# region ornek_16
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
     *
    * *
   * * *
  * * * *
 * * * * *
i, j, n = 0, 0, 5
while i < 5:
    while j <=5:
        if n>0:
            print(".", end="")
        else:
            print(" *", end="")     
        j += 1
        n -=1
    i += 1
    n = 5- i
    j = 0
    print()
"""
# endregion

# ödev →
"""
    - 0dan Kullanıcının girdiği sayıya kadar olan
    - 5e bölünen ama 7ye bölünmeyen sayıları yazdırın
"""


# ödev →
"""
    - Kullanıcının girdiği degere kadar 
    - kaç tane 3e ve 5e bölünen sayı vardır
"""

# ödev →
"""
    - Kullanıcıdan iki sayı alınır.
    - Küçük olandan büyük olana kadar olan sayılar yazılır.
"""

# ödev →
"""
    - kullanıcıdan ad ve şifre değeri alınır.
    - taaki kullancı admin 123 değerleri girene kadar.
    - girilen her hatalı girişte HATALI GIRIS,
    - doğru girildiğinde HOŞGELDİNİZ yazar.
"""

"""
Lütfen metin giriniz:"İstanbul"
"""
# i=0
# metin=input("lütfen metin giriniz:\t")
# while i<5:
#     print(istanbul)
#     i+=1

"""
Lütfen metin giriniz:"İstanbul"
kaç adet:3
"""
# i=0
# adet=0
# metin=input("Lütfen metin giriniz:\t")
# adet=int(input("Kaç adet yazılmasını istersiniz:\t"))
# while i<adet:
#     print(metin)
#     i+=1


# pattern
"""
$ $ $ $ $ $ $ $ $ $
"""
# i=0
# while i <10:
#     print(f"$", end=" ")
#     i+=1

"""
$ # $ # $ # $ # $ # 

"""

# i=0
# while i <10:
#     if i%2 ==1:
#         print(f"#", end=" ")
#     else:
#         print(f"$" , end=" ")
#     i+=1

"""
*
*
*
*
*
*
*
*
*
*
*
"""

# i=0
# while i <10:
#     print(" * ")
#     i+=1

"""
*
$
*
$
*
$
*
$
*
$

"""

# i=0
# while i < 10 :
#     if i%2==1:
#         print(" $ ")
#     else:
#         print(" * ")
#     i+=1

"""
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
"""

# i,j=0,0
# while i <10:
#     while j<10:
#         if i%2==0:
#             print(" * " , end="")
#         else:
#             print(" . ",end="" )
#         j+=1
#     i+=1
#     j=0
#     print()

"""
açıl...açıl  : kahve
hehehehe ne oldu çıkamıyor musun:-)
açıl...açıl  :
hehehehe ne oldu çıkamıyor musun:-)
açıl...açıl  : susam
"""

# secret= "susam"
# answer= input(" açıl...açıl , Lütfen boşluğu doldurunuz:\t")
# deneme=0
# while answer!= secret:
#     print("hehehehe ne oldu çıkamıyor musun:-) ")
#     answer= input(" açıl...açıl , Lütfen boşluğu doldurunuz:\t")
#     deneme+=1
# print(f"{deneme} kez denediniz!")

# """
1 3 5 7 9 11 13 ... 99
"""

# i=0
# x=0
# while i <100:
#     if i %2!=0:
#         if i ==49:
#             print("..", end=" ")
#         else:
#             print(f"{i}" , end=" ")
#         x+=1
#         if x==10:
#             print()
#             x=0
#     i+=1

"""
Sayı Giriniz:5
"""
# sayi=int(input("Lütfen 1-9 arası rakam giriniz:\t"))

# i=1
# while i <=sayi:
#     print(f"{sayi}x{i}={sayi*i}")
#     i+=1

"""
1 1
2 2 
3 6
4 24
5 120
"""

# i=1
# sonuc=1
# while i <6:
#     sonuc*=i
#     print(f"{i} sayısının faktoriyeli {sonuc}")
#     i+=1

# i=0
# while i <100:
#     if i %7==0:
#         print(i , end=" ")
#     i+=1


"""
Lütfen bir rakam giriniz:7
7 14 21
7 ye tam bölenlerinin adedi 8 dir.

"""


# i=1
# counter=0
# sayi=int(input("Lütfen rakam giriniz:\t"))
# while i <100:
#     if i % sayi==0:
#         print(i , end=" ")
#         counter+=1
#     i+=1
# print(f"\n{sayi} ye tam bölünenlerin adedi {counter}")

# i=1
# counter=0
# toplam=0
# sayi=int(input("Lütfen rakam giriniz:\t"))
# while i <100:
#     if i % sayi==0:
#         print(i , end=" ")
#         counter+=1
#         toplam+=i
#     i+=1
# print(f"\n{sayi} ye tam bölünenlerin adedi {counter}")
# print(f"{sayi} ye tam bölünenlerin toplamı {toplam}")

"""
hanelerin toplamı , hane sayısına eşit olan 100-999 arası tam sayıları ekrana yazdırınız.
102(3 haneli, hanelerin toplamı 3)
111(3 haneli, hanelerin toplamı 3)

"""

# i=100
# while i <1000:
#     kalan = i %10
#     birler=kalan//1
#     kalan = i %100
#     onlar=kalan//10
#     kalan = i %1000
#     yüzler=kalan//100
#     haneler=birler+onlar+yüzler
#     if haneler==3:
#         print(f"{i} (3 haneli, hanelerin toplamı 3)  ")
#     i+=1

# 1  2 3 4 5

# i=5
# while i>0 :
#     print(i)
#     i-=1

# i=0
# while i<6:
#     print(i)
#     i+=1

"""
*
* *
* * *
* * * *
* * * * *
"""

# i,j=0,0
# while i<10:
#     while j<=i:
#         print(" * ", end=" ")
#         j+=1
#     print()
#     j=0
#     i+=1

"""

* * * * *
* * * *
* * *
* *
*
"""

# i,j=0,10
# while i <10:
#     while j>0:
#         print(" * ", end="")
#         j-=1
#     i+=1
#     print()
#     j=10-i


"""
* * * * *
  * * * *
    * * *
        *
"""

# i, j = 0, 0
# while i < 4:
#     while j < 4:
#         if i<= j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#         j += 1
#     print()
#     j = 0
#     i += 1

"""
# # # # # # # # # #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
# # # # # # # # # #                

"""


"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
     *
    * *
   * * *
  * * * *
 * * * * *

"""

# i, j, n = 0, 0, 5
# while i < 5:
#     while j <=5:
#         if n>0:
#             print(".", end="")
#         else:
#             print(" *", end="")     
#         j += 1
#         n -=1
#     i += 1
#     n = 5- i
#     j = 0
#     print()

"""
*
* *
* * * 
* * * * 
* * * * *
iç içe while ile yapacağımız kesindir. 5 gibi degil 10 gibi düşünün
"""

# i,j=0,0
# while i <10:
#     while j<=i:
#         print(" * " , end="")
#         j+=1
#     print()
#     j=0
#     i+=1

"""
* * * * *
* * * * 
* * * 
* *
*

iç içe while ile yapacağımız kesindir.
"""

# i , j = 0 , 10
# while i <10:
#     while j >0:
#         print(" * ", end="")
#         j-=1
#     print()
#     i+=1
#     j=10-i

#pattern
"""
* * * * 
. * * *
. . * *
. . . *
"""

# i,j=0,0
# while i <4:
#     while j <4:
#         if i <=j:
#             print(" * ", end="")
#         else:
#             print("   ", end="")
#         j+=1
#     print()
#     j=0
#     i+=1

#pattern

"""
# # # # # # # # # #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
# # # # # # # # # #                

"""


"""
        *
       * *
      * * *
     * * * *
    * * * * *   
"""



