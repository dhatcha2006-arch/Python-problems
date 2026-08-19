
class laptop():
    color = "black"  # class variable

    def __init__(self,brand,price):
        self.brand=brand   #Instance variable
        self.price=price
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)

    @classmethod
    def changeColor(cls):
        cls.color="white"
        print("Color changed successfully...!")
    def details(self):
        print(self.color)
        print(self.price)
        print(self.brand)

    @staticmethod
    def info():
        print("just printing")

hp = laptop("HP",20000)
hp.setPrice(100000)
hp.getPrice()
hp.changeColor()

dell = laptop("dell",22000)
dell.details()

acer = laptop("acer",30000)
acer.details()

hp.info()
