"""
hyperiondev - Software Engineering (Fundamentals)
Task 11 - "OOP - Inheritance"
Author: Helder P - HP24010013265
Date: 06/04/2024

Practical Task 1 - "practical_task_1.py"
"""

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        # Method to print contact website
        print("Please contact us by visiting", self.contact_website)
    
    def head_office_location(self):
        # Method to print head office location
        print("Head Office Location: Cape Town")


class OOPCourse(Course):
    def __init__(self):
        # Initialize attributes for the OOPCourse subclass
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        # Method to print course description and trainer details
        print("Course Description:", self.description)
        print("Trainer:", self.trainer)

    def show_course_id(self):
        # Method to print course ID
        print("Course ID:", "#12345")


# Creating an object of the subclass
course_1 = OOPCourse()

# Calling the methods
course_1.contact_details()  # Print contact website
course_1.head_office_location()  # Print head office location
course_1.trainer_details()  # Print course description and trainer details
course_1.show_course_id()  # Print course ID
