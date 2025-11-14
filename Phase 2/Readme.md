# Phase 2 — Software Development (HNC L7)  
**Samod Subhasha — Phase 2 (Weeks 1–3) — Self-Learning Repository**

This README summarizes Phase 2 (weeks 1–3): file handling fundamentals, exception hierarchies, custom error management, and preparation for GUI development with Django.

---

# Phase 2

## Quick Overview
- **Focus**: File I/O operations (text, CSV, JSON), exception handling, custom exception hierarchies, data persistence, validation patterns, and event-driven programming foundations.
- **Audience Benefits**:
  - Peers: Production-ready file handling patterns and robust error management strategies.
  - Instructors: Progressive skill development from basic I/O to complex multi-format systems.
  - Employers: Demonstrated ability to build resilient data-driven applications with proper error handling.
- **Repo Highlights**: 15+ exercises covering text files, CSV/JSON manipulation, custom exception systems, and a complete student marks database with dual-format persistence.

## Skills and Concepts Summary
A scannable table linking weeks to topics, projects, and folders for quick navigation:

| Week | Core Topics | Key Projects/Exercises | Skills Gained | Folder Link |
|------|-------------|------------------------|---------------|-------------|
| 1 | File Handling Fundamentals | Personal Info System, Logger, CSV Grade Manager, Format Converter, Quiz Game, Student Marks Database | Text I/O, CSV operations, JSON manipulation, pathlib, datetime, OOP persistence | [week 1/File Handling/](Phase%202/week%201/File%20Handling/) |
| 2 | GUI & Web Frameworks (Prep) | Django Introduction, Event-Driven Programming Theory | Event loops, Django basics, MVC architecture concepts | [week 2/](Phase%202/week%202/) |
| 3 | Exception Hierarchies & Custom Exceptions | Exception Exploration, Bank Account System, Student Grade Management | Exception inheritance, validation patterns, multi-level hierarchies, error data storage | [week 3/Exception hierarchy & custom exceptions/](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/) |

## Folder Structure
Complete repository tree with all subfolders and files for transparent exploration:

