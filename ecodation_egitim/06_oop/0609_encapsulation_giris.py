"""
capsulation / encapsulation
capsulation : bir classtaki üye elemanları (metod, propertie, field) → private yaparak kapatmak
kendi class'ından veya dışardan erişimi izin verilecek/verilmeyecek kavramıdır
encapsulation: bu kapsulun açılma anıdır
"""


class Ogrenci:
    def __init__(self, ad , soyad , tc , sinif) -> None:
        self.ad=ad
        self.soyad=soyad
        self.tc=tc
        self.__sinif=sinif

 
    def setSinif(self,arg):
        if 8 <arg < 13:
            self.__sinif=arg
        else:
            self.__sinif=-1
            print("HATALI VERİLER MEVCUTTUR.")

    def getSinif(self):
        return self.__sinif

    def __str__(self) -> str:
        if self.getSinif()==-1:
            return "üzgünüm!!! sınıf seviyesi [9-12] dışında olamaz"
        return f"{self.ad} {self.soyad} {self.tc} {self.__sinif} "

o=Ogrenci("Ali" , "Kemal" , 12345, 10)
#o.__sinif="4-B" →→→→→→ bu bir hata , private attribute e böyle erişemezsin setter fonk. ile erişebilirsin.
o.setSinif(15)
print(o)

