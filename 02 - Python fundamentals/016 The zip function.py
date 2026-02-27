# 016 The zip function
# The zip function is used to combine two or more iterables (like lists, tuples, etc.) into a single iterable of tuples. Each tuple contains one element from each of the input iterables.

# 1. Using the zip function
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped_list = zip(list1, list2)
print(zipped_list)  # Output: <zip object at 0x...>
print(type(zipped_list))  # Output: <class 'zip'>
print(list(zipped_list))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 2. Using the zip function with more than two iterables
list3 = [True, False, True]
zipped_list = zip(list1, list2, list3)
print(list(zipped_list))  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# 3. Using the zip function with iterables of different lengths
list4 = [10, 20]
zipped_list = zip(list1, list4)
print(list(zipped_list))  # Output: [(1, 10), (2, 20)]

# 4. Unzipping a list of tuples using the zip function
zipped_list = [(1, "a"), (2, "b"), (3, "c")]
unzipped_list1, unzipped_list2 = zip(*zipped_list)
print(unzipped_list1)  # Output: (1, 2, 3)
print(unzipped_list2)  # Output: ('a', 'b', 'c')

# 5. Using the zip function in a for loop
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")

# 6. Using the zip function with a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
keys, values = zip(*my_dict.items())
print(keys)  # Output: ('name', 'age', 'city')
print(values)  # Output: ('Alice', 30, 'New York')

# 7. Using the zip function with a generator expression
squared_numbers = (x**2 for x in range(5))
zipped_list = zip(list1, squared_numbers)
print(list(zipped_list))  # Output: [(1, 0), (2, 1), (3, 4)]
