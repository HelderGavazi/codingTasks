"""
hyperiondev - Software Engineering (Fundamentals)
Task 14 - "Sorting and Searching"
Author: Helder P - HP24010013265
Date: 30/03/2024

Description: (Auto-graded) Practical Task 3 - "sort_and_search.py"
"""

def linear_search(arr, target):
    """
    Linear search algorithm to find the target in the array.
    Returns the index of the target if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def insertion_sort(arr):
    """
    Insertion sort algorithm to sort the array in ascending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Given array
arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Search for the number 9 using Linear Search
target = 9
index = linear_search(arr, target)
if index != -1:
    print(f"Linear Search: {target} found at index {index}")
else:
    print(f"Linear Search: {target} not found")

# Sort the array using Insertion Sort
sorted_arr = insertion_sort(arr.copy())
print("Sorted Array using Insertion Sort:", sorted_arr)

# Implementing Binary Search on the sorted array
def binary_search(arr, target):
    """
    Binary search algorithm to find the target in the sorted array.
    Returns the index of the target if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Search for the number 9 using Binary Search on the sorted array
index = binary_search(sorted_arr, target)
if index != -1:
    print(f"Binary Search: {target} found at index {index}")
else:
    print(f"Binary Search: {target} not found")
