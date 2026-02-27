# 019 Functions in Python
# Functions are reusable blocks of code that perform a specific task. They allow you to organize your code, improve readability, and avoid repetition.


# 1. Basic function definition and usage
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!


# 2. Function with multiple parameters
def add(a, b):
    return a + b


print(add(5, 3))  # Output: 8


# 3. Function with default parameters
def greet_default(name="World"):
    return f"Hello, {name}!"


print(greet_default())  # Output: Hello, World!
print(greet_default("Bob"))  # Output: Hello, Bob!


# 4. Function with variable-length arguments
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))  # Output: 9


# 5. Function with keyword arguments
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")


print_info(age=30, name="Charlie")  # Output: Name: Charlie, Age: 30


# 6. Function with a return value
def square(x):
    return x**2


print(square(4))  # Output: 16


# 7. Function with a docstring
def factorial(n):
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120
print(factorial.__doc__)  # Output: Returns the factorial of a number.

# 8. Lambda function (anonymous function)
square_lambda = lambda x: x**2
print(square_lambda(4))  # Output: 16


# 9. Higher-order function (function that takes another function as an argument)
def apply_function(func, value):
    return func(value)


print(apply_function(square, 5))  # Output: 25
print(apply_function(lambda x: x + 10, 5))  # Output: 15


# 10. Recursive function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Output: 55

# 11. Global and local variables
x = 10  # Global variable


def modify_global():
    global x
    x = 20  # Modifying the global variable


modify_global()
print(x)  # Output: 20


# 12. Function with variable scope
def outer_function():
    x = 5  # Local variable in outer_function

    def inner_function():
        nonlocal x
        x = 10  # Modifying the nonlocal variable

    inner_function()
    return x


print(outer_function())  # Output: 10


# 13. Function with keyword-only arguments
def print_info_keyword(name, *, age):
    print(f"Name: {name}, Age: {age}")


print_info_keyword("Alice", age=30)  # Output: Name: Alice, Age: 30


# 14. Function with variable-length keyword arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Bob", age=25, city="New York")
# Output:
# name: Bob
# age: 25
# city: New York


# 15. Function with a generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5

# 16. Function with a generator expression
squares = (x**2 for x in range(5))
print(list(squares))  # Output: [0, 1, 4, 9, 16]


# 17. Function with a decorator
def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")

    return wrapper


@decorator
def my_function():
    print("Inside the function.")


my_function()
# Output:
# Before the function call.
# Inside the function.
# After the function call.


# 18. Function with a recursive decorator
def recursive_decorator(func):
    def wrapper(n):
        if n > 0:
            print(f"Recursion level: {n}")
            return wrapper(n - 1)
        else:
            return func()

    return wrapper


@recursive_decorator
def base_function():
    print("Base function reached.")


base_function(3)  # pylint: disable=too-many-function-args
# Output:
# Recursion level: 3
# Recursion level: 2
# Recursion level: 1
# Base function reached.


# 19. Function with a default argument that is mutable
def append_to_list_bad(value, my_list=[]):
    my_list.append(value)
    return my_list


print(append_to_list_bad(1))  # Output: [1]
print(append_to_list_bad(2))  # Output: [1, 2]
print(append_to_list_bad(3, []))  # Output: [3]
print(append_to_list_bad(4))  # Output: [1, 2, 4]


# 20. Function with a default argument that is mutable
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]
print(append_to_list(3, []))  # Output: [3]
print(append_to_list(4))  # Output: [4]
