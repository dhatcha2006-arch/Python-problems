class teacher:
    def __init__(self,n,r):
        self.name=n
        self.regno=r
    def display(self):
        print("name :",self.name)
        print("register num :",self.regno)

t1=teacher("dhatcha",1)
t2=teacher("hello",2)

t1.display()
t2.display()

