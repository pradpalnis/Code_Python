class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point() 
point1.draw()
   
point1.x = 10
print(point1.x)


point2 = Point() 
print(point2.x)


#constructors

class NewPoint:
    def __init__(self,x ,y) -> None:
        self.x = x
        self.y = y

point = NewPoint(10, 20)
print(point.x)
point.x = 11
print(point.x)


class Person:
    def __init__(self,name) -> None:
        self.name = name
    
    def talk(self):
        print(f"talk {self.name}")


person1 = Person("Tinto")        
person1.talk()
person1.name = "Bunty"
person1.talk()






