# 001 Intro to Object-Oriented Programming with Python
# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. It allows for the creation of reusable code and helps to organize complex programs.
# In Python, OOP is implemented using classes and objects, which are used to define and represent entities that have attributes and behavior.
# Here's an example of a simple OOP program in Python:
# pylint: disable=function-redefined  # Classes are intentionally redefined across sections to show progressive examples.
# 1. Defining a class
class Dog:
    """Represents a dog with a name and age."""

    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age  # Attribute

    def bark(self):  # Method
        return f"{self.name} says woof!"


# 2. Creating an object (instance) of the class
my_dog = Dog("Buddy", 3)
# 3. Accessing attributes and methods of the object
print(my_dog.name)  # Output: Buddy
print(my_dog.age)  # Output: 3
print(my_dog.bark())  # Output: Buddy says woof!
# 4. Creating another object (instance) of the class
another_dog = Dog("Max", 5)
print(another_dog.name)  # Output: Max
print(another_dog.age)  # Output: 5
print(another_dog.bark())  # Output: Max says woof!


# In this example, we defined a class called `Dog` with an initializer method `__init__` that sets the attributes `name` and `age`. We also defined a method called
# `bark` that returns a string when called. We then created two instances of the `Dog` class, `my_dog` and `another_dog`, and accessed their attributes and methods.
# 5. Inheritance in OOP
# Inheritance is a fundamental concept in OOP that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and can make it easier to create and maintain applications.
# Here's an example of inheritance in Python:
# 1. Defining a parent class
class Animal:
    """Base class representing an animal with a name."""

    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."


# 2. Defining a child class that inherits from the parent class
class Cat(Animal):
    """A cat that inherits from Animal and can meow."""

    def meow(self):
        return f"{self.name} says meow!"


# 3. Creating an object of the child class
my_cat = Cat("Whiskers")
# 4. Accessing attributes and methods of the child class
print(my_cat.name)  # Output: Whiskers (inherited from Animal)
print(my_cat.eat())  # Output: Whiskers is eating. (inherited from Animal)
print(my_cat.meow())  # Output: Whiskers says meow!


# In this example, we defined a parent class called `Animal` with an initializer method `__init__` and a method called `eat`. We then defined a child class called `Cat
# that inherits from `Animal` and has its own method called `meow`. We created an instance of the `Cat` class and accessed both the inherited attributes and methods from the `Animal` class, as well as the method defined in the `Cat` class.
# 6. Polymorphism in OOP
# Polymorphism is another fundamental concept in OOP that allows objects of different classes to be treated as objects of a common superclass. It is often achieved through method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class.
# Here's an example of polymorphism in Python:
# 1. Defining a parent class
class Shape:
    """Base class for geometric shapes."""

    def area(self):
        pass  # This method will be overridden in child classes


# 2. Defining child classes that inherit from the parent class and override the area method
class Circle(Shape):
    """A circle shape defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    """A rectangle shape defined by its width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 3. Creating objects of the child classes
circle = Circle(5)
rectangle = Rectangle(4, 6)
# 4. Accessing the area method of the child classes
print(f"Area of the circle: {circle.area()}")  # Output: Area of the circle: 78.5
print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 24


# In this example, we defined a parent class called `Shape` with a method `area` that is meant to be overridden. We then defined two child classes, `Circle` and `Rectangle`, that inherit from `Shape` and provide their own implementations of the `area` method. We created instances of both child classes and called their `area` methods, demonstrating polymorphism as both objects are treated as instances of the `Shape` class while still providing their specific implementations of the `area` method.
# 7. Encapsulation in OOP
# Encapsulation is a fundamental concept in OOP that refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, or class. It also involves restricting access to certain components of an object, which can help to prevent unintended interference and misuse of the data.
# In Python, encapsulation is often achieved using private attributes and methods, which are denoted by a double underscore prefix (`__`). Here's an example of encapsulation in Python:
# 1. Defining a class with encapsulation
class BankAccount:
    """A bank account with an owner and a protected balance."""

    def __init__(self, owner, balance=0):
        self.owner = owner  # Public attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def get_balance(self):
        return f"Current balance: {self._balance}"


