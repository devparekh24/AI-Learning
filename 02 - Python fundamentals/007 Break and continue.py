# 007 Break and continue
# The break statement is used to exit a loop prematurely when a certain condition is met.
# The continue statement is used to skip the current iteration of a loop and move on to the next iteration.

# Example of break statement
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Output: 1, 2, 3, 4

# Example of continue statement
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip the current iteration if i is even
    print(i)  # Output: 1, 3, 5, 7, 9
