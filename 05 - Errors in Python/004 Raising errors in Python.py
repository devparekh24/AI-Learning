# 004 Raising errors in Python
# In Python, you can raise errors using the 'raise' keyword followed by an exception type and an optional message.
# This allows you to signal that something went wrong in your code and provide meaningful error information.

import math
import traceback


# ============================================================================
# 1. RAISING BUILT-IN EXCEPTIONS: Common exception types
# ============================================================================
def example_1_raise_built_in():
    """Raise built-in exceptions with descriptive messages"""
    print("\n--- 1. Raising Built-in Exceptions ---")

    # ValueError
    def calculate_square_root(x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(x)

    try:
        result = calculate_square_root(-4)
    except ValueError as e:
        print(f"❌ ValueError: {e}")

    # TypeError
    def add_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return a + b

    try:
        result = add_numbers(5, "10")
    except TypeError as e:
        print(f"❌ TypeError: {e}")

    # ZeroDivisionError
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    try:
        result = divide(10, 0)
    except ZeroDivisionError as e:
        print(f"❌ ZeroDivisionError: {e}")


# ============================================================================
# 2. SIMPLE CUSTOM EXCEPTION: Inherit from Exception
# ============================================================================
class InvalidAgeError(Exception):
    """Raised when age is invalid"""

    pass


def example_2_simple_custom():
    """Create and raise a simple custom exception"""
    print("\n--- 2. Simple Custom Exception ---")

    def set_age(age):
        if age < 0 or age > 150:
            raise InvalidAgeError(f"Age must be between 0 and 150, got {age}.")
        return age

    try:
        set_age(-5)
    except InvalidAgeError as e:
        print(f"❌ Custom Error: {e}")


# ============================================================================
# 3. CUSTOM EXCEPTION WITH ATTRIBUTES: Store additional data
# ============================================================================
class APIError(Exception):
    """Raised when API request fails"""

    def __init__(self, message, status_code, endpoint):
        self.message = message
        self.status_code = status_code
        self.endpoint = endpoint
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} [Code: {self.status_code}] [Endpoint: {self.endpoint}]"


def example_3_custom_with_attributes():
    """Custom exception with multiple attributes"""
    print("\n--- 3. Custom Exception with Attributes ---")

    def fetch_user(user_id, endpoint):
        if user_id < 0:
            raise APIError(
                message="Invalid user ID", status_code=400, endpoint=endpoint
            )
        return f"User {user_id}"

    try:
        fetch_user(-1, "/api/users")
    except APIError as e:
        print(f"❌ {e}")
        print(f"   Status: {e.status_code}")


# ============================================================================
# 4. CUSTOM EXCEPTION HIERARCHY: Organize related errors
# ============================================================================
class ValidationError(Exception):
    """Base class for validation errors"""

    pass


class EmailError(ValidationError):
    """Raised when email is invalid"""

    pass


class PasswordError(ValidationError):
    """Raised when password is invalid"""

    pass


def example_4_exception_hierarchy():
    """Create hierarchy of related exceptions"""
    print("\n--- 4. Exception Hierarchy ---")

    def validate_email(email):
        if "@" not in email:
            raise EmailError(f"Invalid email format: {email}")
        return email

    def validate_password(password):
        if len(password) < 8:
            raise PasswordError("Password must be at least 8 characters.")
        return password

    try:
        validate_email("invalid_email")
    except EmailError as e:
        print(f"❌ Email Error: {e}")

    try:
        validate_password("123")
    except PasswordError as e:
        print(f"❌ Password Error: {e}")

    # Catch all validation errors at once
    try:
        validate_email("test@example.com")
        print("✓ Email valid")
    except ValidationError as e:
        print(f"❌ Validation Error: {e}")


