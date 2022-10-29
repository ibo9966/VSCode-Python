"""
ÖDEV 1 : 
"""

# age=int(input("Lütfen yaş giriniz:\t"))

# if age<18 or age >40 :
#     print("Pariye giremezsiniz.")
# else:
#     print("Hoş geldiniz!!!!")

"""
ÖDEV 2

"""
# nameSurn=input("Lütfen kullanıcı adı şifre giriniz:\t ")
# if nameSurn==nameSurn.title():
#     print("Tamam")
# else:
#     print("Tamam değil")


"""
ÖDEV 3 
"""


# from curses.ascii import isalnum

# sayi1=(input("Lütfen 1.sayı değerini giriniz:\t"))
# sayi2=(input("Lütfen 2.sayı değerini giriniz:\t"))
# if sayi1.isdigit() and sayi2.isdigit():
#     print(f"Sayı1 ve sayı2 'nin toplamı → {int(sayi1)+int(sayi2)}" )
# else:
#     print("Lütfen sayısal değer giriniz.")

#else yerine aşağıdaki ifadeyide kullanbilirsin.
# elif sayi1.isalnum() or sayi2.isalnum():


"""
ÖDEV 4
"""
# className=[]
# classAve=[]
# while True:
#     i=0
#     studentName=input("Lütfen ogrenci adi giriniz, cikmak icin 00 yaziniz:\t")
#     if studentName == "00" :
#         print("Tekrar bekleriz.")
#         break
#     note1 = int(input("Birinci ders notunuzu giriniz:\t")) 
#     note2 = int(input("ikinci ders notunuzu giriniz:\t"))
#     ave = (note1 + note2)/2
#     i+=1
#     className.append(studentName)
#     classAve.append(ave)
#     if ave>=50 :
#         print("gecti")
#     elif 0<=ave<50 : 
#         print("kaldı")
#     else : 
#         print("Sınav notunuzu 100-0 arasında giriniz")
# for i in range(0,len(className)):
#     print(f"{className[i]} isimli öğrencinin nor ortalaması {classAve[i]} dir.")


"""
ÖDEV5
"""

# sayi=int(input("Lütfen sayı giriniz:\t"))
# if sayi >0:
#     print("Sayı poziftir.")
# elif sayi<0:
#     print("Sayi negatiftir.")
# else:
#     print("Sayı sıfıra eşittir.")

"""
ÖDEV6

"""

# secim=input("Lütfen seçim yapınız Sinema seçmek isterseniz S tiyatro seçmek isterseniz T yazınız:   ")
# if secim =="S":
#     print("Sinema seçimi yaptınız iyi  seyirler.")
# elif secim =="T":
#     print("Tiyatro seçimi yaptınız iyi  seyirler.")
# else:
#     print("Hataalı seçim  yaptınız . Tekrar deneyiniz.")

# from ctypes.wintypes import RGB
# import colorama
# from colorama import Fore

# lol=["akali" , "nami" , "lulu"]
# print(lol)
# print(Fore.RED + lol[0],Fore.YELLOW +lol[1] ,Fore.BLUE + lol[2])
