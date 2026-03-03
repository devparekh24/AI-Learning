# 002 Intro to errors in Python
# Errors are issues in code that prevent it from running correctly. Common types include:
# - SyntaxError: Code structure is incorrect (e.g., missing parentheses).
# - NameError: Using a variable that hasn't been defined.
# - TypeError: Performing an operation on incompatible types (e.g., adding a string and a number).
# - ValueError: Using a function with an argument of the right type but inappropriate value (e.g., converting a non-numeric string to an integer).
# - IndexError: Accessing an index that is out of range in a list or string.
# - KeyError: Accessing a key that doesn't exist in a dictionary.
# - AttributeError: Accessing an attribute that doesn't exist on an object.
# - ZeroDivisionError: Dividing a number by zero.
# - ImportError: Importing a module that can't be found.
# - ModuleNotFoundError: Importing a module that doesn't exist.

# Example of a SyntaxError
# print("Hello World"  # Missing closing parenthesis

# Example of a NameError
# print(x)  # Using a variable that hasn't been defined

# Example of a TypeError
# result = "Hello" + 5  # Cannot add a string and an integer

# Example of a ValueError
# number = int("abc")  # Cannot convert a non-numeric string to an integer

# Example of an IndexError
# my_list = [1, 2, 3]
# print(my_list[5])  # Index out of range

# Example of a KeyError
# my_dict = {"name": "Alice", "age": 30}
# print(my_dict["city"])  # Key does not exist in the dictionary

# Example of an AttributeError
# my_string = "Hello"
# print(my_string.uppercase())  # Method does not exist on string objects

# Example of a ZeroDivisionError
# result = 10 / 0  # Cannot divide by zero

# Example of an ImportError
# import my_module  # Module not found

# Example of a ModuleNotFoundError
# import non_existent_module  # Module does not exist
