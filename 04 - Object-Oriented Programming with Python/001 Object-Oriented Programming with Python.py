# Object-Oriented Programming (OOP) in Python
# OOP allows creation of reusable code through classes and objects with attributes and behavior.
from abc import ABC, abstractmethod


# ============================================================================
# 1. BASIC CONCEPTS: Classes and Objects
# ============================================================================


class Dog:
    """Simple class demonstrating basic attributes and methods."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


# Example usage
my_dog = Dog("Buddy", 3)
print(my_dog.name, my_dog.age, my_dog.bark())

another_dog = Dog("Max", 5)
print(another_dog.name, another_dog.age, another_dog.bark())


# ============================================================================
# 2. INHERITANCE: Reusing Code with Parent/Child Classes
# ============================================================================


class Animal:
    """Parent class with common animal behavior."""

    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."


class Cat(Animal):
    """Child class that inherits from Animal."""

    def meow(self):
        return f"{self.name} says meow!"


# Example usage
my_cat = Cat("Whiskers")
print(my_cat.name, my_cat.eat(), my_cat.meow())


# ============================================================================
# 3. POLYMORPHISM: Method Overriding
# ============================================================================


class Shape:
    """Parent class defining shape interface."""

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")


# ============================================================================
# 4. ENCAPSULATION: Data Hiding with Private Attributes
# ============================================================================


class BankAccount:
    """Bank account with protected balance attribute."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = (
            balance  # Protected: accessible to subclasses, hidden from outside
        )

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        return "Invalid withdrawal amount."

    def get_balance(self):
        return self._balance


# Example usage
account = BankAccount("Alice", 1000)
print(account.owner)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: {account.get_balance()}")


# ============================================================================
# 5. INHERITANCE + POLYMORPHISM: Specialized Account Types
# ============================================================================


class SavingsAccount(BankAccount):
    """Savings account with interest."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest:.2f}. New balance: {self._balance:.2f}"


class CheckingAccount(BankAccount):
    """Checking account with overdraft protection."""

    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        max_withdrawal = self._balance + self.overdraft_limit
        if 0 < amount <= max_withdrawal:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        return "Exceeds balance and overdraft limit."


# Example usage
savings = SavingsAccount("Bob", 2000, 0.02)
print(savings.deposit(500))
print(savings.apply_interest())
print(f"Balance: {savings.get_balance()}")

checking = CheckingAccount("Carol", 500, 200)
print(checking.withdraw(600))  # Uses overdraft
print(f"Balance: {checking.get_balance()}")


# ============================================================================
# 6. ABSTRACTION: Abstract Base Classes
# ============================================================================


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    """Concrete implementation of Vehicle."""

    def start(self):
        return f"{self.make} {self.model} engine started."

    def stop(self):
        return f"{self.make} {self.model} engine stopped."


class Motorcycle(Vehicle):
    """Concrete implementation of Vehicle."""

    def start(self):
        return f"{self.make} {self.model} motorcycle started."

    def stop(self):
        return f"{self.make} {self.model} motorcycle stopped."


# Example usage
vehicles = [Car("Toyota", "Camry"), Motorcycle("Harley", "Davidson")]
for vehicle in vehicles:
    print(vehicle.start())
    print(vehicle.stop())
