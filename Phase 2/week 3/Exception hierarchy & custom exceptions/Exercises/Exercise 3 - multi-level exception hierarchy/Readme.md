# Exercise 3: Student Grade Management System

## Overview
This is a comprehensive exercise that requires you to build a complete student grade management system with a hierarchical exception structure, demonstrating advanced exception handling techniques.

## Learning Objectives
By completing this exercise, you will:
- Design and implement a multi-level exception hierarchy
- Create a complex system with proper error handling
- Validate data using custom exceptions
- Practice object-oriented programming with dictionaries
- Handle multiple exception types in a coordinated way
- Write robust, production-quality code

## Background Theory
In real-world applications, exception hierarchies allow you to:
- Group related errors under common base classes
- Catch errors at different levels of specificity
- Organize error handling in a logical, maintainable way
- Create self-documenting code through exception names

## Task Description

### Part 1: Design Exception Hierarchy

Create a five-level exception hierarchy:

```
StudentSystemError (inherits from Exception)
├── InvalidStudentIDError
├── DuplicateStudentError
├── StudentNotFoundError
└── GradeError (base for grade-related errors)
    ├── GradeOutOfRangeError
    └── InvalidGradeTypeError
```

**Exception Specifications:**

- **StudentSystemError**: Base for all student system errors
- **InvalidStudentIDError**: Raised when student ID format is invalid (must be 6 digits)
- **DuplicateStudentError**: Raised when trying to add a student that already exists
- **StudentNotFoundError**: Raised when student ID doesn't exist in system
- **GradeError**: Base for all grade-related errors
- **GradeOutOfRangeError**: Raised when grade is not between 0-100
- **InvalidGradeTypeError**: Raised when grade is not a number

All exceptions must include descriptive docstrings.

### Part 2: Create GradeBook Class

Implement a `GradeBook` class with the following structure:

**Attributes:**
- `students` (dictionary): Stores student data
  - Key: student_id (string)
  - Value: dictionary with 'name' and 'grades' (dictionary of subject:grade pairs)

**Methods:**

**`__init__(self)`**
- Initialize empty students dictionary

**`add_student(self, student_id, name)`**
- Validates student_id is exactly 6 digits
- Raises `InvalidStudentIDError` if format is invalid
- Raises `DuplicateStudentError` if student_id already exists
- Adds student with empty grades dictionary
- Returns success message

**`add_grade(self, student_id, subject, grade)`**
- Raises `StudentNotFoundError` if student doesn't exist
- Raises `InvalidGradeTypeError` if grade is not a number
- Raises `GradeOutOfRangeError` if grade < 0 or grade > 100
- Adds or updates the grade for the subject
- Returns success message

**`get_student(self, student_id)`**
- Raises `StudentNotFoundError` if student doesn't exist
- Returns student data (name and grades)

**`get_average(self, student_id)`** (Challenge)
- Raises `StudentNotFoundError` if student doesn't exist
- Raises a custom exception if student has no grades
- Calculates and returns average grade

**`display_all_students(self)`**
- Prints all students and their grades in a formatted way
- Handles empty gradebook gracefully

### Part 3: Create Main Test Program

Write a comprehensive test program that:

1. Creates a GradeBook instance
2. Successfully adds 3 students with valid IDs
3. Adds grades for each student (at least 3 subjects per student)
4. Displays all students
5. Tests each exception type:
   - Try to add a student with invalid ID format
   - Try to add a duplicate student
   - Try to add grade for non-existent student
   - Try to add grade outside 0-100 range
   - Try to add non-numeric grade
   - Try to get non-existent student
6. Uses appropriate exception handling:
   - Specific catches for each exception type
   - A general `StudentSystemError` catch as fallback
   - A final `Exception` catch for unexpected errors
7. Demonstrates that catching `StudentSystemError` catches all system exceptions
8. Calculates and displays average grades

## Expected Output

```
=== Student Grade Management System ===

Adding students...
✓ Student 123456 (Alice Smith) added successfully
✓ Student 234567 (Bob Jones) added successfully
✓ Student 345678 (Carol White) added successfully

Adding grades...
✓ Grade added: 123456 - Mathematics: 85
✓ Grade added: 123456 - English: 92
✓ Grade added: 123456 - Science: 88
✓ Grade added: 234567 - Mathematics: 78
✓ Grade added: 234567 - English: 85
✓ Grade added: 234567 - Science: 90

All Students:
-------------------
ID: 123456 | Name: Alice Smith
  Mathematics: 85
  English: 92
  Science: 88
  Average: 88.33

ID: 234567 | Name: Bob Jones
  Mathematics: 78
  English: 85
  Science: 90
  Average: 84.33

=== Testing Exception Handling ===

Test 1: Invalid Student ID
✗ Error: Student ID must be exactly 6 digits

Test 2: Duplicate Student
✗ Error: Student with ID 123456 already exists

Test 3: Student Not Found
✗ Error: Student with ID 999999 not found

Test 4: Grade Out of Range
✗ Error: Grade must be between 0 and 100 (received: 150)

Test 5: Invalid Grade Type
✗ Error: Grade must be a number (received: "A+")

Test 6: Catching Base Exception
✗ A student system error occurred: Student with ID 888888 not found
```

