from typing import Union


def divide(divident: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return divident / divisor


def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError("At one value must be provided")
    result = 1
    for a in args:
        result *= a
    return result
