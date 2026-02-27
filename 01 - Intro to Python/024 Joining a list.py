# 024 Joining a list
# 1. Joining a list of strings
words = ["Hello", "World", "Python", "is", "great"]
sentence = " ".join(words)
print(sentence)  # Output: Hello World Python is great

# 2. Joining a list of numbers (after converting them to strings)
numbers = [1, 2, 3, 4, 5]
number_string = ", ".join(str(num) for num in numbers)
print(number_string)  # Output: 1, 2, 3, 4, 5

# 3. Joining a list of mixed data types (after converting them to strings)
mixed_list = ["Alice", 30, True, 3.14]
mixed_string = " | ".join(str(item) for item in mixed_list)
print(mixed_string)  # Output: Alice | 30 | True | 3.14

# 4. Joining a list of strings with a custom separator
fruits = ["apple", "banana", "cherry"]
fruit_string = " & ".join(fruits)
print(fruit_string)  # Output: apple & banana & cherry

# 5. Joining a list of strings with a newline character
lines = ["Line 1", "Line 2", "Line 3"]
multiline_string = "\n".join(lines)
print(multiline_string)
# Output:
# Line 1
# Line 2
# Line 3

# 6. Joining a list of strings with an empty string (concatenation)
chars = ["H", "e", "l", "l", "o"]
word = "".join(chars)
print(word)  # Output: Hello
