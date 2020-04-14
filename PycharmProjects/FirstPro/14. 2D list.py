matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(f"First row {matrix[0]}")
print(f"First row second value: {matrix[0][1]}")

matrix[0][1]=20
print(f"Replace Value {matrix[0][1]}")

for row in matrix:
    for item in row:
        print(item)
print("All number done")