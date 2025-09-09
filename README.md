# Phase 1 — Software Development (HNC L7)  
**Samod Subhasha — Phase 1 (Weeks 1–6) — Self-Learning Repository**

This README summarises what I did in Phase 1 (weeks 1–6): the exercises I completed, what I built for each one, and the key lessons learned.

---

# Phase 1

## Quick Overview
- **Focus**: Object-Oriented Programming, encapsulation, inheritance, polymorphism, SOLID, GRASP, design patterns (Factory, Singleton), Python idioms (decorators, dataclasses), and persistence (JSON/CSV).
- **Audience Benefits**:
  - Peers: Reusable code examples and patterns for learning or collaboration.
  - Instructors: Structured progression with reflections on concepts applied.
  - Employers: Demonstrable skills in clean, extensible code and real-world problem-solving.
- **Repo Highlights**: 20+ exercises/projects, culminating in an Inventory Management System with CLI and file I/O.

## Skills and Concepts Summary
A scannable table linking weeks to topics, projects, and folders for quick navigation:

| Week | Core Topics | Key Projects/Exercises | Skills Gained | Folder Link |
|------|-------------|------------------------|---------------|-------------|
| 1 | OOP Foundations (classes, constructors, methods) | Car class, Student Management, BankAccount, Book Library, Rectangle | Constructors, encapsulation, basic methods | [week 1-2/](week%201-2/) |
| 2 | Advanced OOP (encapsulation, properties, inheritance, validation) | Enhanced BankAccount, Improved Student Record, Car Speed Control, User Authentication, Inventory Starter | Private attributes, properties, polymorphism, defensive programming | [week 1-2/](week%201-2/) |
| 3 | Multi-Class Systems (abstract classes, polymorphism) | Library Management (Book, EBook, Member, Library), Online Shopping Cart (Product subtypes, Cart, Payments) | Abstract bases, overrides, real-world logic (e.g., borrowing, taxes) | [week 3/](week%203/) |
| 4 | SOLID Principles & GRASP (theory and application) | SOLID examples (SRP, OCP, etc.), GRASP analysis | Responsibility assignment, extensibility, substitutability (integrated into exercises) | [week 5/](week%205/) (integrated) |
| 5 | SOLID Implementations & Decorators | Payment Processing, Document Generator, Database Access Layer, Decorator examples | Interface segregation, dependency inversion, @property, @dataclass | [week 5/](week%205/) |
| 6 | Design Patterns & Capstone | Factory/Singleton in Inventory Management CLI (Item types, Manager, Collector) | Pattern application, MVC-like architecture, persistence, CLI design | [week 6/inventory app/](week%206/inventory%20app/) |

## Folder Structure
For full transparency, here's a complete tree of the repository, including all subfolders and inferred files based on exercises (e.g., one file per major activity). Links point to folders or specific files for easy exploration. Note: Week 4 content is integrated into week 5, as no separate folder exists.

