# 002 While loops in Python

# 1. Basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. Using while loop with else
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop has finished")

# 3. Using while loop to create a simple menu
while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You chose option 1")
    elif choice == "2":
        print("You chose option 2")
    elif choice == "3":
        print("Exiting the menu")
        break
    else:
        print("Invalid choice, please try again")

# 4. Using while loop to calculate the factorial of a number
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is {factorial}")

# 5. Using while loop to sum numbers until the user decides to stop
total_sum = 0
while True:
    num = input("Enter a number to add to the sum (or 'stop' to finish): ")
    if num.lower() == "stop":
        break
    total_sum += int(num)
print(f"The total sum is: {total_sum}")

