"""
╔════════════════════════════════════════════════════════════════╗
║           HackerRank: Python Lists - BEGINNER GUIDE            ║
╚════════════════════════════════════════════════════════════════╝

WHAT IS A LIST?
- A list is a container that holds multiple values in order
- Think of it as a shopping cart where you can add/remove/rearrange items
- Example: arr = [1, 2, 3, 5]

THE 7 COMMANDS:
1. insert i e   → Add value e at position i
2. print        → Display the entire list
3. remove e     → Delete the first occurrence of value e
4. append e     → Add value e to the end of the list
5. sort         → Arrange all items from smallest to largest
6. pop          → Remove and discard the last item
7. reverse      → Flip the list backwards

EXAMPLE SESSION:
Input:
  6
  append 1
  append 2
  insert 2 3
  print
  remove 2
  print

Output:
  [1, 2, 3]
  [1, 3]
"""

if __name__ == "__main__":
    # STEP 1: Read the number of commands (n)
    # Example: if user types "5", we'll execute 5 commands
    n = int(input())
    
    # STEP 2: Create an empty list
    # arr = [] means the list starts empty (like an empty shopping cart)
    arr = []

    # STEP 3: Loop n times to read and execute n commands
    # Example: if n = 6, this loop runs 6 times
    for _ in range(n):
        # Read one line of input and split it into parts
        # Example: user types "insert 2 5" → parts = ["insert", "2", "5"]
        parts = input().strip().split()
        
        # Unpack the parts: first part is command, rest are arguments
        # cmd = "insert", args = ["2", "5"]
        # cmd = "print", args = []
        cmd, *args = parts

        # ════════════════════════════════════════════════════════
        # COMMAND 1: insert i e
        # ════════════════════════════════════════════════════════
        # PURPOSE: Add value e at position i
        # 
        # HOW IT WORKS:
        # - Position i is where you want to insert
        # - Value e is what you want to insert
        # - Everything at position i and after SHIFTS RIGHT
        #
        # EXAMPLE:
        # arr = [1, 2, 5]
        # Command: insert 2 3
        # Result: arr = [1, 2, 3, 5]
        #         pos: 0  1  2  3
        # → The value 3 is inserted at position 2
        # → The value 5 shifts from position 2 to position 3
        if cmd == "insert":
            index, value = map(int, args)
            # arr.insert(index, value) adds 'value' at position 'index'
            arr.insert(index, value)

        # ════════════════════════════════════════════════════════
        # COMMAND 2: print
        # ════════════════════════════════════════════════════════
        # PURPOSE: Display the entire list
        #
        # HOW IT WORKS:
        # - Shows all items currently in the list
        # - Useful to verify your changes
        #
        # EXAMPLE:
        # arr = [1, 2, 3, 5]
        # Command: print
        # Output: [1, 2, 3, 5]
        elif cmd == "print":
            print(arr)

        # ════════════════════════════════════════════════════════
        # COMMAND 3: remove e
        # ════════════════════════════════════════════════════════
        # PURPOSE: Delete the FIRST occurrence of value e
        #
        # HOW IT WORKS:
        # - Searches for value e in the list
        # - Removes the FIRST occurrence found
        # - If there are duplicates, only the first is removed
        # - Everything after the removed item SHIFTS LEFT
        #
        # EXAMPLE:
        # arr = [1, 2, 3, 2, 5]
        # Command: remove 2
        # Result: arr = [1, 3, 2, 5]
        # → Only the first 2 (at position 1) is removed
        # → The second 2 (at position 3) remains
        elif cmd == "remove":
            value = int(args[0])
            # arr.remove(value) removes the first occurrence of 'value'
            arr.remove(value)

        # ════════════════════════════════════════════════════════
        # COMMAND 4: append e
        # ════════════════════════════════════════════════════════
        # PURPOSE: Add value e to the END of the list
        #
        # HOW IT WORKS:
        # - Takes value e and puts it at the very end
        # - Doesn't change any existing items
        # - List grows by 1
        #
        # EXAMPLE:
        # arr = [1, 2, 3]
        # Command: append 5
        # Result: arr = [1, 2, 3, 5]
        # → 5 is added at the very end
        elif cmd == "append":
            value = int(args[0])
            # arr.append(value) adds 'value' to the end
            arr.append(value)

        # ════════════════════════════════════════════════════════
        # COMMAND 5: sort
        # ════════════════════════════════════════════════════════
        # PURPOSE: Arrange all items in order (smallest to largest)
        #
        # HOW IT WORKS:
        # - Rearranges all items from smallest to largest
        # - Original order is lost
        # - Works with numbers
        #
        # EXAMPLE:
        # arr = [3, 1, 5, 2]
        # Command: sort
        # Result: arr = [1, 2, 3, 5]
        # → All items are now in ascending order
        elif cmd == "sort":
            # arr.sort() arranges items in ascending order
            arr.sort()

        # ════════════════════════════════════════════════════════
        # COMMAND 6: pop
        # ════════════════════════════════════════════════════════
        # PURPOSE: Remove the LAST item from the list
        #
        # HOW IT WORKS:
        # - Removes the last item permanently
        # - List shrinks by 1
        # - If list is empty, it might cause an error
        #
        # EXAMPLE:
        # arr = [1, 2, 3, 5]
        # Command: pop
        # Result: arr = [1, 2, 3]
        # → The 5 (last item) is removed
        elif cmd == "pop":
            # Check if arr is NOT empty before popping
            # (to avoid errors if list is already empty)
            if arr:
                # arr.pop() removes the last item
                arr.pop()

        # ════════════════════════════════════════════════════════
        # COMMAND 7: reverse
        # ════════════════════════════════════════════════════════
        # PURPOSE: Flip the list backwards (reverse order)
        #
        # HOW IT WORKS:
        # - The first item becomes last
        # - The last item becomes first
        # - Original order is completely flipped
        #
        # EXAMPLE:
        # arr = [1, 2, 3, 5]
        # Command: reverse
        # Result: arr = [5, 3, 2, 1]
        # → Everything is flipped
        elif cmd == "reverse":
            # arr.reverse() flips the entire list
            arr.reverse()
        
        else:
            # If someone types an unknown command, ignore it
            continue


# ════════════════════════════════════════════════════════════════
# QUICK REFERENCE: POSITION INDEXING
# ════════════════════════════════════════════════════════════════
# Positions start at 0, NOT 1
#
# arr = [10, 20, 30, 40]
#       pos: 0   1   2   3
#
# - Position 0 = 10 (first item)
# - Position 1 = 20 (second item)
# - Position 2 = 30 (third item)
# - Position 3 = 40 (fourth item)
#
# For insert: "insert 2 5" means insert 5 at position 2
#            (between the current position 1 and position 2)