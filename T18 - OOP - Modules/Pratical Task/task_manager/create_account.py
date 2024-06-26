""" /create_account.py"""

from objects import Employee, AdminUser


def create_user_account(app):
    """Prompt the user to create a new account, either as an Employee or Admin.

    Args:
        app: An object containing the application context,
             including the current user and method to display the menu.
    """
    while True:
        user_level = input(
            """Which account would you like to create? (Enter 1 or 2)
                            1. Employee account 
                            2. Admin account
                            """
        )
        if user_level not in ["1", "2"]:
            print("Invalid input. Please try again.")
            continue

        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")

        # Check if email already exists in employees or admins file
        if is_email_registered(email):
            print("Email already exists. Would you like to:")
            print("1. Log in")
            print("2. Enter another email")
            choice = input()
            if choice == "1":
                login.login(app)
                return
            elif choice == "2":
                continue  # Restart account creation process
            else:
                print("Invalid input. Returning to main menu.")
                app.display_menu()
                return

        password = input("Enter a password: ")

        if user_level == "1":
            new_user = Employee(first_name, last_name, email, password)
            create_employee_account(app, new_user)
            break
        elif user_level == "2":
            new_user = AdminUser(first_name, last_name, email, password)
            create_admin_account(app, new_user)
            break


def is_email_registered(email):
    """Check if the given email is already registered in either the employees or admins file.

    Args:
        email (str): The email address to check.

    Returns:
        bool: True if the email is found in either file, False otherwise.
    """
    try:
        with open("all_employees.txt", "r") as emp_file:
            for line in emp_file:
                if email == line.strip().split(",")[2]:
                    return True
    except FileNotFoundError:
        pass

    try:
        with open("all_admin.txt", "r") as admin_file:
            for line in admin_file:
                if email == line.strip().split(",")[2]:
                    return True
    except FileNotFoundError:
        pass

    return False


def create_employee_account(app, new_user):
    """Create a new employee account and log in the user.

    Args:
        app: An object containing the application context,
             including the current user.
        new_user (Employee): The new Employee object to be created.
    """
    with open("all_employees.txt", "a") as file:
        file.write(
            f"{new_user.first_name},{new_user.last_name},{new_user.email},{new_user.password}\n"
        )
    app.current_user = new_user
    print("Employee account created and logged in successfully!")


def create_admin_account(app, new_user):
    """Create a new admin account and log in the user.

    Args:
        app: An object containing the application context,
             including the current user.
        new_user (AdminUser): The new AdminUser object to be created.
    """
    with open("all_admin.txt", "a") as file:
        file.write(
            f"{new_user.first_name},{new_user.last_name},{new_user.email},{new_user.password}\n"
        )
    app.current_user = new_user
    print("Admin account created and logged in successfully!")
