# 004 For loops in Python

# for variable in iterable:
#     # code to execute for each item in the iterable

# 1. Basic for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. For loop with a range
for i in range(5):
    print(i)

# 3. For loop with a string
my_string = "Hello"
for char in my_string:
    print(char)

# 4. For loop with a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)
print(my_dict.items())
print(type(my_dict.items()))
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# 5. For loop with a nested list
print("Items in the nested list:")
nested_list = [[1, 2], [3, 4], [5, 6]]
for sublist in nested_list:
    for item in sublist:
        print(item)

# 5.1 For loop with a nested list  and some non-list items
print("Items in the nested list with some non-list items:")
nested_list = [[1, 2], 7, 8, 9, [3, 4], [5, 6]]
for sublist in nested_list:
    if isinstance(sublist, list):
        for item in sublist:
            print(item)
    else:
        print(sublist)

# 6. For loop with a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

# 7. For loop with a tuple
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)

# 8. For loop with a generator expression
print("Squares of numbers from 0 to 4:")
my_generator = (x**2 for x in range(5))
print(my_generator)  # Output: <generator object <genexpr> at 0x...>
print(type(my_generator))
for item in my_generator:
    print(item)

# 9. For loop with enumerate
print("Enumerating a list:")
my_list = ["a", "b", "c", "d"]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# 10. For loop with zip
print("Zipping two lists:")
list1 = [1, 2, 3]
list2 = ["one", "two", "three"]
for num, word in zip(list1, list2):
    print(f"Number: {num}, Word: {word}")
