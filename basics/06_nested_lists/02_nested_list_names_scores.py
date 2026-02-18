# 02: HackerRank-style Nested Lists problem
# Problem: Print names of students who have the second lowest score (alphabetical order)

# Step 1: Read number of students
n = int(input().strip())
# - input().strip() gets input and removes extra whitespace/newline
# - int() converts string "5" -> number 5
# - store in variable n

# Step 2: Create empty list to store all student records
records = []
# This will hold nested lists like: [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2]]

# Step 3: Loop N times to read each student's data
for _ in range(n):
    # "_" means we don't need the loop counter value, just repeat n times
    
    # Read student name (one line)
    name = input().strip()
    # Example: if user types "Harry  \n", strip() makes it "Harry"
    
    # Read student score (next line)
    score = float(input().strip())
    # float() converts "37.21" -> 37.21 (decimal number)
    # Use float for scores that can have decimals
    
    # Add [name, score] as a nested list into records
    records.append([name, score])
    # After 3 students: records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2]]

# Step 4: Extract unique sorted scores
scores = sorted(set(score for _, score in records))
# Breaking down this complex line:
# 
# 1. "for _, score in records" 
#    - Loop through records
#    - Unpack each [name, score] pair
#    - "_" ignores name, we only take score
#    Example: from [["Harry", 37.21], ["Tina", 37.2]]
#    -> gets [37.21, 37.2]
#
# 2. "set(...)" 
#    - Removes duplicate scores
#    Example: [37.21, 37.21, 37.2] -> {37.21, 37.2}
#
# 3. "sorted(...)"
#    - Sorts unique scores in ascending order
#    Example: {37.2, 37.21} -> [37.2, 37.21]
#
# Result: scores = [37.2, 37.21] (lowest to highest, no duplicates)

# Step 5: Check if second lowest exists
if len(scores) < 2:
    # If all students have same score, or only 1 unique score exists
    # Example: scores = [50.0] (only one unique score)
    print("NO")
else:
    # Step 6: Get the second lowest score
    second_lowest = scores[1]
    # scores[0] = lowest
    # scores[1] = second lowest
    # Example: if scores = [37.2, 37.21, 40.0]
    # second_lowest = 37.21
    
    # Step 7: Filter students with second lowest score and sort names alphabetically
    names = sorted(name for name, score in records if score == second_lowest)
    # Breaking down:
    # 
    # 1. "for name, score in records"
    #    - Loop through each [name, score] pair
    #    - Unpack both values
    #
    # 2. "if score == second_lowest"
    #    - Only keep students whose score matches second_lowest
    #    Example: from [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2]]
    #    -> keeps ["Harry", "Berry"] (both have 37.21)
    #
    # 3. "sorted(...)"
    #    - Sort names alphabetically
    #    Example: ["Harry", "Berry"] -> ["Berry", "Harry"]
    #
    # Result: names = ["Berry", "Harry"]
    
    # Step 8: Print each name on a new line
    for name in names:
        print(name)
    # Output:
    # Berry
    # Harry