```
Phase 2/
├── README.md  # This comprehensive README file
├── Readme.md  # Weekly reflection document (Week 3 focus)
├── week 1/  # File handling fundamentals - Link to folder
│   ├── File Handling/  # Main file handling module - Link to subfolder
│   │   ├── Readme.md  # Module overview and architecture
│   │   ├── Theory/  # Theoretical concepts - Link to subfolder
│   │   │   ├── txt_file_handling.md  # Text file operations
│   │   │   ├── csv_file_handling.md  # CSV module usage
│   │   │   └── json_file_handling.md  # JSON operations
│   │   ├── Exercises/  # Progressive exercises - Link to subfolder
│   │   │   ├── Readme.md  # Exercise overview
│   │   │   ├── exercise1/  # Basic text files - Link to subfolder
│   │   │   │   ├── Exercise1.py  # Personal info system
│   │   │   │   └── data.txt  # Data storage
│   │   │   ├── exercise2/  # Logging system - Link to subfolder
│   │   │   │   ├── exercise2.py  # Timestamp logger
│   │   │   │   └── data.txt  # Log entries
│   │   │   ├── exercise3/  # CSV basics - Link to subfolder
│   │   │   │   ├── exercise3.py  # Student grades
│   │   │   │   └── data.csv  # CSV storage
│   │   │   ├── exercise4/  # CSV to JSON - Link to subfolder
│   │   │   │   ├── exercise4.py  # Format converter
│   │   │   │   ├── student_data.csv  # Source data
│   │   │   │   └── student_data.json  # Converted output
│   │   │   └── exercise5/  # OOP quiz game - Link to subfolder
│   │   │       ├── __init__.py  # Module initialization
│   │   │       ├── exercise5.py  # QuizzGame class
│   │   │       ├── main.py  # Application entry point
│   │   │       ├── questions.json  # Question bank
│   │   │       └── score_board.json  # Player scores
│   │   └── practice/  # Advanced implementation - Link to subfolder
│   │       ├── readme.md  # System documentation
│   │       └── exercise1/  # Student marks database - Link to subfolder
│   │           ├── Readme.md  # Project specifications
│   │           ├── main.py  # CLI interface
│   │           ├── student.py  # Student class (orchestrator)
│   │           ├── marks_analyzer.py  # Analytics engine
│   │           ├── file_handling_CSV.py  # CSV operations handler
│   │           ├── file_handling_JSON.py  # JSON operations handler
│   │           └── files/  # Data storage - Link to subfolder
│   │               ├── student_details.csv  # Primary storage
│   │               └── student_details_with_marks.json  # Analytics format
│   └── blank.md  # Template file
├── week 2/  # GUI and web frameworks preparation - Link to folder
│   ├── Django/  # Django framework introduction - Link to subfolder
│   │   └── Readme.md  # Django features overview
│   └── Event-driven programming/  # EDP fundamentals - Link to subfolder
│       └── Readme.md  # Event-driven concepts
└── week 3/  # Exception handling mastery - Link to folder
    └── Exception hierarchy & custom exceptions/  # Main module - Link to subfolder
        ├── Reame.md  # Exception hierarchy theory (comprehensive study notes)
        └── Exercises/  # Progressive exception exercises - Link to subfolder
            ├── Exercise 1 - Exception Hierarchy Exploration/  # Basics - Link to subfolder
            │   ├── Readme.md  # Exercise specifications
            │   ├── part1.py  # LookupError catching
            │   ├── part2.py  # IndexError specific
            │   ├── part3.py  # Multiple except blocks
            │   └── part4.py  # Wrong order demonstration
            ├── Exercise 2 - Custom Exceptions/  # Intermediate - Link to subfolder
            │   ├── Readme.md  # Bank system specifications
            │   ├── bank_exeptions.py  # Custom exception classes (NegativeAmountError, InsufficientFundsError)
            │   ├── bank_account.py  # BankAccount class with validation
            │   └── test_bank.py  # Comprehensive test suite
            └── Exercise 3 - multi-level exception hierarchy/  # Advanced - Link to subfolder
                ├── Readme.md  # Grade management specifications
                ├── student_exeptions.py  # Multi-level hierarchy (StudentSystemError tree, GradeError tree)
                ├── grade_book.py  # Gradebook class with validation
                └── main.py  # Interactive test program
```

## Key Concepts Explained
Brief definitions with links to practical implementations:

### File Handling Concepts
- **Text Files**: Sequential data storage; see [Exercise1.py](Phase%202/week%201/File%20Handling/Exercises/exercise1/Exercise1.py) for CRUD operations.
- **CSV Operations**: Structured tabular data with `csv.reader`/`csv.writer`; applied in [exercise3.py](Phase%202/week%201/File%20Handling/Exercises/exercise3/exercise3.py).
- **JSON Manipulation**: Hierarchical data structures; demonstrated in [exercise5.py](Phase%202/week%201/File%20Handling/Exercises/exercise5/exercise5.py) with quiz system.
- **Dual-Format Persistence**: CSV for operations + JSON for analytics; architected in [Student Marks Database](Phase%202/week%201/File%20Handling/practice/exercise1/).

### Exception Handling Concepts
- **Exception Hierarchy**: Python's tree structure from `BaseException` → `Exception` → specific errors; explored in [Reame.md](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Reame.md).
- **Custom Exceptions**: Application-specific error types with data storage; implemented in [bank_exeptions.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%202%20-%20Custom%20Exceptions/bank_exeptions.py).
- **Multi-Level Hierarchies**: Grouped error categories (e.g., `StudentSystemError` → `GradeError` → specific types); designed in [student_exeptions.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%203%20-%20multi-level%20exception%20hierarchy/student_exeptions.py).

