"""
hyperiondev - Software Engineering (Fundamentals)
Task 8 - "IO Operations"
Author: Helder P - HP24010013265
Date: 30/03/2024

Practical Task 1 - "dob_task.py"
"""

# Open the file in read mode
with open("DOB.txt", "r") as file:
    # Initialize lists to store names and birthdates
    names = []
    birthdates = []
    
    # Iterate through each line in the file
    for line in file:
        # Split each line into name and birthdate using space as delimiter
        data = line.strip().split(' ')
        
        # Join the parts of the name (if there are more than two)
        name = ' '.join(data[:-3])
        
        # Extract the birthdate from the last three parts
        birthdate = ' '.join(data[-3:])
        
        # Append name and birthdate to their respective lists
        names.append(name)
        birthdates.append(birthdate)

# Print section header for names
print("Name: ")
# Print each name in the names list
for name in names:
    print(name)

# Print a newline for separation
print()

# Print section header for birthdates
print("Birthdate: ")
# Print each birthdate in the birthdates list
for birthdate in birthdates:
    print(birthdate)
