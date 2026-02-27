# 007 Calculating the remainder of a division
# The modulus operator (%) is used to calculate the remainder of a division operation.
# It returns the remainder after dividing the left operand by the right operand.
a = 10
b = 3
print(a % b)  # Output: 1, because 10 divided by 3 is 3 with a remainder of 1
# The modulus operator can also be used with negative numbers.
a = -10
b = 3
print(a % b)  # Output: 2, because -10 divided by 3 is -4 with a remainder of 2
# The modulus operator can be useful in various applications, such as determining if a number is even or odd.
number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
# The modulus operator can also be used to wrap around values, such as in a circular buffer or when working with angles.
angle = 370
normalized_angle = angle % 360
print(
    f"Normalized angle: {normalized_angle} degrees"
)  # Output: Normalized angle: 10 degrees

# In summary, the modulus operator (%) is used to calculate the remainder of a division operation.
# It returns the remainder after dividing the left operand by the right operand.
# It can be used with both positive and negative numbers, and it has various applications in programming.
