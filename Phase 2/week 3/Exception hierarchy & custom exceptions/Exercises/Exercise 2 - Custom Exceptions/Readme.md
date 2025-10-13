# Exercise 2: Bank Account System with Custom Exceptions

## Overview
This exercise involves building a simple bank account system with custom exceptions that store additional data and demonstrate proper exception hierarchy.

## Learning Objectives
By completing this exercise, you will:
- Create custom exception classes with additional attributes
- Build an exception hierarchy with a base exception
- Store and retrieve error-specific data from exceptions
- Apply exception handling in a real-world scenario
- Practice object-oriented programming with error handling

## Background Theory
Custom exceptions allow you to:
- Create application-specific error types
- Store additional information about errors
- Group related exceptions under a common base class
- Make error handling more meaningful and specific

## Task Description

### Part 1: Create Custom Exceptions

Create three custom exception classes:

**AccountError** (Base Exception)
- Inherits from `Exception`
- Base class for all account-related errors
- Include a docstring

**NegativeAmountError**
- Inherits from `AccountError`
- Raised when negative amounts are used
- Should store the invalid amount
- Include a docstring

**InsufficientFundsError**
- Inherits from `AccountError`
- Raised when withdrawal exceeds balance
- Should store: current balance, requested amount, and shortage (calculated)
- Include a custom error message
- Include a docstring

### Part 2: Create BankAccount Class

Implement a `BankAccount` class with the following:

**Attributes:**
- `balance` (private, initialized to 0 or provided value)

**Methods:**
- `__init__(self, balance=0)` - Initialize account with optional starting balance
- `deposit(amount)` - Add money to account, raises `NegativeAmountError` if amount < 0
- `withdraw(amount)` - Remove money from account, raises appropriate exceptions
- `get_balance()` - Return current balance

### Part 3: Implement Business Logic

The `withdraw` method should:
1. Check if amount is negative → raise `NegativeAmountError`
2. Check if amount > balance → raise `InsufficientFundsError` with all required data
3. Otherwise, subtract amount from balance and return new balance

The `deposit` method should:
1. Check if amount is negative → raise `NegativeAmountError`
2. Otherwise, add amount to balance and return new balance

### Part 4: Test Your System

Create a test program that:
1. Creates a bank account with £100 initial balance
2. Successfully deposits £50
3. Displays the new balance
4. Attempts to withdraw £200 (should raise exception)
5. Catches and handles the `InsufficientFundsError`, displaying the shortage
6. Attempts to deposit -£30 (should raise exception)
7. Catches and handles the `NegativeAmountError`
8. Includes a general catch for `AccountError` as a safety net

## Expected Output

Your program should produce output similar to:

```
=== Bank Account System Test ===

Initial balance: £100.00

Depositing £50.00...
Deposit successful! New balance: £150.00

Attempting to withdraw £200.00...
Error: Insufficient funds. Need £200.00, but only £150.00 available
You are short £50.00

Attempting to deposit -£30.00...
Error: Cannot deposit negative amount: -£30.00

Attempting to withdraw -£20.00...
Error: Cannot withdraw negative amount: -£20.00

Final balance: £150.00
```

## Project Structure

```
exercise2/
│
├── bank_exceptions.py    # Contains custom exception classes
├── bank_account.py       # Contains BankAccount class
├── test_bank.py          # Test program
└── README.md             # This file
```

Alternatively, you can put everything in one file for simplicity.

## Testing Checklist
- [ ] `AccountError` base exception created
- [ ] `NegativeAmountError` inherits from `AccountError`
- [ ] `InsufficientFundsError` inherits from `AccountError`
- [ ] `InsufficientFundsError` stores balance, amount, and shortage
- [ ] `BankAccount` class initializes correctly
- [ ] `deposit()` method works with positive amounts
- [ ] `deposit()` raises exception for negative amounts
- [ ] `withdraw()` method works with valid amounts
- [ ] `withdraw()` raises `InsufficientFundsError` when needed
- [ ] `withdraw()` raises `NegativeAmountError` for negative amounts
- [ ] Test program catches specific exceptions
- [ ] Error messages display relevant information
- [ ] All exceptions include docstrings

## Extension Challenges

1. **Transaction History**: Add a list to store all transactions with timestamps
2. **Overdraft Protection**: Add an optional overdraft limit feature
3. **Account Types**: Create subclasses like `SavingsAccount` with withdrawal limits
4. **Transfer Method**: Add a `transfer(other_account, amount)` method with proper exception handling
5. **Minimum Balance**: Add a `MinimumBalanceError` when balance falls below a threshold

## Common Mistakes to Avoid
- Forgetting to call `super().__init__()` in custom exceptions
- Not storing the additional data in `InsufficientFundsError`
- Catching general exceptions before specific ones
- Not validating input in both deposit and withdraw methods
- Forgetting to update the balance after successful operations

## Submission Requirements

Your submission should include:
1. All three custom exception classes with proper docstrings
2. A complete `BankAccount` class with all required methods
3. A test program that demonstrates all functionality
4. Comments explaining your exception handling strategy
5. Clear output showing successful operations and error handling

## Assessment Criteria

- **Exception Design (30%)**: Custom exceptions properly structured with inheritance
- **Functionality (30%)**: BankAccount class works correctly
- **Error Handling (25%)**: Appropriate exceptions raised and caught
- **Code Quality (15%)**: Clean, readable code with good comments

## Resources
- Python class and inheritance documentation
- Exception handling best practices
- Your exception hierarchy study notes

## Estimated Time
60-90 minutes

## Difficulty Level
⭐⭐⭐☆☆ (Intermediate)

## Tips for Success
- Start by creating and testing exceptions independently
- Build the BankAccount class incrementally (one method at a time)
- Test each method thoroughly before moving to the next
- Use meaningful variable names and comments
- Print intermediate values during testing to debug issues