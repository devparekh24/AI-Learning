# 005 Destructuring syntax
# Destructuring syntax allows you to unpack values from data structures like lists, tuples, and dictionaries into individual variables.

# 1. Unpacking a list
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# 2. Unpacking a tuple
my_tuple = (4, 5, 6)
x, y, z = my_tuple
print(x)  # Output: 4
print(y)  # Output: 5
print(z)  # Output: 6

# 3. Unpacking a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
name, age, city = my_dict.values()
print(name)  # Output: Alice
print(age)  # Output: 30
print(city)  # Output: New York

# 4. Unpacking with the * operator
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5

# 5. Unpacking with the ** operator
person = {"name": "Alice", "age": 30, "city": "New York"}
name, *_, city = person
print(name)  # Output: Alice
print(city)  # Output: New York
