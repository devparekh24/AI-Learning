# if statements in Python
# if condition:
#     statement
# else:
#     statement

a = 10
b = 20

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# if condition1:
#     statement
# elif condition2:
#     statement
# else:
#     statement

a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("a and b are equal")

# if condition1:
#     statement
# elif condition2:
#     statement
# elif condition3:
#     statement
# else:
#     statement

a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("Invalid input")


# input with if statements
friend = "Rolf"
user_name = input("Enter your friend's name: ")

if user_name == friend:
    print("Hello, Rolf!")
else:
    print("Hello, stranger!")
print("This will always be printed")


# list of friends with if statements
friends = ["Rolf", "Bob", "Jen"]
family = ["Alice", "Charlie", "David"]
user_name = input("Enter your friend's or family name: ")

if user_name in friends:
    print("Hello, {}!".format(user_name))
elif user_name in family:
    print("Hello, family member {}!".format(user_name))
else:
    print("Hello, stranger!")
