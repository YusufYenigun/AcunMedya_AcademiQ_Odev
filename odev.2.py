faiz=1.59
vade=36
krediAdi="İhtiyac"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)

faiz=str(faiz)
print(type(faiz))

vade=int(input("İstediğiniz vadeyi giriniz: "))



print(type(vade))
print("Seçtiğinia vade sonucu ortaya çikan vade "+str(vade))
print("Seçtiğinia vade sonucu ortaya çikan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim="Yusuf"
metin="merhaba {name}".format(name=isim)
print(metin)
print(f"Merhaba {isim}")


krediler = ["İhtiyaç Kredisi","Tasit Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #lengeth
#print(krediler[3]) => hata verir

dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)


krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.remove("Tasit Kredisi")
print(krediler)

krediler.extend("Y Kredisi")
print(krediler)

for i in range(10):
   print("xx")
   print(i)
print("*"*50)

for i in range(5,11):
   print(i)
   print("*"*50)

for i in range(0,51,10):
    print(i)


krediler = ["İhtiyaç Kredisi","Tasit Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*"*50)

for i in range(len(krediler)):
  print(krediler[1])


#While Döngüsü
i = 0
while i < 10:
 print("x")
 i += 1

print("y")

print("*"*50)

while True:
    print("X")
    break

print("****** Son Döngü ******")

i = 0
while i < len(krediler):

   print(i)
   print(krediler[i])
   i += 1

   if krediler[i] == "Konut Kredisi":
      break


#Fonskiyonlar 

fiyat = 100
indirim = 20

#definition define
def calculate(fiyat,indirim):
   print(fiyat-indirim)

def calculateWithParams(fiyat,indirim):
   print(fiyat - indirim)


def sayHello(name):
   print(f"Merhaba {name}")


calculate(100,20)
calculateWithParams(100,20)
calculate(50,10)
sayHello("Yusuf")
sayHello("Yenigün")


def calculateAndReturn(fiyat,indirim):
   return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)