# 2. Creating an object of the BankAccount class
account = BankAccount("Alice", 1000)
# 3. Accessing public attributes and methods
print(account.owner)  # Output: Alice
print(account.deposit(500))  # Output: Deposited 500. New balance: 1500
print(account.withdraw(200))  # Output: Withdrew 200. New balance: 1300
print(account.get_balance())  # Output: Current balance: 1300


# 4. Attempting to access the private attribute directly (this will raise an error)
# print(account.__balance)  # This will raise an AttributeError
# In this example, we defined a class called `BankAccount` with a public attribute `owner` and a private attribute `__balance`. We also defined methods for depositing, withdrawing, and getting the balance. We created an instance of the `BankAccount` class and accessed the public attributes and methods, while attempting to access the private attribute directly would result in an error, demonstrating encapsulation.
# 8. Inheritance and Polymorphism
# Inheritance and polymorphism can be combined to create more complex and flexible class hierarchies. For example, we can create a base class for different types of bank accounts and then create subclasses that inherit from it and provide specific implementations for certain methods.
# Here's an example:
# 1. Defining a base class for bank accounts
class BankAccount:
    """A bank account used as a base class for inheritance examples."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def get_balance(self):
        return f"Current balance: {self._balance}"


# 2. Defining a subclass for a savings account that inherits from BankAccount
class SavingsAccount(BankAccount):
    """A savings account that earns interest, inheriting from BankAccount."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)  # Call the initializer of the parent class
        self.interest_rate = interest_rate  # Additional attribute for savings account

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest}. New balance: {self._balance}"


# 3. Creating an object of the SavingsAccount class
savings_account = SavingsAccount("Bob", 2000, 0.02)
# 4. Accessing methods from the parent class and the child class
print(savings_account.owner)  # Output: Bob
print(savings_account.deposit(500))  # Output: Deposited 500. New balance: 2500
print(
    savings_account.apply_interest()
)  # Output: Applied interest: 50.0. New balance: 2550.0
print(savings_account.get_balance())  # Output: Current balance: 2550.0
# In this example, we defined a base class `BankAccount` and a subclass `SavingsAccount` that inherits from it.
# The `SavingsAccount` class has an additional attribute `interest_rate` and a method `apply_interest` that calculates and applies interest to the balance. We created an instance of the `SavingsAccount` class and accessed both the inherited methods from the `BankAccount` class and the new method defined in the `SavingsAccount` class, demonstrating both inheritance and polymorphism.

# 9. Encapsulation and Abstraction
# Encapsulation and abstraction are closely related concepts in OOP. Encapsulation refers to the bundling of data and methods within a class, while abstraction refers to the concept of hiding the complex implementation details and showing only the necessary features of an object.
# In Python, we can achieve abstraction by defining abstract classes and methods using the `abc` module. Here's an example:
from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract base class for bank accounts, defining the required interface."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return f"Current balance: {self._balance}"

    @abstractmethod
    def apply_interest(self):
        pass


class SavingsAccount(BankAccount):
    """A concrete savings account implementing the abstract BankAccount interface."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest}. New balance: {self._balance}"


# In this example, we defined an abstract base class `BankAccount` with abstract methods `deposit`, `withdraw`, and `apply_interest`. The `SavingsAccount` class inherits from `BankAccount` and provides concrete implementations for these abstract methods. This allows us to create a clear separation between the interface (the abstract class) and the implementation (the concrete subclass), demonstrating both encapsulation and abstraction in OOP.


# 10. Inheritance and Polymorphism
# Inheritance and polymorphism can be combined to create more complex and flexible class hierarchies. For example, we can create a base class for different types of bank accounts and then create subclasses that inherit from it and provide specific implementations for certain methods.
# Here's an example:
# 1. Defining a base class for bank accounts
class BankAccount:
    """A bank account demonstrating inheritance and polymorphism."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def get_balance(self):
        return f"Current balance: {self._balance}"


