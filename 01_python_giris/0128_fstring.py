#output anıdna casting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız

#region format
#ekrana output formatlarken ilk yöntem → format
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))
a = int(input("l. a. de. giriniz: "))
b = int(input("l. b. de. giriniz: "))
print("{} değeri ile {} değerinin toplamı {}". format(a, b, (a+b)))
"""
#endregion

#region fstring
#ekrana output formatlarken ilk yöntem → fstring
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")
a = int(input("l. a. de. giriniz: "))
b = int(input("l. b. de. giriniz: "))
print(f"{a} değeri ile {b} değerinin toplamı {a+b}")
"""
#endregion

#region ornek
"""
s1 = int(input("l. s. g. : "))
s2 = int(input("l. s. g. : "))
print(f"girdiğiniz sayıların toplamı {s1+s2}")
print(f"{s1} + {s2} = {s1+s2}")
"""
"""
#girdiğiniz sayıların toplamı 8
#3 + 5 = 8
"""
#endregion

# kilo = int(input("lütfen kilonuzu giriniz : "))
# boy = float(input("lütfen boyunuzu giriniz : "))
# vki=kilo/boy**2

# print(f"boyu {boy} mt kilosu {kilo} kg olan nisa'nın vki değeri, {round(vki,2)} ")

#region x
#lütfen 1.sayı giriniz : 5
#lütfen 1.sayı giriniz : 10
#lütfen 1.sayı giriniz : 45
#Girilen 5, 10 45 sayılarının ortalamasını:20.0

# sayi1=int(input("1.sayıyı giriniz\t→ "))
# sayi2=int(input("2.sayıyı giriniz\t→ "))
# sayi3=int(input("3.sayıyı giriniz\t→ "))
# ort=(sayi1+sayi2+sayi3)/3
# print(f"Girilen {sayi1}, {sayi2} {sayi3} sayılarının ortalamasını:{ort}")
#endregion x


# saat = int(input("Bir saat giriniz : "))
# saniye = (60**2)*saat

# print(f"ekrandaki {saat} saat değerinin saniye karşılığı {saniye} sn.")


# rakam = int (input("lütfen 0-9 arasında rakam giriniz: "))
# print("girdiğiniz rakaman 1 fazlası" + str(rakam+1))


# rakam = int (input("lütfen 0-9 arasında rakam giriniz: "))
# print("girdiğiniz rakaman 1 fazlası {}" .format(rakam+1))

# a = 5 
# b = 10
# c = a+b
# print("girilen {} ve {} değerlerinin toplamı {} " .format(a, b , c  ))


# a = 5 
# b = 10
# c = a+b
# print(f"girilen {a} ve {b} değerlerinin toplamı {c} ")

# rakam = int (input("lütfen 0-9 arasında rakam giriniz: "))
# print(f"girdiğiniz rakaman 1 fazlası {rakam+1}")



# kilo=int(input("lütfen kilonuzu giriniz:"))
# boy=float(input("lütfen boyunuzu giriniz:"))
# vki=(kilo/(boy**2))
# print(f" boyu {boy} mt kilosu {kilo} kg olan nisa'nın vki değeri , {round(vki,2)} ")



# sayi1=int(input("lütfen 1.sayıyı giriniz:\t "))
# sayi2=int(input("lütfen 2.sayıyı giriniz:\t "))
# sayi3=int(input("lütfen 3.sayıyı giriniz:\t "))
# ort=(sayi1+sayi2+sayi3)/3
# print(f"girilen {sayi1}, {sayi2}, {sayi3} sayılarının ortalaması {20} dir .")

# boy=int(input("Lütfen boyunuzu giriniz:  "))
# m=boy//100
# cm=boy%100
# print(f"{m} metre {cm} santim")

# sehir=input("yaşadığınız şehir: ")
# lsehir=len(sehir)
# #girdiğiniz ankara şehrinin uzunluğu 6
# print(f"girdiğiniz {sehir} şehrinin uzunluğu {lsehir}")

# r=int(input("yarıçap kaç olduğunu yazınız:  "))
# alan=(3.14*(r**2))
# print(f"{r} cm yarıçap değerine sahip dairenin alanı {alan} cm kare")

saat=int(input("saati yazınız :  "))
saniye=saat*60*60
print(f"ekrandaki {saat} değerinin saniye karşılığı {saniye} ")