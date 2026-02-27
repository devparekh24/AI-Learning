# 024 First-class functions in Python
# In Python, functions are first-class citizens, which means they can be treated like any other object. You can assign them to variables, pass them as arguments to other functions, and return them from functions.
# 1. Assigning a function to a variable
def greet(name):
    return f"Hello, {name}!"


greeting = greet
print(greeting("Alice"))  # Output: Hello, Alice!


# 2. Passing a function as an argument
def apply_function(func, value):
    return func(value)


result = apply_function(greet, "Bob")
print(result)  # Output: Hello, Bob!


# 3. Returning a function from a function
def create_greeting(name):
    def greet():
        return f"Hello, {name}!"

    return greet


greet_bob = create_greeting("Bob")
print(greet_bob())  # Output: Hello, Bob!

# 4. Using a lambda function (anonymous function)
square = lambda x: x**2
print(square(5))  # Output: 25
