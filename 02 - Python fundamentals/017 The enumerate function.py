# 017 The enumerate function
# The enumerate function is used to add a counter to an iterable and returns it as an enumerate object.
# This is often used in for loops to get both the index and the value of each item in the iterable.

# 1. Using the enumerate function
my_list = ["a", "b", "c", "d"]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# 2. Using the enumerate function with a start index
for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")

# 3. Using the enumerate function with a tuple
my_tuple = ("apple", "banana", "cherry")
for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")

# 4. Using the enumerate function with a string
my_string = "Hello"
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")

# 5. Using the enumerate function with a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

# 6. Using the enumerate function with a set
my_set = {1, 2, 3, 4, 5}
for index, value in enumerate(my_set):
    print(f"Index: {index}, Value: {value}")

# 7. Using the enumerate function with a generator expression
squared_numbers = (x**2 for x in range(5))
for index, value in enumerate(squared_numbers):
    print(f"Index: {index}, Value: {value}")

# 8. Using the enumerate function in a list comprehension
squared_list = [value**2 for index, value in enumerate(my_list)]
print(
    squared_list
)  # Output: ['a', 'b', 'c', 'd'] (Note: This will not work as expected since my_list contains strings, not numbers)
