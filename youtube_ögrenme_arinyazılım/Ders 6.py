#daire cevresini ondalıklı şekilde hesaplayınız.
r=5
pi=3.14159
print(2*pi*r)
#Sayıyı ondalık sayıdan kurtarmak için ne yapmalıyız.
print(round(2*pi*r))
#sayının virgülden sonra belli bir basamagını göstersin.
print(round(2*pi*r,2))
print(round(2*pi*r,3))
print(round(2*pi*r,1))
#daire alanı hesaplayınız
#aşağıdaki 4 ü de aynı anlama gelmektedir.
print(pi*r*r)
print(pi*(r**2))
print(pi*(pow(r,2)))
import math
print(math.pi*(r**2))

x=21
if(x %2 == 0 ):
    print("x bir çift sayıdır")
else:
    print("x bir tek sayıdır.")

#Mutlak değer içerisinde sayıları abs diye belirtebiliriz.
print(abs(4-7)* (4+7))

x="welcome to python code"
print(x)
print(type(x))

#aşağıdaki 3 farklı metodda yaz.
name="Arin"
print("My name is " + name)
print("My name is {}" .format(name))
print(f"My name is {name}")

name="Arin"
Age="23"
married = True
#print isim yaş medeni hal
print(name , Age , married)

x="100"
y=50
#print(int(x-y)) --->Bu şekilde hatalı olur. Sebebi ise x i stringden inte çevirdi.
print(int(x)-y)

#kullanıcıdan ismini al (input) ve büyük küçük harfle yazdır.

my_string = input("isminiz nedir?")
print(my_string.upper())
print(my_string.lower())