### Event-Driven Programming
- **Event Loop**: Mechanism listening for and dispatching events; theory covered in [Event-driven programming Readme](Phase%202/week%202/Event-driven%20programming/Readme.md).
- **Callbacks**: Functions executed in response to events; foundational for GUI development.

## Setup and Usage
Clear steps for running Phase 2 projects:

### Prerequisites
```bash
# Python 3.x required (developed with Python 3.9+)
python --version

# Clone repository
git clone https://github.com/BugSlayer9000/personal-HNC-journey.git
cd personal-HNC-journey/Phase\ 2
```

### Running File Handling Exercises
```bash
# Basic text file operations
cd "week 1/File Handling/Exercises/exercise1"
python Exercise1.py

# CSV operations
cd ../exercise3
python exercise3.py

# OOP quiz game system
cd ../exercise5
python main.py

# Advanced student marks database
cd "../../practice/exercise1"
python main.py
```

### Running Exception Handling Exercises
```bash
# Exception hierarchy exploration
cd "week 3/Exception hierarchy & custom exceptions/Exercises"
cd "Exercise 1 - Exception Hierarchy Exploration"
python part1.py  # Through part4.py

# Bank account system with custom exceptions
cd "../Exercise 2 - Custom Exceptions"
python test_bank.py

# Multi-level exception hierarchy
cd "../Exercise 3 - multi-level exception hierarchy"
python main.py
```

## Practice Project Spotlight: Student Marks Database
**Advanced dual-format file handling system demonstrating production-ready architecture**

### System Architecture
```
┌─────────────────────┐
│   main.py (CLI)     │ ← User Interface Layer
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   student.py        │ ← Business Logic (Orchestrator)
│   - add_student()   │
│   - remove_student()│
│   - csv_to_json()   │
└─────┬───────────┬───┘
      │           │
      ▼           ▼
┌─────────────┐ ┌─────────────────┐
│ file_       │ │ file_           │ ← Data Access Layer
│ handling_   │ │ handling_       │
│ CSV.py      │ │ JSON.py         │
└──────┬──────┘ └────────┬────────┘
       │                 │
       ▼                 ▼
┌─────────────┐   ┌─────────────┐
│student_     │   │student_     │ ← Persistence Layer
│details.csv  │   │details.json │
└─────────────┘   └─────────────┘
                         │
                         ▼
                  ┌─────────────────┐
                  │ marks_          │ ← Analytics Layer
                  │ analyzer.py     │
                  │ - get_average() │
                  │ - most_marks()  │
                  └─────────────────┘
```

### Key Features
- **Separation of Concerns**: 5 distinct classes with single responsibilities
- **Dual Persistence**: CSV for operations, JSON for analytics (format conversion on-demand)
- **Composition Pattern**: Student class composes file handlers
- **Menu-Driven Interface**: Interactive CLI with validation
- **Statistical Analysis**: Average calculations, highest marks identification

### Technical Highlights
- **Pathlib Usage**: Cross-platform file path management
- **Context Managers**: Safe file operations with automatic cleanup
- **DictReader/DictWriter**: Structured CSV access
- **Error Handling**: FileNotFoundError, ValueError catching
- **Data Validation**: Length checks, type enforcement, boundary validation

## Highlights — Skills & Concepts Gained

### File Handling Mastery
- **Text Files**: read(), write(), append modes; context managers; line counting
- **CSV Operations**: csv.reader/writer, DictReader/DictWriter, header management, newline handling
- **JSON Manipulation**: json.dump/load, indent formatting, nested structures, list serialization
- **Pathlib**: Modern path handling with Path.touch(), cross-platform compatibility
- **Data Conversion**: CSV ↔ JSON transformation, format-specific optimizations

