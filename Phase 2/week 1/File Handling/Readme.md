# File Handling - Phase 2 Week 1

A comprehensive learning module covering file handling techniques in Python, from basic text operations to advanced JSON and CSV manipulation.

## 📂 Module Structure

```
File Handling/
├── Theory/                 # Theoretical concepts and explanations
│   ├── txt_file_handling.md
│   ├── csv_file_handling.md
│   └── json_file_handling.md
├── Exercises/              # Practical exercises with solutions
│   ├── exercise1/          # Basic text file handling
│   ├── exercise2/          # Logging system
│   ├── exercise3/          # CSV basics
│   ├── exercise4/          # CSV to JSON conversion
│   └── exercise5/          # OOP Quiz game system
└── README.md              # This file
```

## 🎯 Learning Objectives

By completing this module, you will:
- Master basic file I/O operations in Python
- Understand different file modes and when to use them
- Work confidently with CSV files and data manipulation
- Handle JSON files for data persistence and API integration
- Implement error handling for robust file operations
- Apply object-oriented principles to file-based systems
- Convert between different data formats (CSV ↔ JSON)

## 📖 Theory Overview

### Text File Handling (`txt_file_handling.md`)
- File opening modes (`r`, `w`, `a`, `b`, `x`)
- Best practices with `with` statements
- Reading methods (`read()`, `readline()`, `readlines()`)
- Writing operations and file pointers
- Path management with `pathlib`
- Exception handling for file operations

### CSV File Handling (`csv_file_handling.md`)
- Understanding CSV format structure
- Using `csv.reader` and `csv.writer`
- Dictionary-based operations (`csv.DictReader`, `csv.DictWriter`)
- Handling different delimiters and edge cases
- Data validation and error handling
- Level 8 extensions: large file processing, format conversion

### JSON File Handling (`json_file_handling.md`)
- JSON structure and syntax
- Python's `json` module operations
- Reading and writing JSON files
- Handling nested data structures
- Error handling for malformed JSON
- Data manipulation and updates

## 🛠️ Practical Exercises

### Exercise 1: Personal Information System
- **Focus:** Basic text file operations
- **Skills:** File I/O, menu systems, data validation
- **Features:** Create, read, delete entries; line/character counting

### Exercise 2: Timestamp Logger
- **Focus:** Structured logging with timestamps
- **Skills:** DateTime handling, path management
- **Features:** Automatic timestamping, log viewing

### Exercise 3: Student Grade Manager (CSV)
- **Focus:** CSV file creation and manipulation
- **Skills:** Structured data storage, CSV module usage
- **Features:** Student record management, grade tracking

### Exercise 4: Data Format Converter
- **Focus:** CSV to JSON conversion
- **Skills:** Data format conversion, dictionary operations
- **Features:** Format transformation, pretty printing

### Exercise 5: Quiz Game System
- **Focus:** Object-oriented file handling
- **Skills:** Class design, complex data structures, modular programming
- **Features:** Question management, score tracking, persistent storage

## 🔗 Exercise Links and Descriptions

| Exercise | Description | Key Concepts | Difficulty |
|----------|-------------|--------------|------------|
| [Exercise 1](Exercises/exercise1/) | Personal data management with text files | Basic I/O, file modes, string handling | Beginner |
| [Exercise 2](Exercises/exercise2/) | Timestamp-based logging system | DateTime, pathlib, structured logging | Beginner+ |
| [Exercise 3](Exercises/exercise3/) | CSV-based student grade system | CSV module, structured data | Intermediate |
| [Exercise 4](Exercises/exercise4/) | CSV to JSON data converter | Format conversion, dictionaries | Intermediate+ |
| [Exercise 5](Exercises/exercise5/) | Object-oriented quiz game | OOP, complex data structures, modules | Advanced |

## 🏆 Skills Assessment

**Beginner Level (HNC Level 7):**
- ✅ Open and close files properly
- ✅ Read and write text data
- ✅ Handle basic file exceptions
- ✅ Use appropriate file modes

**Intermediate Level:**
- ✅ Work with CSV files and structured data
- ✅ Implement data validation
- ✅ Handle different file formats
- ✅ Create reusable file handling functions

**Advanced Level (Level 8+):**
- ✅ Design object-oriented file systems
- ✅ Convert between data formats
- ✅ Handle complex nested data structures
- ✅ Implement robust error handling
- ✅ Create modular, maintainable code

## 📋 Prerequisites

- Basic Python syntax and control structures
- Understanding of functions and scope
- Basic knowledge of data types (strings, lists, dictionaries)
- Familiarity with exception handling (for advanced exercises)

## 🚀 Getting Started

1. **Start with Theory:** Review the markdown files in the Theory folder
2. **Follow the Progression:** Complete exercises in order (1 → 5)
3. **Practice Variations:** Modify exercises to explore different scenarios
4. **Apply Knowledge:** Create your own file-handling projects

## 💡 Best Practices Demonstrated

- Always use `with` statements for file operations
- Implement proper exception handling
- Validate data before writing to files
- Use appropriate data formats for different use cases
- Design modular, reusable code
- Include comprehensive error messages
- Document code thoroughly

## 🔧 Technologies Used

- **Python 3.x** - Core programming language
- **csv module** - CSV file handling
- **json module** - JSON data operations
- **pathlib** - Modern path handling
- **datetime** - Timestamp generation
- **Object-oriented programming** - System design

This module provides a solid foundation for file handling in Python, preparing you for real-world applications involving data persistence, configuration management, and data processing systems.
