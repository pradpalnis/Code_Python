is_hot = False
if(is_hot):
    print("Drink more water")
else:
    print("All good")
print("Thank you !!!")    


is_hot = False
is_cold = True
if(is_hot):
    print("Drink more water")
elif(is_cold):
    print("Drink Hot Water")
else:
    print("All good")

print("Thank you !!!")    



secret_num = 9 
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guessed_num = int(input("Guess the number "))

    if(secret_num == guessed_num):
        print("You Won!!!")
        break
    guess_count+=1


while True:
    break 


for item in 'python':
    print(item)

for item in ['Atom' , 'Nucleus', 'Photon']:
    print(item)


for item in range(5):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,15,2):
    print(item)    


prices = [ 10 , 20 ,30 ]

total = 0
for item in prices:
    total += item
print("Total " + str(total))
print(f" or Total {total}")


for x in range(4):
    for y in range(4):
        print(f"{x,y}")


numbers = [5,2,5,2,2]

for num in numbers:
    str = ''
    for x in range(num):
        str+= 'x'
    print(str)
