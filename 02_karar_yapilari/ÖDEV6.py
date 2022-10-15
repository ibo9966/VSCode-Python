# ürün_fiyatı=float(input("satın alınan ürün fiyatı:\→"))
# kargo_fiyatı= 7.5 
# if ürün_fiyatı>250 :
#     print(f"Ürünün toplam fiyatı: {ürün_fiyatı} TL ")
# if ürün_fiyatı<=250:
#     print(f"Ürünün toplam fiyatı: {ürün_fiyatı+kargo_fiyatı} TL ")
    
fiyatBilgisi = int(input("Lütfen satın aldığınız ürünlerin toplam ücretini giriniz: "))
kargoBedeli=7.5 
if fiyatBilgisi <=250 :
    fiyatBilgisi+=kargoBedeli
print(f"Ödeceğiniz tutar {fiyatBilgisi} TL dir")

