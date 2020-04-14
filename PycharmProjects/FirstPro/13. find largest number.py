numbers = [3,5,6,8,9,90,1,5,80]
max = numbers[0]

#Maximum Number
for number in numbers:
    if number>max:
        max = number
print(f"Largest Number is {max} ")

#Minimum Number
for number in numbers:
    if number<max:
        max = number
print(f"Smallest Number is {max} ")