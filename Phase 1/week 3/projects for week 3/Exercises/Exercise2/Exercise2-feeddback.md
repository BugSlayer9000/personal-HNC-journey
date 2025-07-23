# ✅ Project Evaluation – Online Shopping Cart (HNC Level 7)

**Overall Score:** `7.2 / 10`  
**Total Grade:** `70 / 100`  
**Assessment Level:** *Approaching HNC Level 7 standard with solid fundamentals and room for critical improvements in validation, structure, and test coverage.*

---

## 📊 Grading Breakdown

| **Criteria**                                  | **Weight** | **Score**     |
|-----------------------------------------------|------------|----------------|
| OOP Principles (Encapsulation, Inheritance, Abstraction, Polymorphism) | 25%       | ✅ **21 / 25**  |
| Code Quality / Structure                      | 20%       | 🟡 **13 / 20**  |
| Input Validation / Error Handling             | 15%       | ❌ **7 / 15**   |
| Design Scalability                            | 15%       | 🟡 **10 / 15**  |
| Test Coverage / Demo Use Cases                | 15%       | 🟡 **10 / 15**  |
| Maintainability / Readability                 | 10%       | ✅ **9 / 10**   |

---

### 🔚 **Final Score: 70 / 100**

> To reach full HNC Level 7 compliance, focus on improving validation logic, refactoring discount handling, expanding test coverage, and modularizing your architecture.




# 🛠️ Refactor TODO List — Online Shopping Cart (HNC Level 7 Standards)

This document outlines the critical tasks needed to elevate this project to HNC Level 7 standards, focusing on software engineering best practices, OOP architecture, testability, and maintainability.

---

> This checklist is designed to turn a functional prototype into a maintainable, scalable, and testable application — aligned with industry expectations at HNC Level 7.

## 🧱 Product Architecture & Design

- [ ] Delegate SKU generation logic to child classes (avoid using `isinstance()` in base class).
- [ ] Centralize and standardize validation for all product fields (name, price, quantity, etc.).
- [ ] Separate product data from product operations (discounts, tax, shipping).
- [ ] Ensure abstract methods in the base class are clearly implemented by subclasses.

---

## 🧮 Discount & Price Handling

- [ ] Avoid modifying the `price` attribute directly — make discount application non-destructive.
- [ ] Implement cart-level discount handling (not per product).
- [ ] Add support for validating discount codes before applying them.
- [ ] (Optional) Support stacking/chaining discounts using design patterns (e.g., Decorator or Strategy).

---

## 📦 Shopping Cart Logic

- [ ] Allow multiple quantities of the same product (don’t restrict to one instance).
- [ ] Track product quantities correctly without duplicating product objects.
- [ ] Move all pricing logic (subtotal, tax, shipping, discounts) into clear, separate methods.
- [ ] Separate state-changing operations (add/remove) from validation/reporting logic.

---

## 🧾 Order & Payment Flow

- [ ] Integrate tax calculations into the final order total.
- [ ] Improve `get_order_summary()` to include quantity, unit price, subtotal, tax, shipping, and total.
- [ ] Improve formatting of timestamps and UUIDs for clarity.
- [ ] Centralize cart validation logic (avoid repeating it in every payment processor).

---

## 🧪 Validation & Error Handling

- [ ] Enforce strict input validation across constructors and public methods.
- [ ] Raise specific, meaningful exceptions when validation fails.
- [ ] Log or surface validation failures — avoid silent errors.
- [ ] Include negative test scenarios (e.g., invalid price, missing name, invalid discount).

---

## 🧼 Clean Code & Professional Practices

- [ ] Remove unused comments and print/debug statements.
- [ ] Improve naming consistency (functions, variables, classes).
- [ ] Add complete type annotations for all function inputs and return values.
- [ ] Standardize `__str__` and `__repr__` implementations across all classes.
- [ ] Split codebase into logical modules (`products.py`, `cart.py`, `payments.py`, `order.py`, etc.).

---

## 🧪 Testing Coverage

- [ ] Add test cases for:
  - Product creation and validation
  - Discount logic
  - Shipping/tax logic
  - Cart operations
  - Payment processing
- [ ] Include edge case testing: invalid prices, 0 quantity, bad discount codes, etc.
- [ ] Compare test outputs against expected results (especially totals and logic branches).
- [ ] Simulate mixed cart scenarios (e.g., both digital and physical products in a single order).

---

## 🧭 Optional Stretch Goals

- [ ] Implement Strategy Pattern for tax/shipping logic.
- [ ] Add basic unit testing using `unittest` or `pytest`.
- [ ] Replace `print()` statements with structured logging.
- [ ] Enable basic JSON file input/output for product/cart persistence.

---


