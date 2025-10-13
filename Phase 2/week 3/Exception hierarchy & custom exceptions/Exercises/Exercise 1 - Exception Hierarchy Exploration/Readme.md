# Exercise 1: Exception Hierarchy Exploration

## Overview
This exercise helps you understand how Python's exception hierarchy works and how parent exceptions can catch child exceptions.

## Learning Objectives
By completing this exercise, you will:
- Understand the relationship between parent and child exceptions
- Learn how exception catching order affects program behavior
- Discover how `LookupError` catches both `IndexError` and `KeyError`
- Practice proper exception handling syntax

## Background Theory
In Python's exception hierarchy:
- `LookupError` is a parent exception
- `IndexError` and `KeyError` are children of `LookupError`
- When you catch a parent exception, it also catches all child exceptions
- The order of except blocks matters - Python uses the first matching block

## Task Description

### Part 1: Basic Exception Catching
Create a Python program that:
1. Creates a list with exactly 5 elements (any values)
2. Attempts to access an invalid index (e.g., index 10)
3. Uses a try-except block to catch `LookupError`
4. Prints a message when the exception is caught

### Part 2: Specific Exception
Modify your program to:
1. Change the except block to catch `IndexError` instead of `LookupError`
2. Observe that it still works (because `IndexError` is the specific exception raised)

### Part 3: Multiple Except Blocks
Extend your program with multiple except blocks:
1. Add an except block for `IndexError`
2. Add an except block for `LookupError`
3. Add an except block for `Exception`
4. Observe which block executes

### Part 4: Wrong Order (Extension)
Create a version that demonstrates incorrect ordering:
1. Put the `Exception` catch block first
2. Put the `IndexError` catch block second
3. Observe that the second block never executes
4. Document why this happens in comments

## Expected Output
Your program should produce output similar to:

```
Testing LookupError catch:
Caught a lookup error!

Testing IndexError catch:
Caught an index error!

Testing multiple catches (correct order):
Caught a specific IndexError!

Testing wrong order:
Caught a general Exception (IndexError never reached!)
```

## Testing Checklist
- [ ] Program creates a list with 5 elements
- [ ] Program attempts to access an invalid index
- [ ] `LookupError` successfully catches the `IndexError`
- [ ] `IndexError` catch block works when used
- [ ] Multiple except blocks are in correct order (specific to general)
- [ ] Program demonstrates the wrong order problem
- [ ] Code includes comments explaining the behavior

## Extension Challenge
Try these additional experiments:
1. Create a dictionary and try to access a non-existent key - does `LookupError` catch it?
2. Use both `IndexError` and `KeyError` in the same try block with different except handlers
3. Research and try catching `ArithmeticError` with its children (`ZeroDivisionError`, `OverflowError`)

## Common Mistakes to Avoid
- Putting general exceptions (like `Exception`) before specific ones
- Forgetting that parent exceptions catch all children
- Not testing your code with actual exception-raising scenarios
- Catching exceptions you don't actually need to handle

## Submission Requirements
Your Python file should include:
1. Clear comments explaining each part
2. At least 4 different try-except examples
3. Print statements showing which exception was caught
4. A demonstration of correct vs incorrect exception ordering

## Assessment Criteria
- **Functionality**: Does the code demonstrate exception hierarchy correctly?
- **Understanding**: Do comments show comprehension of why things work?
- **Completeness**: Are all parts of the exercise completed?
- **Code Quality**: Is the code well-organized and readable?

## Resources
- Python Exception Hierarchy documentation
- Your exception study notes
- Python `try-except` syntax guide

## Estimated Time
30-45 minutes

## Difficulty Level
⭐⭐☆☆☆ (Beginner to Intermediate)