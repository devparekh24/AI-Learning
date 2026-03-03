# 008 Dealing with Python errors
# Comprehensive guide to handling errors gracefully in Python using try-except blocks,
# exception inspection, defensive programming, and error recovery strategies.

import sys
import logging
from typing import Optional, Any

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# 1. BASIC TRY-EXCEPT: Handle a single exception type
# ============================================================================
def example_1_basic_handling():
    """Basic error handling with try-except"""
    print("\n--- 1. Basic Try-Except ---")

    try:
        number = int("abc")  # This will raise a ValueError
    except ValueError as e:
        print(f"❌ Caught ValueError: {e}")

    print("✓ Program continues after error handling")


# ============================================================================
# 2. MULTIPLE EXCEPTIONS IN ONE HANDLER: Tuple of exception types
# ============================================================================
def example_2_multiple_exceptions_tuple():
    """Handle multiple exception types in a single handler"""
    print("\n--- 2. Multiple Exceptions in One Handler ---")

    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print(f"❌ Caught a math/type error: {type(e).__name__}: {e}")


# ============================================================================
# 3. MULTIPLE HANDLERS: Different handlers for different exceptions
# ============================================================================
def example_3_multiple_handlers():
    """Handle different exceptions with different handlers"""
    print("\n--- 3. Multiple Handlers ---")

    try:
        data = {"name": "Alice"}
        # Try different operations that might fail
        age = int(data["age"])  # KeyError or ValueError
    except KeyError as e:
        print(f"❌ Key not found in dictionary: {e}")
    except ValueError as e:
        print(f"❌ Value conversion failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# ============================================================================
# 4. EXCEPTION ATTRIBUTES: Access error information
# ============================================================================
def example_4_exception_attributes():
    """Inspect exception objects for detailed information"""
    print("\n--- 4. Exception Attributes ---")

    try:
        my_list = [1, 2, 3]
        value = my_list[10]  # IndexError
    except IndexError as error:
        print(f"❌ Error Type: {type(error).__name__}")
        print(f"   Error Message: {error}")
        print(f"   Error Args: {error.args}")
        print(f"   String Representation: {str(error)}")


# ============================================================================
# 5. ELSE BLOCK: Execute code only if no exception occurs
# ============================================================================
def example_5_else_block():
    """Use else block for success path"""
    print("\n--- 5. Else Block ---")

    try:
        number = int("123")
    except ValueError as e:
        print(f"❌ Conversion failed: {e}")
    else:
        print(f"✓ Success! Converted to: {number}")
        print(f"✓ This only runs if no exception occurred")


# ============================================================================
# 6. FINALLY BLOCK: Cleanup code that always runs
# ============================================================================
def example_6_finally_block():
    """Finally block always executes"""
    print("\n--- 6. Finally Block ---")

    try:
        result = 10 / 2
        print(f"✓ Result: {result}")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
    else:
        print("✓ Division was successful")
    finally:
        print("✓ Cleanup/finally: Always executes regardless of exception")


# ============================================================================
# 7. ALL BLOCKS TOGETHER: try-except-else-finally
# ============================================================================
def example_7_all_blocks():
    """Comprehensive example with all block types"""
    print("\n--- 7. All Blocks Together ---")

    def process_score(score_str):
        try:
            score = int(score_str)
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")
            print(f"✓ Score valid: {score}")
        except ValueError as e:
            print(f"❌ Invalid score: {e}")
        else:
            print(f"✓ Else: Score {score} accepted")
            return score
        finally:
            print("✓ Finally: Processing complete")

    process_score("85")
    print()
    process_score("invalid")


# ============================================================================
# 8. EXCEPTION TYPE INSPECTION: Check error type and respond accordingly
# ============================================================================
def example_8_type_inspection():
    """Respond differently based on exception type"""
    print("\n--- 8. Exception Type Inspection ---")

    def handle_operation(operation_type, value):
        try:
            if operation_type == "convert":
                result = int(value)
            elif operation_type == "divide":
                result = 10 / int(value)
            else:
                raise ValueError("Unknown operation")
        except ZeroDivisionError:
            print("❌ Division by zero occurred")
        except ValueError:
            print(f"❌ ValueError in {operation_type}")
        except Exception as e:
            print(f"❌ Unexpected error: {type(e).__name__}")
        else:
            print(f"✓ {operation_type} succeeded: {result}")

    handle_operation("convert", "42")
    handle_operation("divide", "0")
    handle_operation("divide", "5")


# ============================================================================
# 9. DEFENSIVE PROGRAMMING: Validate before operations
# ============================================================================
def example_9_defensive_programming():
    """Prevent errors through validation"""
    print("\n--- 9. Defensive Programming ---")

    def safe_divide(a, b):
        # Defensive checks before try block
        if not isinstance(a, (int, float)):
            print(f"❌ First argument must be a number, got {type(a).__name__}")
            return None
        if not isinstance(b, (int, float)):
            print(f"❌ Second argument must be a number, got {type(b).__name__}")
            return None

        try:
            result = a / b
            print(f"✓ {a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            print("❌ Cannot divide by zero")
            return None

    safe_divide(10, 2)
    safe_divide("10", 2)
    safe_divide(10, 0)


# ============================================================================
# 10. ASSERTIONS: Quick validation during development
# ============================================================================
def example_10_assertions():
    """Use assertions for pre-condition checking"""
    print("\n--- 10. Assertions ---")

    try:
        # Assertion fails if condition is False
        assert 1 + 1 == 2, "Math is broken!"
        print("✓ Assertion 1 passed: 1 + 1 == 2")

        result = 10 * 5
        assert result == 50, f"Expected 50, got {result}"
        print("✓ Assertion 2 passed: 10 * 5 == 50")

        # This will fail
        assert 5 > 10, "5 is not greater than 10"
    except AssertionError as e:
        print(f"❌ Assertion failed: {e}")


# ============================================================================
# 11. ERROR RECOVERY: Different strategies for different errors
# ============================================================================
def example_11_error_recovery():
    """Recover from errors with alternative approaches"""
    print("\n--- 11. Error Recovery ---")

    def read_user_preference(user_data, key, default=None):
        """Try multiple sources for a value"""
        try:
            # Try primary source
            return user_data[key]
        except KeyError:
            print(f"⚠ Key '{key}' not found, using default")
            return default
        except TypeError:
            print(f"⚠ user_data is not a dictionary, returning default")
            return default

    user_data = {"name": "Alice"}
    age = read_user_preference(user_data, "age", default=18)
    print(f"✓ Age: {age}")

    name = read_user_preference(None, "name", default="Unknown")
    print(f"✓ Name: {name}")


# ============================================================================
# 12. LOGGING ERRORS: Record errors for debugging
# ============================================================================
def example_12_logging_errors():
    """Log errors for debugging and monitoring"""
    print("\n--- 12. Logging Errors ---")

    def process_file(filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(f"✓ File read successfully")
                return content
        except FileNotFoundError:
            logger.warning(f"File not found: {filename}")
            print(f"⚠ File '{filename}' not found")
        except IOError as e:
            logger.error(f"IO error reading {filename}: {e}", exc_info=True)
            print(f"❌ Failed to read file: {e}")
        except Exception as e:
            logger.critical(f"Unexpected error: {e}", exc_info=True)
            print(f"❌ Unexpected error: {e}")

    process_file("/nonexistent/file.txt")


# ============================================================================
# 13. SAFE FALLBACKS: Graceful degradation
# ============================================================================
def example_13_safe_fallbacks():
    """Provide fallback values when errors occur"""
    print("\n--- 13. Safe Fallbacks ---")

    def get_config_value(config, key, fallback):
        """Get config value with automatic fallback"""
        try:
            value = config[key]
            if not value:  # Check for empty/None
                raise ValueError(f"Value for '{key}' is empty")
            return value
        except (KeyError, TypeError, ValueError):
            print(f"⚠ Using fallback for '{key}': {fallback}")
            return fallback

    config = {"username": "alice", "password": ""}
    username = get_config_value(config, "username", "guest")
    password = get_config_value(config, "password", "default_pass")
    timeout = get_config_value(config, "timeout", 30)

    print(f"✓ Config - Username: {username}, Password: {password}, Timeout: {timeout}")


# ============================================================================
# 14. CUSTOM ERROR MESSAGES: Provide context-specific messages
# ============================================================================
def example_14_custom_messages():
    """Provide meaningful error messages for users"""
    print("\n--- 14. Custom Error Messages ---")

    def calculate_percentage(part, total):
        """Calculate percentage with user-friendly error messages"""
        try:
            if total == 0:
                raise ValueError("Total cannot be zero")
            if part < 0 or total < 0:
                raise ValueError("Values cannot be negative")
            percentage = (part / total) * 100
            print(f"✓ {part} out of {total} = {percentage:.2f}%")
            return percentage
        except ValueError as e:
            print(f"❌ Invalid input: {e}")
        except TypeError:
            print(f"❌ Please provide numeric values (numbers, not text)")

    calculate_percentage(25, 100)
    calculate_percentage(50, 0)
    calculate_percentage(-10, 100)


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("DEALING WITH PYTHON ERRORS - COMPREHENSIVE GUIDE")
    print("=" * 70)

    example_1_basic_handling()
    example_2_multiple_exceptions_tuple()
    example_3_multiple_handlers()
    example_4_exception_attributes()
    example_5_else_block()
    example_6_finally_block()
    example_7_all_blocks()
    example_8_type_inspection()
    example_9_defensive_programming()
    example_10_assertions()
    example_11_error_recovery()
    example_12_logging_errors()
    example_13_safe_fallbacks()
    example_14_custom_messages()

    print("\n" + "=" * 70)
    print("Key Strategies for Dealing with Errors:")
    print("=" * 70)
    print("1. Use try-except blocks to catch predictable errors")
    print("2. Handle different exception types appropriately")
    print("3. Use else block for success path code")
    print("4. Use finally block for cleanup (file handling, resource cleanup)")
    print("5. Implement defensive programming (validate inputs early)")
    print("6. Provide meaningful error messages to users")
    print("7. Log errors for debugging and monitoring")
    print("8. Gracefully degrade with fallback values")
    print("9. Use assertions during development for quick validation")
    print("10. Don't catch Exception too broadly - be specific when possible")
    print("=" * 70)
