# region optional_arguments_default_value
"""
Namı diğer → değişken sayıda parametre gönderimi
Fonksiyonu tanımlama anında argümanlarına default değer atayabiliriz
Bu sayede, değişken sayıda argüman gönderebiliriz
a= zorunlu
b = zorunlu
c = opsiyonel
def topla(a, b, c=5):
    print(f"{a} + {b} + {c} = {a+b+c}")
topla(a=2, b=3)
"""
# endregion


# region ornek_1
"""
default argüman ve non-default argüman birlikte kullanılır mı EVET
ancak önce non-default argümanlar yazılmalı
def topla(a=2, b, c):
    print(f"{a} + {b} + {c} = {a+b+c}")
topla(b=3, c= 10)
"""
# endregion


# region ornek_2
"""
opsiyonel olmasına rağmen fonk. çağırırken değer ataması yapar isek
fonksiyonda tanımlı değeri ezer!!!!
def topla(a, b, c=5):
    print(f"{a} + {b} + {c} = {a+b+c}")
topla(a= 2, b=3, c= 10)
"""
# endregion


from curses.ascii import isdigit


def absu(a):
    if str(a).lstrip("-").isdigit():
        if a < 0:
            print(f"a sayısının mutlak değeri {-a}")
        elif a > 0:
            print(f"a sayısının mutlak değeri {a}")
        else:
            print("Lütfen sıfır haricinde bir değer giriniz.")
    else:
        print("bad operand type for abs(): 'str' ")

# absu(-8)
# absu(58)
# absu("beş")

absu(-5)


def kayitOl(tcKimlik, isim="isimsiz",eMail="@"):
    print(f"Hoş geldin {tcKimlik} {isim} {eMail}")

kayitOl(34567890)
kayitOl(34567890,"irem")
kayitOl(34567890,"irem","asdfghj@com")          
