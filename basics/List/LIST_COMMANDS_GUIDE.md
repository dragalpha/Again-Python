# Python Lists: Complete Command Guide

## What is a List?
A list is like a container that holds multiple values in order. Think of it as a shopping cart where you can add, remove, or rearrange items.

```python
arr = []  # Empty list (like an empty cart)
arr = [1, 2, 3]  # List with 3 items: 1, 2, 3
```

---

## The 7 List Commands Explained

### 1. **insert i e** — Add an item at a specific position
Insert the value `e` at position `i`.

**Syntax:**
```
insert i e
```

**Example:**
```python
arr = [1, 2, 5]
# Command: insert 2 3
arr.insert(2, 3)
# Result: arr = [1, 2, 3, 5]
# Position: 0  1  2  3
```

**What it does:**
- Takes value `3` and puts it at position `2`
- Everything after position 2 shifts right
- Original: `[1, 2, 5]`
- After insert: `[1, 2, 3, 5]`

**Real-world analogy:**
Inserting a card into a deck at a specific position — all cards after it shift one spot over.

---

### 2. **print** — Display the entire list
Print shows all items in the list in order.

**Syntax:**
```
print
```

**Example:**
```python
arr = [1, 2, 3, 5]
# Command: print
print(arr)
# Output: [1, 2, 3, 5]
```

**What it does:**
- Shows the list exactly as it currently is
- Useful to verify your changes

---

### 3. **remove e** — Delete the first occurrence of a value
Remove the first item with value `e`.

**Syntax:**
```
remove e
```

**Example:**
```python
arr = [1, 2, 3, 2, 5]
# Command: remove 2
arr.remove(2)
# Result: arr = [1, 3, 2, 5]
# Only the FIRST 2 is removed
```

**What it does:**
- Searches for the value `2` in the list
- Removes the **first** occurrence (the first `2` at position 1)
- If there are duplicates, only the first is removed
- Items after the removed item shift left

**Real-world analogy:**
Removing a specific card from a deck—only the first one found is removed.

---

### 4. **append e** — Add an item to the end
Add value `e` to the end of the list.

**Syntax:**
```
append e
```

**Example:**
```python
arr = [1, 2, 3]
# Command: append 5
arr.append(5)
# Result: arr = [1, 2, 3, 5]
```

**What it does:**
- Takes value `5` and puts it at the very end
- Doesn't change any existing items
- List grows by 1

**Real-world analogy:**
Adding a new person to the back of a line.

---

### 5. **sort** — Arrange items in ascending order
Sort arranges all items from smallest to largest.

**Syntax:**
```
sort
```

**Example:**
```python
arr = [3, 1, 5, 2]
# Command: sort
arr.sort()
# Result: arr = [1, 2, 3, 5]
```

**What it does:**
- Rearranges all items in order (smallest → largest)
- Original order is lost
- Works with numbers and strings

**Real-world analogy:**
Arranging students by height from shortest to tallest.

---

### 6. **pop** — Remove the last item
Pop removes and discards the last item in the list.

**Syntax:**
```
pop
```

**Example:**
```python
arr = [1, 2, 3, 5]
# Command: pop
arr.pop()
# Result: arr = [1, 2, 3]
# The 5 (last item) is removed
```

**What it does:**
- Removes the **last** item permanently
- List shrinks by 1
- Returns the removed value (but we don't save it)

**Real-world analogy:**
Removing the last person from the back of a line.

---

### 7. **reverse** — Flip the list backwards
Reverse flips the entire list in the opposite order.

**Syntax:**
```
reverse
```

**Example:**
```python
arr = [1, 2, 3, 5]
# Command: reverse
arr.reverse()
# Result: arr = [5, 3, 2, 1]
```

**What it does:**
- The first item becomes last
- The last item becomes first
- Original order is flipped

**Real-world analogy:**
Reading a sentence backwards.

---

## Complete Working Example

**Input:**
```
6
append 1
append 2
insert 2 3
print
remove 2
print
```

**Step-by-step:**
```
Step 1: n = 6 (we'll do 6 commands)
Step 2: append 1        → arr = [1]
Step 3: append 2        → arr = [1, 2]
Step 4: insert 2 3      → arr = [1, 2, 3]  (insert 3 at position 2)
Step 5: print           → Output: [1, 2, 3]
Step 6: remove 2        → arr = [1, 3]     (remove first occurrence of 2)
Step 7: print           → Output: [1, 3]
```

**Output:**
```
[1, 2, 3]
[1, 3]
```

---

## Position Index Reminder

Positions start at **0**, not 1:

```
arr = [10, 20, 30, 40]
     Position: 0   1   2   3
```

So:
- Position 0 = `10` (first item)
- Position 1 = `20` (second item)
- Position 2 = `30` (third item)
- Position 3 = `40` (fourth item)

---

## Quick Command Cheat Sheet

| Command | Does What | Example |
|---------|-----------|---------|
| `insert i e` | Add `e` at position `i` | `insert 2 5` → Put 5 at position 2 |
| `print` | Show the list | `print` → Displays current list |
| `remove e` | Delete first occurrence of `e` | `remove 5` → Remove first 5 |
| `append e` | Add `e` to the end | `append 5` → Add 5 at the end |
| `sort` | Sort smallest to largest | `sort` → Arrange in order |
| `pop` | Remove last item | `pop` → Delete the last item |
| `reverse` | Flip the list | `reverse` → Reverse order |

---

## Try It Yourself!

Open your terminal and run:
```bash
python basics/List/list.py
```

Then test with this input:
```
5
append 10
append 20
insert 1 15
print
sort
```

Expected output:
```
[10, 15, 20]
```

---

## Common Mistakes to Avoid

❌ **Wrong:** `insert 1 2 3` (too many values)  
✅ **Correct:** `insert 1 2` (position, then value)

❌ **Wrong:** `remove` (missing the value to remove)  
✅ **Correct:** `remove 5` (which value to remove)

❌ **Wrong:** `print 1` (print doesn't take arguments)  
✅ **Correct:** `print` (no arguments)

---

You're all set! Start with small examples and build up. Good luck! 🚀
