"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
# a="* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
# print(len(a))
# i=0
# while i<37:
#     print("*" , end=" ")
#     i+=1

"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
* $ * $ * $ * $ * $
"""

# i=0
# while i<10:
#     if i % 2 ==0:
#         print(" * " , end="")
#     else:
#         print(" $ " , end="")
#     i+=1


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

# i , j =0 ,0
# while i <10:
#     while j<10:
#         if i % 2 == 0:
#             print(" * " , end="")
#         else:
#             print(" $ " , end="")
#         j+=1
#     i+=1
#     j=0
#     print()

"""
+ + + + + 
- - - - -
+ + + + + 
- - - - -

"""

# x,y=0,0
# while x<4:
#     while y<5:
#         if x % 2 == 0:
#             print("+", end=" ")
#         else:
#             print("-", end=" ")
#         y+=1
#     x+=1
#     y=0
#     print()


"""
1→  [1-99] arası tek sayıları yan yana yazdıralım
2→  Her bir 10 adet sayıda alt satıra alalım
1 3 5 7 9 11 13 15 17 19 
21 23 25 ..
"""


# i=1
# sayac=0
# while i<100:
#     if sayac % 10 ==0:
#         print()
#     print(i , end=" ")
#     i+=2
#     sayac+=1

"""
sayı iste 
sayı x 1= sayıx1
sayı x 2= sayıx2
.
.
.
.
sayıx 9=sayıx9
"""
# i=0
# sayi=int(input("Lütfen sayı giriniz:\t"))
# while i < 10:
#     print(f"{sayi}x{i}= {sayi*i}")
#     i+=1


"""
Kırk Haramilerin hazine dolu mağarasından çıkmak için, gizli kelime olan
susamı bulmaya çalışan kahramanımızın hikayesini python ile yazalım
1→  kullanıcı gizli kelime girecek
2→  sonsuz döngü içinde kelimeyi bulmaya çalışırken, bulduğu anda döngüden çıkacak
"""

# cevap="susam"
# kullaniciCevap=input("Lütfen cevap giriniz:\t")
# while cevap!=kullaniciCevap:
#     print("Giriş denemesi başarısız.Tekrar deneyiniz:")
#     kullaniciCevap=input("Lütfen cevap giriniz:\t")
# print("başarılı bir şekilde giriş yaptınız.")


"""
bir yarışmada 1 . olana kadar yarışçılar yarışmaya devam etmektedir.
sonsuz döngüde bunu sorucaz
kaçındı yarışında 1. olduğunu ve o zamana kadar kaçıncılıklar olduğunu toplayacaz

"""
# win=1
# deneme=0
# skor=0
# tryToWin=int(input("Lütfen sıralama giriniz:\t"))
# while win!=tryToWin:
#     print("1.olamadınız tekrar giriniz.")
#     tryToWin=int(input("Lütfen sıralama giriniz:\t"))
#     deneme+=1
#     skor+=(tryToWin)
# print(f"{deneme+1} kez denendi. {skor} skor alındı. Artık zirvede bırakınız.")

"""
Kullanıcıdan sonsuz döngü içinde sayı girmesi istenir. 0 girdiğinde döngüden çıkılacak.
1→  döngü sonunda girilen sayıların ortalaması hesaplanacak

"""

# adet,toplam=0,0
# sayi=int(input("Lütfen sayı giriniz, çıkmak istediğinizde 0 'a basnız :"))
# while sayi!=0:
#     toplam+=sayi
#     adet+=1
#     sayi=int(input("Lütfen sayı giriniz, çıkmak istediğinizde 0 'a basnız :"))
# print(f"girdiğiniz sayıların toplamı {toplam} , adet sayısı {adet}  ve rtalaması → {toplam/adet}")

"""
1→  sayıların faktoriyelini bulacağız: [1-5] arası
2→  döngü 5 kez tekrar edecek
Çıktı:
1   1
2   2
3   6
4   24
5   120
"""

# i=1
# sonuc=1
# while i<6:
#     sonuc*=i
#     print(f"{i} sayısının faktöriyeli {sonuc}")
#     i+=1

# i = 0
# sayi = int(input("Bir sayı giriniz: "))
# factorial = 1
# if sayi < 0:
#    print("Lütfen negatif bir sayı girmeyin.")
# elif sayi == 0:
#    print("0 ' ın faktoriyeli 1")
# else:
#    for i in range(1,sayi + 1):
#        factorial = factorial*i
#    print(f"{sayi} sayısının faktoriyeli → {factorial}")


"""
Kullanıcının girdiği rakama göre aşağıdaki gibi bir seri ekrana yazılacak
x - 2x - 3x - 4x - 5x
1→  kullanıcı rakam girecek
2→  int dönüşümü yapılacak
3→  döngü 5 kez tekrar ederek ekrandaki gibi bir çıktı yazılacak
örnek Çıktı:
Lütfen [1-9] arası rakam giriniz:  4
4  8  12  16  20

