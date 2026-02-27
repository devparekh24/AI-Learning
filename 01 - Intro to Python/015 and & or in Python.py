# 015 and & or in Python
# 1. Using and
a = 10
b = 20
c = 30
if a > b and b > c:
    print("a is greater than b and b is greater than c")
else:
    print("The condition is not met")
# 2. Using or
if a > b or b > c:
    print("a is greater than b or b is greater than c")
else:
    print("The condition is not met")
# 3. Combining and and or
if (a > b and b > c) or (a < b and b < c):
    print(
        "Either a is greater than b and b is greater than c, or a is less than b and b is less than c"
    )
else:
    print("The condition is not met")
