"""
    - 0dan Kullanıcının girdiği sayıya kadar olan
    - 5e bölünen ama 7ye bölünmeyen sayıları yazdırın
"""

# i=0
# sayi=int(input("Lütfen Sayi giriniz:\t"))
# while i <sayi:
#     if i%5==0:
#         if i%7!=0:
#             print(f"{i} sayıları 5 e tam bölünür ama 7 ye tam bölünemez.")
#     i+=1


"""
    - Kullanıcının girdiği degere kadar 
    - kaç tane 3e ve 5e bölünen sayı vardır
"""

# i=0
# sayi=int(input("Lütfen Sayi giriniz:\t"))
# while i <sayi:
#     if (i%3==0)and(i%5==0):
#         print(f"{i} sayıları 3 e ve 5 e tam bölünebilir.")
#     i+=1

"""
    - Kullanıcıdan iki sayı alınır.
    - Küçük olandan büyük olana kadar olan sayılar yazılır.
"""

# def calculate(s1,s2):
#     for i in range(s1,s2):
#         print(i)
# a=int(input("Lütfen  a Sayisini giriniz:\t"))
# b=int(input("Lütfen  b Sayisini giriniz:\t"))
# if a>b:
#     calculate(b,a)
# else:
#     calculate(a,b)

"""
    - kullanıcıdan ad ve şifre değeri alınır.
    - taaki kullancı admin 123 değerleri girene kadar.
    - girilen her hatalı girişte HATALI GIRIS,
    - doğru girildiğinde HOŞGELDİNİZ yazar.

# """
id="admin"
pw="123"
kullanici_id=input("Lütfen Kullanıcı Adı Giriniz:\t")
kullanici_pw=input("Lütfen Parolanızı Giriniz:\t")
while True:
    if(kullanici_id==id):
        if(kullanici_pw==pw):
            print("Başarılı şekilde giriş yaptınız.")
            break
        else:
            print("Parola yanlış")
            kullanici_pw=input("Lütfen Parolanızı Giriniz:\t")
    else:
        print("Lütfen tekrar deneyiniz. ")
        kullanici_id=input("Lütfen Kullanıcı Adı Giriniz:\t")
        kullanici_pw=input("Lütfen Parolanızı Giriniz:\t")


# tekHaneli = 0
# ciftHaneli = 0
# ucHaneli = 0
# sayac = 0
# sayi = int(input("Lütfen Sayı Giriniz. Çıkmak için 0 basınız:\t"))
# while True:
#     if sayi == 0:
#         print(f"{tekHaneli} adet tek haneli sayı vardır")
#         print(f"{ciftHaneli} adet çift haneli sayı vardır.")
#         print(f"{ucHaneli} adet üç haneli sayı vardır.")
#         break
#     else:
#         basamakSayisi = 0
#         while sayi / 10 >= 1:
#             sayi = sayi / 10
#             basamakSayisi += 1
#         basamakSayisi += 1
#         if basamakSayisi == 1:
#             tekHaneli += 1
#         elif basamakSayisi == 2:
#             ciftHaneli += 1
#         elif basamakSayisi == 3:
#             ucHaneli += 1
#         sayi = int(input("Lütfen Sayı Giriniz. Çıkmak için 0 basınız:\t"))



