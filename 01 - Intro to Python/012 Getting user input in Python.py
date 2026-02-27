# 012 Getting user input in Python

# 1. Using the input() function
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Getting numerical input and not converting it to an integer
age = input("Enter your age: ")
print(f"You are {age} years old.")
# This will cause an error because age is a string
# print(f"Next year, you will be {age + 1} years old.")
print(f"You are {age*12} years old.")

# 3. Getting numerical input and converting it to an integer
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
