# 010 Handling those pesky user errors!
# Comprehensive error handling covers various techniques to prevent crashes and handle exceptions gracefully.

import logging
from typing import Optional

# Setup logging for error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# 1. BASIC TRY-EXCEPT: Handle a single exception type
# ============================================================================
def example_1_basic_try_except():
    """Basic error handling for ValueError"""
    print("\n--- 1. Basic Try-Except ---")
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("❌ That's not a valid number.")


# ============================================================================
# 2. MULTIPLE EXCEPTION HANDLERS: Catch different exception types separately
# ============================================================================
def example_2_multiple_exceptions():
    """Handle different exceptions with different messages"""
    print("\n--- 2. Multiple Exception Handlers ---")
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        result = 10 / number
        print(f"10 divided by {number} is {result}")
    except ValueError:
        print("❌ Invalid input - please enter a number.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    except TypeError:
        print("❌ Type mismatch occurred.")


# ============================================================================
# 3. CATCH MULTIPLE EXCEPTIONS IN ONE HANDLER
# ============================================================================
def example_3_catch_multiple():
    """Catch multiple exceptions in a single handler"""
    print("\n--- 3. Catch Multiple Exceptions Together ---")
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"Number: {number}")
    except (ValueError, TypeError):
        print("❌ That's not a valid number or type error occurred.")


# ============================================================================
# 4. CATCH ALL EXCEPTIONS (Use with caution!)
# ============================================================================
def example_4_catch_all():
    """Catch any exception without specifying type"""
    print("\n--- 4. Catch All Exceptions ---")
    try:
        user_input = input("Enter something: ")
        result = eval(user_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"❌ An error occurred: {type(e).__name__}: {e}")


# ============================================================================
# 5. EXCEPTION INFORMATION: Access error details with 'as e'
# ============================================================================
def example_5_exception_info():
    """Access exception object to get detailed information"""
    print("\n--- 5. Exception Information ---")
    try:
        numbers = [1, 2, 3]
        print(numbers[10])
    except IndexError as error:
        print(f"❌ Error Type: {type(error).__name__}")
        print(f"   Error Message: {error}")
        print(f"   Error Args: {error.args}")


# ============================================================================
# 6. ELSE BLOCK: Executes only when no exception occurs
# ============================================================================
def example_6_else_block():
    """Use else to execute code only if try block succeeds"""
    print("\n--- 6. Else Block (Success Path) ---")
    user_input = input("Enter a positive number: ")
    try:
        number = int(user_input)
    except ValueError:
        print("❌ Invalid number format.")
    else:
        if number > 0:
            print(f"✓ Successfully processed: {number}")
        else:
            print(f"❌ Number must be positive, got: {number}")


# ============================================================================
# 7. FINALLY BLOCK: Always executes (cleanup code)
# ============================================================================
def example_7_finally_block():
    """Finally block always executes, regardless of exceptions"""
    print("\n--- 7. Finally Block (Always Executes) ---")
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"Number: {number}")
    except ValueError:
        print("❌ Invalid input.")
    else:
        print("✓ Input was valid.")
    finally:
        print("✓ Cleanup completed (this always runs).")


# ============================================================================
# 8. CUSTOM EXCEPTIONS: Create domain-specific errors
# ============================================================================
class InvalidAgeError(Exception):
    """Custom exception for invalid age"""

    pass


