def asal_mi(x):
    if x==2 or x==3 or x==5 or x==7:
        print(f"{x} asal bir sayidir.")
    elif x%2==0 or x%3==0 or x%5==0 or x%7==0:
        print(f"{x} sayisi asal değildir.")
    else:
        print(f"{x} asal bir sayidir.")    

        
x=int(input("Bir sayi giriniz: "))
asal_mi(x)


print('*'*50)

def hesap_makinesi(sayi1,sayi2,islem):
    
    if islem =="+":
        print(f"{sayi1} + {sayi2} = {sayi1+sayi2} dir.")
    
    elif islem =="-":
        print(f"{sayi1} - {sayi2} = {sayi1-sayi2} dir.")
    
    elif islem =="*":
        print(f"{sayi1} * {sayi2} = {sayi1*sayi2} dir.")

    elif islem =="/":
        if sayi2==0:
            print("Bir sayi 0'a bölünemez...")
        else:
            print(f"{sayi1} / {sayi2} = {sayi1/sayi2} dir.")
    else:
        print("İslem düzgün girilmedi")            

sayi1= int(input("İlk sayiyi giriniz: "))
sayi2= int(input("İkinci sayiyi giriniz: "))         
islem= input("Hangi islemi yapmak istediğiniz giriniz(+ - * /): ")

hesap_makinesi(sayi1,sayi2,islem)
