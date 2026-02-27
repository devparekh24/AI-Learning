# 017 Tuples in Python

# 1. Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)


# 2. Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5


# 3. Modifying elements
# my_tuple[0] = 10  # This line will raise a TypeError because tuples are immutable


# 4. Tuple packing and unpacking
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5


# 5. Tuple methods
print(
    my_tuple.count(2)
)  # Output: 1, counts the number of occurrences of 2 in the tuple
print(
    my_tuple.index(3)
)  # Output: 2, returns the index of the first occurrence of 3 in the tuple


# 6. Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[0][1])  # Output: 2


# 7. Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)


# 8. Tuple repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 9. Tuple slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)
print(my_tuple[:3])  # Output: (1, 2, 3)
print(my_tuple[3:])  # Output: (4, 5)


# 10. Tuple immutability
# my_tuple[0] = 10  # This line will raise a TypeError because tuples are immutable


# 11. Tuple unpacking
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5


# 12. Tuple methods
print(
    my_tuple.count(2)
)  # Output: 1, counts the number of occurrences of 2 in the tuple
print(
    my_tuple.index(3)
)  # Output: 2, returns the index of the first occurrence of 3 in the tuple