## Project Structure

```
exercise3/
│
├── student_exceptions.py  # All custom exceptions
├── gradebook.py          # GradeBook class
├── main.py               # Test program
└── README.md             # This file
```

## Testing Checklist

**Exception Hierarchy:**
- [x] `StudentSystemError` created as base
- [x] `InvalidStudentIDError` inherits correctly
- [x] `DuplicateStudentError` inherits correctly
- [x] `StudentNotFoundError` inherits correctly
- [x] `GradeError` inherits from `StudentSystemError`
- [x] `GradeOutOfRangeError` inherits from `GradeError`
- [x] `InvalidGradeTypeError` inherits from `GradeError`
- [x] All exceptions have docstrings

**GradeBook Functionality:**
- [x] Students stored in dictionary correctly
- [x] `add_student()` validates ID format (6 digits)
- [x] `add_student()` prevents duplicates
- [x] `add_grade()` validates student exists
- [x] `add_grade()` validates grade is numeric
- [x] `add_grade()` validates grade range (0-100)
- [x] `get_student()` retrieves correct data
- [x] `get_average()` calculates correctly
- [x] `display_all_students()` formats output nicely

**Exception Handling:**
- [x] Each exception type is triggered at least once
- [x] Specific exceptions are caught individually
- [ ] General `StudentSystemError` catch works
- [x] Exception messages are clear and helpful
- [x] Program continues after exceptions

## Extension Challenges

1. **Delete Student**: Add method to remove students with proper validation
2. **Grade Statistics**: Add methods for highest/lowest grade, class average
3. **Grade Letters**: Add method to convert numeric grades to letter grades
4. **Data Persistence**: Save/load gradebook to/from a file
5. **Search Functionality**: Search students by name or grade range
6. **Weighted Grades**: Allow subjects to have different weights
7. **Attendance Tracking**: Add attendance feature with its own exception hierarchy
8. **Report Generation**: Create formatted report cards with exception handling

## Common Mistakes to Avoid

- Creating exceptions that don't inherit properly
- Not validating student ID format (must be string of 6 digits)
- Forgetting to check if student exists before operations
- Not handling edge cases (empty gradebook, no grades for average)
- Catching exceptions in wrong order
- Using bare `except:` clauses
- Not providing helpful error messages
- Forgetting to initialize grades dictionary when adding students

## Submission Requirements

Your submission should include:

1. **student_exceptions.py**: All exception classes with docstrings
2. **gradebook.py**: Complete GradeBook class with all methods
3. **main.py**: Comprehensive test program
4. **Documentation**: Comments explaining your design decisions
5. **Test Results**: Output showing all functionality and exception handling
6. **README**: Brief explanation of your implementation approach

## Assessment Criteria

- **Exception Design (25%)**: Proper hierarchy and inheritance
- **Functionality (30%)**: All methods work correctly
- **Validation (20%)**: Proper input validation with appropriate exceptions
- **Error Handling (15%)**: Comprehensive exception catching and handling
- **Code Quality (10%)**: Clean, readable, well-documented code

## Resources

- Python dictionaries documentation
- Exception handling best practices
- Your exception hierarchy study notes
- Object-oriented programming principles

## Estimated Time
90-120 minutes

## Difficulty Level
⭐⭐⭐⭐☆ (Intermediate to Advanced)

## Tips for Success

1. **Start with exceptions**: Build and test your exception hierarchy first
2. **Incremental development**: Add one method at a time, test thoroughly
3. **Use helper methods**: Create private validation methods if needed
4. **Test edge cases**: Empty strings, None values, boundary conditions
5. **Print debug info**: Use print statements during development
6. **Refactor**: Clean up your code after it works
7. **Document**: Write clear docstrings and comments
8. **Use meaningful names**: Make your code self-documenting

## Grading Rubric

| Criteria | Excellent (90-100%) | Good (70-89%) | Satisfactory (50-69%) | Needs Improvement (<50%) |
|----------|-------------------|---------------|---------------------|------------------------|
| Exception Hierarchy | Perfect structure, all inherit correctly | Minor issues in hierarchy | Some inheritance problems | Major structural problems |
| Validation | All inputs validated properly | Most validation works | Some validation missing | Little to no validation |
| Functionality | All methods work perfectly | Most methods work | Some methods work | Few methods work |
| Error Handling | Comprehensive, specific catches | Good coverage | Basic handling | Minimal handling |
| Code Quality | Clean, professional code | Well-organized | Somewhat messy | Poor organization |

Good luck! This is a challenging exercise that will significantly improve your understanding of exception handling in Python.
