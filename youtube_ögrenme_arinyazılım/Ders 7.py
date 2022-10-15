cities=["barcelona","floransa","moskova","belgrad","tahran"]
print(cities)
print(cities[0])
print(len(cities))
print(cities[4])
print(cities[-1])
print(cities[-2])
print(cities[0:2])
print(cities[0:4])
print(cities[0:-1])
cities=["barcelona","floransa","moskova","belgrad","tahran"]
#aşağıdaki cities[0] yazması ile tekrar bir tanımla yapacağımızı açıkladık ve barcelona yerine tiflis olmuştur
cities[0]="tiflis"
print(cities)

cities=["barcelona","floransa","moskova","belgrad","tahran"]
print(cities)
#.append listenin sonuna ifade ettiğimiz terimi yazar.
cities.append("beyoğlu")
print(cities)
#.insert ( ) istediğimiz liste sırasını ve ne yazacağımızı belirtiyoruz.
cities.insert(2,  "taksim")
print(cities)
#del cities yazarak istediğimiz index sayısını yazıyoruz ve siliyoruz ama del kullanınca tekrar sildiğimize ulaşamıyoruz.
del cities[0]
print(cities)
#pop ile sildiğimize ulaşırız

cities.pop()
print(cities)

print(cities)
cities2=cities.pop()
print(cities)
print(cities2)


####Bunun devamına çalışılacak video izlenecek