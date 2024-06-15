"""
hyperiondev - Software Engineering (Fundamentals)
Task 4 - "Iteration"
Author: Helder P - HP24010013265
Date: 21/03/2024

Practical Task 2 - "pattern.py"
"""

# Define the maximum number of stars in a row
max_stars = 5

# Iterate from 1 to max_stars*2-1
for i in range(1, max_stars * 2):
    # Calculate the number of stars for this row
    if i <= max_stars:
        num_stars = i
    else:
       num_stars = max_stars * 2 - i
    
    # Print the stars for this row
    print('*' * num_stars)
