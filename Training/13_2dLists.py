matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])
matrix[0][1] = 12
print(matrix[0][1])
matrix[0][1] = 2

for row in matrix:
    for item in row:
        print(item)