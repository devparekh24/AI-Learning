# 013 List comprehension in Python
# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, optionally filtering items using a condition.

# 1. Basic list comprehension
my_list = [1, 2, 3, 4, 5]
new_list = [item * 2 for item in my_list]
print(new_list)  # Output: [2, 4, 6, 8, 10]

# 2. List comprehension with a condition
even_numbers = [item for item in my_list if item % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# 3. List comprehension with a nested loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 4. List comprehension with a function
def square(x):
    return x**2


squared_list = [square(item) for item in my_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# 5. List comprehension with a string
my_string = "Hello"
char_list = [char for char in my_string]
print(char_list)  # Output: ['H', 'e', 'l', 'l', 'o']

# 6. List comprehension with a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
key_list = [key for key in my_dict]
value_list = [value for value in my_dict.values()]
print(key_list)  # Output: ['a', 'b', 'c']
print(value_list)  # Output: [1, 2, 3]

# 7. List comprehension with a set
my_set = {1, 2, 3, 4, 5}
squared_set = {item**2 for item in my_set}
print(squared_set)  # Output: {1, 4, 9, 16, 25}

# 8. List comprehension with a generator expression
squared_generator = (item**2 for item in my_list)
print(squared_generator)  # Output: <generator object <genexpr> at 0x...>
print(type(squared_generator))
for item in squared_generator:
    print(item)  # Output: 1, 4, 9, 16, 25

# 9. List comprehension with a conditional expression
conditional_list = [item * 2 if item % 2 == 0 else item for item in my_list]
print(conditional_list)  # Output: [1, 4, 3, 8, 5]

# 10. List comprehension with multiple conditions
filtered_list = [item for item in my_list if item > 2 and item < 5]
print(filtered_list)  # Output: [3, 4]

# 11. List comprehension with a nested list comprehension
nested_list = [[item for item in sublist] for sublist in matrix]
print(nested_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 12. List comprehension with a nested list comprehension and a condition
filtered_nested_list = [
    [item for item in sublist if item % 2 == 0] for sublist in matrix
]
print(filtered_nested_list)  # Output: [[2], [4, 6], [8]]


# 13. List comprehension with a nested list comprehension and a function
def is_even(x):
    return x % 2 == 0


even_nested_list = [[item for item in sublist if is_even(item)] for sublist in matrix]
print(even_nested_list)  # Output: [[2, 4, 6], [4, 6], [8]]
