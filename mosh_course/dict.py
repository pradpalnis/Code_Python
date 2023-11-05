#key, value - Key unique


customer = {
    "name" : "John",
    "age":30,
    "is_verfied": True 
}

customer["name"] = "Jack"

print(customer["name"])
print(customer.get("name"))
print(customer.get("birth"))


message = input(">")
words = message.split(" ")
emojis = {
    ":)":"😀",
    ":(":"🥹"
}

output=""
for word in words:
    output += emojis.get(word, word) + " " # second parm is default, if ket not found use default

print(output)    