### Exception Handling Excellence
- **Exception Hierarchy**: BaseException tree, parent-child relationships, catching order
- **Custom Exceptions**: Inheriting from Exception, storing error data, meaningful messages
- **Multi-Level Hierarchies**: Base exceptions grouping related errors (StudentSystemError → GradeError → specific types)
- **Validation Patterns**: Input validation, range checking, type enforcement, format validation
- **Error Recovery**: Graceful degradation, informative messages, program continuation

### Design Patterns Applied
- **Composition**: Student class composes FileHandlingCSV and FileHandlingJSON
- **Separation of Concerns**: Data access, business logic, UI, analytics in separate classes
- **Factory-Like Creation**: ItemCollector pattern for user input processing
- **Single Responsibility**: Each class has one clear purpose

### Python Idioms & Best Practices
- **Context Managers**: `with open()` for automatic resource cleanup
- **List Comprehensions**: Efficient data filtering and transformation
- **Dictionary Operations**: .items(), .keys(), .values(), .update()
- **Type Hints**: Function signatures with parameter types
- **Docstrings**: Comprehensive exception documentation
- **Private Methods**: Leading underscore convention (_method_name)

---

## Exercises (Detailed)

### Week 1 — File Handling Fundamentals  
**Focus:** Text files, CSV operations, JSON manipulation, pathlib, datetime, and OOP persistence patterns.

#### Exercise 1: Personal Information System
**What I built:** Interactive menu system with append mode, line/character counting, and delete functionality.  
**File:** [Exercise1.py](Phase%202/week%201/File%20Handling/Exercises/exercise1/Exercise1.py)  
**What I learned:**
- File modes (r, w, a) and when to use each
- `with` statement for automatic file closure
- `splitlines()` vs `readlines()` for cross-platform compatibility
- List comprehension for filtering data
- Menu-driven user interfaces with input validation

**Key Code Patterns:**
```python
# Append mode preserves history
with open(file_path, "a") as write:
    write.write(content)

# Delete by filtering
updated_list = [row for row in lines if delete_name not in row]
```

#### Exercise 2: Timestamp Logger
**What I built:** Logging system with automatic timestamp generation and formatted display.  
**File:** [exercise2.py](Phase%202/week%201/File%20Handling/Exercises/exercise2/exercise2.py)  
**What I learned:**
- `datetime.now()` for timestamp generation
- `pathlib.Path` for modern file handling
- `Path.touch(exist_ok=True)` for safe file creation
- String formatting with timestamps
- Enumerate for numbered output

**Key Code Patterns:**
```python
from pathlib import Path
from datetime import datetime

logfile = Path("data.txt")
logfile.touch(exist_ok=True)

timestamp = datetime.now()
f.write(f"Date and time - {timestamp} -> msg - {msg}\n")
```

#### Exercise 3: CSV Grade Management
**What I built:** Student grade system with CSV storage, headers, and structured reading.  
**File:** [exercise3.py](Phase%202/week%201/File%20Handling/Exercises/exercise3/exercise3.py)  
**What I learned:**
- `csv.writer` and `csv.reader` basics
- `newline=""` parameter importance (prevents blank lines on Windows)
- Header row management
- `next(reader)` to skip headers
- Row unpacking for clean code

**Key Code Patterns:**
```python
import csv

# Writing with headers
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","grade"])  # Header
    writer.writerow([1, "Alice", "A"])      # Data

# Reading and skipping header
with open(file_path, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        id, name, grade = row  # Unpacking
```

#### Exercise 4: CSV to JSON Converter
**What I built:** Format conversion system using `csv.DictReader` and `json.dump` with pretty printing.  
**File:** [exercise4.py](Phase%202/week%201/File%20Handling/Exercises/exercise4/exercise4.py)  
**What I learned:**
- `csv.DictReader` for dictionary-based row access (keys from headers)
- `json.dump()` with `indent=4` for readable output
- `list(reader)` to convert CSV rows to list of dicts
- Dual-format iteration patterns
- Type conversion awareness (CSV reads as strings)

