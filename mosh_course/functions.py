def greet_user():
    print("Hello There!!")
    print("Welcome Aboard")

print("Start")
greet_user()    
print("Finish")


#parameters
def message_user(name):
    print(f"Hello There!! {name}")
    print("Welcome Aboard")


message_user("Tinto")

message_user("Mary")


#parameters
def message_user1(first_name,last_name):
    print(f"Hello There!! {first_name}  {last_name}")
    print("Welcome Aboard")

message_user1("Tinto", "bunty")

message_user1(first_name="John", last_name="Smith")


def square(numbers):
    return numbers * numbers

result = square(3)
print(result)



def display_msg(msg):
    
    words = msg.split(" ")
    emojis = {
    ":)":"😀",
    ":(":"🥹"
    }

    output=""
    for word in words:
        output += emojis.get(word, word) + " " # second parm is default, if ket not found use default
    return output        

message = input("start :")
print(display_msg(message))    




