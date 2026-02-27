# 022 Length and sum

# 1. Length of a String
my_string = "Hello, World!"
length_of_string = len(my_string)
print(f"The length of the string '{my_string}' is: {length_of_string}")

# 2. Length of a List
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print(f"The length of the list {my_list} is: {length_of_list}")

# 3. Sum of a List
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print(f"The sum of the list {numbers} is: {sum_of_numbers}")

# 4. Length and Sum of a Tuple
my_tuple = (1, 2, 3, 4, 5)
length_of_tuple = len(my_tuple)
sum_of_tuple = sum(my_tuple)
print(f"The length of the tuple {my_tuple} is: {length_of_tuple}")
print(f"The sum of the tuple {my_tuple} is: {sum_of_tuple}")

# 5. Length and Sum of a Set
my_set = {1, 2, 3, 4, 5}
length_of_set = len(my_set)
sum_of_set = sum(my_set)
print(f"The length of the set {my_set} is: {length_of_set}")
print(f"The sum of the set {my_set} is: {sum_of_set}")

# 6. Length and Sum of a Dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
length_of_dict = len(my_dict)
sum_of_dict_values = sum(my_dict.values())
print(f"The length of the dictionary {my_dict} is: {length_of_dict}")
print(f"The sum of the values in the dictionary {my_dict} is: {sum_of_dict_values}")

# 7. Length and Sum of a Range
my_range = range(1, 6)
length_of_range = len(my_range)
sum_of_range = sum(my_range)
print(f"The length of the range {my_range} is: {length_of_range}")
print(f"The sum of the range {my_range} is: {sum_of_range}")

# 8. Length and Sum of a Generator
my_generator = (x for x in range(1, 6))
length_of_generator = len(my_generator)
sum_of_generator = sum(my_generator)
print(f"The length of the generator {my_generator} is: {length_of_generator}")
print(f"The sum of the generator {my_generator} is: {sum_of_generator}")
