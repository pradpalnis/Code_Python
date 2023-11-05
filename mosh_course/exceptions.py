age = int(input("Age: ")) #ValueError: invalid literal for int() with base 10: 'er'
print(age)


try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")    


try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero ")    
except ValueError:
    print("Invalid value")        
