weight = int(input("Weight: "))

unit = input("(L)bs or (K)g : ")

if unit.upper()=='L':
    converted = weight*0.45
    print(f"Weight is {converted} kg")
elif unit.upper()=='K':
    converted = weight / 0.45
    print(f"Weight is {converted} pounds")
else:
    print("Invalid Unit")
