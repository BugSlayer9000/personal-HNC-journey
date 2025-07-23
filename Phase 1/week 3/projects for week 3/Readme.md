# OOP EXERCISES - PROGRESSIVE DIFFICULTY  
# Instructions and Test Code Only - You Implement the Solutions!

"""
================================================================================
EXERCISE 1: LIBRARY MANAGEMENT SYSTEM (BEGINNER-INTERMEDIATE)
================================================================================

MODULES TO IMPORT:
- from datetime import datetime
- import re
- from collections import Counter

INSTRUCTIONS:
Create a library management system using solid object-oriented principles.

CLASS RESPONSIBILITIES:

1. Book:
   - Attributes: title, author, isbn, year, genre, _available
   - Methods:
     * checkout() - marks as checked out
     * return_book() - marks as available
     * is_available() - returns availability status
     * validate_isbn() - checks if ISBN is exactly 13 digits

2. Member:
   - Attributes: name, member_id, email, join_date, _borrowed_books
   - Methods:
     * borrow_book(book) - adds to borrowed list (max 3 books)
     * return_book(book) - removes from borrowed list
     * get_membership_duration() - returns days since joined
     * list_borrowed_books() - shows current borrowed books

3. Library:
   - Attributes: books (list), members (list)
   - Methods:
     * add_book(book), add_member(member)
     * search_books(by title/author/genre)
     * checkout_book(isbn, member_id)
     * return_book(isbn, member_id)
     * generate_report() - overdue books, popular genres
     * validate_member(member_id)

KEY OOP CONCEPTS TO APPLY:
- Encapsulation: Use protected attributes
- Abstraction: Hide internal search/validation logic
- Inheritance: Plan for extended Book types
- Polymorphism: Unified search interface

EXTRA CHALLENGE:
Implement a reservation system for checked-out books.
"""


"""
================================================================================
EXERCISE 2: ONLINE SHOPPING CART WITH PAYMENT PROCESSING (INTERMEDIATE)
================================================================================

MODULES TO IMPORT:
- from abc import ABC, abstractmethod
- from enum import Enum
- from decimal import Decimal
- from uuid import uuid4
- from datetime import datetime

INSTRUCTIONS:
Create an online store system supporting both digital and physical products.

CLASS RESPONSIBILITIES:

1. Product (Abstract Base):
   - Attributes: name, price, sku, description
   - Methods:
     * get_tax()
     * get_shipping_cost()
     * validate_price()
   - Abstract methods: get_tax(), get_shipping_cost()
   - **Responsibilities**
      * Store common product attributes (name, price, SKU, description)
      * Define abstract methods for tax calculation and shipping costs
      * Handle price validation

2. DigitalProduct (inherits Product):
   - Additional attributes: file_size, download_link
   - get_tax(): digital tax rate
   - get_shipping_cost(): always 0
   
   - **Responsibilities**
      * No shipping costs
      * Immediate delivery
      * Different tax rates
      * File size and download link attributes

3. PhysicalProduct (inherits Product):
   - Additional attributes: weight, dimensions
   - get_tax(): physical product tax
   - get_shipping_cost(): based on weight/dimensions
   - **Responsibilities**
      * Weight and dimensions for shipping calculation
      * Inventory tracking
      * Shipping costs based on weight/size
      * File size and download link attributes

4. ShoppingCart:
   - Attributes: product list
   - Methods:
     * add_product(), remove_product()
     * calculate_subtotal(), calculate_total()
     * apply_discount(code)
     * validate_cart()
   - **Responsibilities**
      * Add/remove products
      * Calculate subtotals, taxes, and shipping
      * Apply discount codes
      * Validate cart contents before checkout

5. PaymentProcessor (Abstract Base):
   - Method: process_payment(amount)
   - **Responsibilities**
      * Define common payment interface
      * Handle payment validation

6. CreditCardProcessor / PayPalProcessor:
   - Specific validation rules, fee structures
   - **Responsibilities**
      * Implement specific payment methods
      * Different validation rules
      * Different fee structures

7. Order:
   - Attributes: cart, timestamp, payment_status
   - Methods: calculate_final_total(), get_order_summary()
   - **Responsibilities**
        * Store order details and history
        * Track order status
        * Calculate final totals

KEY OOP CONCEPTS TO APPLY:
- Abstraction: Abstract base for Product and PaymentProcessor
- Inheritance: Digital and Physical Product types
- Polymorphism: PaymentProcessor interface
- Encapsulation: Price and payment logic


HOW IT SHOULD WORK
- How It Should Work: Users can add different types of products to their cart, apply discounts, choose payment methods, and complete purchases. The system should handle different tax rates, shipping costs, and payment processing fees.
Extra Challenge: Implement a decorator pattern for dynamic discount application (percentage off, buy-one-get-one, seasonal discounts) that can be stacked.



EXTRA CHALLENGE:
Implement a decorator system for dynamic discounts (BOGO, %, seasonal).
"""


