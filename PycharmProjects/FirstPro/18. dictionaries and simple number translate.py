customer = {
    "name": "John Smith",
    "age" : 30,
    "is_verified": True
}
print(customer["name"])
customer["name"]= "Jack Smith"
print(customer["name"])
print(customer.get("birthdate", "Jun 20, 2000"))

#Number to word converter program
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


#Emoji converter
message = input("->")
words = message.split(' ')
emojis = {
#emoji windows + >
    ":)":"😃",
    ":(":"😒"
}
result = ""
for word in words:
    result += emojis.get(word, word) + " "
print(result)