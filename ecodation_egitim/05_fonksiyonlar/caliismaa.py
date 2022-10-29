kullanicilar=[]
uye={
    "ad":"",
    "soyad":"",
    "yas":0
    
}
def degerAl():
    while True:
        ad=input("Lütfen adınızı giriniz, çıkmak için 00 basınız:\t")
        if ad=="00":
            break
        soyad=input("Lütfen soyadınızı giriniz:\t")
        yas=(input("Lütfen yaşınızı giriniz:\t"))
        uye={
            "ad":ad,
            "soyad":soyad,
            "yas":yas
        }
        kullanicilar.append(uye)
    return kullanicilar

def listele():
    degerAl()
    for i in kullanicilar:
        print(i)
listele()

