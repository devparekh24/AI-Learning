# 009 The else block and re-raising exceptions
# In Python, the else block executes only if no exceptions occur in the try block.
# Re-raising allows you to catch exceptions, process them, and propagate them up the call stack.

import logging
import traceback

# Setup logging for error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# 1. ELSE BLOCK: Executes only when try block succeeds
# ============================================================================
def example_1_else_block():
    """Demonstrate the else block in try-except"""
    print("\n--- 1. Else Block ---")

    # Example 1: No exception occurs
    try:
        result = 10 / 2
    except ValueError as e:
        print(f"❌ ValueError: {e}")
    else:
        print(f"✓ Success! Result: {result}")

    # Example 2: Exception occurs
    try:
        number = int("not_a_number")
    except ValueError as e:
        print(f"❌ ValueError: {e}")
    else:
        print(f"✓ This won't print because exception occurred")


# ============================================================================
# 2. ELSE BLOCK WITH MULTIPLE EXCEPTIONS: Else only runs if try succeeds
# ============================================================================
def example_2_else_with_multiple_exceptions():
    """Else block works with multiple except clauses"""
    print("\n--- 2. Else Block with Multiple Exception Handlers ---")

    def safe_divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print(f"❌ Cannot divide by zero")
        except TypeError:
            print(f"❌ Invalid types for division")
        else:
            print(f"✓ Division successful: {a} / {b} = {result}")
            return result

    safe_divide(10, 2)  # else block will execute
    safe_divide(10, 0)  # else block will NOT execute
    safe_divide(10, "2")  # else block will NOT execute


# ============================================================================
# 3. ELSE + FINALLY: Combining multiple blocks
# ============================================================================
def example_3_else_finally():
    """Combine else and finally blocks"""
    print("\n--- 3. Else Block + Finally Block ---")

    def process_data(data):
        try:
            number = int(data)
            print(f"✓ Converted to: {number}")
        except ValueError:
            print("❌ Invalid number format")
        else:
            print("✓ Else block: Conversion successful")
        finally:
            print("✓ Finally block: Cleanup (always runs)")

    process_data("42")
    print()
    process_data("invalid")


# ============================================================================
# 4. SIMPLE RE-RAISING: Catch and propagate the same exception
# ============================================================================
def example_4_simple_reraise():
    """Re-raise the original exception using bare raise"""
    print("\n--- 4. Simple Re-raising ---")

    def inner_function(value):
        try:
            return int(value)
        except ValueError as e:
            # Log the error locally, then re-raise
            logger.error(f"Conversion failed in inner_function: {value}")
            raise  # Re-raises the exact same exception

    try:
        result = inner_function("not_a_number")
    except ValueError as e:
        print(f"❌ ValueError caught in outer handler: {e}")


# ============================================================================
# 5. RE-RAISING WITH NEW MESSAGE: Raise a new exception of same type
# ============================================================================
def example_5_reraise_new_message():
    """Raise a new exception with a different message"""
    print("\n--- 5. Re-raising with New Message ---")

    def validate_age(age):
        try:
            age_int = int(age)
            if age_int < 0:
                raise ValueError("Age cannot be negative")
            if age_int > 150:
                raise ValueError("Age seems unrealistic")
        except ValueError as e:
            # Raise a new ValueError with more context
            raise ValueError(f"Invalid age input '{age}': {str(e)}")

    try:
        validate_age("-5")
    except ValueError as e:
        print(f"❌ {e}")


# ============================================================================
# 6. EXCEPTION CHAINING: Using 'raise from' to preserve context
# ============================================================================
def example_6_exception_chaining():
    """Use 'raise from' to chain exceptions and preserve context"""
    print("\n--- 6. Exception Chaining (raise from) ---")

    def parse_config(config_str):
        try:
            # Simulate parsing error
            result = eval(config_str)
            return result
        except (SyntaxError, TypeError) as original_error:
            # Raise a new, more meaningful exception while preserving the original
            raise ValueError("Invalid configuration format") from original_error

    try:
        parse_config("{ invalid syntax }")
    except ValueError as e:
        print(f"❌ {e}")
        print(f"   Caused by: {type(e.__cause__).__name__}: {e.__cause__}")


