import random

print(random.random())

for i in range(3):
    print(random.randint(10,20))



members = ["Ram", "Kholi" , "Rohit"]
print(random.choice(members)    )





class Dice:
    def roll(self):
        self.x = random.randint(1,6)
        self.y = random.randint(1,6)
        return self
    
dice1 = Dice()
print(dice1.roll().x)
    

