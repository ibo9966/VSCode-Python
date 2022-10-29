#region 1
# vize = input('Vize Notunuz : ')
# final = input('Final Notunuz : ')
# ortalama=(float(vize)*0.3)+(float(final)*0.7)
# print("Ortalama :{0} ".format(ortalama))
# if(ortalama<50):
#       print("Kaldınız")
# else:
#       print("Geçtiniz")
#endregion1

#region2
# vize = input("vize notu: ")
# final = input("final notunuz:")
# ortalama=(float(vize)*0.3)+(float(final)*0.70)
# print("ortalama:{0})" .format(ortalama))
# if(ortalama<65):
#     print("Kaldınız")
# else:
#     print("Geçtiniz")
#endregion2

#region3

# HAFTA1=input("alınan puan")
# Hafta2=input("alınan puan")
# Hafta3=input("alınan puan")
# Haft4=input("alınan puan")
# toplam=(int(HAFTA1))+(int(Hafta2))+(int(Hafta3))+(float(Haft4))
# if(toplam<50):
#     print("helal olsun ")

#endregion3

#region4
# Bir çalışanın sicil numarası verilecektir.
# Sicil numarası  tek olanların saatlik ücreti bir ise sicil numarası çift olanların saatlik ücreti iki ile çarpılacaktır.
# Haftalık çalışma saati 45
# Saatlik çalışma ücreti 60 TL

# a=int(input("sicil numarası\t"))
# b=int(input("haftalık çalışma saati\t"))
# c=int(input("saatlik ücret\t"))
# if a % 2==1 :
#     maas=(b*c)
#     print(maas)

# else :
#     maas=(2*b*c)
#     print(maas)

# a=float(input("sicil numarası\t"))
# b=float(input("haftalık çalışma saati\t"))
# c=float(input("saatlik ücret\t"))
# if a % 2==1 :
#     maas=(b*c)
#     print(maas)

# else :
#     maas=(2*b*c)
#     print(maas)

#endregion4

#region5
#İş yerinde ortalamanın altında kalındığı taktirde başarısız sayılmaktadır.
#iş yerine günde gece vardiyasında 100 iş geliyorsa ve 4 kişi çalışıyorsa kimler başarısız sayılmaktadır.


# Emre=int(input("Emrenin yaptığı iş\t→"))
# İbrahim=int(input("İbrahimin yaptığı iş\t→"))
# Furkan=int(input("Furkanın yaptığı iş\t→"))
# Duygu=int(input("Duygunun yaptığı iş\t→"))
# if(Emre<25):
#     print("BAŞARISIZ")
# else:
#     print("BAŞARILI")
# if(İbrahim<25):
#     print("BAŞARISIZ")
# else:
#     print("BAŞARILI")
# if(Furkan<25):
#         print("BAŞARISIZ")
# else:
#     print("BAŞARILI")  
# if(Duygu<25):
#         print("BAŞARISIZ")
# else:
#     print("BAŞARILI")

#endregion5

#region6



#A ve B ye sayı var hangisinin büyük olduğunu yazdır.

# a=int(input("a'nın değeri\t→"))
# b=int(input("b'nın değeri\t→"))
# if(a>b):
#     print("a b'den büyük")
# elif(a==b):
#     print("a b'ye eşit")
# else:
#     print("a b'den küçüktür.")
#endregion6

#region7

#print("Mehmet","Akif","Ersoy",sep="♥",end="→")
#print("İstiklal","Marsının","yazarıdır",sep="↨",end=".")

#endregion7

#region8

#print("Haftanın\nÖdevlerini\t\tbitirdim\nBundan\n\ndolayı\t\t\trahatım.")

#endregion8

#region9
# a=((5**2)/(4*2*3)+5)**(1/2)
# print(a)
#endregion9

#region10

# a=int(input("a'nın degeri"))
# if a % 2 == 1 :
#     print("Sayı tektir.")
# else:
#     print("sayı çifttir.")

#endregion10

#region11

# a=("ben bir stringim")
# b=(15)
# c=(1.4)
# d=(16.15)
# print(type(a),type(b),type(c),type(d))

#endregion11

#region12

# print(35 % 2==1)
# print(40 % 2==1)
# print(45 % 2==1)
# print(57 % 2==1)

#endregion12

#region13

# x = y = z = 10
# a,b,c=10,20,30
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)

#endregion13

#region14

#Bir okuldaki 3 öğretmenin maaşlarını okuyup maaş toplamını ekrana yazdıran algoritma ve akış şemasını hazırlayınız.

# # number of elements as input
# import string

