# This code demonstrates the use of f-strings in Python to create a formatted string that includes variable values.
name = "Alice"
age = 25

message = f"My name is {name} and I am {age} years old."
print(message)

# Using Expressions Inside f-Strings
# You can put calculations inside {}:
a = 10
b = 5

print(f"The sum of {a} and {b} is {a + b}.")
print(f"The product of {a} and {b} is {a * b}.")

# Formatting Numbers
price = 49.9876

print(f"Price: ${price:.2f}")

number = 1234.56789
print(f"Formatted number: {number:.2f}")  # Format to 2 decimal places
print(
    f"Formatted number: {number:,.2f}"
)  # Format with comma separator and 2 decimal places


# Using the format() method

#  1. Basic Example
name = "Alice"
age = 25

message = "My name is {} and I am {} years old.".format(name, age)
print(message)

#  2. Using Index Positions
message = "My name is {0} and I am {1} years old. {0} is my name.".format(name, age)
print(message)


#  3. Using Named Arguments
print("My name is {name} and I am {age} years old.".format(name="Alice", age=25))

#  4. Formatting Numbers (Decimals)
price = 49.9876
print("Price: {:.2f}".format(price))

#  5. Padding and Alignment
print("|{:10}|".format("cat"))  # Left align (default)
print("|{:>10}|".format("cat"))  # Right align
print("|{:^10}|".format("cat"))  # Center align

#  6. Formatting Integers
number = 42
print("Binary: {:b}".format(number))
print("Hex: {:x}".format(number))
print("With commas: {:,}".format(1000000))