"""
# i=1
# sayi=int(input("Lütfen 1-9 arası rakam giriniz:\t"))
# if 1<=sayi<=9:
#     while i<6:
#         print(f"{sayi*i}", end=" ")
#         i+=1
# else:
#     print("Lütfen 1 ve 9 arasında rakam gir.")

"""
100-999
haneleri toplamı, hane sayısına eşit olanları ekrana yazalım
"""

# i=100
# while i<1000:
#     kalan = i % 10
#     birler = kalan // 1
#     kalan = i % 100
#     onlar = kalan // 10
#     kalan = i % 1000
#     yuzler = kalan //100
#     haneleriToplami = birler + onlar + yuzler
#     if haneleriToplami == 3:

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
"""


# i,j=0,0
# while i<10:
#     while j>0:
#         print(" * ", end="")
#         j-=1
#     i+=1
#     j=10-i
#     print()
# i,j=0,0
# while i <10:
#     while j<i:
#         print(" * ", end="")
#         j+=1
#     i+=1
#     j=0
#     print()

"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
* * * *
  * * *
    * *
      *
"""

# i, j, n = 0, 0, 0
# while i<4:
#     while j<4:
#         if n<i:
#             print("   ", end="")
#         else:
#             print(" * ", end="")
#         j +=1
#         n +=1
#     i +=1
#     j = 0
#     n = 0
#     print()

"""
    - 0dan Kullanıcının girdiği sayıya kadar olan
    - 5e bölünen ama 7ye bölünmeyen sayıları yazdırın
"""

# i=0
# sayi=int(input("Lütfen sayı giriniz:\t"))
# while i<sayi:
#     if i % 5==0:
#         if i % 7!=0:
#             print(f"{i} sayısı 5e tam bölünür fakat 7 ye tam bölünmez.")
#     i+=1

# ödev →

"""
    - Kullanıcının girdiği degere kadar 
    - kaç tane 3e ve 5e bölünen sayı vardır
"""

# i=0
# sayi=int(input("Lütfen sayı giriniz:\t"))
# while i < sayi:
#     if i %3==0 and i%5==0:
#         print(f"{i} sayıları 3'e ve 5'e tam bölünür")
#     i+=1

"""
    - Kullanıcıdan iki sayı alınır.
    - Küçük olandan büyük olana kadar olan sayılar yazılır.
"""
# ek=0
# eb=999999999999999
# sayi1=int(input("Lütfen 1.sayıyı giriniz:\t"))
# sayi2=int(input("Lütfen 2.sayıyı giriniz:\t"))
# if sayi1>sayi2:
#     ek=sayi2
#     eb=sayi1
#     while ek<eb:
#         print()
# elif sayi2>sayi1:
#     ek=sayi1
#     eb=sayi2
#     while ek<eb:
#         print()
# else :
#     print("Sayı 1 sayı 2'ye eşittir.")


# sayi1=int(input("Lütfen 1.sayıyı giriniz:\t"))
# sayi2=int(input("Lütfen 2.sayıyı giriniz:\t"))
# if sayi1>sayi2:
#     ek=sayi2
#     eb=sayi1
# elif sayi2>sayi1:
#     ek=sayi1
#     eb=sayi2
# else :
#     print("Sayı 1 sayı 2'ye eşittir.")
# while ek<eb:
#     print(ek)
#     ek = ek + 1


"""

    - kullanıcıdan ad ve şifre değeri alınır.
    - taaki kullancı admin 123 değerleri girene kadar.
    - girilen her hatalı girişte HATALI GIRIS,
    - doğru girildiğinde HOŞGELDİNİZ yazar.

"""


# id="admin"
# pw="123"
# kullanici_id=input("Lütfen kullanıcı adı giriniz:\t")
# kullanici_pw=input("Lütfen parola giriniz:\t")
# while True:
#     if  kullanici_id==id:
#         if kullanici_pw==pw:
#             print("Başarılı bir şekilde giriş yaptınız.")
#             break
#         else:
#             print("Parola yanlış, lütfen tekrar deneyiniz.")
#             kullanici_pw=input("Lütfen parola giriniz:\t")
#     else:
#         print("Lütfen tekrar deneyiniz.")
#         kullanıci_id=input("Lütfen kullanıcı adı giriniz:\t")
#         kullanici_pw=input("Lütfen parola giriniz:\t")


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

# i=0
# while i<10:
#     print("#",end=" ")
#     i+=1
# print()
# i,j=0,0
# while i<8:
#     while j<10:
#         if j==0 or j==9:
#             print("#" ,end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     j=0
#     print()
# i=0
# while i<10:
#     print("#",end=" ")
#     i+=1


# i=0
# while i<10:
#     print("#",end=" ")
#     i+=1
# print()
# i,j=0,0
# while i<8:
#     while j<10:
#         if j==0 or j==9:
#             print("#" ,end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     j=0
#     print()
# i=0
# while i<10:
#     print("#",end=" ")
#     i+=1
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
     *
    * *
   * * *
  * * * *
 * * * * * 
"""
# i = 1
# while i < 6:
#     for i in range (6):
#         print(" " * (6-i), " *"*i)
#         i += 1

