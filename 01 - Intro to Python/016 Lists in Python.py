# 016 Lists in Python

# 1. Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]


# 2. Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5


# 3. Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]


# 4. Adding elements
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]


# 5. Removing elements
my_list.remove(3)
print(my_list)  # Output: [10, 2, 4, 5, 6]


# 6. Sorting a list
my_list.sort()
print(my_list)  # Output: [2, 4, 5, 6, 10]


# 7. List slicing
print(my_list[1:4])  # Output: [4, 5, 6]
print(my_list[:3])  # Output: [2, 4, 5]
print(my_list[3:])  # Output: [6, 10]


# 8. List comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [4, 16, 25, 36, 100]


# 9. Nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2]
print(nested_list[0][1])  # Output: 2


# 10. List methods
my_list.append(7)
print(my_list)  # Output: [2, 4, 5, 6, 10, 7]
my_list.insert(0, 1)
print(my_list)  # Output: [1, 2, 4, 5, 6, 10, 7]
my_list.pop()
print(my_list)  # Output: [1, 2, 4, 5, 6, 10]
my_list.clear()
print(my_list)  # Output: []
