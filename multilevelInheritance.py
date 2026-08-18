
class grandpa():
    def land(self):
        print("Grandpa's Land")

class dad(grandpa):
    def phone(self):
        print("Dad's phone")

class son(dad):
    def laptop(self):
        print("son laptop")

s1=son()
s1.land()
s1.phone()
s1.laptop()