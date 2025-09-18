# Student Marks Database and Analyzer System

## Overview
This is a comprehensive student marks management system that demonstrates advanced file handling techniques using both CSV and JSON formats. The system provides functionality to store, retrieve, analyze, and manage student academic records with a clean object-oriented design.

## System Architecture

### Core Components

#### 1. FileHandlingCSV Class (`file_handling_CSV.py`)
**Purpose:** Manages CSV file operations for student data storage
- **File Location:** `files/student_details.csv`
- **Data Structure:** CSV with columns: name, subject, score
- **Key Features:**
  - Automatic file initialization with headers
  - CRUD operations (Create, Read, Update, Delete)
  - Data conversion to dictionary format
  - Bulk rewriting capabilities

**Methods:**
- `_initialize_file()`: Creates CSV with headers if empty
- `_load_file()`: Reads CSV data as list of rows
- `_save_file(name, subject, score)`: Appends new student record
- `rewrite_csv(updated_student_list)`: Rewrites entire CSV file
- `csv_to_dict()`: Converts CSV to list of dictionaries using DictReader

#### 2. FileHandlingJSON Class (`file_handling_JSON.py`)
**Purpose:** Manages JSON file operations for enhanced data analysis
- **File Location:** `files/student_details_with_marks.json`
- **Data Structure:** Array of JSON objects with name, subject, score fields
- **Key Features:**
  - Pretty-printed JSON formatting (indent=4)
  - Automatic initialization with empty array
  - Complete file rewriting for updates

**Methods:**
- `_initialize_file()`: Creates empty JSON array
- `_load_file()`: Reads and parses JSON data
- `_save_file(data)`: Writes formatted JSON to file
- `_get_file_content()`: Returns JSON content as list

#### 3. Student Class (`student.py`)
**Purpose:** Main business logic layer that orchestrates file operations
- **Dependencies:** Uses both FileHandlingCSV and FileHandlingJSON classes
- **Role:** Provides high-level interface for student management operations

**Methods:**
- `add_student(name, subject, score)`: Adds new student record to CSV
- `remove_student(name)`: Removes all records for specified student
- `get_student(name)`: Searches and displays student information
- `get_a_dict()`: Returns all students as dictionary list
- `csv_to_json()`: Converts CSV data to JSON format for analysis

#### 4. MarksAnalyzer Class (`marks_analyzer.py`)
**Purpose:** Provides analytical capabilities for student performance
- **Data Source:** Reads from JSON file for analysis
- **Features:** Statistical analysis and performance insights

**Methods:**
- `_get_details()`: Loads JSON data with error handling
- `get_average_marks()`: Calculates overall average score
- `most_marks()`: Finds student with highest score

#### 5. Main Application (`main.py`)
**Purpose:** User interface and application flow control
- **Features:** Menu-driven console interface
- **Integration:** Coordinates Student and MarksAnalyzer classes

## Data Flow Architecture

```
User Input → main.py → Student Class → FileHandling Classes → File System
                    ↓
                MarksAnalyzer ← JSON File ← CSV to JSON Conversion
```

## File Structure
```
exercise1/
├── main.py                          # Application entry point
├── student.py                       # Student management logic
├── marks_analyzer.py                # Analytics engine
├── file_handling_CSV.py             # CSV operations handler
├── file_handling_JSON.py            # JSON operations handler
└── files/
    ├── student_details.csv          # Primary data storage
    └── student_details_with_marks.json # Analysis data format
```

## Key Features Implemented

### 1. Dual Format Storage
- **CSV for Operations:** Fast, simple structure for basic CRUD
- **JSON for Analytics:** Rich format enabling complex data analysis

### 2. Robust Error Handling
- File existence validation
- Input type checking (ValueError handling)
- Graceful handling of missing records

### 3. Data Validation
- Name and subject length validation
- Score type enforcement (integer)
- Empty file initialization

### 4. Advanced File Operations
- Automatic file creation using `Path.touch(exist_ok=True)`
- Context managers (`with` statements) for safe file handling
- Proper CSV handling with newline management

## User Interface Flow

### Main Menu Options:
1. **View Students and Marks** - Displays all records in formatted output
2. **Add Student and Marks** - Interactive input with validation
3. **Remove Students and Marks** - Name-based record deletion
4. **Check Who Got Most Marks** - Analytics feature using JSON data
5. **See Average Marks Per Student** - Statistical analysis

## Technical Highlights

### Object-Oriented Design Principles
- **Separation of Concerns:** Each class has single responsibility
- **Encapsulation:** Private methods (prefixed with `_`) for internal operations
- **Composition:** Student class composes FileHandling classes

### File Handling Best Practices
- **Path Management:** Using `pathlib.Path` for cross-platform compatibility
- **Safe File Operations:** Context managers prevent resource leaks
- **Data Integrity:** Atomic operations where possible

### Performance Considerations
- **Lazy Loading:** Files loaded only when needed
- **Efficient Updates:** Bulk operations for multiple changes
- **Memory Management:** Proper file closure and resource cleanup

## Sample Data Structure

### CSV Format:
```csv
name,subject,score
samod,science,30
robert,science,40
robert,kelum,60
pakaya,computer science,100
```

### JSON Format:
```json
[
    {
        "name": "samod",
        "subject": "science",
        "score": "30"
    },
    {
        "name": "robert",
        "subject": "science", 
        "score": "40"
    }
]
```

## Running the Application

1. **Prerequisites:** Python 3.x with standard library modules (pathlib, csv, json)
2. **Execution:** Run `python main.py` from the exercise1 directory
3. **Data Persistence:** Files are automatically created in the `files/` subdirectory

## Learning Outcomes Demonstrated

- **File I/O Mastery:** Reading, writing, appending operations
- **Data Format Handling:** CSV and JSON manipulation
- **Error Handling:** Robust exception management
- **Object-Oriented Programming:** Class design and composition
- **User Interface Design:** Menu-driven console application
- **Data Analysis:** Statistical computation and reporting
- **Code Organization:** Modular design with clear separation of concerns

This exercise showcases advanced file handling techniques while maintaining clean, maintainable code structure suitable for real-world applications.