"""
Filename: file_handling_and_lambdas_practice.py
Topics Covered:
  File Pointers (seek, tell, truncate)
  Lambda Functions & Ternary Operators
  Higher-Order Functions (map, filter)
  Object Identity vs Equality (is vs ==)
"""

import os

# ==========================================
# DAY 51: seek(), tell(), and truncate()
# ==========================================
def run_day_51():
    print("--- Day 51: File Pointer Manipulation ---")

    # Setup temporary files for testing
    with open("data.txt", "w") as f:
        f.write("abcdefghij")

    with open("notes.txt", "w") as f:
        f.write("Python Programming")

    # Exercise 1: seek() & tell()
    print("\n[Exercise 1: seek & tell]")
    with open("data.txt", "r") as f:
        f.seek(3)
        print(f"Cursor position: {f.tell()}")
        remaining_content = f.read()
        print(f"Remaining text: {remaining_content}")

    # Exercise 2: truncate() & pointer reset
    print("\n[Exercise 2: truncate]")
    with open("notes.txt", "r+") as f:
        f.truncate(6)  
        f.seek(0)      
        content = f.read()
        print(f"Truncated file content: {content}")

    # Cleanup temporary files
    os.remove("data.txt")
    os.remove("notes.txt")


# ==========================================
# DAY 52: Lambda Functions
# ==========================================
def run_day_52():
    print("\n--- Day 52: Lambda Functions ---")

    # Exercise 1: Check even number
    print("\n[Exercise 1: is_even]")
    is_even = lambda x: x % 2 == 0
    print(f"Is 2 even? {is_even(2)}")
    print(f"Is 3 even? {is_even(3)}")

    # Exercise 2: Max of two numbers using ternary operator
    print("\n[Exercise 2: max_two]")
    max_two = lambda a, b: a if a > b else b
    print(f"Max between two numbers: {max_two(2, 3)}")


# ==========================================
# DAY 53 & 54: map(), filter(), and 'is' vs '=='
# ==========================================
def run_day_53_and_54():
    print("\n--- Day 53: Map & Filter ---")

    # Exercise 1: Filter odd numbers and square them
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    odd_num_ext = list(filter(lambda a: a % 2 != 0, nums))
    print(f"Filtered Odd Numbers: {odd_num_ext}")

    sqr_cleaned_num = list(map(lambda b: b**2, odd_num_ext))
    print(f"Squared Odd Numbers:  {sqr_cleaned_num}")

    print("\n--- Day 54: Identity (is) vs Value (==) ---")
    
    # Exercise 2: Memory & Identity check
    x = 257
    y = 257

    p = "hello"
    q = "hello"

    print(f"x is y: {x is y} (Integers > 256 create separate objects outside cache)")
    print(f"p is q: {p is q} (Short strings are interned in memory)")


# ==========================================
# MAIN EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    run_day_51()
    run_day_52()
    run_day_53_and_54()