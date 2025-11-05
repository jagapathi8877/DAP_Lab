
def find_largest_number(numbers):
    """Finds the largest number in a list."""
    
    return max(numbers)


my_numbers = [5, 12, 4, 86, 23, 7]
largest = find_largest_number(my_numbers)
print(f"The list is: {my_numbers}")
print(f"The largest number in the list is: {largest}")