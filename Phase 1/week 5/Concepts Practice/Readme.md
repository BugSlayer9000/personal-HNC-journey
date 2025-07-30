# GRASP Patterns Exercises

## Exercise 1: Library Management System (Information Expert & Controller)

Design a library system where books can be borrowed and returned. Create classes for `Book`, `Member`, `Library`, and `LibraryController`. Focus on:

- Assigning responsibility for calculating late fees to the class that has the most information  
  (e.g., `Book` knows due date, `Member` knows borrowing history)  
- Creating a controller that handles borrowing/returning operations without embedding business logic itself  

**Challenge:**  
Add different member types (`Student`, `Faculty`) with different borrowing limits and fee structures.

---

## Exercise 2: Online Shopping Cart (Creator & Low Coupling)

Build a shopping system with `Product`, `CartItem`, `ShoppingCart`, and `Order` classes. Practice:

- Deciding which class should create `CartItem` objects (Creator pattern)  
- Minimizing dependencies between classes (Low Coupling)  

**Challenge:**  
Implement different discount strategies (percentage, fixed amount, buy-one-get-one) while maintaining loose coupling.

---

## Exercise 3: Game Character System (Polymorphism & High Cohesion)

Create an RPG character system with different character types (`Warrior`, `Mage`, `Archer`). Focus on:

- Using polymorphism for different attack behaviors and special abilities  
- Ensuring each class has a single, well-defined purpose (High Cohesion)  

**Challenge:**  
Add an equipment system where different items modify character abilities differently based on character type.

---

# SOLID Principles Exercises

## Exercise 4: Payment Processing System (Single Responsibility & Open/Closed)

Design a payment system handling credit cards, PayPal, and bank transfers. Practice:

- Each class having one reason to change (Single Responsibility Principle - SRP)  
- Adding new payment methods without modifying existing code (Open/Closed Principle - OCP)  

**Challenge:**  
Add payment validation, logging, and notification features while maintaining SRP across all classes.

---

## Exercise 5: Document Generator (Liskov Substitution & Interface Segregation)

Create a document generation system for PDF, Word, and HTML formats. Focus on:

- Ensuring derived classes can replace base classes without breaking functionality (Liskov Substitution Principle - LSP)  
- Creating focused interfaces rather than one large interface (Interface Segregation Principle - ISP)  

**Challenge:**  
Add features like password protection, watermarks, and templates, but note that not all document types support all features.

---

## Exercise 6: Database Access Layer (Dependency Inversion)

Build a data access system for a student management application. Practice:

- Depending on abstractions rather than concrete implementations (Dependency Inversion Principle - DIP)  
- Creating interfaces for data access that can work with different databases  

**Challenge:**  
Implement caching, connection pooling, and transaction management while maintaining dependency inversion.

---

# General Instructions

For **each exercise**:

1. Create UML class diagrams before coding.  
2. Implement the solution in code.  
3. Refactor to better apply the respective principles and patterns.  
4. Justify your design decisions in writing.  
5. Explain how each principle or pattern improves maintainability and extensibility.

---

*End of Exercises*