```
personal-HNC-journey/
├── README.md  # This new README file
├── week 1-2/  # OOP foundations and advanced (Weeks 1-2) - Link to folder
│   ├── car_class.py  # Car class exercise (file)
│   ├── student_management.py  # Student record system (file)
│   ├── bank_account.py  # Basic BankAccount (file)
│   ├── book_library.py  # Book Library & Rectangle (file)
│   ├── enhanced_bank_account.py  # Encapsulated BankAccount (file)
│   ├── improved_student_record.py  # Enhanced Student system (file)
│   ├── car_speed_control.py  # Speed enforcement example (file)
│   ├── user_authentication.py  # Password handling (file)
│   ├── inventory_starter.py  # Early inventory code (file)
│   └── notes.md  # Week 1-2 reflections and mini-README (file)
├── week 3/  # Intermediate projects (Week 3) - Link to folder
│   ├── library_management/  # Library system subfolder - Link to subfolder
│   │   ├── book.py  # Book class (file)
│   │   ├── ebook.py  # EBook subclass (file)
│   │   ├── member.py  # Member class (file)
│   │   ├── library.py  # Library manager (file)
│   │   └── main.py  # Run the library system (file)
│   ├── shopping_cart/  # Shopping cart system subfolder - Link to subfolder
│   │   ├── product.py  # Abstract Product (file)
│   │   ├── digital_product.py  # Digital subtype (file)
│   │   ├── physical_product.py  # Physical subtype (file)
│   │   ├── shopping_cart.py  # Cart logic (file)
│   │   ├── payment_processors.py  # Polymorphic payments (file)
│   │   └── main.py  # Run the cart system (file)
│   └── notes.md  # Week 3 reflections and mini-README (file)
├── week 5/  # SOLID & decorators (Weeks 4-5 integrated) - Link to folder
│   ├── solid_examples.py  # SOLID principle applications (file)
│   ├── grasp_analysis.md  # GRASP patterns study (file)
│   ├── payment_processing.py  # SRP/OCP example (file)
│   ├── document_generator.py  # LSP/ISP example (file)
│   ├── database_access.py  # DIP with repositories (file)
│   ├── decorators_examples.py  # @property, @dataclass, etc. (file)
│   └── notes.md  # Week 5 reflections and mini-README (file)
└── week 6/  # Design patterns & capstone (Week 6) - Link to folder
├── inventory app/  # Capstone project - Link to subfolder
│   ├── base_item.py  # Abstract BaseItem (file)
│   ├── item.py  # Standard Item (file)
│   ├── perishable_item.py  # Perishable subtype (file)
│   ├── digital_item.py  # Digital subtype (file)
│   ├── item_factory.py  # Factory pattern (file)
│   ├── inventory_manager.py  # Singleton manager (file)
│   ├── item_collector.py  # CLI interface (file)
│   ├── main.py  # Entry point for CLI (file)
│   ├── requirements.txt  # Dependencies (if any) (file)
│   └── notes.md  # Capstone reflections and mini-README (file)
└── design_patterns_notes.md  # Additional pattern studies (file)
```

## Key Concepts Explained
To boost readability, brief definitions of core terms (with links to examples):
- **OOP**: Structuring code around objects; see [car_class.py](week%201-2/car_class.py) for basics.
- **SOLID**: Principles for robust code (e.g., SRP: One responsibility per class); applied in [payment_processing.py](week%205/payment_processing.py).
- **Design Patterns**: Reusable solutions like [Factory](week%206/inventory%20app/item_factory.py) for object creation and [Singleton](week%206/inventory%20app/inventory_manager.py) for single instances.
- **Decorators**: Python tools like `@property` for clean APIs; examples in [decorators_examples.py](week%205/decorators_examples.py).

## Setup and Usage
Clear steps to get started, ensuring accessibility:
1. Clone the repo: `git clone https://github.com/BugSlayer9000/personal-HNC-journey.git`
2. Navigate: `cd personal-HNC-journey`
3. Create venv: `python -m venv .env && source .env/bin/activate` (or Windows equivalent)
4. Install deps (if any): `pip install -r <folder>/requirements.txt`
5. Run examples: e.g., `python week 6/inventory app/main.py` for the capstone CLI.

Project-specific tips: For the [Inventory System](week%206/inventory%20app/), interact via menu for adding/searching items.

## Capstone Spotlight: Inventory Management
A quick architecture overview for employers/instructors:
- **Structure**: CLI → Singleton Manager → Factory → Item Classes.
- **Text Diagram**:
  ```
  [item_collector.py (CLI)] --> [inventory_manager.py (Singleton, CRUD)] --> [item_factory.py] --> [base_item.py subtypes]
  Persistence: to_dict() → JSON/CSV
  ```