# 2. Defining a subclass for a savings account that inherits from BankAccount
class SavingsAccount(BankAccount):
    """A savings account that applies interest to the balance."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)  # Call the initializer of the parent class
        self.interest_rate = interest_rate  # Additional attribute for savings account

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest}. New balance: {self._balance}"


# 3. Creating an object of the SavingsAccount class
my_savings_account = SavingsAccount("John Doe", 1000, 0.05)

# 4. Calling methods on the object
print(my_savings_account.get_balance())  # Output: Current balance: 1000
print(my_savings_account.deposit(500))  # Output: Deposited 500. New balance: 1500
print(my_savings_account.withdraw(200))  # Output: Withdrew 200. New balance: 1300
print(
    my_savings_account.apply_interest()
)  # Output: Applied interest: 5.0. New balance: 1350

# In this example, we defined a base class `BankAccount` and a subclass `SavingsAccount` that inherits from it. The `SavingsAccount` class has an additional attribute `interest_rate` and a method `apply_interest` that calculates and applies interest to the balance. We created an instance of the `SavingsAccount` class and accessed both the inherited methods from the `BankAccount` class and the new method defined in the `SavingsAccount` class, demonstrating both inheritance and polymorphism.

# 11. Encapsulation and Abstraction
# Encapsulation and abstraction are closely related concepts in OOP. Encapsulation refers to the bundling of data and methods within a class, while abstraction refers to the concept of hiding the complex implementation details and showing only the necessary features of an object.
# In Python, we can achieve abstraction by defining abstract classes and methods using the `abc` module. Here's an example:
from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract bank account combining encapsulation and abstraction."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return f"Current balance: {self._balance}"

    @abstractmethod
    def apply_interest(self):
        pass


class SavingsAccount(BankAccount):
    """A savings account implementing the abstract BankAccount with interest support."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest}. New balance: {self._balance}"


# In this example, we defined an abstract base class `BankAccount` with abstract methods `deposit`, `withdraw`, and `apply_interest`. The `SavingsAccount` class inherits from `BankAccount` and provides concrete implementations for these abstract methods. This allows us to create a clear separation between the interface (the abstract class) and the implementation (the concrete subclass), demonstrating both encapsulation and abstraction in OOP.


# 12. Polymorphism
# Polymorphism is a concept in OOP where objects of different classes can be treated as instances of a common superclass. In Python, this is achieved through method overriding and method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. Here's an example:
class BankAccount:
    """A bank account serving as a polymorphic base class."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def get_balance(self):
        return f"Current balance: {self._balance}"


class SavingsAccount(BankAccount):
    """A savings account that overrides no withdrawal behaviour but adds interest."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest}. New balance: {self._balance}"


class CheckingAccount(BankAccount):
    """A checking account that allows withdrawals up to an overdraft limit."""

    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount exceeds the balance and overdraft limit."


# In this example, we have a base class `BankAccount` and two subclasses `SavingsAccount` and `CheckingAccount`. Both subclasses inherit from `BankAccount` and provide their own implementations of the `withdraw` method. This allows us to treat both `SavingsAccount` and `CheckingAccount` objects as instances of the `BankAccount` class while still providing specific behavior for each type of account, demonstrating polymorphism in OOP.

# 13. Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. In Python, we can achieve abstraction using abstract classes and methods. Here's an example:
from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract base class enforcing a contract for all bank account types."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return f"Current balance: {self._balance}"

    @abstractmethod
    def apply_interest(self):
        pass


class SavingsAccount(BankAccount):
    """A fully concrete savings account implementing the abstract BankAccount contract."""

    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Applied interest: {interest}. New balance: {self._balance}"


# In this example, we defined an abstract base class `BankAccount` with abstract methods `deposit`, `withdraw`, and `apply_interest`. The `SavingsAccount` class inherits from `BankAccount` and provides concrete implementations for these abstract methods. This allows us to create a clear separation between the interface (the abstract class) and the implementation (the concrete subclass), demonstrating abstraction in OOP.
