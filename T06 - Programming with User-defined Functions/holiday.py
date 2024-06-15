"""
hyperiondev - Software Engineering (Fundamentals)
Task 6 - "Programming with User-defined Functions"
Author: Helder P - HP24010013265
Date: 21/03/2024

Description: Practical Task 1 - "holiday.py"
"""

def hotel_cost(num_nights):
    # Assuming a hotel cost of £100 per night
    return num_nights * 100

def plane_cost(city_flight):
    # Assuming some predefined flight costs for different cities
    if city_flight == "New York":
        return 500
    elif city_flight == "Paris":
        return 700
    elif city_flight == "Tokyo":
        return 900
    else:
        return 0  # If city not found, return 0

def car_rental(rental_days):
    # Assuming a daily car rental cost of £50
    return rental_days * 50

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

if __name__ == "__main__":
    # Getting user inputs
    city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    # Calculating costs
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental_cost)

    # Printing holiday details
    print("\nHoliday Details:")
    print("City of Flight:", city_flight)
    print("Number of Nights in Hotel:", num_nights)
    print("Number of Days for Car Rental:", rental_days)
    print("Total Hotel Cost: £", total_hotel_cost)
    print("Total Plane Cost: £", total_plane_cost)
    print("Total Car Rental Cost: £", total_car_rental_cost)
    print("Total Holiday Cost: £", total_holiday_cost)
