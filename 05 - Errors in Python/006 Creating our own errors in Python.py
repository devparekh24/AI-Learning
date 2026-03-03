# 006 Creating our own errors in Python
# In Python, you can create custom errors by defining a class that inherits from the built-in Exception class.
# This allows you to create specific error types that provide meaningful information about what went wrong.

from datetime import datetime
from typing import Optional


# ============================================================================
# 1. BASIC CUSTOM EXCEPTION: Simple inheritance from Exception
# ============================================================================
class AuthenticationError(Exception):
    """Raised when authentication fails"""

    pass


def example_1_basic_custom():
    """Create and raise a basic custom exception"""
    print("\n--- 1. Basic Custom Exception ---")

    def login(username, password):
        if password != "secret":
            raise AuthenticationError("Invalid credentials.")
        return f"Welcome {username}!"

    try:
        login("alice", "wrongpass")
    except AuthenticationError as e:
        print(f"❌ {e}")


# ============================================================================
# 2. CUSTOM EXCEPTION WITH MESSAGE: Enhanced message handling
# ============================================================================
class ValidationError(Exception):
    """Raised when input validation fails"""

    def __init__(self, field_name, reason):
        self.field_name = field_name
        self.reason = reason
        super().__init__(f"Validation failed for '{field_name}': {reason}")


def example_2_with_message():
    """Custom exception with structured message"""
    print("\n--- 2. Custom Exception with Message ---")

    def validate_email(email):
        if "@" not in email:
            raise ValidationError("email", "Missing @ symbol")
        if email.count("@") > 1:
            raise ValidationError("email", "Multiple @ symbols")
        return email

    try:
        validate_email("invalid_email")
    except ValidationError as e:
        print(f"❌ {e}")


# ============================================================================
# 3. CUSTOM EXCEPTION WITH ATTRIBUTES: Store multiple data points
# ============================================================================
class BusinessError(Exception):
    """Raised for business logic violations"""

    def __init__(self, message, error_code, severity="normal"):
        self.message = message
        self.error_code = error_code
        self.severity = severity
        self.timestamp = datetime.now()
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.error_code}] {self.message} (Severity: {self.severity})"


def example_3_with_attributes():
    """Custom exception with multiple attributes"""
    print("\n--- 3. Custom Exception with Attributes ---")

    def withdraw_money(account_balance, amount):
        if amount > account_balance:
            raise BusinessError(
                message="Insufficient funds", error_code="INSUFF_001", severity="high"
            )
        return account_balance - amount

    try:
        withdraw_money(100, 200)
    except BusinessError as e:
        print(f"❌ {e}")
        print(f"   Code: {e.error_code}")
        print(f"   Timestamp: {e.timestamp}")


# ============================================================================
# 4. CUSTOM EXCEPTION HIERARCHY: Parent and child exceptions
# ============================================================================
class ApplicationError(Exception):
    """Base exception for all application errors"""

    pass


class DatabaseError(ApplicationError):
    """Raised when database operations fail"""

    pass


class ConnectionError(DatabaseError):
    """Raised when database connection fails"""

    pass


class QueryError(DatabaseError):
    """Raised when database query fails"""

    pass


def example_4_exception_hierarchy():
    """Create and handle exception hierarchies"""
    print("\n--- 4. Exception Hierarchy ---")

    def execute_query(query):
        if query == "":
            raise QueryError("Query cannot be empty")
        if query == "connect_fail":
            raise ConnectionError("Failed to connect to database")
        return "Query executed successfully"

    try:
        execute_query("")
    except ConnectionError as e:
        print(f"❌ Connection Error: {e}")
    except QueryError as e:
        print(f"❌ Query Error: {e}")
    except DatabaseError as e:
        print(f"❌ Database Error: {e}")

    # Catch all application errors
    try:
        execute_query("connect_fail")
    except ApplicationError as e:
        print(f"❌ Application Error: {e}")


# ============================================================================
# 5. CUSTOM EXCEPTION WITH __STR__ AND __REPR__: Better representations
# ============================================================================
class ConfigurationError(Exception):
    """Raised when configuration is invalid"""

    def __init__(self, setting_name, expected_type, got_type):
        self.setting_name = setting_name
        self.expected_type = expected_type
        self.got_type = got_type
        super().__init__()

    def __str__(self):
        return (
            f"Configuration Error: '{self.setting_name}' "
            f"expects {self.expected_type.__name__} "
            f"but got {self.got_type.__name__}"
        )

    def __repr__(self):
        return (
            f"ConfigurationError(setting_name='{self.setting_name}', "
            f"expected={self.expected_type.__name__}, "
            f"got={self.got_type.__name__})"
        )


def example_5_str_repr():
    """Custom exception with __str__ and __repr__"""
    print("\n--- 5. Custom Exception with __str__ and __repr__ ---")

    def set_config(setting, value, expected_type):
        if not isinstance(value, expected_type):
            raise ConfigurationError(setting, expected_type, type(value))
        return value

    try:
        set_config("timeout", "not_a_number", int)
    except ConfigurationError as e:
        print(f"❌ {e}")
        print(f"   repr: {repr(e)}")


