# 02: HackerRank-style Nested Lists problem
# Problem idea:
# - Read N students
# - Each student has [name, score]
# - Print names of students who have the second lowest score (alphabetical order)

n = int(input().strip())
records = []

for _ in range(n):
    name = input().strip()
    score = float(input().strip())
    records.append([name, score])

# Extract unique sorted scores
scores = sorted(set(score for _, score in records))

if len(scores) < 2:
    print("NO")
else:
    second_lowest = scores[1]
    names = sorted(name for name, score in records if score == second_lowest)
    for name in names:
        print(name)