**Key Code Patterns:**
```python
# CSV to dictionary to JSON pipeline
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)  # Each row is a dict
    data = list(reader)             # Convert to list

with open(json_file, "w") as json_file:
    json.dump(data, json_file, indent=4)  # Pretty print

# Accessing converted data
for item in data:
    print(f"Name: {item['name']}, Grade: {item['grade']}")
```

#### Exercise 5: OOP Quiz Game System
**What I built:** Class-based quiz game with question CRUD, score tracking, and JSON persistence.  
**Files:** [exercise5.py](Phase%202/week%201/File%20Handling/Exercises/exercise5/exercise5.py), [main.py](Phase%202/week%201/File%20Handling/Exercises/exercise5/main.py)  
**What I learned:**
- Class-level file path constants with `pathlib.Path`
- Private methods convention (`_method_name`)
- `os.path.exists()` for file checking
- JSON list initialization with empty array `[]`
- Modular design with separate main file
- Score update logic (find existing player vs add new)

**Key Code Patterns:**
```python
class QuizzGame():
    QUESTIONS = Path("questions.json")
    SCORE_BOARD = Path("score_board.json")
    
    def _load_file_questions(self):
        with open(self.QUESTIONS, "r") as f:
            return json.load(f)
    
    def add_question(self, question, answer):
        data = self._load_file_questions()
        data.append({"question": question, "answer": answer})
        self._savefile_questions(data)
```

#### Practice Exercise: Student Marks Database System
**What I built:** Complete CRUD system with dual-format persistence, analytics engine, and interactive CLI.  
**Files:** [main.py](Phase%202/week%201/File%20Handling/practice/exercise1/main.py), [student.py](Phase%202/week%201/File%20Handling/practice/exercise1/student.py), [file_handling_CSV.py](Phase%202/week%201/File%20Handling/practice/exercise1/file_handling_CSV.py), [file_handling_JSON.py](Phase%202/week%201/File%20Handling/practice/exercise1/file_handling_JSON.py), [marks_analyzer.py](Phase%202/week%201/File%20Handling/practice/exercise1/marks_analyzer.py)  

**Architecture Overview:**
```
5-Class System:
1. main.py           → CLI interface (menu, input, display)
2. student.py        → Business logic orchestrator
3. file_handling_CSV → CSV operations layer
4. file_handling_JSON→ JSON operations layer
5. marks_analyzer    → Statistical analysis engine
```

**What I learned:**
- **Composition Pattern**: Student class composes file handler instances
- **Separation of Concerns**: Each class has single responsibility
- **Dual Persistence**: CSV for operations, JSON for analytics
- **Data Consistency**: `csv_to_json()` ensures synchronized formats
- **Analytics Design**: Separate analyzer class reads JSON for calculations
- **Initialization Patterns**: Empty file detection and header creation
- **CRUD Operations**: Complete Create, Read, Update, Delete implementation
- **Error Handling**: Try-except for file operations, ValueError for input

**Key Features Implemented:**
```python
# Student class orchestration (composition)
class Student():
    JSON_file = FileHandlingJSON()
    CSV_file = FileHandlingCSV()
    
    def add_student(self, name, subject, score):
        self.CSV_file._save_file(name, subject, score)
    
    def csv_to_json(self):
        data = self.CSV_file.csv_to_dict()
        self.JSON_file._save_file(data)

# Analytics on JSON data
class MarksAnalyzer:
    def get_average_marks(self):
        data = self._get_details()
        scores = [int(i["score"]) for i in data]
        return sum(scores) / len(scores)
```

**System Capabilities:**
- Add student with subject and marks
- Remove student records by name
- Display all students with formatting
- Calculate average marks across all students
- Identify highest-scoring student
- Convert between CSV and JSON formats on-demand

---

### Week 2 — GUI & Web Frameworks Preparation  
**Focus:** Django introduction, event-driven programming theory, and MVC architecture concepts.

