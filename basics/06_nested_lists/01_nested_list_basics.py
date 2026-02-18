# 01: Nested list basics

# A 3x3 matrix (3 rows, 3 columns)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Full matrix:", matrix)

# Accessing values
print("matrix[0][0] =", matrix[0][0])  # first row, first col
print("matrix[1][2] =", matrix[1][2])  # second row, third col

# Updating a value
matrix[2][1] = 88
print("After update matrix[2][1] = 88:", matrix)

# Loop rows
print("\nRows:")
for row in matrix:
    print(row)

# Loop each element (nested loop)
print("\nEvery element:")
for row in matrix:
    for value in row:
        print(value, end=" ")
print()

# Add a new row
matrix.append([10, 11, 12])
print("\nAfter append row:", matrix)
