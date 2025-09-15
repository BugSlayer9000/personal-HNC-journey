# File Handling Exercises - Phase 2 Week 1

This folder contains practical exercises for learning file handling in Python, covering text files, CSV files, and JSON files. Each exercise builds upon the previous one, introducing new concepts and techniques.

## 📁 Exercise Structure

### Exercise 1: Basic Text File Handling
**Files:** `Exercise1.py`, `data.txt`
- **Objective:** Write and read personal information (name, course, date) to/from a text file
- **Features:**
  - Interactive menu system
  - Append mode to preserve data
  - Line counting and character counting
  - Delete functionality for specific entries
- **Skills Learned:**
  - Basic file I/O operations (`open`, `read`, `write`)
  - Using `with` statement for proper file handling
  - String manipulation and user input validation

### Exercise 2: Simple Logging System
**Files:** `exercise2.py`, `data.txt`
- **Objective:** Create a timestamp-based logging system
- **Features:**
  - Automatic timestamp generation using `datetime`
  - Log entry creation and viewing
  - Proper file path handling with `pathlib.Path`
- **Skills Learned:**
  - Working with datetime module
  - File existence checking with `touch(exist_ok=True)`
  - Formatted string output with timestamps

### Exercise 3: CSV File Basics
**Files:** `exercise3.py`, `data.csv`
- **Objective:** Handle student grade data using CSV format
- **Features:**
  - CSV file creation with headers
  - Adding student records (ID, name, grade)
  - Reading and displaying CSV data
  - Proper CSV formatting with `newline=""` parameter
- **Skills Learned:**
  - `csv.writer` and `csv.reader` modules
  - Header row management
  - Structured data storage

### Exercise 4: Advanced CSV & JSON Integration
**Files:** `exercise4.py`, `student_data.csv`, `student_data.json`
- **Objective:** Convert CSV data to JSON format and work with dictionaries
- **Features:**
  - CSV to JSON conversion
  - Dictionary-based data reading with `csv.DictReader`
  - JSON file creation and manipulation
  - Data formatting and pretty printing
- **Skills Learned:**
  - `csv.DictReader` for structured data access
  - `json.dump` and `json.load` operations
  - Data format conversion techniques

### Exercise 5: Object-Oriented Quiz Game System
**Files:** `exercise5.py`, `main.py`, `questions.json`, `score_board.json`, `__init__.py`
- **Objective:** Build a complete quiz game with question management and scoring
- **Features:**
  - Class-based architecture (`QuizzGame` class)
  - Question CRUD operations (Create, Read, Update, Delete)
  - Score tracking and player management
  - JSON file persistence
  - Modular design with separate main file
- **Skills Learned:**
  - Object-oriented programming with file handling
  - JSON data manipulation
  - Complex data structures (lists of dictionaries)
  - Error handling and data validation
  - Module separation and imports

## 🎯 Learning Progression

1. **Basic File Operations** → Text files, read/write modes
2. **Data Formatting** → Timestamps, structured logging
3. **Structured Data** → CSV format, headers, data integrity
4. **Data Conversion** → CSV to JSON, dictionary handling
5. **Advanced Systems** → OOP, complex data management, persistence

## 🔧 Key Python Concepts Demonstrated

- File I/O operations (`open`, `with` statements)
- Error handling (`try/except`)
- Data serialization (CSV, JSON)
- Object-oriented programming
- Module organization
- Path management (`pathlib.Path`)
- String manipulation and validation
- Data structure manipulation (lists, dictionaries)

## 📚 Supporting Theory

Refer to the Theory folder for detailed explanations:
- `txt_file_handling.md` - Text file operations and best practices
- `csv_file_handling.md` - CSV module usage and data handling
- `json_file_handling.md` - JSON operations and data structures

## 🚀 Getting Started

Each exercise is self-contained. Start with Exercise 1 and work through them sequentially:

```bash
# Run individual exercises
python Exercise1.py
python exercise2.py
python exercise3.py
python exercise4.py

# For Exercise 5 (modular design)
python main.py
```

## 📝 Notes

- All exercises include proper error handling
- File paths are configured for the local development environment
- Each exercise demonstrates progressive complexity
- Code includes detailed comments explaining functionality
- Exercises cover both procedural and object-oriented approaches