#### Django Framework Introduction
**What I studied:** Django's core features and architecture patterns.  
**File:** [Django/Readme.md](Phase%202/week%202/Django/Readme.md)  
**Key Concepts:**
- Admin site for data management
- Object-Relational Mapper (ORM) for database abstraction
- Built-in authentication system
- Caching mechanisms

**Significance:** Foundation for upcoming web development projects integrating file handling with web interfaces.

#### Event-Driven Programming Fundamentals
**What I studied:** Event loops, handlers, callbacks, and event-driven architecture.  
**File:** [Event-driven programming/Readme.md](Phase%202/week%202/Event-driven%20programming/Readme.md)  
**Core Components:**
- **Event Source**: Objects generating events (buttons, sensors, sockets)
- **Event Loop**: Mechanism listening and dispatching events (e.g., `tk.mainloop()`)
- **Event Handler**: Callback functions executing on events
- **Event Object**: Data about the event (mouse position, key pressed)

**Connection to Phase 2:**
Event-driven paradigm is essential for:
- GUI applications (button clicks, form submissions)
- Async file operations
- Real-time data updates
- User interaction handling

---

### Week 3 — Exception Hierarchy & Custom Exceptions  
**Focus:** Python's exception tree, custom error classes, multi-level hierarchies, and validation patterns.

#### Exercise 1: Exception Hierarchy Exploration
**What I built:** Four-part demonstration of exception catching behavior and ordering.  
**Files:** [part1.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%201%20-%20Exception%20Hierarchy%20Exploration/part1.py) through [part4.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%201%20-%20Exception%20Hierarchy%20Exploration/part4.py)  
**Difficulty:** ⭐⭐☆☆☆ (Beginner to Intermediate)

**What I learned:**
- **Parent-Child Relationships**: `LookupError` catches both `IndexError` and `KeyError`
- **Catching Order Critical**: Specific exceptions MUST come before general ones
- **Exception Propagation**: How Python searches exception handlers from specific to general
- **Common Mistakes**: Putting general exceptions first prevents specific handlers from executing

**Code Demonstrations:**
```python
# Part 1: LookupError catches IndexError (child)
try:
    value = [1,2,3][10]
except LookupError:  # Catches IndexError
    print("Lookup error caught!")

# Part 3: Correct order (specific → general)
try:
    value = [1,2,3][10]
except IndexError:      # Most specific
    print("Index error")
except LookupError:     # More general
    print("Lookup error")
except Exception:       # Most general
    print("General exception")

# Part 4: Wrong order demonstration
try:
    value = [1,2,3][10]
except LookupError:     # Catches IndexError first!
    print("Lookup error")
# except IndexError:    # NEVER reached - commented out to show issue
#     print("Index error")
```

**Key Takeaway:** Exception hierarchy order determines which handler executes. Always catch specific exceptions before their parents.

#### Exercise 2: Bank Account System with Custom Exceptions
**What I built:** Banking system with validation and custom exceptions storing error data.  
**Files:** [bank_exeptions.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%202%20-%20Custom%20Exceptions/bank_exeptions.py), [bank_account.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%202%20-%20Custom%20Exceptions/bank_account.py), [test_bank.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%202%20-%20Custom%20Exceptions/test_bank.py)  
**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)  
**Grade:** 100% ✓ (Significant improvement after applying feedback)

**Exception Hierarchy Designed:**
```
Exception
└── AccountError (base for all account errors)
    ├── NegativeAmountError (stores invalid amount)
    └── InsufficientFundsError (stores balance, amount, shortage)
```

**What I learned:**
- **Custom Exception Structure**: Inherit from `Exception`, call `super().__init__(message)`
- **Storing Error Data**: Add attributes to exceptions (e.g., `self.shortage = amount - balance`)
- **Validation Patterns**: Check negative amounts, insufficient funds before operations
- **Raise vs Return**: CRITICAL - exceptions must be `raise`d, not `return`ed
- **Meaningful Messages**: Format strings with error context (`f"Need £{amount}, have £{balance}"`)

