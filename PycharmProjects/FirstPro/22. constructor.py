class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(10, 20)
#point1.x = 11
print(point1.x)



class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
