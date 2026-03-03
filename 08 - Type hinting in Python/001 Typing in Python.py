# 001 Typing in Python
# Type hinting in Python allows you to specify the expected data types of variables, function parameters, and return values. This can help improve code readability and catch potential type-related errors during development. Here are some common type hints in Python:
# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Example usage
print(greet("Alice"))  # Output: Hello, Alice!
# Type hints for variables
age: int = 30
# Type hints for lists and dictionaries
from typing import List, Dict

my_list: List[int] = [1, 2, 3]
my_dict: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
# Type hints for optional values
from typing import Optional


def get_user_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    elif user_id == 2:
        return "Bob"
    else:
        return None


# Example usage
print(get_user_name(1))  # Output: Alice
print(get_user_name(3))  # Output: None


# Type hints for functions with multiple parameters
def add_numbers(a: int, b: int) -> int:
    return a + b


# Example usage
print(add_numbers(5, 10))  # Output: 15
# Type hints for functions that return multiple values
from typing import Tuple


def get_coordinates() -> Tuple[float, float]:
    return 40.7128, -74.0060


# Example usage
latitude, longitude = get_coordinates()
print(
    f"Latitude: {latitude}, Longitude: {longitude}"
)  # Output: Latitude: 40.7128, Longitude: -74.006


# Type hints for functions that accept variable-length arguments
def sum_numbers(*args: int) -> int:
    return sum(args)


# Example usage
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15


# Type hints for functions that accept keyword arguments
def print_user_info(name: str, age: int, city: str) -> None:
    print(f"Name: {name}, Age: {age}, City: {city}")


# Example usage
print_user_info(
    name="Alice", age=30, city="New York"
)  # Output: Name: Alice, Age: 30, City: New York


# Type hints for functions that accept a list of items
def process_items(items: List[str]) -> None:
    for item in items:
        print(f"Processing item: {item}")


# Example usage
process_items(["apple", "banana", "cherry"])  # Output: Processing item: apple


# Processing item: banana
# Processing item: cherry
# Type hints for functions that accept a dictionary of items
def process_user_data(user_data: Dict[str, str]) -> None:
    for key, value in user_data.items():
        print(f"{key}: {value}")


# Example usage
process_user_data({"name": "Alice", "age": "30", "city": "New York"})
# Output:
# name: Alice
# age: 30
# city: New York
# Type hints for functions that accept a union of types
from typing import Union


def process_value(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Processing integer: {value}")
    elif isinstance(value, str):
        print(f"Processing string: {value}")


# Example usage
process_value(42)  # Output: Processing integer: 42
process_value("Hello")  # Output: Processing string: Hello
# Type hints for functions that accept a callable (function) as an argument
from typing import Callable


def execute_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


# Example usage
def add(a: int, b: int) -> int:
    return a + b


result = execute_function(add, 5, 10)
print(result)  # Output: 15
# Type hints for functions that accept a generator
from typing import Generator


def count_up_to(n: int) -> Generator[int, None, None]:
    for i in range(1, n + 1):
        yield i


# Example usage
for number in count_up_to(5):
    print(number)  # Output: 1, 2, 3, 4, 5
# Type hints for functions that accept an asynchronous function
from typing import Awaitable
import asyncio


async def async_function() -> str:
    await asyncio.sleep(1)
    return "Async result"


def execute_async_function(func: Callable[[], Awaitable[str]]) -> None:
    result = asyncio.run(func())
    print(result)


# Example usage
execute_async_function(async_function)  # Output: Async result
# Type hints for functions that accept a context manager
from typing import ContextManager


def use_context_manager(cm: ContextManager) -> None:
    with cm:
        print("Inside the context manager.")


# Example usage
from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Entering the context manager.")
    yield
    print("Exiting the context manager.")


use_context_manager(my_context_manager())
# Output:
# Entering the context manager.
# Inside the context manager.
# Exiting the context manager.
