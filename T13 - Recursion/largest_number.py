"""
hyperiondev - Software Engineering (Fundamentals)
Task 13 - "Recursion"
Author: Helder P - HP24010013265
Date: 17/04/2024

Description: Practical Task 2 - "largest_number.py"
"""

def largest_number(lst):
    # Base case: if the list has only one element, return that element
    if len(lst) == 1:
        return lst[0]
    else:
        # Recursive case: compare the first element with the largest element of the rest of the list
        return max(lst[0], largest_number(lst[1:]))

# Test cases
print(largest_number([1, 4, 5, 3]))              # Output: 5
print(largest_number([3, 1, 6, 8, 2, 4, 5]))    # Output: 8