# ============================================================================
# 7. SELECTIVE RE-RAISING: Only re-raise certain exceptions
# ============================================================================
def example_7_selective_reraise():
    """Re-raise only specific exceptions, handle others locally"""
    print("\n--- 7. Selective Re-raising ---")

    def process_file(filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            print(f"⚠ File not found: {filename}")
        except PermissionError as e:
            print(f"❌ Permission denied: {filename}")
            raise  # Re-raise critical errors
        except Exception as e:
            print(f"⚠ Unexpected error: {e}")

    try:
        process_file("/nonexistent/file.txt")  # FileNotFoundError - handled locally
        print("✓ Processing completed")
    except PermissionError:
        print("❌ Must exit due to permission error")


# ============================================================================
# 8. RE-RAISING WITH DIFFERENT EXCEPTION TYPE: Transform exceptions
# ============================================================================
def example_8_transform_exception():
    """Catch one exception type, raise a different one"""
    print("\n--- 8. Transforming Exception Types ---")

    class APIError(Exception):
        """Custom exception for API operations"""

        pass

    def fetch_user_data(user_id):
        try:
            # Simulate API call
            if user_id < 0:
                raise ValueError("Invalid user ID")
            return {"id": user_id, "name": "John"}
        except ValueError as e:
            # Convert to domain-specific exception
            raise APIError(f"API call failed: {str(e)}")

    try:
        fetch_user_data(-1)
    except APIError as e:
        print(f"❌ {e}")


# ============================================================================
# 9. NESTED RE-RAISING: Re-raise at multiple levels
# ============================================================================
def example_9_nested_reraise():
    """Re-raise through multiple function calls"""
    print("\n--- 9. Nested Re-raising ---")

    def level_1():
        raise ValueError("Error at level 1")

    def level_2():
        try:
            level_1()
        except ValueError as e:
            logger.error(f"Level 2 caught: {e}")
            raise  # Re-raise to level 3

    def level_3():
        try:
            level_2()
        except ValueError as e:
            print(f"❌ Level 3 caught: {e}")

    level_3()


# ============================================================================
# 10. RE-RAISING WITH MODIFIED STATE: Add context before re-raising
# ============================================================================
def example_10_reraise_with_context():
    """Add state/context before re-raising"""
    print("\n--- 10. Re-raising with Context ---")

    class OperationError(Exception):
        """Exception with context information"""

        def __init__(self, message, operation_id=None, attempt=None):
            self.message = message
            self.operation_id = operation_id
            self.attempt = attempt
            super().__init__(self.message)

    def risky_operation(operation_id):
        attempt = 0
        try:
            attempt += 1
            # Simulate error
            raise ValueError("Operation failed")
        except ValueError as e:
            # Wrap with context and re-raise
            raise OperationError(
                str(e), operation_id=operation_id, attempt=attempt
            ) from e

    try:
        risky_operation("OP_12345")
    except OperationError as e:
        print(f"❌ {e.message}")
        print(f"   Operation ID: {e.operation_id}")
        print(f"   Attempt: {e.attempt}")


# ============================================================================
# 11. CONDITIONAL RE-RAISING: Decide whether to re-raise
# ============================================================================
def example_11_conditional_reraise():
    """Re-raise exceptions based on conditions"""
    print("\n--- 11. Conditional Re-raising ---")

    def handle_error(error_code):
        try:
            if error_code < 100:
                raise ValueError(f"Error code {error_code} (recoverable)")
            else:
                raise RuntimeError(f"Error code {error_code} (critical)")
        except ValueError as e:
            print(f"⚠ Recoverable error: {e}")
            # Don't re-raise - handle it locally
        except RuntimeError as e:
            print(f"❌ Critical error: {e}")
            raise  # Re-raise critical errors

    try:
        handle_error(200)  # Will be re-raised
    except RuntimeError:
        print("❌ Program must exit due to critical error")


# ============================================================================
# 12. LOGGING AND RE-RAISING: Log details before propagating
# ============================================================================
def example_12_logging_reraise():
    """Log exception details before re-raising"""
    print("\n--- 12. Logging and Re-raising ---")

    def save_to_database(data):
        try:
            if not isinstance(data, dict):
                raise TypeError("Data must be a dictionary")
            print("✓ Data saved")
        except TypeError as e:
            # Log full traceback and details
            logger.error(f"Database operation failed: {e}", exc_info=True)
            raise  # Re-raise after logging

    try:
        save_to_database("not_a_dict")
    except TypeError:
        print("❌ Database operation failed and was logged")


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("ELSE BLOCK AND RE-RAISING EXCEPTIONS - COMPREHENSIVE EXAMPLES")
    print("=" * 70)

    example_1_else_block()
    example_2_else_with_multiple_exceptions()
    example_3_else_finally()
    example_4_simple_reraise()
    example_5_reraise_new_message()
    example_6_exception_chaining()
    example_7_selective_reraise()
    example_8_transform_exception()
    example_9_nested_reraise()
    example_10_reraise_with_context()
    example_11_conditional_reraise()
    example_12_logging_reraise()

    print("\n" + "=" * 70)
    print("Key Takeaways:")
    print("=" * 70)
    print("1. Use else block to execute code only if try succeeds")
    print("2. Use bare 'raise' to re-raise the original exception")
    print("3. Use 'raise from' to chain exceptions and preserve context")
    print("4. Transform exceptions to create domain-specific errors")
    print("5. Log exceptions before re-raising for better debugging")
    print("6. Use conditional re-raising to handle recoverable vs critical errors")
    print("7. Add context information to exceptions before re-raising")
    print("=" * 70)
