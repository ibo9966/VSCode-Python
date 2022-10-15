"""
rakamlar = [6, 2, 7, 3, 5]
Çıktı:
["ALTI", "İKİ", "YEDİ", "ÜÇ, "BEŞ"]
"""

# i=0
# rakamlar=[6, 2, 7, 3, 5]
# yazi=[" ","BİR","İKİ","ÜÇ","DÖRT","BEŞ","ALTI","YEDİ","SEKİZ","DOKUZ"]
# for i in range(0,len(rakamlar)):
#     x=int(rakamlar[i])
#     print(f"{yazi[x%10]}",end=" ")
    
 
"""
Çözülen ticket adetini ve çözen kişileri  belirten uygulama yazınız.
"""

# cozulenAdet=[]
# calisanEkip=[]
# while True:
#     i=0
#     cozenKisi=input("Lütfen ad soyad giriniz: çıkmak için 00 yazınız:\t")
#     if cozenKisi=="00":
#         print("Çıkış yaptınız.Güle güle")
#         break
#     ticketAdet=int(input("Lütfen çözülen ticket sayısınız giriniz :\t"))
#     if ticketAdet>=34:
#         print(f"{cozenKisi} Tebrik ederiz.Ticket çözme adedinden 3 puan aldınız.Devam ediniz.")
#     elif ticketAdet>=21:
#         print(f"{cozenKisi} Tebrik ederiz.Ticket çözme adedinden 2 puan aldınız.Gayret gösteriniz.")
#     elif ticketAdet>=10:
#         print(f"{cozenKisi} Tebrik ederiz.Ticket çözme adedinden 1 puan aldınız.Daha çok çalışınız")
#     elif 0<=ticketAdet<=9:
#         print(f"{cozenKisi} .Ticket çözme adedinden 0 puan aldınız.Uyarı alacaksınız.")
#     else:
#         print("Hatalı sayı girdiniz tekrar giriniz.")
#     calisanEkip.append(cozenKisi)
#     cozulenAdet.append(ticketAdet)
#     i+=1  
# for i in range(0,len(calisanEkip)):
#     if int(cozulenAdet[i])>=34:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} Tebrik ederiz.Ticket çözme adedinden 3 puan aldınız.Devam ediniz")
#     elif int(cozulenAdet[i])>=21:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} Tebrik ederiz.Ticket çözme adedinden 2 puan aldınız.Gayret gösteriniz.")
#     elif int(cozulenAdet[i])>=10:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} Tebrik ederiz.Ticket çözme adedinden 1 puan aldınız.Daha çok çalışınız")
#     elif 0<=int(cozulenAdet[i])<=9:
#         print(f"{calisanEkip[i]}→{cozulenAdet[i]}")
#         print(f"{calisanEkip[i]} .Ticket çözme adedinden 0 puan aldınız.Uyarı alacaksınız.")
#     else:
#         print("Hatalı sayı girdiniz tekrar giriniz.")



"""
ÖDEV 2

"""

sinif=[
    [1,     "Ali Kemal",        80,     50,      80],
    [2,     "Murat Çalışkan",   50,     30,      70],
    [3,     "Efe Aydın",        50,     20,      100]

]
for i in range(len(sinif)):
    for j in range(len(sinif[i])):
        print(sinif[i][j], end=" ")
    print()
print(f"{sinif[0][1]} isimli öğrencinin dönem ortalaması {((sinif[0][2])+(sinif[0][3])+(sinif[0][4]))/3}")
print(f"{sinif[1][1]} isimli öğrencinin en yüksek notu {max(sinif[1][2],sinif[1][3],sinif[1][4])}")
print(f"Matematik dersinin sınıf ortalaması {((sinif[0][2])+(sinif[1][2])+(sinif[2][2]))/3}")







"""
ÖDEV 3
meyveler = ["elma", "armut", "erik", "şeftali"]
Çıktı:
ismi e ile başlayan meyve elma
ismi e ile başlayan meyve erik
"""

# meyveler = ["elma", "armut", "erik", "şeftali"]
# for i in range (len(meyveler)):
#     if meyveler[i][0]=="e":
#         print(f"ismi e ile başlayan meyve {meyveler[i]} ")

