"""
hyperiondev - Software Engineering (Fundamentals)
Task 9 - "OOP & Classes"
Author: Helder P - HP24010013265
Date: 02/04/2024

Practical Task: 1 - " email simulator"
"""

class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Constructor for the Email class.

        Args:
            email_address (str): The email address of the sender.
            subject_line (str): The subject line of the email.
            email_content (str): The contents of the email.
        """
        # Initialize instance variables
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # By default, email is unread

    def mark_as_read(self):
        """
        Method to mark the email as read.
        """
        self.has_been_read = True


class EmailSimulator:
    def __init__(self):
        """
        Constructor for the EmailSimulator class.
        """
        self.inbox = []  # Initialize empty inbox

    def populate_inbox(self, email_address, subject_line, email_content):
        """
        Function to create an email object and add it to the inbox list.

        Args:
            email_address (str): The email address of the sender.
            subject_line (str): The subject line of the email.
            email_content (str): The contents of the email.
        """
        new_email = Email(email_address, subject_line, email_content)
        self.inbox.append(new_email)

    def list_emails(self):
        """
        Function to list all emails in the inbox.
        """
        print("\nYour Inbox:")
        for i, email in enumerate(self.inbox):
            print(f"{i} {email.subject_line}")

    def read_email(self, index):
        """
        Function to read a selected email from the inbox.

        Args:
            index (int): The index of the email to be read.
        """
        if 0 <= index < len(self.inbox):
            email = self.inbox[index]
            print(f"\nFrom: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print(f"Content: {email.email_content}\n")
            email.mark_as_read()  # Mark the email as read
        else:
            print("Invalid email index.")


def main():
    email_simulator = EmailSimulator()
    # Populating inbox with sample emails
    email_simulator.populate_inbox("sender@example.com", "Welcome to HyperionDev!", "This is your welcome email.")
    email_simulator.populate_inbox("another_sender@example.com", "Great work on the bootcamp!", "Keep up the good work!")
    email_simulator.populate_inbox("yet_another_sender@example.com", "Your excellent marks!", "Congratulations on your achievements!")

    while True:
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")

        choice = input("Enter your choice: ")

        if choice == "1":
            email_simulator.list_emails()
            index = int(input("Enter the index of the email you want to read: "))
            email_simulator.read_email(index)
        elif choice == "2":
            unread_emails = [email.subject_line for email in email_simulator.inbox if not email.has_been_read]
            if unread_emails:
                print("\nUnread emails:")
                for subject_line in unread_emails:
                    print(subject_line)
            else:
                print("\nNo unread emails.")
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