# ============================================================================
# 6. CUSTOM EXCEPTION WITH RECOVERY OPTIONS: Include solutions
# ============================================================================
class EnvironmentError(Exception):
    """Raised when environment variables are missing"""

    def __init__(self, variable_name, suggestion):
        self.variable_name = variable_name
        self.suggestion = suggestion
        super().__init__(f"Missing environment variable: {variable_name}")

    def get_solution(self):
        return f"Solution: {self.suggestion}"


def example_6_with_solutions():
    """Custom exception with recovery suggestions"""
    print("\n--- 6. Custom Exception with Solutions ---")

    def get_env_variable(var_name):
        env_vars = {"API_KEY": "set_API_KEY_env_variable"}
        if var_name not in env_vars:
            raise EnvironmentError(
                var_name, "Set the environment variable in your shell or .env file"
            )
        return env_vars[var_name]

    try:
        get_env_variable("API_KEY")
    except EnvironmentError as e:
        print(f"❌ {e}")
        print(f"   {e.get_solution()}")


# ============================================================================
# 7. CUSTOM EXCEPTION FOR RETRIES: Include retry information
# ============================================================================
class RetryableError(Exception):
    """Raised for errors that can be retried"""

    def __init__(self, message, max_retries=3, wait_seconds=2):
        self.message = message
        self.max_retries = max_retries
        self.wait_seconds = wait_seconds
        self.attempt = 0
        super().__init__(self.message)

    def should_retry(self):
        self.attempt += 1
        return self.attempt < self.max_retries


def example_7_retryable_error():
    """Custom exception for retryable operations"""
    print("\n--- 7. Retryable Error ---")

    def unstable_operation(attempt):
        if attempt < 2:
            raise RetryableError("Connection timeout", max_retries=3, wait_seconds=1)
        return "Success on attempt " + str(attempt)

    error = None
    for i in range(1, 4):
        try:
            result = unstable_operation(i)
            print(f"✓ {result}")
            break
        except RetryableError as e:
            error = e
            if i < 3:
                print(f"❌ Attempt {i} failed: {e}. Retrying...")
            else:
                print(f"❌ Failed after {i} attempts")


# ============================================================================
# 8. CUSTOM EXCEPTION WITH CONTEXT: Store related information
# ============================================================================
class PaymentError(Exception):
    """Raised when payment processing fails"""

    def __init__(
        self,
        reason,
        transaction_id: Optional[str] = None,
        amount: Optional[float] = None,
    ):
        self.reason = reason
        self.transaction_id = transaction_id
        self.amount = amount
        super().__init__(reason)

    def get_context(self):
        context = {"reason": self.reason}
        if self.transaction_id:
            context["transaction_id"] = self.transaction_id
        if self.amount:
            context["amount"] = self.amount
        return context


def example_8_with_context():
    """Custom exception with contextual information"""
    print("\n--- 8. Exception with Context ---")

    def process_payment(amount, transaction_id):
        if amount <= 0:
            raise PaymentError(
                reason="Invalid amount", transaction_id=transaction_id, amount=amount
            )
        return f"Payment of ${amount} processed"

    try:
        process_payment(-50, "TXN_12345")
    except PaymentError as e:
        print(f"❌ {e}")
        print(f"   Context: {e.get_context()}")


# ============================================================================
# 9. DOMAIN-SPECIFIC CUSTOM EXCEPTIONS: Real-world example
# ============================================================================
class GameError(Exception):
    """Base class for game errors"""

    pass


class InsufficientHealthError(GameError):
    """Raised when character health is too low"""

    def __init__(self, current_health):
        self.current_health = current_health
        super().__init__(f"Health too low: {current_health}/100")


class InvalidMoveError(GameError):
    """Raised when move is invalid"""

    def __init__(self, move, valid_moves):
        self.move = move
        self.valid_moves = valid_moves
        super().__init__(f"Invalid move '{move}'. Valid: {valid_moves}")


def example_9_domain_specific():
    """Create domain-specific exception hierarchy"""
    print("\n--- 9. Domain-Specific Exceptions (Game) ---")

    def attack(current_health, damage):
        if current_health - damage <= 0:
            raise InsufficientHealthError(current_health - damage)
        return current_health - damage

    def move(direction):
        valid = ["up", "down", "left", "right"]
        if direction not in valid:
            raise InvalidMoveError(direction, valid)
        return f"Moved {direction}"

    try:
        attack(10, 20)
    except InsufficientHealthError as e:
        print(f"❌ {e}")

    try:
        move("diagonal")
    except InvalidMoveError as e:
        print(f"❌ {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("CREATING CUSTOM ERRORS IN PYTHON - COMPREHENSIVE EXAMPLES")
    print("=" * 70)

    example_1_basic_custom()
    example_2_with_message()
    example_3_with_attributes()
    example_4_exception_hierarchy()
    example_5_str_repr()
    example_6_with_solutions()
    example_7_retryable_error()
    example_8_with_context()
    example_9_domain_specific()

    print("\n" + "=" * 70)
    print("Key Takeaways:")
    print("=" * 70)
    print("1. Inherit from Exception to create custom exceptions")
    print("2. Use descriptive names for custom exceptions")
    print("3. Add attributes to store contextual information")
    print("4. Create exception hierarchies for related errors")
    print("5. Implement __str__() and __repr__() for better representations")
    print("6. Include recovery suggestions or solutions")
    print("7. Use custom exceptions to make error handling domain-specific")
    print("=" * 70)
