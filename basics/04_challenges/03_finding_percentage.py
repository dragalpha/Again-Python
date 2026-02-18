# HackerRank: Finding the Percentage
# Problem: Store student marks in a dictionary, then print average for a queried student

# Step 1: Read number of students
n = int(input())
# Example: if input is "3", n = 3

# Step 2: Create empty dictionary to store student data
student_marks = {}
# Dictionary structure will be:
# {
#   "Harry": [20.0, 30.0, 40.0],
#   "Berry": [50.0, 60.0, 70.0],
#   "Tina": [10.0, 20.0, 30.0]
# }

# Step 3: Read N students' data (name + 3 marks per line)
for _ in range(n):
    # Read one line like: "Harry 20 30 40"
    # Split it into parts: ["Harry", "20", "30", "40"]
    
    # IMPORTANT: *line is advanced unpacking
    name, *line = input().split()
    # How this works:
    # - input().split() gives ["Harry", "20", "30", "40"]
    # - "name" gets first item: "Harry"
    # - "*line" gets ALL remaining items: ["20", "30", "40"]
    #
    # This is called "unpacking with *"
    # The * collects all leftovers into a list
    
    # Convert string marks to float numbers
    scores = list(map(float, line))
    # line = ["20", "30", "40"]
    # map(float, line) converts each to float
    # list(...) stores it: [20.0, 30.0, 40.0]
    
    # Store in dictionary: name as key, scores as value
    student_marks[name] = scores
    # After first iteration: student_marks = {"Harry": [20.0, 30.0, 40.0]}

# Step 4: Read the query name
query_name = input()
# Example: "Berry"

# Step 5: Get marks for the queried student
marks = student_marks[query_name]
# If query_name = "Berry" and student_marks = {"Berry": [50.0, 60.0, 70.0]}
# Then marks = [50.0, 60.0, 70.0]

# Step 6: Calculate average
average = sum(marks) / len(marks)
# sum(marks) = 50.0 + 60.0 + 70.0 = 180.0
# len(marks) = 3
# average = 180.0 / 3 = 60.0

# Step 7: Print average with exactly 2 decimal places
print(f"{average:.2f}")
# Format explanation:
# f"..." = f-string (formatted string)
# {average:.2f} means:
#   - average = the variable
#   - : = start format spec
#   - .2f = 2 decimal places, float format
#
# Examples:
# 60.0 -> "60.00"
# 50.666666 -> "50.67" (rounds)
# 37.5 -> "37.50"
