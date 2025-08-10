# 📦 Inventory Manager CLI App – Phase 1 Integration Project

## **📌 Project Requirements – Inventory Manager CLI**

### **Core Objective**
A command-line inventory management tool that:
- Tracks items (name, category, price, quantity)
- Supports adding, updating, deleting, and listing items
- Applies **all OOP concepts from Weeks 1–5** in a cohesive design

---

## **🎯 Phase 1 Topics to Demonstrate**

| Phase Topic | Implementation in the App |
|-------------|----------------------------|
| **Classes & Objects** (Week 1) | Create an `Item` class with attributes (name, category, price, quantity) and a constructor. Create a `InventoryManager` class to manage the collection. |
| **Encapsulation** (Week 2) | Protect sensitive attributes like `_price` and `_quantity` with getters/setters that validate data. |
| **Inheritance** (Week 2) | Create specialized subclasses like `PerishableItem` (expiry date) or `DigitalItem` (download link) that inherit from `Item`. |
| **Polymorphism & Interfaces** (Week 3) | Implement a `display_info()` method in `Item` and override it in subclasses to display extra data. Use an abstract base class `IExportable` for exporting inventory data. |
| **Abstract Classes & SOLID** (Week 4) | Create an abstract class `BaseItem` with abstract methods for updating stock. Apply SRP (separate item logic from CLI logic) and OCP (allow new item types without changing existing code). |
| **Design Patterns** (Week 5) | Use a **Factory Pattern** to create items based on type. Use **Singleton Pattern** for the inventory storage (only one inventory instance in the whole app). |

---

## **🛠 Functional Requirements**
1. **Add Item**  
   - Prompt user for type (Perishable, Digital, Standard).  
   - Use **Factory** to create the right object.
2. **Update Item**  
   - Modify price/quantity with validation (encapsulation).
3. **Delete Item**  
   - Remove item by ID or name.
4. **List Items**  
   - Show all items, using polymorphic `display_info()`.
5. **Export Inventory**  
   - Implement an `IExportable` interface for exporting to CSV or JSON.
6. **Exit Program**  

---

## **💡 Architectural Guidance**
- **Classes to Implement**
  - `BaseItem` (abstract class)
  - `Item` (concrete)
  - `PerishableItem` (inherits `Item`)
  - `DigitalItem` (inherits `Item`)
  - `ItemFactory` (Factory Pattern)
  - `InventoryManager` (Singleton Pattern)
  - `IExportable` (interface for export feature)
  - `CLI` (handles input/output — keeps UI separate from logic)

---

## 📂 Suggested File Structure


```plaintext
inventory_app/
├── items/
│   ├── base_item.py
│   ├── item.py
│   ├── perishable_item.py
│   └── digital_item.py
├── managers/
│   └── inventory_manager.py
├── patterns/
│   ├── item_factory.py
│   └── singleton.py
├── interfaces/
│   └── exportable.py
├── cli.py
└── main.py


---

## **🚀 Implementation Instructions**
1. **Start with Abstract Base Class**  
   Use `abc.ABC` for `BaseItem` with `update_stock()` and `display_info()` as abstract methods.
2. **Implement Concrete Item Classes**  
   Add encapsulated attributes with validation in setters.
3. **Add Inheritance and Polymorphism**  
   Override `display_info()` in each subclass to include unique attributes.
4. **Implement Factory Pattern**  
   In `ItemFactory`, use a `create_item(type, **kwargs)` method that returns the right subclass.
5. **Implement Singleton InventoryManager**  
   Store items in a dictionary keyed by ID. Only one inventory instance allowed.
6. **Add Interface for Export**  
   `IExportable` with `export_data()` method — implement CSV export for now.
7. **Build CLI Layer**  
   Menu-driven loop: Add / Update / Delete / List / Export / Exit.
8. **Test Each Feature Incrementally**  
   Don’t write the whole thing at once — build in layers.

---

## **📊 Example Flow**
=== Inventory Manager ===

Add Item

Update Item

Delete Item

List Items

Export

Exit
Select an option: 1
Enter item type (standard/perishable/digital): perishable
Enter name: Milk
Enter category: Dairy
Enter price: 1.99
Enter quantity: 50
Enter expiry date: 2025-09-01
Item added successfully!

Copy
Edit
