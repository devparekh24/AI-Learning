# .format() vs f-strings

# 1. Basic Variable Insertion
name = "Alice"
age = 30
# Using .format()
print("My name is {} and I am {} years old.".format(name, age))
# Using f-string
print(f"My name is {name} and I am {age} years old.")


# 2.Expressions Inside Strings
a = 10
b = 5
# Using format()
print("The sum is {}.".format(a + b))
# Using f-string
print(f"The sum is {a + b}.")


# 3.Number Formatting
price = 49.9876
# Using format()
print("Price: ${:.2f}".format(price))
# Using f-string
print(f"Price: ${price:.2f}")


# 4. Dictionary Example
person = {"name": "Alice", "age": 25}
# Using format()
print("Name: {name}, Age: {age}".format(**person))
# Using f-string
print(f"Name: {person['name']}, Age: {person['age']}")

############################################################
# real-world examples in Python using f-strings.

# 1.Invoice Example
customer = "John Smith"
item = "Laptop"
price = 899.99
quantity = 2
total = price * quantity

invoice = f"""
Invoice
-----------------------
Customer : {customer}
Item     : {item}
Price    : ${price:.2f}
Quantity : {quantity}
-----------------------
Total    : ${total:.2f}
"""

print(invoice)


# 2. Report Example (Aligned Columns)
# Example 1
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]

report = """Name     Age  City
------------------------
"""
for person in data:
    report += f"{person['name']:<8} {person['age']:<4} {person['city']}\n"

# Example 2
name = "Alice"
score = 93.456

print(f"{'Student':<10} | {'Score':>8}")
print("-" * 22)
print(f"{name:<10} | {score:>8.2f}")


# 3. Date Formatting Example
from datetime import datetime

now = datetime.now()
# Using format()
print("Current date and time: {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
# Using f-string
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

print(f"Today is {now:%B %d, %Y}")
print(f"Time: {now:%H:%M:%S}")


# 4. Large Numbers with Commas
revenue_list = [1250, 12500, 125000, 1250000, 12500000, 125000000]
for revenue in revenue_list:
    # using f-strings in a loop
    print(f"Total Revenue: ${revenue:,}")
    # using format() in a loop
    print("Total Revenue: ${:,}".format(revenue))


# 5. Debugging Trick (Very Useful)
x = 10
y = 5
# using f-strings
print(f"{x=}, {y=}, {x+y=}")
# using format()
print("x={}, y={}, x+y={}".format(x, y, x + y))
