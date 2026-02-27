# 012 List slicing in Python
# List slicing allows you to extract a portion of a list by specifying a start index, an end index, and an optional step.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Basic slicing
print(my_list[2:5])  # Output: [3, 4, 5]

# 2. Slicing with a step
print(my_list[1:10:2])  # Output: [2, 4, 6, 8, 10]

# 3. Slicing with negative indices
print(my_list[-5:-2])  # Output: [6, 7, 8]

# 4. Slicing with negative step
print(my_list[9:0:-2])  # Output: [10, 8, 6, 4, 2]

# 5. Slicing with omitted start and end indices
print(my_list[:5])  # Output: [1, 2, 3, 4, 5]
print(my_list[5:])  # Output: [6, 7, 8, 9, 10]
print(my_list[:])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 6. Slicing with a step of -1 (reversing the list)
print(my_list[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 7. Slicing with a step of -2 (reversing the list with a step)
print(my_list[::-2])  # Output: [10, 8, 6, 4, 2]

# 8. Slicing with a step of 0 (raises an error)
# print(my_list[::0])  # This will raise a ValueError: slice step cannot be zero

# 9. Slicing with a step larger than the list length
print(my_list[::15])  # Output: [1] (only the first element is included)

# 10. Slicing with a step of 1 (same as basic slicing)
print(my_list[::1])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
