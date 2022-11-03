# region list_arguments_giris
"""
Argüman olarak → int, float, string,tuple, gönderebiliyorum, peki
Argüman olarak → list gönderebilir miyim? Cevabı, Evet
"""
# endregion

# region ornek
"""
def ortalama(liste):
    # print(type(liste))
    tekSayilarinToplami, tekSayilarinAdedi= 0,0
    for i in liste:
        if i%2==1:
            tekSayilarinAdedi += 1
            tekSayilarinToplami += i
    return f"listedeki {tekSayilarinAdedi} adet tek sayının toplamı {tekSayilarinToplami}"
print(ortalama([3,5,7,10,11,12])) 
"""

# endregion


# def ortalama(liste):
#     tst = 0
#     tsa = 0
#     for i in liste:
#         if i % 2 != 0:
#             tst += i
#             tsa += 1
#     return (tsa, tst)


# print(ortalama([3, 8, 9, 7, 1, 3]))

# import time
# print(time.time())
# from datetime import date,datetime
# print(datetime.now())  
# print(datetime.now().timestamp())

# import time
# from datetime import datetime
# def urunKontrol(liste):
#     for i in liste:
#         cTime=time.time()
#         pTime=datetime.fromisoformat(i).timestamp()
#         if (cTime-pTime)/86400>60:
#             print(i)
        
# urunTarihleri=[
#     "2022-08-25",
#     "2022-09-26",
#     "2022-09-27",
#     "2022-09-28",
#     "2022-09-30",
#     "2022-07-30",

# ]

# urunKontrol(urunTarihleri)