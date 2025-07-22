# 🛠️ Refactor TODO List — Online Shopping Cart (HNC Level 7 Standards)

This document outlines the critical tasks needed to elevate this project to HNC Level 7 standards, focusing on software engineering best practices, OOP architecture, testability, and maintainability.

---

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

> This checklist is designed to turn a functional prototype into a maintainable, scalable, and testable application — aligned with industry expectations at HNC Level 7.
