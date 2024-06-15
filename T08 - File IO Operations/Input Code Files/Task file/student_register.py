"""
hyperiondev - Software Engineering (Fundamentals)
Task 8 - "IO Operations"
Author: Helder P - HP24010013265
Date: 02/04/2024

Practical Task 2 - "studen_register.py"
"""
import os


def register_students():
    print("\nWelcome to the Students Registration Portal! \n")
    # Ask the user how many students are registering
    while True:
        try:  # Convert user input to an integer to determine the number of students
            num_students = int(input("How many students are registering? "))
            if num_students <= 0:  # Check if the number of students is positive
                print("Please enter a positive integer.")
            else:  # Exit the loop if the input is valid
                break
        # Handle the case where the user inputs a value that cannot be converted to an integer
        except ValueError: 
            print("Please enter a valid integer.")

    # Create an empty set to store student IDs (to ensure uniqueness)
    student_ids = set()

    # Create a for loop that runs for the number of students
    for i in range(num_students):
        while True:
            # Ask the user to enter the next student ID number
            student_id = input(f"Enter student ID number for student {i+1}: ")
            if student_id in student_ids:
                print("Student ID already exists...\n")
            else:
                student_ids.add(student_id)
                break  # Exit the loop if the entered ID is unique

    # Check if the file reg_form.txt already exists
    if os.path.exists("reg_form.txt"):
        # Read existing student IDs from the file
        with open("reg_form.txt", "r") as file:
            existing_ids = set(file.read().splitlines())

        # Add new student IDs if they are not already in the existing set
        student_ids = student_ids.union(existing_ids)

    # Write student IDs to the text file with dotted lines
    with open("reg_form.txt", "w") as file:
        for student_id in student_ids:
            file.write(student_id + "\n")
            file.write("-" * len(student_id) + "\n")  # Dotted line after each ID

    print("\nRegistration form updated successfully.\n")

# Call the function to run the program
register_students()
