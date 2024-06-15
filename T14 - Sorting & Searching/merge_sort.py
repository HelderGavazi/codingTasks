"""
hyperiondev - Software Engineering (Fundamentals)
Task 14 - "Sorting and Searching"
Author: Helder P - HP24010013265
Date: 30/03/2024

Description: (Auto-graded) Practical Task 2 - "merge_sort.py"
"""

def merge_sort(strings):
    if len(strings) <= 1:
        return strings

    # Split the list into two halves
    middle = len(strings) // 2
    left_half = strings[:middle]
    right_half = strings[middle:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Merge the two lists while sorting by string length
    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) >= len(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add remaining elements from left list
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Add remaining elements from right list
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

# Example usage
if __name__ == "__main__":
    # Example lists of strings
    list1 = ["banana", "apple", "orange", "strawberry", "blueberry", "kiwi", "pineapple", "grape", "peach", "mango"]
    list2 = ["python", "java", "c", "javascript", "ruby", "php", "swift", "kotlin", "typescript", "rust"]
    list3 = ["elephant", "giraffe", "lion", "tiger", "zebra", "rhinoceros", "hippopotamus", "cheetah", "leopard", "kangaroo"]

    # Run merge sort on each list
    sorted_list1 = merge_sort(list1)
    sorted_list2 = merge_sort(list2)
    sorted_list3 = merge_sort(list3)

    # Print sorted lists
    print("Sorted List 1:", sorted_list1)
    print("Sorted List 2:", sorted_list2)
    print("Sorted List 3:", sorted_list3)