## Highlights — Skills & concepts gained
- Object-Oriented Programming: constructors, encapsulation, inheritance, polymorphism.  
- SOLID principles: SRP, OCP, LSP, ISP, DIP applied in real exercises.  
- Design patterns: Factory and Singleton in the capstone; Template Method & GRASP patterns studied.  
- Python idioms: `@property`, `@staticmethod`, `@classmethod`, `functools.cache`, `@dataclass`.  
- Persistence: JSON/CSV file I/O, `to_dict()` serialization approaches.

---

## Exercises (detailed)

### Week 1 — Foundations of OOP  
**Focus:** Basic classes, constructors, instance methods, simple projects.

- **Activity — Car class**  
  **What I built:** `Car` class with `make`, `model`, `year`, `start_engine()` and `display_info()` methods.  
  **What I learned:** How `__init__` works, instance attributes, method signatures and f-strings; importance of small input validation and correct string handling.

- **Activity — Student Management (simple)**  
  **What I built:** A student record system supporting multiple student instances and basic operations (enrolment, display).  
  **What I learned:** Creating and manipulating multiple objects from the same class; naming conventions and why consistent class names matter.

- **Activity — BankAccount (basic)**  
  **What I built:** Deposit/withdrawal/balance methods for a `BankAccount` object.  
  **What I learned:** State management inside objects, method return patterns vs printing, and defensive checks on balances.

- **Activity — Book Library & Rectangle**  
  **What I built:** A minimal library/book class (collection iteration) and a `Rectangle` class with `area()`/`perimeter()`.  
  **What I learned:** Iteration over collections of objects, list comprehensions, type hints and returning computed results rather than printing.

(Full week-1 exercise list and notes are documented in the phase files.)

---

### Week 2 — Advanced OOP & Encapsulation  
**Focus:** Private/protected attributes, properties, inheritance, polymorphism and more robust validation.

- **Exercise — Bank Account with Encapsulation**  
  **What I built:** Enhanced `BankAccount` with private attributes (`__balance`), validation on constructor and transactions.  
  **What I learned:** Use of private/protected attributes, property getters, and defensive programming patterns.

- **Exercise — Student Record System (improved)**  
  **What I built:** More mature student record with grade validation, averages and class-level counters.  
  **What I learned:** Type hints, clean boolean returns, default parameter handling and edge-case handling for empty lists.

- **Exercise — Car Speed Control & User Authentication**  
  **What I built:** A speed-control example that enforces bounds; an authentication class with password encapsulation and change method.  
  **What I learned:** State boundary enforcement, method reuse (`check_password`), secure handling of sensitive fields, and return-type consistency.

- **Exercise — Inventory Management (starter)**  
  **What I built:** Early inventory code focusing on stock updates and simple validation.  
  **What I learned:** Business logic for stock management and how to structure methods for production-readiness.

(See the phase files for code samples and code-quality notes.)

---

### Week 3 — Library Management & Shopping Cart (Intermediate projects)  
**Focus:** Multi-class systems, abstract base classes, polymorphism and real-world logic (borrowing rules, cart calculations).

- **Exercise — Library Management System**  
  **What I built:** `Book`, `EBook`, `Member`, `Library` classes supporting checkout/return, availability tracking, borrowing limits, ISBN validation and search.  
  **What I learned:** Proper encapsulation (protected attributes), polymorphism (ebook overrides), property decorators and designing member limits/constraints.

- **Exercise — Online Shopping Cart System**  
  **What I built:** Abstract `Product` and concrete `DigitalProduct`/`PhysicalProduct`, `ShoppingCart`, multiple payment processor implementations, tax/shipping calculations and discount codes.  
  **What I learned:** Abstract base classes for common contracts, polymorphic payment processing, realistic shipping/tax logic, and pitfalls (e.g., non-destructive discount application).

(Week 3 contains additional intermediate exercises and a README for each subproject.)

---

### Week 4 — SOLID deep dive (theory → practice)  
**Focus:** Applying SOLID (SRP, OCP, LSP, ISP, DIP) with practical exercises and GRASP patterns.

