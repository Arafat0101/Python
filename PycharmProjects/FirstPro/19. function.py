#define function
def greet_user():
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user()
print("Finish")

#parameter pass in function
def new_function(first_name, last_name):
    print(f"hello {first_name} {last_name}")
    print("how are you?")


print("start parameter pass")
new_function("Arafat", "Yasir")
new_function("Yasir", "Arafat")


#keyword arguments
def new_function1(first_name, last_name):
    print(f"hello {first_name} {last_name}")
    print("how are you?")


print("start keyword argument pass")
new_function1(last_name= "Arafat", first_name="Yasir")
new_function1(first_name="Yasir", last_name="Arafat")


#return statement
def square(number):
    return number*number


result = square(3)
print(result)


#creating a reusable function
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😃",
        ":(": "😒"
    }
    result1 = ""
    for word in words:
        result1 += emojis.get(word, word) + " "
    return result1


message = input("->")
print(emoji_converter(message))