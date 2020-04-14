#program 1
for x in range(5):
    for y in range(4):
        for z in range(3):
            print(f"({x}, {y}, {z})")


#program 2
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print("X" * x_count)

print("another system")
numbers1 = [5, 2, 5, 2, 2]
for x_count1 in numbers1:
    output = ''
    for count in range(x_count1):
        output +='x'
    print(output)