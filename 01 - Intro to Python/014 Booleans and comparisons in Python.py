# 014 Booleans and comparisons in Python
# 1. Boolean Values
is_raining = True
is_sunny = False
print(is_raining)  # Output: True
print(is_sunny)  # Output: False
# 2. Comparisons
a = 10
b = 5
print(a > b)  # Output: True
print(a < b)  # Output: False
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a >= b)  # Output: True
print(a <= b)  # Output: False
# 3. Combining Comparisons
c = 15
print(a < c < b)  # Output: False, because 10 is less than 15 but 15 is not less than 5
print(a < c and c < b)  # Output: False, because 15 is not less than 5
print(a < c or c < b)  # Output: True, because 10 is less than 15
