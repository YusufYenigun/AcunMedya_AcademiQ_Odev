class Human:
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"STR Fonskiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name},is walking...")

human1 = Human("Yusuf")
human1.talk("Merhaba")
human1.walk()
print(human1)
print("*"*50)

human2 = Human("Enes")
#human2.name = "Enes"
human2.talk("Selam")
human2.walk()
print(human2)