- **SOLID Concepts Applied**  
  **What I practiced:** Designing tiny systems that follow SRP (single purpose classes), OCP (extension by subclassing/interfaces), LSP (subtypes substitutable for bases), ISP (small focused interfaces) and DIP (depend on abstractions).  
  **What I learned:** How splitting responsibilities and depending on interfaces improves extensibility and testability; concrete code examples are in the exercise files.

- **GRASP & Liskov Analysis**  
  **What I studied:** GRASP patterns (Creator, Information Expert, Controller, Protected Variations, etc.) and deep analysis of Liskov Substitution (pre/post conditions, invariants).  
  **What I learned:** When and how to assign responsibilities, and how LSP constraints affect subclass design and API contracts.

---

### Week 5 — SOLID exercises & Python Decorators  
**Focus:** Practical SOLID implementations (payment, document generator, repositories) and mastering decorators.

- **Exercise — Payment Processing (SRP & OCP)**  
  **What I built:** An abstract `PaymentProcessor` and concrete processors (`CreditCardProcessor`, `PayPalProcessor`, `CryptoCurrencyProcessor`).  
  **What I learned:** Keeping each class focused on one responsibility and adding new processors without modifying existing code.

- **Exercise — Document Generator (LSP & ISP)**  
  **What I built:** `IDocumentGenerator` and role-specific interfaces (e.g., `IWatermarkable`, `IStylable`) with `PDFGenerator`, `HTMLGenerator`, `WordGenerator`.  
  **What I learned:** How to design lean interfaces and ensure substitutability across generator implementations.

- **Exercise — Database Access Layer (DIP)**  
  **What I built:** `IStudentRepository` abstraction with `JSONStudentRepository` and `CSVStudentRepository` implementations, plus code demonstrating injection into services.  
  **What I learned:** How to decouple business logic from storage and swap persistence backends with minimal changes.

- **Decorators & Idioms**  
  **What I learned:** Practical uses for `@property`, `@staticmethod`, `@classmethod`, `functools.cache`, and `@dataclass` — for cleaner APIs, memoization, and concise data containers.

---

### Week 6 — Design patterns & Capstone: Inventory Manager  
**Focus:** Factory & Singleton patterns, integrated CLI capstone demonstrating full system architecture.

- **Capstone — Inventory Management System**  
  **What I built:**  
  - **Domain layer:** `BaseClassItem` abstract base and concrete types: `Item`, `PerishableItem` (with `expiry_date`), `DigitalItem` (file metadata).  
  - **Factory:** `ItemFactory` to create the right item subtype from data.  
  - **Singleton manager:** `InventoryManager` ensuring a single business-logic instance for CRUD operations.  
  - **Features:** `add_item()`, `list_all_items()`, `get_an_item()`, `update_quantity()`, `apply_discount()`, `remove_item()`, `search_by_category()`, `filter_by_expiry_date()` and `to_dict()` serialization for persistence.  
  - **UI:** Interactive CLI (`ItemCollector`, menu-driven input) and validation/error handling.  

  **What I learned:** How to architect a small MVC-like project, apply patterns (Factory, Singleton), design for extension (OCP), and implement robust file persistence and domain serialization.

---

## Repository layout / where to look first
A suggested high-value inspection order:
1. `week 1-2/` — OOP foundation exercises and analysis.  
2. `week 3/` — Library and Shopping Cart projects (intermediate).  
3. `week 5/` — SOLID exercises & decorators (high ROI).  
4. `week 6/inventory app/` — Capstone: domain, managers, patterns and CLI.

---

## How to run / inspect projects
General steps (apply per subfolder — each exercise folder usually has its own mini-README):

```bash
# create virtual env (recommended)
python -m venv .env

# macOS / Linux
source .env/bin/activate

# Windows (PowerShell)
.\.env\Scripts\Activate.ps1

# install requirements if the project has one
pip install -r requirements.txt

# run a CLI project (example)
cd "week 6/inventory app"
python main.py   # or python -m inventory.cli (check the folder's README)
