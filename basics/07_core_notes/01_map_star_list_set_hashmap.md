# Python Core Notes: map, `*`, list, set, hashmap (dict)

This note is for interview-style coding and daily problem solving.

---

## 1) `map()` — convert/apply fast

`map(function, iterable)` applies a function to every item.

### Most common usage

```python
arr = list(map(int, input().split()))
```

Flow:
- `input()` -> string like `"1 3 5"`
- `.split()` -> `["1", "3", "5"]`
- `map(int, ...)` -> converts each to int (lazy stream)
- `list(...)` -> stores values

### Important
- `map` is an iterator in Python 3 (one-time use).
- If you consume it once, it becomes empty.

```python
m = map(int, "1 2 3".split())
print(list(m))  # [1, 2, 3]
print(list(m))  # []
```

---

## 2) `*` in Python — three common meanings

## A) Multiply

```python
print(3 * 4)  # 12
```

## B) Repeat sequence

```python
print([1] * 4)      # [1, 1, 1, 1]
print("ab" * 3)    # ababab
```

## C) Unpacking (very important)

### In function call

```python
def add(a, b, c):
    return a + b + c

nums = [2, 3, 4]
print(add(*nums))  # same as add(2, 3, 4)
```

### In function definition (`*args`)

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))
```

### Dictionary unpacking (`**kwargs`)

```python
def user(name, age):
    print(name, age)

data = {"name": "Sam", "age": 21}
user(**data)
```

---

## 3) `list` — ordered, mutable, duplicates allowed

Use when:
- order matters
- indexing needed
- duplicates allowed

```python
arr = [4, 1, 4, 2]
arr.append(9)
arr.sort()
print(arr)  # [1, 2, 4, 4, 9]
```

Common interview methods:
- `append`, `pop`, `sort`, `reverse`
- slicing: `arr[l:r]`

---

## 4) `set` — unique items, fast lookup

Use when:
- remove duplicates
- membership check fast

```python
nums = [2, 3, 3, 5, 2]
s = set(nums)
print(s)          # {2, 3, 5}
print(3 in s)     # True
```

Set ops:
- union: `a | b`
- intersection: `a & b`
- difference: `a - b`

Note:
- no index access (`s[0]` invalid)
- no guaranteed order

---

## 5) HashMap in Python = `dict`

Use when:
- key -> value mapping
- counting frequency
- fast lookup/update

```python
freq = {}
for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1

print(freq)  # {'b': 1, 'a': 3, 'n': 2}
```

Very common patterns:

```python
# seen pattern
seen = set()
for x in arr:
    if x in seen:
        print("duplicate", x)
    seen.add(x)

# index map
pos = {}
for i, x in enumerate(arr):
    pos[x] = i
```

---

## 6) List vs Set vs Dict (quick choose)

- Use `list` -> keep order + duplicates + indexing
- Use `set` -> uniqueness + membership checks
- Use `dict` -> key-value mapping + frequency counting

---

## 7) Mini drills (do now)

1. Input one line numbers and print sum using `map`.
2. Remove duplicates from list and print sorted unique values.
3. Count frequency of each number using `dict`.
4. Write `def mul(*args):` to multiply all values.
5. Given `d = {"a":1, "b":2}`, pass into function using `**d`.

---

## 8) Mistakes to avoid

- Consuming `map` twice.
- Using `set` when order/index is needed.
- Forgetting `dict.get(key, 0)` for counting.
- Confusing `*args` (tuple) and `**kwargs` (dict).

---

If you master this file, most beginner-to-intermediate coding questions become much easier.