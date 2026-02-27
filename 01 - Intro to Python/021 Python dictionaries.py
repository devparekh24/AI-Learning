# 021 Python dictionaries

# 1. Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


# 2. Accessing values in a dictionary
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30


# 3. Modifying values in a dictionary
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}


# 4. Adding new key-value pairs to a dictionary
my_dict["country"] = "USA"
print(
    my_dict
)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}


# 5. Removing key-value pairs from a dictionary
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}


# 6. Dictionary methods
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(my_dict.values())  # Output: dict_values(['John', 31, 'USA'])
print(
    my_dict.items()
)  # Output: dict_items([('name', 'John'), ('age', 31), ('country', 'USA')])


# 7. Dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 8. Nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
}
print(
    nested_dict
)  # Output: {'person1': {'name': 'Alice', 'age': 25}, 'person2': {'name': 'Bob', 'age': 30}}
print(nested_dict["person1"]["name"])  # Output: Alice
print(nested_dict["person2"]["age"])  # Output: 30


# 9. Using f-strings with dictionaries
name = my_dict["name"]
age = my_dict["age"]
country = my_dict["country"]
formatted_string = f"{name} is {age} years old and lives in {country}."
print(formatted_string)  # Output: John is 31 years old and lives in USA.


# 10. Dictionary immutability
# my_dict["name"] = "Jane"  # This line will raise a TypeError because dictionaries are mutable, but the keys themselves are immutable.


# 11. Dictionary update method
my_dict.update({"name": "Jane", "age": 32})
print(
    my_dict
)  # Output: {'name': 'Jane', 'age': 32, 'country': 'USA'}


# 12. Dictionary copy method
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Jane', 'age': 32, 'country': 'USA'}
new_dict["name"] = "Alice"
print(new_dict)  # Output: {'name': 'Alice', 'age': 32, 'country': 'USA'}
print(my_dict)  # Output: {'name': 'Jane', 'age': 32, 'country': 'USA'}


# 13. Dictionary clear method
my_dict.clear()
print(my_dict)  # Output: {}


# 14. Dictionary pop method
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict.pop("age"))  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}


# 15. Dictionary popitem method
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict.popitem())  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 30}


# 16. Dictionary setdefault method
my_dict = {"name": "John", "age": 30}
print(my_dict.setdefault("city", "New York"))  # Output: 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


# 17. Dictionary view methods
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])


# 18. Dictionary get method
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict.get("name"))  # Output: 'John'
print(my_dict.get("country"))  # Output: None


# 19. Dictionary fromkeys method
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
my_dict = dict.fromkeys(keys, values)
print(my_dict)  # Output: {'name': ['John', 30, 'New York'], 'age': ['John', 30, 'New York'], 'city': ['John', 30, 'New York']}


# 20. Dictionary items method
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 30
# city: New York


# 21. Dictionary keys method
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key in my_dict.keys():
    print(key)
# Output:
# name
# age
# city


# 22. Dictionary values method
my_dict = {"name": "John", "age": 30, "city": "New York"}
for value in my_dict.values():
    print(value)
# Output:
# John
# 30
# New York
