"""
hyperiondev - Software Engineering (Fundamentals)
Task 11 - "OOP - Inheritance"
Author: Helder P - HP24010013265
Date: 06/04/2024

Practical Task 2 - "method_override.py"
"""

class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        # Initialize attributes for the Adult class
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        # Method to determine if the person is old enough to drive
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def can_drive(self):
        # Method to determine if the person is too young to drive
        print(f"{self.name} is too young to drive.")

def get_non_empty_input(prompt):
    # Function to get non-empty user input
    while True:
        value = input(prompt).strip()  # Strip whitespace from input
        if value:
            return value  # Return non-empty input
        print("Input cannot be empty. Please try again.")

def get_integer_input(prompt):
    # Function to get integer user input
    while True:
        try:
            value = int(get_non_empty_input(prompt))  # Get non-empty input
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value  # Return valid integer input
        except ValueError:
            print("Please enter a valid integer.")  # Handle invalid input

# Take user inputs with validation
name = get_non_empty_input("Enter name: ")  # Get non-empty name input

age = get_integer_input("Enter age: ")  # Get integer age input

hair_colour = get_non_empty_input("Enter hair colour: ")  # Get non-empty hair colour input
eye_colour = get_non_empty_input("Enter eye colour: ")  # Get non-empty eye colour input

# Check if person is 18 or older
if age >= 18:
    # Create an instance of Adult class if the person is an adult
    person = Adult(name, age, hair_colour, eye_colour)
else:
    # Create an instance of Child class if the person is a child
    person = Child(name, age, hair_colour, eye_colour)

# Call the can_drive() method
person.can_drive()
