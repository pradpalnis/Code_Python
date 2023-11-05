class Dog:
    def walk(self):
        print("walk")


#repeat same for cat 
class Cat:
    def walk(self):
        print("walk")      

#############----------------############


class Mammal:
    def walk(self):
        print("walk")      

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass #nothing in this class

dog1 = Dog()
dog1.walk()
dog1.bark()
