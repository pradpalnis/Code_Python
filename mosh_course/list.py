numbers = [5, 4, 1, 7, 1]
numbers.insert(0,6)
print(numbers)
numbers.remove(4)
print(numbers)
print(numbers.index(1))
print(numbers.count(1))

print(numbers)
sorted_num = numbers.sort()
print(sorted_num)

print(numbers.reverse())
numbers.append(10)
print(numbers)


#tuple are immutable , doesnt have insert or remove , 
# if you dont want to modify the list use tuples
numbers = (1,2,3)
numbers.count(1)
numbers[1]


coordinates =  (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x)
#unpacking - same as above
x,y,z = coordinates

print(y)

