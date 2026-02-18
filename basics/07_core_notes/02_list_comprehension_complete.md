# List Comprehension — Complete Guide

List comprehension is a **compact way to create lists** in Python. It's faster, cleaner, and very common in coding interviews.

---

## Basic Syntax

```python
new_list = [expression for item in iterable]
```

**Equivalent to:**

```python
new_list = []
for item in iterable:
    new_list.append(expression)
```

---

## Example 1: Basic transformation

```python
# Regular loop
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension (same result)
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

## Example 2: With condition (filter)

```python
# Get only even numbers from 0 to 9
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

**Expanded form:**

```python
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
```

---

## Syntax with condition

```python
new_list = [expression for item in iterable if condition]
```

**Order matters:**
1. `expression` → what to put in list
2. `for item in iterable` → loop source
3. `if condition` → optional filter

---

## Example 3: Transform + filter

```python
# Square only the odd numbers
odd_squares = [i ** 2 for i in range(10) if i % 2 == 1]
print(odd_squares)  # [1, 9, 25, 49, 81]
```

---

## Example 4: String manipulation

```python
names = ["harry", "berry", "tina"]

# Convert to uppercase
upper_names = [name.upper() for name in names]
print(upper_names)  # ['HARRY', 'BERRY', 'TINA']

# Get names with length > 4
long_names = [name for name in names if len(name) > 4]
print(long_names)  # ['harry', 'berry']
```

---

## Example 5: Nested list comprehension

### Pattern 1: Flatten a nested list

```python
matrix = [[1, 2], [3, 4], [5, 6]]

# Flatten into one list
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

**Equivalent:**

```python
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
```

### Pattern 2: Create a matrix

```python
# Create 3x3 matrix of zeros
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## Example 6: Using multiple variables

```python
records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2]]

# Extract only names
names = [name for name, score in records]
print(names)  # ['Harry', 'Berry', 'Tina']

# Extract only scores
scores = [score for name, score in records]
print(scores)  # [37.21, 37.21, 37.2]
```

---

## Example 7: With if-else (ternary operator)

```python
# Mark even/odd
nums = [1, 2, 3, 4, 5]
labels = ["even" if i % 2 == 0 else "odd" for i in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']
```

**Note the position:**

```python
# With condition only (filter)
[i for i in nums if i % 2 == 0]

# With if-else (transform)
["even" if i % 2 == 0 else "odd" for i in nums]
```

---

## Example 8: Common interview patterns

### Pattern 1: Filter and transform

```python
# Get squares of positive numbers only
nums = [-2, -1, 0, 1, 2, 3]
positive_squares = [x ** 2 for x in nums if x > 0]
print(positive_squares)  # [1, 4, 9]
```

### Pattern 2: Nested filtering

```python
# Get all coordinates where i + j + k != n
x, y, z, n = 1, 1, 1, 2
coords = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(coords)
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### Pattern 3: Extracting from dict

```python
students = [
    {"name": "Harry", "age": 21},
    {"name": "Berry", "age": 19},
    {"name": "Tina", "age": 21}
]

# Get names of students aged 21
names_21 = [s["name"] for s in students if s["age"] == 21]
print(names_21)  # ['Harry', 'Tina']
```

---

## When to use list comprehension

✅ **Use when:**
- One-liner logic
- Simple transformation or filter
- Need a new list from existing iterable
- Improves readability

❌ **Avoid when:**
- Complex multi-step logic
- Need to debug step-by-step
- Multiple nested loops (gets hard to read)

---

## Common mistakes

### 1. Missing brackets

```python
# Wrong (generator, not list)
result = (i for i in range(5))

# Correct
result = [i for i in range(5)]
```

### 2. Wrong if-else position

```python
# Wrong
result = [i for i in range(10) if i % 2 == 0 else -1]  # SyntaxError

# Correct
result = [i if i % 2 == 0 else -1 for i in range(10)]
```

### 3. Forgetting to return/store

```python
# Wrong (does nothing)
[i ** 2 for i in range(5)]

# Correct
squares = [i ** 2 for i in range(5)]
print(squares)
```

---

## Practice drills

Try writing list comprehensions for these:

1. Get all numbers divisible by 3 from 1 to 30
2. Convert `["1", "2", "3"]` to `[1, 2, 3]`
3. From `[1, 2, 3, 4]`, create `[1, 4, 9, 16]`
4. Filter words longer than 3 chars from `["hi", "hello", "bye", "world"]`
5. Flatten `[[1, 2], [3], [4, 5, 6]]` into `[1, 2, 3, 4, 5, 6]`

---

## Answers

```python
# 1
result = [i for i in range(1, 31) if i % 3 == 0]

# 2
result = [int(x) for x in ["1", "2", "3"]]

# 3
result = [i ** 2 for i in [1, 2, 3, 4]]

# 4
result = [word for word in ["hi", "hello", "bye", "world"] if len(word) > 3]

# 5
result = [num for sublist in [[1, 2], [3], [4, 5, 6]] for num in sublist]
```

---

## Speed comparison

```python
import time

# Regular loop
start = time.time()
result = []
for i in range(1000000):
    result.append(i * 2)
print(time.time() - start)  # ~0.15 seconds

# List comprehension
start = time.time()
result = [i * 2 for i in range(1000000)]
print(time.time() - start)  # ~0.08 seconds
```

List comprehension is **faster** because it's optimized at the C level inside Python.

---

Master this concept — it's in 80% of LeetCode Python solutions.