"""
hyperiondev - Software Engineering (Fundamentals)
Task 7 - "Handling Strings, Lists and Dictionaries"
Author: Helder P - HP24010013265
Date: 27/03/2024

Practical Task 1 - "alternative.py"
"""

""" Test alternate_case_characters """
# Input string
input_string = "alternative character into an upper and lower case!"

# Initialize an empty string to store the altered string
altered_string = ''

# Iterate over each character in the input string
for i in range(len(input_string)):
    # Check if the index is even
    if i % 2 == 0:
        # If the index is even, convert the character to uppercase and append to the altered string
        altered_string += input_string[i].upper()
    else:
        # If the index is odd, convert the character to lowercase and append to the altered string
        altered_string += input_string[i].lower()

# Print the altered string
print(altered_string, "\n")


""" Test alternate_case_words """
# Input string
input_string = "Making each alternative word lower and upper case!"

# Split the input string into words
words = input_string.split()

# List to store altered words
altered_words = []

# Iterate over each word and alternately convert to lowercase and uppercase
for i, word in enumerate(words):
    if i % 2 == 0:  # Check if the index is even
        altered_words.append(word.lower())  # Convert word to lowercase
    else:
        altered_words.append(word.upper())  # Convert word to uppercase

# Join the altered words back into a string with spaces in between
altered_string = ' '.join(altered_words)

# Print the altered string
print(altered_string, "\n")
