from os import remove
from secrets import choice


heroList=[]
print("URFTA HERO SEÇME UYGULAMASINA HOŞ GELDİNİZ.")
print("Çıkmak için 00 yazınız.\n\n")
while True:
    i=0
    hero=input("Lütfen hero ismi giriniz:\t")
    if hero=="00":
        print("Çıkış yaptınız.")
        break
    i+=1
    heroList.append(hero)
print(heroList)
ibo=choice(heroList)
print(f"İbo'nun herosu {ibo}")
heroList.remove(ibo)
yusuf=choice(heroList)
print(f"yusuf'nun herosu {yusuf}")
heroList.remove(yusuf)
furkan=choice(heroList)
print(f"furkanın'nun herosu {furkan}")
heroList.remove(furkan)
atakan=choice(heroList)
print(f"atakanın'nun herosu {atakan}")
heroList.remove(atakan)









# random.seed("ibo")
# print(f"İbo'nun herosu {random.choice(heroList)}")
# random.seed("fiko")
# print(f"fiko'nun herosu {random.choice(heroList)}")
# random.seed("yusuf")
# print(f"yusuf'nun herosu {random.choice(heroList)}")
# random.seed("atakan")
# print(f"atakan'nun herosu {random.choice(heroList)}")
    
