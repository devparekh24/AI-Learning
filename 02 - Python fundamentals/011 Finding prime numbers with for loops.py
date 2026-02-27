# 011 Finding prime numbers with for loops
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# To find prime numbers, we can use a for loop to check if a number is divisible by any number other than 1 and itself.
# Using for loop to find prime numbers between 1 and 10

print("Prime numbers between 1 and 10:")
for num in range(2, 11):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"Prime number: {num}")
