name="arin software"
#print(len())→→len şeklinde yazınca seçmiş olduğumuzun karakter sayısını belirtiyor.
print(len(name))
#print(name[])→→print(değişken[]-> kaçıncı karakter olduğunu göstermekte)
print(name[0])
print(name[6])
#print(name[0:8])->"0'dan 8 e kadar hepsini yazdırıyor."(ilk harf 0'dır.)
print(name[0:8])
#print(name.title())->İlk harflerini büyüttü.
print(name.title())

#print(name.upper())->Tüm harfleri büyüttü.
print(name.upper())

#print(name.lower())->Hepsini küçülttü.
print(name.lower())

#print(name.count("a"))>kaç tane a harfi olduğunu gösteri.
print(name.count("a"))
print(name.count("x"))

#print(name.find("n"))->Karekterin kaçıncı sırada olduğunu belirtiyor.
print(name.find("n"))

#print(name.replace("software","yazılım"))->parametreleri arasında değiştiriyor.
print(name.replace("software","yazılım"))

#print(dir(name))-->İlgili değişkenle ilgili kullanabileceğimiz komutları  bulabiliriz.

#print(help(str))-->String'e ait tüm komutları getiriyor(terminalde enter tusuna basarak hepsini görebiliriz.)
print(help(str))

#print(help(str.lower))-->Özel bir komut arıyorsak str.lower str.upper gibi yazabiliriz.
print(help(str.lower))















