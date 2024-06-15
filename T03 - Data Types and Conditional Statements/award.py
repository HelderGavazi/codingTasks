"""
hyperiondev - Software Engineering (Fundamentals)
Task 3 - Data Types and Conditional Statements"
Author: Helder P - HP24010013265
Date: 16/03/2024

Description: (Auto-graded) Practical Task 3 - "award.py"
"""

# Read in the times (in minutes) for swimming, cycling, and running events
swimming_time = float(input("Enter the time taken for swimming (in minutes): "))
cycling_time = float(input("Enter the time taken for cycling (in minutes): "))
running_time = float(input("Enter the time taken for running (in minutes): "))

# Calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

# Determine the award based on the total time
if total_time <= 100:
    award = "Gold Medal"
elif total_time <= 150:
    award = "Silver Medal"
elif total_time <= 200:
    award = "Bronze Medal"
else:
    award = "Participant Award"

# Display the total time taken and the award
print("Total time taken for the triathlon:", total_time, "minutes")
print("Award:", award)