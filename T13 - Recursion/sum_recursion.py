"""
hyperiondev - Software Engineering (Fundamentals)
Task 13 - "Recursion"
Author: Helder P - HP24010013265
Date: 17/04/2024

Description: Practical Task 1 - "sum_recursion.py"
"""

def adding_up_to(lst, index):
    # Base case: if index is 0, return the value at index 0
    if index == 0:
        return lst[0]
    # Recursive case: add the value at the current index to the sum of the values up to the previous index
    else:
        return lst[index] + adding_up_to(lst, index - 1)

# Test cases
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Output: 25
print(adding_up_to([4, 3, 1, 5], 1))          # Output: 7
