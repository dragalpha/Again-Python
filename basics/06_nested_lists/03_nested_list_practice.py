# 03: Practice (with simple answers)

# Exercise 1:
# Given this nested list, print only the value 50
arr = [[10, 20], [30, 40], [50, 60]]
print("Exercise 1 answer:", arr[2][0])

# Exercise 2:
# Update 40 -> 99 and print list
arr[1][1] = 99
print("Exercise 2 answer:", arr)

# Exercise 3:
# Print sum of all values in nested list
nums = [[1, 2, 3], [4, 5], [6]]
total = 0
for row in nums:
    for value in row:
        total += value
print("Exercise 3 answer:", total)

# Exercise 4:
# Count how many odd numbers are present
odd_count = 0
for row in nums:
    for value in row:
        if value % 2 == 1:
            odd_count += 1
print("Exercise 4 answer:", odd_count)
