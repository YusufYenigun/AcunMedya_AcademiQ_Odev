# number=10
# print(number)

# name='Yusuf'
# print(name)
# print(type(name))
# print(1==1 and 5==5 )
# x=5
# y=2
# print(x/y)
# print("******************************")
# for i in range(5):
#     print(i)
# print("******************************")


# students=["yusf", "ali","ahmet","baris","hilmi"]
# for student in students:
#     print("Öğrenci: "+student)    
# print("******************************")

# text="merhaba"
# for letter in text:
#     print(letter)    
# print("******************************")

# for i in range (5,10):
#     print(i)
# print("******************************")

# for i in range(6,12,2):
#     print(i)
# print("******************************")

# for i in range (5,10):
#     print(i)
#     forVaraible=5    
# print(forVaraible)    #bu değeri başka bir forda da kullanabiliriz

# userInput=input("Bir degerseçin cikmak için q:")

# while userInput!="q":
#     print("Girdiğiniz deger:" +userInput)
#     userInput=input("Bir deger sec:")
# print ("Döngü bitti")

# x=10
# # while x<20:
# #     print(x)
# #     x+=1
# # print ("Döngü bitti")

# for i in range(50):
#     if i >20:
#         break
#     print(i)

# for i in range(50):
#     if i ==26:
#         continue
#     print(i)   

# age=18
# if (age>18):
#     print("Reşitsiniz")
# elif(age==18):
#     print("Sinirdan Reşitsiniz")

# else:
#     print("Reşit değilsiniz")

# logging_enabled=True
# if logging_enabled==True:
#     print("Loglaniyor...")

# price =500
# total_price=price+(price*0.2)
# print(total_price)


# def calculate_tax(price , rate=20): #rate parametersini normal parametreden sonra yazılır
#     return price+ (price*(rate/100))
    

# price1= calculate_tax(100)
# price2=calculate_tax(200)    
# price3=calculate_tax(300,25)
# price4=calculate_tax(1000,50)

# print(price1+price4)

# def topla(*args):
#     if len(args)<=0:
#         print("En az 1 eleman yazılması gerekiyor")
#     sonuc=0
#     for sayi in args:
#         sonuc+=sayi
#     return sonuc

# print(topla(1,2))
# print(topla(20,30,50,90))
# print(topla())

topla =lambda a,b :a+b
print(topla(5,10))