# n=3
# sum=0
# for i in range(0, n):
#     print("maasi giriniz.")
#     maas = int(input())
#     sum+=maas #sum=maas+sum 
# print(sum)

#endregion14

#region15

#print("Çalışan adı\tÇözülen ticket adeti\tYapılan Aramalar\tAlınan İyi\tAlınan Kötü\nİbrahim\t\t20\t\t\t5\t\t\t3\t\t1\nFurkan\t\t40\t\t\t8\t\t\t4\t\t2\nEmre\t\t33\t\t\t8\t\t\t1\t\t2\nDuygu\t\t32\t\t\t1\t\t\t7\t\t1\nNazlı\t\t33\t\t\t8\t\t\t11\t\t8\nYusuf\t\t13\t\t\t4\t\t\t2\t\t0\nSena\t\t18\t\t\t7\t\t\t1\t\t3\nNil\t\t10\t\t\t2\t\t\t2\t\t2\nAyşe\t\t20\t\t\t5\t\t\t6\t\t1\nFatma\t\t26\t\t\t4\t\t\t3\t\t1\nYağmur\t\t33\t\t\t7\t\t\t2\t\t3\nKerem\t\t29\t\t\t9\t\t\t8\t\t6\nCivan\t\t21\t\t\t4\t\t\t2\t\t3\nLeyla\t\t17\t\t\t8\t\t\t3\t\t4\nOguzhan\t\t20\t\t\t5\t\t\t3\t\t1")

#endregion15

#region16

# print("Çocuktum","ufacıktım",sep=", ",end=",\n")
# print("Top oynadım","acıktım",sep=", ",end=".\n\n")
# print("Buldum bir yerde bir erik",end=",\n")
# print("Kaptı bir Ala Geyik",end=".\n\n")
# print("Geyik kaçtı ormana", end=",\n")
# print("Bindim bir ak doğana",end=".\n\n")
# print("Doğan","yolu şaşırdı", sep=", ",end=",\n")
# print("Kaf Dağından aşırdı",end=".")

#endregion16

#region17

# result=((120/3)-(5*7))
# print(result)
# resulta=(165/(31-26)*3)
# print(resulta)
# resultb=(7*(12+5)-4)
# print(resultb)
# resultc=(85-45)*(13+17)
# print(resultc)
# resultd=((85-40)**(1/2)+(5*3)*(3/2))
# print(resultd)

#endregion17

#region18

# import turtle

# turtle.bgcolor("black")
# turtle.pensize(2)

# def curve():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)

# turtle.speed(0)
# turtle.color("red", "pink")

# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(111.65)
# curve()

# turtle.left(120)
# curve()
# turtle.forward(111.65)
# turtle.end_fill()
# turtle.hideturtle()


#endregion18

#region19

print("""

HESAP MAKİNESİ

TOPLAMA İŞLEMİ YAPMAK İÇİN 1 'e BASIN.
ÇIKARMA İŞLEMİ YAPMAK İÇİN 2 'e BASIN.
ÇARPMA İŞLEMİ  YAPMAK İÇİN 3 'e BASIN.
BÖLME İŞLEMİ   YAPMAK İÇİN 4 'e BASIN.

""")

# islem = str(input("İşlem seçiniz: "))

# if islem == "1":
#     sayi1 = int(input("sayi1 giriniz: "))
#     sayi2 = int(input("sayi2 giriniz: "))
#     print("Sonuç:", sayi1 + sayi2)
# elif islem == "2":
#     sayi1 = int(input("sayi1 giriniz: "))
#     sayi2 = int(input("sayi2 giriniz: "))
#     print("Sonuç:", sayi1 - sayi2)
# elif islem == "3":
#     sayi1 = int(input("sayi1 giriniz: "))
#     sayi2 = int(input("sayi2 giriniz: "))
#     print("Sonuç:", sayi1 * sayi2)
# elif islem == "4":
#     sayi1 = int(input("sayi1 giriniz: "))
#     sayi2 = int(input("sayi2 giriniz: "))
#     print("Sonuç:", sayi1/sayi2)
# else:
#     print("geçersiz işlem girdiniz...")

#endregion19

#region20
# import turtle

# turtle.bgcolor("black")
# turtle.pensize(2)

# def curve():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)

# turtle.speed(0)
# turtle.color("red", "pink")

# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(111.65)
# curve()

# turtle.left(120)
# curve()
# turtle.forward(111.65)
# turtle.end_fill()
# turtle.hideturtle()
#endregion20

#region21
# import turtle
 
# #pencere
# pencere=turtle.Screen()
# pencere.bgcolor("black")
 
# #cizim
# turtle.color("red")
# turtle.circle(100)

#endregion21

#region22