**Initial Mistakes (27% → 100%):**
- Returned exceptions instead of raising them
- Forgot to call `super().__init__()`
- Inconsistent error message formatting
- Missing data storage in exceptions

**Corrected Implementation:**
```python
class InsufficientFundsError(AccountError):
    """Raised when withdrawal exceeds available balance"""
    
    def __init__(self, current_balance: float, requested_amount: float):
        self.current_balance = current_balance
        self.requested_amount = requested_amount
        self.shortage = requested_amount - current_balance  # Calculated data
        message = f"Insufficient funds. Need £{requested_amount:.2f}, but only £{current_balance:.2f} available"
        super().__init__(message)  # Must call super!

# BankAccount usage
def withdraw(self, amount: float):
    if amount < 0:
        raise NegativeAmountError(amount)  # RAISE, not return!
    if amount > self.balance:
        raise InsufficientFundsError(self.balance, amount)
    self.balance -= amount
```

**Test Program Features:**
- Successful operations (deposit £50)
- InsufficientFundsError with shortage calculation
- NegativeAmountError for invalid inputs
- General AccountError catch as fallback

#### Exercise 3: Multi-Level Exception Hierarchy (Student Grade Management)
**What I built:** Comprehensive gradebook system with 7 custom exceptions in 3 levels.  
**Files:** [student_exeptions.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%203%20-%20multi-level%20exception%20hierarchy/student_exeptions.py), [grade_book.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%203%20-%20multi-level%20exception%20hierarchy/grade_book.py), [main.py](Phase%202/week%203/Exception%20hierarchy%20%26%20custom%20exceptions/Exercises/Exercise%203%20-%20multi-level%20exception%20hierarchy/main.py)  
**Difficulty:** ⭐⭐⭐⭐☆ (Intermediate to Advanced)  
**Grade:** 78% (B+) - Good effort with critical fixes needed

**Designed Exception Hierarchy:**
```
Exception
└── StudentSystemError (base for ALL student system errors)
    ├── InvalidStudentIDError (6-digit validation)
    ├── DuplicateStudentError (already exists)
    ├── StudentNotFoundError (ID not in system)
    └── GradeError (base for grade-related errors) ⚠️ Should inherit from StudentSystemError
        ├── GradeOutOfRangeError (0-100 validation)
        └── InvalidGradeTypeError (must be numeric)
```

**⚠️ Critical Issue Identified:**
```python
# WRONG (original implementation)
class GradeError(Exception):  # ❌ Skips StudentSystemError level
    pass

# CORRECT (after feedback)
class GradeError(StudentSystemError):  # ✓ Proper hierarchy
    pass
```

**What I learned:**
- **Multi-Level Hierarchies**: Base → Category → Specific (3+ levels)
- **Inheritance Planning**: Draw diagram BEFORE coding to ensure proper structure
- **Validation Layers**: ID format, existence checks, type validation, range validation
- **Dictionary Operations**: Nested dictionaries for student → grades → subjects
- **Edge Cases**: None values, empty data structures, boundary conditions (0, 100)

**Gradebook Data Structure:**
```python
grade_book = {
    "1234567": {  # student_id as key
        "name": "samod",
        "grades": {
            "Math": 40,
            "English": 60,
            "Science": 20,
            "Computing": None  # Not yet graded
        }
    }
}
```

**Validation Implemented:**
```python
def add_student(self, student_id: str, name: str):
    # Validation 1: Format check
    if not student_id.isdigit() or len(student_id) < 7:  # ⚠️ Should be == 6
        raise InvalidStudentIDError
    
    # Validation 2: Duplicate check
    if student_id in self.get_list_of_student_id():
        raise DuplicateStudentError(student_id)
    
    # Add student with empty grades
    self.