"""
1→  sonsuz döngü içinde kullanıcın girdiği sayıların
    tek olanlarının ortalamasını bulalım
2→  çift sayı girmeye çalıştığında ekrana uyarı verelim
3→  programı continue kulllanmalıyız
"""

# adetTek=0
# tekToplam=0
# while True:
#     sayi=int(input("Lütfen sayı giriniz, çıkmak için 00 giriniz:\t"))
#     if sayi==00:
#         print("BB")
#         break
#     if sayi%2==1:
#         print("Lütfen tek sayı giriniz:")
#         tekToplam+=sayi
#         adetTek+=1
#         continue
#     else:
#         print("çift sayısı girdiniz Lütfen tek sayı giriniz:")
# ort=tekToplam/adetTek
# print(f"listedeki tek sayıların ortalaması {ort}")


"""
Kullanıcı aşağıdaki gibi bir seçim yaparak alt programları çalıştıracağız.
Hiç biri değil ise hatalı seçim diyeceğiz.
[1]     km→mil
[2]     mil→km
[3]     çık
"""

# while True:
#     secim=int(input("Lütfen seçim yapınız:\t"
#     """
#     [1]     km→mil
#     [2]     mil→km
#     [3]     çık))
#     """))

#     if secim==1:
#         km=float(input("Lütfen km bilgisini giriniz:\t"))
#         mil = km * 0.62137
#         print(f"{km} km {mil} mil  eder.")
#     elif secim==2:
#         mil=float(input("Lütfen mil bilgisi giriniz:\t"))
#         km  = mil / 0.62137
#         print(f"{mil} mil {km} km eder")
#     elif secim==3:
#         print("Çıkış yaptınız!")
#         break
#     else:
#         print("Hatalı seçim")

"""
kullanıcı sayı girecek
int dönüşümü yapılacak
girilen sayının tam bölenleri ekrana yazılacak
"""

# i=1
# sayi=int(input("Lütfen sayı giriniz:\t"))
# for i in range(1,sayi+1):
#     if sayi%i==0:
#         print(i, end=" ")

"""
girilen sayıya kadar olan asal sayıları 
ekrana yazdıran programı yazalımkullanıcı sayı girecek
"""

# sayac=0
# sayi=int(input("Lütfen sayı giriniz:\t"))
# for i in range(2,sayi+1):
#     for j in range(1,i):
#         if i % j ==0:
#             sayac+=1
#     if sayac<2:
#         print(i, end=" ")
#     sayac=0


"""
obeb uygulaması yapınız.
"""
# obeb = 0
# s1 = int(input("lütfen 1. s . gi "))
# s2 = int(input("lütfen 2. s . gi "))
# for i in range(1, min(s1, s2)+1):
#     if s1 % i == 0:
#         if s2 % i == 0:
#             obeb = i
# print(obeb)

"""
kullanıcının girdiği sayı TAU sayısı mıdır?
TAU sayısı : 
24 → 1, 2, 3, 4, 6, 8, 12, 24 → 24 % 8 == 0 TAU dur.
15 → 1, 3, 5, 15 → 15 % 4 != 0 TAU değildir.
Anlamı: pozitif bölenleri sayısına bakıldığında mod 0 ise TAU dur.
# """

# sayac = 0
# sayi = int(input("lütfen sy giriniz: "))
# for i in range(1, sayi + 1):
#     if sayi % i == 0:
#         sayac += 1
# if sayi % sayac == 0:
#     print("TAUDUR")
# else:
#     print("TAU DEĞİLDİR")

"""
kullanıcıdan sayı alınız. Mükemmel sayı mı kontrol eden bir uygulama yazınız.
mükemmel sayı kendisi haricindeki tüm çarpanlarının
toplamı kendisini veren sayıdır
6   → 1, 2, 3 → toplamı 6 mükemmel sayı
24 → 1, 2, 3, 4, 6, 8, 12 → toplamı 36 mükemmel sayı değildir
"""

