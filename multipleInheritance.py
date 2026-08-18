
class dad():
    def phone(self):
        print("Dads phone")

class mom():
    def food(self):
        print("mom cooking")

class son(dad,mom):
    def laptop(self):
        print("son laptop")

s1=son()
s1.phone()
s1.food()
s1.laptop()