# #Bir öğrencinin sınav sonuçları  0 ile 5 arasındadır

# sinav_notu=int(input("alınan not"))
# if(sinav_notu>3):
#     print("başarılı")
# else:
#     print("başarısız")


# sayi=int(input("lütfen bir sayı giriniz:\→"))
# if(sayi>0):
#     print("sayı pozitiftir.")
# elif(sayi==0):
#     print("sayı sıfıra eşittir.")
# else:
#     print("sayı negatiftir.")

"""
Lütfen Kullanıcı Adınızı Giriniz : user
user yetkis ile admin paneline giriş yapamazsınız
"""

# kullanici_adi=input("lütfen kullanıcı adınızı giriniz.\t→")
# if kullanici_adi !="admin":
#     print(f"{kullanici_adi} yetkisi ile admin paneline giriş yapamazsınız")

# region if_aciklama
# if kullanımı
"""
1- önce if yazılır
2- sonra koşul yazılır
3- sonra da : iki nokta ile blok başlatılır
"""
# endregion

# region ornek_1
"""
havaDurumu = "güneşli"
print("a")
if havaDurumu == "yağmurlu":
    #print("şemsiye alın lütfen")
    print("b")
print("c")
"""
# endregion

# region ornek_2
"""
a = 10
if a<0:
    print(f"{a} sayısı negatiftir")
"""
# endregion

# region ornek_3
"""
s = int(input("Lütfen sayı giriniz \t : "))
if s == 0:
    print("lütfen 0 değeri girmeyin")
"""
# endregion

# region ornek_4
"""
uName = input("lütfen kullanıcı adınızı giriniz : ")
if uName != "admin":
    print(f"{uName} admin paneline giriş yapamaz")
"""
# endregion


"""
Lütfen Bir Sayı Giriniz: -10
-10 sayısı negatiftir.
"""

# sayi = int(input("lütfen bir sayı giriniz:\t→"))
# if sayi < 0:
#     print(f"{sayi} sayısı negatiftir.")
# elif sayi == 0:
#     print(f"{sayi} sayısı sıfıra eşittir.")
# else:
#     print(f"{sayi} sayısı pozittir..")


"""
Lütfen kullanıcı adınızı giriniz: user
User yetkisi ile admin paneline giriş yapamazsınız.
"""

# iAdi=input("Lütfen kullanıcı adınızı giriniz:\t→")
# if iAdi!="admin":
#     print(f"{iAdi} yetkisi ile admin paneline giriş yapamazsınız.")
# else:
#     print("LOGİN")