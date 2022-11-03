"""a = 10
class Insan:
    insanlar=[]
    def __init__(self, ad, soyad) -> None:
        self.ad = ad
        self.soyad = soyad
        Insan.Ekle(self)
    @classmethod
    def Ekle(cls, insanNesnesi):
        Insan.insanlar.append(insanNesnesi.birlestir())
    def birlestir(self):
        return f"{self.ad} {self.soyad}"""

# def __str__(self):
#     return f"{self.ad} {self.soyad}"

# def bilgiVer(self):
#     pass

# def yazdir(self):
#     pass

"""
i1 = Insan("aliiiiii","kemal")
# i2 = Insan("yusuf","efe")
# mainInsanlar = [i1, i2]
for insan in Insan.insanlar:
    print(insan)
"""


"""
a = 10
class Ogrenci:
    ogrenciNotlari = []
    def __init__(self, adSoyad, n1, n2) -> None:
        self.adSoyad = adSoyad
        self.n1 = n1
        self.n2 = n2
        Ogrenci.genelOrtalama(self)
    @classmethod
    def genelOrtalama(cls, ogrenciNesnesi):
        Ogrenci.ogrenciNotlari.append(ogrenciNesnesi.notHesapla())
    def notHesapla(self):
        return (self.n1+self.n2)/2
o1 = Ogrenci("Ali Kemal", 50, 60)
o2 = Ogrenci("Murat Çalışkan", 90, 100)
for item in Ogrenci.ogrenciNotlari:
    print(item)
"""


"""class Product:
    def __init__(self, pId, pName, pYil) -> None:
        self.pId = pId
        self.pName = pName
        self.pYil = pYil
    def __str__(self) -> str:
        return f"{self.pId} {self.pName} üretim tarihinden bu güne {2022 - self.pYil} yıl geçmiş"
p = Product(1200, "Tea", 2021)
print(p)"""


# class Insan:
#     insanlar=[]

#     def __init__(self , ad , soyad) -> None:
#         self.ad=ad
#         self.soyad=soyad
#         Insan.Ekle(self)
#     @classmethod
#     def Ekle(cls,insannesnesi):
#         Insan.insanlar.append(insannesnesi)


#     def __str__(self) -> str:
#         return f"{self.ad} {self.soyad}"


# i1=Insan("Ali" , "Kemal")
# i2=Insan("serkan" , "kırmızı")
# i3=Insan("kamil" , "Bilge")
# # print(i1)
# # print(i2)
# # print(i3)
# for i in Insan.insanlar:
#     print(i)

# class Ogrenci:
#     ogrenciNotlari = []

#     def __init__(self, adSoyad, n1, n2) -> None:
#         self.adSoyad = adSoyad
#         self.n1 = n1
#         self.n2 = n2
#         Ogrenci.GenelOrtalama(self)

#     @classmethod
#     def GenelOrtalama(cls, ogrenciNesnesi):
#         Ogrenci.ogrenciNotlari.append(ogrenciNesnesi.NotHesapla())

#     def NotHesapla(self):
#         return (self.n1+self.n2)/2


# while True:
#     ad = input("Lütfen ad soyad giriniz, çıkmak için q :")
#     if ad.lower() == "q":
#         break
#     nt1 = int(input("Lütfen not 1 giriniz:"))
#     nt2 = int(input("Lütfen not 2 giriniz:"))
#     o = Ogrenci(ad, nt1, nt2)

# for i in Ogrenci.ogrenciNotlari:
#     print(i)

# class Araba:
#     def __init__(self, marka , model , renk) -> None:
#         self.marka=marka
#         self.model=model
#         self.renk=renk
    
#     def __str__(self) -> str:
#         return f"Arkadaşımın {self.marka}'si  {self.model} modeldir. Ve rengi {self.renk}'dır"
    
#     def BilgiVer(self):
#         return f"{self.marka} {self.model} {self.renk} "

# a=Araba("BMW" , 2022, "mavi")
# print(a)

