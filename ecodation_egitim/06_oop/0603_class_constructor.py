# class Memur:
#     def __init__(self, ad, soyad, derece, kademe) -> None:
#         self.ad = ad
#         self.soyad = soyad
#         self.derece = derece
#         self.kademe = kademe

#     def Yazdir(self):
#         print(f"{self.ad} {self.soyad} {self.derece} {self.kademe}")


# m = Memur("ibrahim", "kayatepe", 1, 4)
# m.Yazdir()


class Kripto:
    def __init__(self, ad, fiyat, yukselisDeger) -> None:
        self.ad = ad
        self.fiyat = fiyat
        self.yukselisDeger = yukselisDeger

    def Yazdir(self):
        print(f"{self.ad} kriptoparasının fiyatı {self.fiyat} $ % {self.yukselisDeger}")

a=Kripto("BTC", 20000, "5")
a.Yazdir()
