# Python Exception Hierarchy & Custom Exceptions - Study Notes

## What are Exceptions?

Exceptions are events that occur during program execution that disrupt the normal flow of instructions. When Python encounters an error, it raises an exception. If not handled, the program terminates.

## The Exception Hierarchy

Python organizes exceptions in a hierarchical tree structure. Understanding this hierarchy is crucial for effective error handling.

### Complete Hierarchy Structure

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError
    ├── AttributeError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   ├── FileExistsError
    │   └── IsADirectoryError
    ├── RuntimeError
    │   ├── RecursionError
    │   └── NotImplementedError
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    └── Warning
        ├── DeprecationWarning
        ├── SyntaxWarning
        └── UserWarning
```

### Key Classes Explained

**BaseException**: The base class for all built-in exceptions. You should rarely catch this directly.

**Exception**: The base class for all non-system-exiting exceptions. This is what you should inherit from when creating custom exceptions.

**ArithmeticError**: Base class for arithmetic errors (division, overflow, etc.)

**LookupError**: Base class for errors raised when a key or index is invalid.

**OSError**: Base class for operating system errors (file operations, permissions, etc.)

## How Inheritance Works in Exception Handling

When you catch a parent exception class, you automatically catch all its child exceptions.

```python
# Catching a parent catches all children
try:
    my_list = [1, 2, 3]
    print(my_list[10])  # Raises IndexError
except LookupError:  # Catches IndexError because it's a child
    print("Lookup error occurred")
```

### Exception Handling Order

The order of except blocks matters. Python checks them from top to bottom and uses the first match.

```python
# WRONG - General exception first
try:
    result = 10 / 0
except Exception:  # This catches everything
    print("General exception")
except ZeroDivisionError:  # This will NEVER execute
    print("Division by zero")

# CORRECT - Specific exceptions first
try:
    result = 10 / 0
except ZeroDivisionError:  # Specific exception first
    print("Division by zero")
except ArithmeticError:  # More general
    print("Arithmetic error")
except Exception:  # Most general last
    print("General exception")
```

## Common Built-in Exceptions

**ValueError**: Raised when a function receives an argument of correct type but inappropriate value.

**TypeError**: Raised when an operation is applied to an object of inappropriate type.

**IndexError**: Raised when trying to access an index that doesn't exist in a sequence.

**KeyError**: Raised when trying to access a dictionary key that doesn't exist.

**FileNotFoundError**: Raised when trying to open a file that doesn't exist.

**ZeroDivisionError**: Raised when dividing by zero.

**AttributeError**: Raised when trying to access an attribute that doesn't exist.

**NameError**: Raised when a variable name is not found.

## Custom Exceptions

Custom exceptions allow you to create application-specific error types that make your code more readable and maintainable.

### Why Create Custom Exceptions?

- Make error handling more specific to your application
- Provide better error messages
- Group related errors together
- Make code more self-documenting
- Allow callers to handle your errors differently from built-in errors

### Basic Custom Exception

The simplest custom exception inherits from `Exception` and uses `pass`:

```python
class InvalidAgeError(Exception):
    """Raised when age is not valid"""
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("Age must be between 0 and 150")
    return age

# Usage
try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")
```

### Custom Exception with Additional Attributes

You can store extra information in custom exceptions:

```python
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        message = f"Insufficient funds. Need £{amount}, but only £{balance} available"
        super().__init__(message)

# Usage
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(e)
    print(f"Shortage: £{e.shortage}")
```

### Custom Exception Hierarchy

You can create your own exception hierarchies for complex applications:

```python
# Base exception for your application
class StudentSystemError(Exception):
    """Base exception for student management system"""
    pass

# Specific exceptions inherit from your base
class InvalidStudentIDError(StudentSystemError):
    """Raised when student ID format is invalid"""
    pass

class DuplicateStudentError(StudentSystemError):
    """Raised when trying to add a student that already exists"""
    pass

class GradeOutOfRangeError(StudentSystemError):
    """Raised when grade is outside valid range (0-100)"""
    pass

class StudentNotFoundError(StudentSystemError):
    """Raised when student ID doesn't exist in system"""
    pass
```

Benefits of this approach:

- Catch all student-related errors with `StudentSystemError`
- Catch specific errors individually when needed
- Easy to add new exception types later
- Clear organization and documentation

### Using Custom Exception Hierarchies

```python
try:
    # Some student system operation
    add_student("ABC", "John")
    update_grade("ABC", 150)
except InvalidStudentIDError:
    print("Invalid ID format")
except GradeOutOfRangeError:
    print("Grade must be 0-100")
except StudentSystemError:
    # Catches any other student system error
    print("A student system error occurred")
```

## Best Practices for Custom Exceptions

1. **Always inherit from Exception** (not BaseException) unless you have a very specific reason.

2. **Use descriptive names** that end in "Error" or "Exception".

3. **Include docstrings** explaining when the exception should be raised.

4. **Keep them simple** unless you need to store additional data.

5. **Create exception hierarchies** for related errors in larger applications.

6. **Don't catch exceptions you can't handle** - let them propagate up.

7. **Be specific** when catching exceptions - avoid bare `except:` clauses.

8. **Call super().__init__()** in your `__init__` method to properly initialize the base Exception class.

## Raising Exceptions

You raise exceptions using the `raise` keyword:

```python
# Raising a built-in exception
raise ValueError("Invalid value provided")

# Raising a custom exception
raise InvalidAgeError("Age cannot be negative")

# Re-raising the current exception
try:
    # some code
    pass
except ValueError:
    print("Logging error...")
    raise  # Re-raises the original exception
```

## Exception Handling Syntax

### Basic try-except

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Cannot divide by zero")
```

### Multiple except blocks

```python
try:
    # Code that might raise exceptions
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input - not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Catching multiple exceptions in one block

```python
try:
    # Code here
    pass
except (ValueError, TypeError, KeyError):
    print("One of several errors occurred")
```

### try-except-else

The `else` block runs if NO exception was raised:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success! Result is {result}")
```

### try-except-finally

The `finally` block ALWAYS runs, whether an exception occurred or not:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs
    try:
        file.close()
    except:
        pass
```

## Summary

- Python's exception hierarchy starts with `BaseException` at the top
- Most exceptions inherit from `Exception`
- Parent exceptions catch all their child exceptions
- Order matters when catching exceptions - most specific first
- Custom exceptions make code more maintainable and self-documenting
- Always inherit custom exceptions from `Exception`
- Use exception hierarchies to organize related errors
- Follow naming conventions (end with "Error" or "Exception")
- Include docstrings in custom exceptions