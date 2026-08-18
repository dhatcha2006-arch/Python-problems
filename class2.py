class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"addition of :{a} and {b} ->",a+b)
    def sub(self):
            print(f"subraction of :{a} and {b} ->",a-b)
    def mul(self):
            print(f"multiplication of :{a} and {b} ->",a*b)
    def div(self):
            print(f"division of :{a} and {b} ->",a/b)
    def fdiv(self):
            print(f"floor divition of :{a} and {b} ->",a//b)
    def sqr(self):
            print(f"squre root of :{a} and {b} ->",a**b)

a=int(input("Enter a :"))
b=int(input("Enter b :"))

t1=calculator(a,b)

t1.add()
t1.sub()
t1.mul()
t1.div()
t1.fdiv()
t1.sqr()
