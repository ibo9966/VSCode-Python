# region none_giris
"""
print(None + 2)
2→ <class int>
None <class NoneType>
"""
# endregion

# region neden_kullaniriz
"""
1. bir değişken yada objeye değeri yok demek için kullanırız
2. koşulda kontrol amaçlı kullanırız, bir değişkenin değeri var mı yok mu
# a = None
a = None
if a == None:
    print("a değişkeninde deger ataması yapılmamış")
"""
# endregion

# region degisken_tiplerinin_initial_degerleri_ile_karistirmayalim
"""
int → 0
boolean → False
string → ""
list []
"""
# endregion

# region ornek_1
"""
def ciftMi(n):
    if n%2==0:
        return True 
    #return → gizli return çalışır, yazsan da olur, yazmasan da. geriye None döner. 
print(ciftMi(13))
"""
# endregion

# region ornek_2
"""
aynı örneği birde c# ta pratik edelim
https://replit.com/
"""
# endregion


def ortalama(liste):
    tst = 0
    tsa = 0
    for i in liste:
        if i  % 2 != 0:
            tst += i
            tsa += 1
    return (tsa, tst)

print(ortalama([3, 8, 9, 7]))
