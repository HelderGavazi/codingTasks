"""
hyperiondev - Software Engineering (Fundamentals)
Task 2 - Getting Started with Your Bootcamp

Author: Helder P - HP24010013265
Date: 13/03/2024

Description:  Practical Task 3 - "details.py"
"""

# Get user details
name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

# Concatenate user details into a single sentence
details_sentence = f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}."

# Print the sentence
print(details_sentence)