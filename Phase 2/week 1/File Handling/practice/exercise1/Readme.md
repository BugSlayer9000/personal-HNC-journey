# Exercise 1 — File Handling Practice  
*Phase 2 · Week 1 · HNC Level 7 Software Development*

## Overview  
This exercise is designed to build and demonstrate your competence in file-handling within Python. It forms part of your HNC Level 7 project work, where you are progressively integrating object-oriented programming (OOP) principles, file I/O, persistence, validation, and design for maintainability.

## Objectives  
By completing this exercise you will:

- Implement file input and output operations (e.g., reading, writing, appending).  
- Use appropriate file formats (e.g., plain text, CSV, JSON) to persist data.  
- Integrate this file-handling with your existing object-oriented design.  
- Ensure your code is testable, maintainable, and aligns with clean architecture principles.  
- Handle basic error conditions (e.g., file not found, parse errors) and validate user input where applicable.

## Scope  
- Create a module or class responsible for persistence (e.g., `FileRepository`, `JSONFileHandler`, `CSVFileHandler`).  
- Demonstrate CRUD operations via file storage: create new entries, retrieve existing ones, update entries, and delete entries.  
- Use appropriate encapsulation: internal file operations should be hidden behind well-defined public methods.  
- Integrate some form of validation (e.g., reject invalid data formats, ensure consistency).  
- Provide at least one unit test or test harness to validate key functionality (optional but strongly recommended for HNC Level 7 standards).

## Setup & Usage  
1. Ensure you have Python 3.x installed (preferably the latest stable version).  
2. Clone or download this repository.  
3. Navigate to the `Practice/Exercise1` directory:  
```bash
   cd Phase\ 2/week\ 1/File\ Handling/practice/exercise1
```
4. (Optional) Create and activate a virtual environment to isolate dependencies:
```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
```
5. If there are dependencies (check requirements.txt if present), install them:
```bash
   pip install -r requirements.txt
```
6. Run the main module to execute the exercise logic. For example:
```bash
   python main.py
```
   Adapt according to your actual module names.

7. (Optional) Run tests, if present:
```bash
   pytest
```
   or
```bash
   python -m unittest discover
```

## Design Considerations & Best Practices
- Use single-responsibility principle (SRP): the file handler class should only handle I/O, not business logic.
- Make your code open-for-extension but closed-for-modification (OCP): e.g., if later you switch from JSON to XML, minimal changes should be required.
- Keep the file path, file format, and encoding as configurable constants or via dependency injection, not hard-coded strings spread across your code.
- Ensure error handling is robust: anticipate missing files, permission issues, corrupted data, and respond gracefully rather than crashing.
- Follow clean code practices: meaningful class/method names, docstrings, spacing, adherence to PEP 8 or your project style guide.
- Write at least one scenario where your file-handling class is mocked or stubbed in testing, so your business logic is not tightly coupled to the file system.

## Deliverables
- Source code implementing file handling per the objectives above.
- A short demonstration (README update or inline comments) of how to run your solution.
- (Recommended) Unit tests covering key functionality.
- A short reflection (in code comments or a separate .md) on what you learned, what you'd improve next time, and how this ties into your broader HNC Level 7 roadmap (see e.g., mobile apps, REST APIs, data structures).

## Next Steps
Once this exercise is completed and reviewed:

- Extend your persistent store to support multiple formats (e.g., JSON and CSV) via a factory or strategy pattern.
- Integrate this with a GUI or CLI front-end to perform file-backed operations in a full end-to-end scenario.
- Add automated tests for concurrency/file locking if working with multi-threaded or multi-process access.
- Begin linking this file-handling layer to a higher-level business logic layer, and then prepare for swapping to a database-backed repository (preparation for upcoming REST API/data persistence modules).