"""
# 🧠 Project Management System – OOP Design (Level 7 with Light Level 8) by chat GPT

This project is a trimmed yet extensible **object-oriented project management system** built for **HNC Level 7 Software Development**. It introduces core OOP principles while lightly touching on Level 8 design patterns like **Factory** and **Observer**, without crossing into full-blown university-level (Level 9) complexity.

---

## 🎯 Project Goals

- Apply **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism**
- Introduce **basic design patterns** in a practical way (Factory + Observer)
- Implement **role-based user permissions**
- Track and manage **tasks with status, deadlines, and priorities**

---

## 🧱 Class Responsibilities

### 🔐 `User` (Abstract Base Class)

| Attribute       | Type       | Description                            |
|----------------|------------|----------------------------------------|
| `username`     | `str`      | Username of the user                   |
| `email`        | `str`      | Email address                          |
| `_password_hash` | `str`    | Hashed password (encapsulated)         |

| Method                     | Description                                           |
|---------------------------|-------------------------------------------------------|
| `check_password(password)`| Validates password input                              |
| `get_role()`              | Returns user role                                     |
| `is_authorized(action)`   | Checks if the user has permission for an action       |
| `can_create_task()`       | Abstract — overridden by subclasses                   |
| `can_assign_task()`       | Abstract — overridden by subclasses                   |

---

### 👥 `Admin`, `Manager`, `Employee` (User Subclasses)

| Role     | Can Create Task | Can Assign Task | Notes                                |
|----------|------------------|-----------------|--------------------------------------|
| Admin    | ✅               | ✅              | Full permissions                     |
| Manager  | ✅               | ✅              | Can assign to employees              |
| Employee | ❌               | ❌              | Can only work on assigned tasks      |

---

### 📌 `Task`

| Attribute     | Type        | Description                                    |
|---------------|-------------|------------------------------------------------|
| `title`       | `str`       | Task title                                     |
| `description` | `str`       | Task details                                   |
| `status`      | `Enum`      | `Todo`, `InProgress`, `Done`                  |
| `priority`    | `Enum`      | `Low`, `Medium`, `High`                       |
| `deadline`    | `datetime`  | Task deadline                                  |
| `history`     | `list[str]` | Logs task status changes                       |

| Method                  | Description                              |
|-------------------------|------------------------------------------|
| `assign_to(user)`       | Assigns task to a user                   |
| `change_status(status)` | Changes task status                      |
| `get_remaining_time()`  | Returns remaining time until deadline    |
| `log_history(message)`  | Logs activity in task history            |

---

### 🧪 `TaskFactory`

| Method             | Description                              |
|--------------------|------------------------------------------|
| `create_task(...)` | Creates and returns a `Task` instance     |

✔ Applies **Factory Pattern**  
✔ Ensures tasks are validated on creation

---

### 📡 `Notifier` + `EmailNotifier`, `SMSNotifier` (Observer Pattern)

| Class         | Description                                          |
|---------------|------------------------------------------------------|
| `Notifier`    | Abstract Observer                                    |
| `EmailNotifier`, `SMSNotifier` | Receive updates on task changes     |
| `update()`    | Called when a task status is changed                 |

✔ Uses a **simple observer** model  
✔ Register notifiers to a task and trigger on `change_status`

---

## 🧩 Optional Level 8 Class: `Project`

| Attribute | Description                    |
|-----------|--------------------------------|
| `tasks`   | List of all tasks              |
| `members` | All users in the project       |

| Method            | Description                         |
|-------------------|-------------------------------------|
| `add_task(task)`  | Adds a task to the project          |
| `remove_task()`   | Removes a task                      |
| `progress_report()` | Generates basic completion report |
| `filter_tasks()`  | Returns tasks by status or priority |

---

## 🧠 How It Works (Explanation)

1. **Users** log in with credentials, stored as a hash.
2. **Admins and Managers** create tasks via the **TaskFactory**.
3. Tasks can be **assigned to employees**.
4. When a task's status changes, all registered **Notifiers** (email, SMS) are triggered.
5. Task deadlines and priorities are used to **organize work**.
6. Optionally, a **Project** can hold groups of tasks and generate reports.

---

## 🧪 How to Test the Program (Testing Instructions)

### Step-by-Step Logic to Validate

✅ In `main.py`, implement:

1. **Create Users:**
   - 1 Admin
   - 1 Manager
   - 1 Employee

2. **Create Tasks:**
   ```python
   task1 = TaskFactory.create_task("Bug Fix", "Fix login issue", "High", datetime(2025, 7, 20))
   task2 = TaskFactory.create_task("New Feature", "Add analytics", "Medium_

