import random

print(random.random())

for i in range(3):
    print(random.randint(10,20))



members = ["Ram", "Kholi" , "Rohit"]
print(random.choice(members)    )




class Dice:
    def roll(self):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return x,y
    
dice1 = Dice()
print(dice1.roll())
print(dice1.roll())
    

