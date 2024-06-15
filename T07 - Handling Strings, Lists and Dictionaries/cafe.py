"""
hyperiondev - Software Engineering (Fundamentals)
Task 7 - "Handling Strings, Lists and Dictionaries"
Author: Helder P - HP24010013265
Date: 27/03/2024

Practical Task 2 - "cafe.py"
"""

# Define the menu list containing items sold in the café
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Define the stock dictionary containing the stock value for each item on the menu
stock = {"Coffee": 100, "Tea": 80, "Sandwich": 50, "Cake": 30}

# Define the price dictionary containing the prices for each item on the menu
price = {"Coffee": 2.5, "Tea": 2.0, "Sandwich": 5.0, "Cake": 3.5}

# Calculate the total stock worth in the café
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print out the result of the calculation
print("Total stock worth in the café is £", total_stock_worth)
