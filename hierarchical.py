class dad():
    def cash(self):
        print("Dad's cash")

class son1(dad):
    def money1(self):
        print("Son1 money")

class son2(dad):
    pass
class son3(dad):
    pass

s1=son1()
s2=son2()
s3=son3()

s1.cash()
s2.cash()
s3.cash()