# toplam = 0
# sayi = int(input("lütfen sy giriniz: "))
# for i in range(1, int(sayi/2)+1):
#     if sayi%i == 0:
#         toplam += i
# if toplam == sayi:
#     print("mükemmeldir")
# else:
#     print("mükemmel değildir")

"""
    - Kullanıcının girdiği 2sayı arasındaki değerleri,
    her zaman küçükten büyüğe sıralayan for döngüsü yazın.
    1,10 -> 1,2,3,4,5,6,7,8,9
    10-1 -> 1,2,3,4,5,6,7,8,9
"""


# sayi1=int(input("Lütfen 1.sayı giriniz:\t"))
# sayi2=int(input("Lütfen 2.sayı giriniz:\t"))
# if sayi1>sayi2:
#     eb=sayi1
#     ek=sayi2
# elif sayi2>sayi1:
#     ek=sayi1
#     eb=sayi2
# else:
#     print("Sayı 1 sayı 2'ye eşittir...")
# for i in range (ek,eb):
#     print(ek)
#     ek=ek+1

"""
Vücüt kitle indeksi hesaplayan bir uygulama yazınız. 
vki=vki =round(kg/mt**2, 2)
"""

# kg=float(input("Lütfen kilogram bilginizi giriniz:\t"))
# boy=float(input("Lütfen boy bilginizi metre cinsinden giriniz:\t"))
# vki=(kg/(boy**2))
# if vki <18.5:
#     print(f" vücüt kitle indeksinizi :{vki} bundan dolayı zayıfsınız." )
# elif 18.5<=vki<=24.9:
#     print(f" vücüt kitle indeksinizi :{vki} bundan dolayı normalsiniz." )
# elif 25<=vki<=29.9:
#     print(f" vücüt kitle indeksinizi :{vki} bundan dolayı kilolusunuz." )
# else:
#     print(f" vücüt kitle indeksinizi :{vki} bundan dolayı obezsiniz." )

"""
    - Youtube izlenme oranı son ek ekleme ile ilgili örneği yapınız.
    - izlenme 18000         → 18 B
    - izlenme 1800000       → 1.8 Mn
    - izlenme 1800000000    → 1.8 Ml
"""
# 1000              B   
# 10000             B   
# 100000            B
# 1000000           Mn 
# 10000000          Mn
# 100000000         Mn
# 1000000000        Ml

# izlenme = int(input("Lütfen izlenme sayınızı giriniz:\t"))
# if 0<=izlenme <= 999:
#     print(f"{izlenme} izlenmeniz bulunmaktadır.")
# elif 1000<=izlenme <= 999999:
#     izlenme//=1000
#     print(f"{izlenme}K izlenmeniz bulunmaktadır.")
# elif 1000000<=izlenme <= 999999999:
#     izlenme/=1000000
#     print(f"{izlenme}Mn izlenmeniz bulunmaktadır.")
# elif 1000000000<=izlenme <= 999999999999:
#     izlenme/=1000000000
#     print(f"{izlenme}Ml izlenmeniz bulunmaktadır.")
# else:
#     print(f"{izlenme}B.....")

"""
2 sayı alarak,
obeb uygulaması yapınız.
okek uygulaması yapınız.
"""
# s1 = int(input("Birinci Sayıyı Giriniz : "))
# s2 = int(input("İkinci Sayıyı Giriniz : "))
# for i in range (1, min(s1,s2)+1):
#     if s1 % i == 0 and s2 % i == 0:
#         ebob = i
#         ekok = (s1*s2)//ebob
# print ("EBOB" , ebob)
# print ("EKOK" , ekok)

"""
3 sayı alarak,
obeb uygulaması yapınız.
okek uygulaması yapınız.
"""

# s1 = int(input("Birinci Sayıyı Giriniz : "))
# s2 = int(input("İkinci Sayıyı Giriniz : "))
# s3 = int(input("üçüncü Sayıyı Giriniz : "))
# for i in range (1, min(s1,s2,s3)+1):
#     if s1 % i == 0 and s2 % i == 0 and s3 % i ==0:
#         ebob = i
#         ekok = (s1*s2*s3)//ebob
# print ("EBOB" , ebob)
# print ("EKOK" , ekok)

"""
girilen sayıya kadar olan asal sayıları 
ekrana yazdıran programı yazalımkullanıcı sayı girecek
"""


# say = 0
# son = int(input("l. son değeri. giriniz \t: "))
# for i in range(2, son+1):
#     for j in range(1, i):
#         if i % j == 0:
#             say +=1
#     if say<2:
#         print(i, end= " ")
#     say = 0
    
            
# sayi = int(input("Lütfen bir sayı giriniz : "))
# for i in range(2,sayi + 1):
#     asal = True
#     for j in range (2,i):
#         if i % j == 0:
#             asal = False
#     if asal == True:
#         print(i, end = " ")

