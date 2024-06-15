"""
hyperiondev - Software Engineering (Fundamentals)
Task 3 - Data Types and Conditional Statements"
Author: Helder P - HP24010013265
Date: 16/03/2024

Description: (Auto-graded) Practical Task 1 - "manipulation.py"
"""

# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Calculate and display the length of str_manip
print("Length of the sentence:", len(str_manip))

# Find the last letter in str_manip sentence
last_letter = str_manip[-1]

# Replace every occurrence of this letter in str_manip with '@'
str_manip_modified = str_manip.replace(last_letter, '@')

# Print the modified sentence
print("Modified sentence:", str_manip_modified)

# Print the last three characters in str_manip backwards
print("Last three characters backwards:", str_manip[-1:-4:-1])

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", five_letter_word)
