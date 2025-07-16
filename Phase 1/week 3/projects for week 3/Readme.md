Exercise 1: Library Management System
Difficulty: Beginner–Intermediate

Class Responsibilities
Book Class
Store book information (title, author, ISBN, publication year, genre)

Track availability status (available / checked out)

Handle book checkout/return operations

Validate ISBN format (must be 13 digits)

Member Class
Store member information (name, member ID, email, join date)

Track books currently borrowed by the member

Enforce borrowing limits (max 3 books per member)

Calculate membership duration

Library Class
Manage collections of books and members

Handle book search operations (by title, author, or genre)

Process checkout/return transactions

Generate reports:

Overdue books

Popular genres

Validate member credentials

Key OOP Concepts to Apply
Encapsulation: Use private/protected attributes for internal data

Abstraction: Hide complex search and validation logic

Inheritance: Consider if you need different types of books or members

Polymorphism: Different search methods that work uniformly

Modules to Import
datetime — for handling dates

re — for ISBN validation

collections — for counting/organizing data

How It Should Work
The system should allow librarians to:

Add books

Register members

Process checkouts/returns

Generate basic reports

⚠️ Members shouldn't be able to:

Borrow more than 3 books

Check out unavailable books

Extra Challenge
Implement a book reservation system where members can reserve books that are currently checked out.

Exercise 2: Online Shopping Cart with Payment Processing
Difficulty: Intermediate

Class Responsibilities
Product Class (Abstract Base)
Store common product attributes: name, price, SKU, description

Define abstract methods for:

Tax calculation

Shipping costs

Handle price validation

DigitalProduct Class (inherits Product)
No shipping costs

Immediate delivery

Different tax rates

Attributes for file size and download link

PhysicalProduct Class (inherits Product)
Track weight and dimensions for shipping

Handle inventory tracking

Calculate shipping costs based on weight/size

ShoppingCart Class
Add/remove products

Calculate:

Subtotals

Taxes

Shipping

Apply discount codes

Validate cart contents before checkout

PaymentProcessor Class (Abstract Base)
Define a common payment interface

Handle payment validation

CreditCardProcessor & PayPalProcessor Classes
Implement specific payment methods

Use different validation rules

Use different fee structures

Order Class
Store order details and history

Track order status

Calculate final totals

Key OOP Concepts to Apply
Abstraction: Abstract base classes for products and payments

Inheritance: Multiple product types with shared behavior

Polymorphism: Different payment methods with same interface

Encapsulation: Protected pricing and payment information

Modules to Import
abc — for abstract base classes

enum — for order status and payment types

decimal — for precise money calculations

uuid — for generating unique IDs

datetime — for order timestamps

How It Should Work
Users can:

Add different types of products to their cart

Apply discounts

Choose payment methods

Complete purchases

The system should handle:

Different tax rates

Shipping costs

Payment processing fees

Extra Challenge
Implement a decorator pattern for dynamic discount application:

Percentage off

Buy-one-get-one

Seasonal discounts

These should be stackable.

Exercise 3: Task Management System with User Roles and Notifications
Difficulty: Intermediate–Advanced

Class Responsibilities
User Class (Abstract Base)
Store user information:

Username

Email

Password hash

Define abstract methods for permission checking

Handle authentication

Admin, Manager, Employee Classes (inherit User)
Provide different permission levels

Contain role-specific methods

Allow different task creation/modification rights

Task Class
Store task details:

Title

Description

Priority

Deadline

Status

Track assignee and creator

Handle status transitions with validation

Calculate time remaining

Project Class
Manage collections of tasks

Track project progress

Handle project-level permissions

Generate project reports

NotificationService Class (Singleton)
Send different types of notifications

Track notification history

Handle notification preferences

TaskObserver Classes (Observer Pattern)
EmailNotifier, SlackNotifier, SMSNotifier

React to task status changes

Use different notification formats

TaskFactory Class
Create different types of tasks:

Bug

Feature

Meeting, etc.

Apply appropriate templates and defaults

Validate task creation parameters

Key OOP Concepts to Apply
Abstraction: Abstract user roles and notification systems

Inheritance: User hierarchy with different permissions

Polymorphism: Multiple notification methods and task types

Encapsulation: Protected user data and task modification methods

Design Patterns:

Observer — for notifications

Factory — for task creation

Singleton — for notification service

Modules to Import
abc — for abstract base classes

enum — for task status, priority, and user roles

datetime — for deadlines and timestamps

hashlib — for password hashing

functools — for decorators (permission checking)

threading — for thread-safe singleton

collections — for task queues and history

How It Should Work
Users with different roles should be able to:

Create, assign, and manage tasks

Operate within projects

Receive notifications on status changes

View progress tracking

The system must:

Enforce role-based permissions

Send role-appropriate alerts

Log task status changes

Extra Challenge
Implement a command pattern for task operations:

create, update, delete, assign

Include:

Undo/redo functionality

Operation logging
