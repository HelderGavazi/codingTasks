"""
hyperiondev - Software Engineering (Fundamentals)
Task 4 - "Iteration"
Author: Helder P - HP24010013265
Date: 21/03/2024

Practical Task 1 - "while.py"

Follow these steps:
● Create a file called while.py.
● Write a program that continually asks the user to enter a number.
● When the user enters “-1”, the program should stop requesting the user to enter a number,
● The program must then calculate the average of the numbers entered, excluding the -1.
● Make use of the while loop repetition structure to implement the program.
"""

# Initialize variables
total = 0
count = 0

# Continually ask the user for input until -1 is entered
while True:
    number = input("Please enter a number: ")
    
    # Check if the input is "-1" to stop the loop
    if number == "-1":
        break
        
    # Convert the input to a float
    try:
        number = float(number)

    # If invalid input entered, requests for a valid number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Add the number to the total and increment the count 
    total += number
    count += 1

# Calculate the average of the numbers
if count > 0:
    average = total / count
    print(f"The average of the numbers entered is: {average} (excluding -1)")

else:
    # If no numbers were entered
    print("No numbers were entered.")