# ============================================================================
# 5. CONDITIONAL RAISING: Raise based on validations
# ============================================================================
def example_5_conditional_raising():
    """Raise exceptions based on multiple conditions"""
    print("\n--- 5. Conditional Raising ---")

    def process_transaction(amount, account_balance, min_amount=100):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount < min_amount:
            raise ValueError(f"Minimum transaction amount is ${min_amount}.")
        if account_balance < amount:
            raise ValueError(f"Insufficient balance. Available: ${account_balance}")
        return account_balance - amount

    try:
        new_balance = process_transaction(150, 100)
    except ValueError as e:
        print(f"❌ Transaction failed: {e}")


# ============================================================================
# 6. RAISING FROM ANOTHER EXCEPTION: Preserve exception context
# ============================================================================
def example_6_raise_from():
    """Use 'raise from' to chain exceptions"""
    print("\n--- 6. Raising From Another Exception (Exception Chaining) ---")

    def parse_config(config_str):
        try:
            # Simulate parsing error
            data = eval(config_str)
        except SyntaxError as e:
            raise ValueError("Invalid configuration format.") from e

    try:
        parse_config("{ invalid syntax }")
    except ValueError as e:
        print(f"❌ {e}")
        print(f"   Caused by: {type(e.__cause__).__name__}")


# ============================================================================
# 7. CUSTOM EXCEPTION WITH FORMATTING: Enhanced error messages
# ============================================================================
class DatabaseError(Exception):
    """Raised when database operation fails"""

    def __init__(self, operation, table, details):
        self.operation = operation
        self.table = table
        self.details = details
        super().__init__()

    def __str__(self):
        return (
            f"Database Error: {self.operation} on table '{self.table}' - {self.details}"
        )


def example_7_custom_with_formatting():
    """Custom exception with formatted error message"""
    print("\n--- 7. Custom Exception with Formatting ---")

    def delete_record(table_name, record_id):
        if record_id == 0:
            raise DatabaseError(
                operation="DELETE", table=table_name, details="Invalid record ID"
            )
        return True

    try:
        delete_record("users", 0)
    except DatabaseError as e:
        print(f"❌ {e}")


# ============================================================================
# 8. RAISING WITH DEFENSIVE PROGRAMMING: Type checking
# ============================================================================
def example_8_defensive_raising():
    """Raise appropriate exceptions for type safety"""
    print("\n--- 8. Defensive Programming (Type Checking) ---")

    def process_list(items):
        if not isinstance(items, list):
            raise TypeError(f"Expected list, got {type(items).__name__}")
        if len(items) == 0:
            raise ValueError("List cannot be empty")
        return sum(items)

    try:
        process_list("not a list")
    except TypeError as e:
        print(f"❌ {e}")

    try:
        process_list([])
    except ValueError as e:
        print(f"❌ {e}")


# ============================================================================
# 9. RAISING IN CONTEXT: With traceback information
# ============================================================================
def example_9_raise_with_traceback():
    """Demonstrate raising with traceback information"""
    print("\n--- 9. Raising with Traceback ---")

    def risky_operation():
        raise RuntimeError("Something went wrong in risky_operation")

    def wrapper_function():
        try:
            risky_operation()
        except RuntimeError:
            print("❌ Error caught, here's the traceback:")
            print("-" * 50)
            traceback.print_exc()
            print("-" * 50)


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("RAISING ERRORS IN PYTHON - COMPREHENSIVE EXAMPLES")
    print("=" * 70)

    example_1_raise_built_in()
    example_2_simple_custom()
    example_3_custom_with_attributes()
    example_4_exception_hierarchy()
    example_5_conditional_raising()
    example_6_raise_from()
    example_7_custom_with_formatting()
    example_8_defensive_raising()
    example_9_raise_with_traceback()

    print("\n" + "=" * 70)
    print("Key Takeaways:")
    print("=" * 70)
    print("1. Use built-in exceptions when appropriate (ValueError, TypeError, etc.)")
    print("2. Create custom exceptions by inheriting from Exception")
    print("3. Add attributes to exceptions for more context")
    print("4. Create exception hierarchies for related errors")
    print("5. Use 'raise from' to preserve exception chains")
    print("6. Use descriptive error messages")
    print("7. Validate inputs and raise appropriate exceptions early")
    print("=" * 70)
