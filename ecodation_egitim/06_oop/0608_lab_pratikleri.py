'''
   - User class
       - init'in içinde kulNick,kulPw vardır. Bunların gelmesi zorunludur.
       - Mainde oluşturulan her User nesnesi, UserListe'si adındaki listeye eklenmelidir.
   - Sistem class
       - init'i içinde ad vardır. Gelmesi zorunludur.
       - Login() fonksiyonuna UserListesi içinden giriş yapılacak kullanıcılar gelmektedir
       Kullanıcılarla beraber, klavyeden girilen ad,pw degerleri de gelecektir.
       - Eğer liste içinde bu ad,pw ye sahip kullanıcı varsa, Sisteme Hoşgeldiniz,
       yoksa Hatalı giriş yazacaktır.
'''


"""class Pc:
    def __init__(self, eBoyutu, eKarti, os, iTipi, ekranHafizasi) -> None:
        pass
    def __str__(self) -> str:
        pass"""

class Ders:
    derslerinToplamKredisi = 0
    def __init__(self, dKodu, ad, donem, kredisi) -> None:
        self.dKodu = dKodu
        self.ad = ad
        self.donem = donem
        self.kredisi = kredisi
        Ders.derslerinToplamKredisi += self.kredisi

    def __str__(self) -> str:
        return f"{self.dKodu}\t{self.ad}\t{self.donem}\t{self.kredisi}\t"

d1 = Ders(101, "mat.", 1, 5)
d2 = Ders(101, "fizik", 2, 4)
d3 = Ders(101, "prog.", 2, 6)
d4 = Ders(101, "fels.", 1, 2)
# print(d1)
# print(d2)
# print(d3)
dersler = [d1, d2, d3, d4]
for i in dersler:
    print(i)
print(f"\t\t\t{Ders.derslerinToplamKredisi}")

import datetime


class Araba:
    def __init__(self, marka, model, motor, yil, renk="TANIMSIZ") -> None:  # renk → default değer
        self.marka = marka
        self.model = model
        self.motor = motor
        self.yil = yil
        self.renk = renk
        self.yas = datetime.datetime.now().year - int(self.yil)

    def show(self):
        print(f"{self.marka} {self.model} {self.motor} {self.yas} {self.renk} ")


a = Araba("Hyndai", "i20", "1.2", 2016 , "siyah")
a.show()
