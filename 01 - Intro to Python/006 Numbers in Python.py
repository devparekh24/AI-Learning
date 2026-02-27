# 006 Numbers in Python
# 1. Basic Arithmetic Operations
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b)  # Floor Division
print(a % b)  # Modulus
print(a**b)  # Exponentiation (raise to the power of)
# 2. Order of Operations
result = a + b * 2  # Multiplication is performed before addition
print(result)  # Output: 20
result = (a + b) * 2  # Parentheses change the order of operations
print(result)  # Output: 30
# 3. Using the math module
import math

print(math.sqrt(25))  # Output: 5.0
print(math.pow(2, 3))  # Output: 8.0
print(math.pi)  # Output: 3.141592653589793
print(math.e)  # Output: 2.718281828459045
