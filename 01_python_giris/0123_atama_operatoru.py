#region atama_operatoru
"""
name = "Jhon"
print(name)
"""
#endregion

#region round
"""
s = 1.838983121212
print(round(s, 3))
"""
kg = 80
mt = 1.60
vki = kg/mt**2
print(round(vki, 2))
#endregion

#region sonucu_yine_kendi_degerine_atama
"""
i = 1
print(i)
i = i + 1
print(i)
sayi = 10
sayi = sayi - 1
sayi = sayi * 2
x=10
x = x + 1
print(sayi)
print(x)
"""
#endregion

#region az_sayida_degisken_kullanma
"""
sayi = 5
toplam = 0
toplam = toplam + sayi
sayi = 10
sayi = sayi + 1
toplam = toplam + sayi
"""
#endregion

# Atama operatörü = (eşittir)
# name = "jhon"
# print(name)

#region vki
# #80 kg -1.68 boy vki=? (vki=(kg/m**2))

# kg = 80
# boy= 1.68
# vki=((kg/(boy**2)))
# print("vki" , round(vki,2))
#endregion vki

#region i 

# i 'nin değerini 1 artır
i = 1 
i = i +1
print("i" , i)

#endregion i 

#80 kg 1.68 boy vki= kg/m**2 vki=?

kg=80
boy=1.68
vki=(80/(1.68)**2)
print("vki " ,round(vki , 2 ))




i=int(input("sayı değeri giriniz."))
if(i<5):
    print("i 4 ten küçüktür")
else:
    print("i 4 den büyük")



