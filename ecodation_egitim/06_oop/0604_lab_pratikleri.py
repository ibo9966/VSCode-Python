"""
   - Araba Galerisi için mimari oluşturulacaktır.
   - Galeri de arabaların her birinin marka, model, motor, yıl, renk, yas özelliği var
     - Marka-Model-Motor-Yıl mecbur girilmek zorundadır,
     - Renk zorunda değil. Girilmez ise tanımsız renk olarak ataması yapılacaktır.
     - Aynı zamanda yaş değeri kullanıcıdan alınmayacak
     - Constructor içinde hesaplama ile atama yapılacaktır. 2019 yılı
   - Show() fonk var. Show içinde arabanı tüm detayları düzgün biçimde formatlanarak gösterilir.
"""

# import datetime

# class Araba:
#     def __init__(self, marka, model, motor, yil, renk="TANIMSIZ") -> None:  # renk → default değer

#         self.marka = marka
#         self.model = model
#         self.motor = motor
#         self.yil = yil
#         self.renk = renk
#         self.yas = datetime.datetime.now().year - int(self.yil)

#     def show(self):
#         print(f"{self.marka} {self.model} {self.motor}{self.yas} {self.renk}")


# a = Araba("Hyndai", "i20", "1.2", 2016 , "siyah")
# a.show()


"""
   - Calisan class
       - ad,soyad,tc,maas
       - BilgiVer() -> Kullanıcının bilgileri yazdırılır
       - ZamYap(tl) -> eğer yapılmak istenen zam miktari, maaşın yarısından fazlaysa
           emin misin diye sorulur. cevap E ise zam yapılır, H ise bişey yapılmaz.
   -Sirket class
       - AlimYap() -> çalışan sınıfından nesneyi gönderip bilgilerini yazıp, işe alım yapılır.
       - IstenCikar() -> çalışan sınıfından nesneyi gönderip bilgilerini yazıp, işten çıkarılır.

# """

# class calisan:
#     def __init__(self , ad , soyad,  maas , tc="111111111" ) -> None:
#         self.ad=ad
#         self.soyad=soyad
#         self.maas=maas
#         self.tc=tc
    
#     def ZamYap(self, miktar):
#         if miktar>=self.maas/2:
#             cvp=input("Girilen miktar maaşın %50 sinden fazla emin misin? e/E")
#             if cvp.lower()=="e":
#                 self.maas+=miktar
#             else:
#                 print("peki peki biz yanlış yaptık")
#         else:
#             self.maas+=miktar

#     def BilgiVer(self):
#         return f"{self.ad} {self.soyad} {self.maas} {self.tc} "
    
# c1=calisan("Ali" , "Kemal" , 1000 , "4656565")
# c1.ZamYap(500)
# print(c1.BilgiVer())



