#condition

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Waer warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment: ${down_payment}")



has_high_income = False
has_good_credit = True
#if has_high_income and has_good_credit:
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


temperature = 30
if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = "Johm Smith"
if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")