class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance"""

    pass


def example_8_custom_exceptions():
    """Raise and handle custom exceptions"""
    print("\n--- 8. Custom Exceptions ---")

    def validate_age(age):
        if age < 0:
            raise InvalidAgeError("Age cannot be negative.")
        if age > 150:
            raise InvalidAgeError("Age seems unrealistic.")
        return age

    try:
        age_input = input("Enter your age: ")
        age = int(age_input)
        validate_age(age)
        print(f"✓ Age {age} is valid.")
    except ValueError:
        print("❌ Please enter a valid number.")
    except InvalidAgeError as e:
        print(f"❌ Invalid age: {e}")


# ============================================================================
# 9. NESTED TRY-EXCEPT: Handle errors at different levels
# ============================================================================
def example_9_nested_try_except():
    """Nested try-except blocks for layered error handling"""
    print("\n--- 9. Nested Try-Except ---")
    try:
        user_input = input("Enter a list of numbers (comma-separated): ")
        numbers = user_input.split(",")
        try:
            # Inner try: Convert each string to int
            int_numbers = [int(n.strip()) for n in numbers]
            average = sum(int_numbers) / len(int_numbers)
            print(f"✓ Average: {average}")
        except ValueError:
            print("❌ One or more values are not valid numbers.")
    except Exception as e:
        print(f"❌ Outer exception: {e}")


# ============================================================================
# 10. RE-RAISING EXCEPTIONS: Catch, log, and re-raise
# ============================================================================
def example_10_reraising():
    """Log an exception and re-raise it for higher-level handling"""
    print("\n--- 10. Re-raising Exceptions ---")

    def process_data(data):
        try:
            return int(data) * 2
        except ValueError as e:
            logger.error(f"Failed to process data '{data}': {e}")
            raise  # Re-raise the original exception

    try:
        process_data("invalid")
    except ValueError:
        print("❌ Exception was re-raised after logging.")


# ============================================================================
# 11. CONTEXT MANAGERS: Safe resource handling with 'with' statement
# ============================================================================
def example_11_context_managers():
    """Use context managers for safe resource management"""
    print("\n--- 11. Context Managers ---")
    try:
        # Write to a file safely - automatically closes file
        with open("/tmp/test.txt", "w") as f:
            f.write("Hello, World!")
        print("✓ File written successfully.")
    except PermissionError:
        print("❌ Permission denied.")
    except IOError as e:
        print(f"❌ File operation failed: {e}")


# ============================================================================
# 12. VALIDATION WITH RETRY LOGIC: Real-world user input handling
# ============================================================================
def get_valid_number(prompt: str, max_retries: int = 3) -> Optional[int]:
    """
    Get valid integer input from user with retry logic.

    Args:
        prompt: Message to display to user
        max_retries: Maximum number of retry attempts

    Returns:
        Valid integer or None if max retries exceeded
    """
    print(f"\n--- 12. Validation with Retry Logic ({max_retries} attempts) ---")

    for attempt in range(1, max_retries + 1):
        try:
            user_input = input(f"{prompt} (Attempt {attempt}/{max_retries}): ")
            number = int(user_input)

            if number < 0:
                raise ValueError("Number must be non-negative.")

            print(f"✓ Valid number: {number}")
            return number

        except ValueError as e:
            if attempt < max_retries:
                print(f"❌ Invalid input: {e}. Try again.")
            else:
                print(f"❌ Max retries exceeded. Failed to get valid input.")
                return None
        except KeyboardInterrupt:
            print("\n❌ Input cancelled by user.")
            return None


# ============================================================================
# 13. ASSERT STATEMENTS: Quick validation (use for debugging)
# ============================================================================
def example_13_assert():
    """Use assertions for input validation (development/testing)"""
    print("\n--- 13. Assert Statements ---")
    try:
        user_input = input("Enter a positive number: ")
        number = int(user_input)

        # Assert fails if condition is False
        assert number > 0, "Number must be positive"
        assert number < 1000, "Number must be less than 1000"

        print(f"✓ Assertions passed. Number: {number}")
    except ValueError:
        print("❌ Invalid number format.")
    except AssertionError as e:
        print(f"❌ Assertion failed: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("ERROR HANDLING IN PYTHON - COMPREHENSIVE EXAMPLES")
    print("=" * 70)

    examples = [
        ("Basic Try-Except", example_1_basic_try_except),
        ("Multiple Exception Handlers", example_2_multiple_exceptions),
        ("Catch Multiple Exceptions", example_3_catch_multiple),
        ("Catch All Exceptions", example_4_catch_all),
        ("Exception Information", example_5_exception_info),
        ("Else Block", example_6_else_block),
        ("Finally Block", example_7_finally_block),
        ("Custom Exceptions", example_8_custom_exceptions),
        ("Nested Try-Except", example_9_nested_try_except),
        ("Re-raising Exceptions", example_10_reraising),
        ("Context Managers", example_11_context_managers),
        ("Retry Logic", get_valid_number),
        ("Assert Statements", example_13_assert),
    ]

    # Uncomment to run individual examples:
    # example_5_exception_info()
    # example_3_catch_multiple()
    # get_valid_number("Enter a number")

    print("\n" + "=" * 70)
    print("Run individual examples by uncommenting them in the __main__ block")
    print("=" * 70)
