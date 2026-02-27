# 010 Python strings

# 1. Basic String Operations
greeting = "Hello, World!"
print(greeting)  # Output: Hello, World!
print(greeting[0])  # Output: H
print(greeting[7:12])  # Output: World
print(greeting.lower())  # Output: hello, world!
print(greeting.upper())  # Output: HELLO, WORLD!
print(greeting.replace("World", "Python"))  # Output: Hello, Python!

# 2. String Concatenation
name = "Alice"
age = 25
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)  # Output: My name is Alice and I am 25 years old.

# 3. String Formatting with f-strings
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 25 years old.

# 4. String Formatting with format() method
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.

# 5. String Formatting with % operator
message = "My name is %s and I am %d years old." % (name, age)
print(message)  # Output: My name is Alice and I am 25 years old.
