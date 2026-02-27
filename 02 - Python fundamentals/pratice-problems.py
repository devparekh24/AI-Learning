# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.

# Let's begin by asking the user to type either 'p' or 'q':
user_input = input("Enter q or p: ")

# Now we must repeat until they type 'q':
while user_input != "q":
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input == "p":
        print("Hello")
    # Now we must ask the user for their input againotherwise we would be in an infinite loop!
    user_input = input("Enter q or p: ")

#################################################################################
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for number in range(101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
