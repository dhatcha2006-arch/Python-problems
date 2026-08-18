
class a():
    def __init__(self):
        print("A")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")

obj=c()