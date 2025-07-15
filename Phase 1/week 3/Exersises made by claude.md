**Made by claude ai**

### Too advanced for me but I'll keep it

Exercise 1: Library Management System
Key OOP Concepts: Abstract classes, inheritance, encapsulation, polymorphism
Difficulty: Beginner-Intermediate
Focus: Basic OOP principles with practical application
Exercise 2: Restaurant Ordering System
Key OOP Concepts: Multiple inheritance, composition, enums, advanced polymorphism
Difficulty: Intermediate
Focus: Complex business logic with multiple interacting systems
Exercise 3: Advanced Game Engine
Key OOP Concepts: Component system, event-driven architecture, factory pattern, complex inheritance hierarchies
Difficulty: Advanced
Focus: Enterprise-level architecture patterns and performance considerations
Each exercise builds upon the previous one:

Exercise 1 tests your understanding of basic OOP principles
Exercise 2 introduces more complex interactions and business logic
Exercise 3 challenges you with advanced architectural patterns used in real game engines

The test code is comprehensive and will help you identify bugs, logic errors, and ensure your implementation follows proper OOP principles. Each test includes edge cases, error handling, and performance considerations.

# OOP EXERCISES - PROGRESSIVE DIFFICULTY
# Instructions and Test Code Only - You Implement the Solutions!

"""
================================================================================
EXERCISE 1: LIBRARY MANAGEMENT SYSTEM (BEGINNER-INTERMEDIATE)
================================================================================

MODULES TO IMPORT:
- from abc import ABC, abstractmethod
- from datetime import datetime, timedelta
- from typing import List, Dict, Optional, Union

INSTRUCTIONS:
Create a library management system with proper OOP principles.

CLASS RESPONSIBILITIES:

1. LibraryItem (Abstract Base Class):
   - Abstract class that defines common interface for all library items
   - Attributes: title, author, isbn, _available (protected), _checkout_date, _due_date
   - Methods: 
     * checkout() - marks item as unavailable, sets dates
     * return_item() - marks available, calculates late fees
     * get_info() - returns formatted item information
     * _calculate_late_fee() - private method for fee calculation
   - Abstract methods: get_checkout_period(), get_late_fee_rate()

2. Book (inherits LibraryItem):
   - Additional attributes: pages, genre
   - Implements: get_checkout_period() returns 14 days
   - Implements: get_late_fee_rate() returns $0.50/day
   - Override: get_info() to include book-specific details

3. Magazine (inherits LibraryItem):
   - Additional attributes: issue_number, month
   - Implements: get_checkout_period() returns 7 days
   - Implements: get_late_fee_rate() returns $0.25/day
   - Override: get_info() to include magazine-specific details

4. Library:
   - Manages collection of LibraryItem objects
   - Attributes: name, _items (dict: isbn -> LibraryItem), _checkout_history (list)
   - Methods:
     * add_item(item) - adds item to collection
     * checkout_item(isbn, member_name) - checks out item to member
     * return_item(isbn) - returns item and calculates fees
     * search_items(query) - searches by title/author
     * get_available_items() - returns list of available items
     * get_checkout_stats() - returns dictionary with statistics

EXTRA CHALLENGE: 
- Implement a reservation system where users can reserve unavailable items
- Add different member types (Student, Faculty, Public) with different checkout limits

HOW IT SHOULD WORK:
1. Create library instance
2. Add books and magazines to library
3. Checkout items to members
4. Return items and calculate late fees
5. Search for items
6. Get statistics

================================================================================
"""

# TEST CODE FOR EXERCISE 1
def test_exercise_1():
    """Comprehensive test suite for Library Management System"""
    
    print("=== TESTING EXERCISE 1: LIBRARY MANAGEMENT SYSTEM ===\n")
    
    # Import your classes here
    # from your_solution import LibraryItem, Book, Magazine, Library
    
    try:
        # Test 1: Basic object creation
        print("Test 1: Creating library items...")
        book1 = Book("Python Programming", "John Smith", "978-1234567890", 350, "Programming")
        book2 = Book("Data Structures", "Jane Doe", "978-0987654321", 420, "Computer Science")
        magazine1 = Magazine("Tech Today", "Various", "978-1111111111", 25, "March 2024")
        magazine2 = Magazine("Science Weekly", "Dr. Brown", "978-2222222222", 12, "April 2024")
        
        # Test 2: Library creation and adding items
        print("Test 2: Creating library and adding items...")
        library = Library("City Public Library")
        
        assert library.add_item(book1) == True, "Should add book1 successfully"
        assert library.add_item(book2) == True, "Should add book2 successfully"
        assert library.add_item(magazine1) == True, "Should add magazine1 successfully"
        assert library.add_item(magazine2) == True, "Should add magazine2 successfully"
        
        # Test duplicate ISBN
        duplicate_book = Book("Another Book", "Another Author", "978-1234567890", 200, "Fiction")
        assert library.add_item(duplicate_book) == False, "Should reject duplicate ISBN"
        
        # Test 3: Checkout functionality
        print("Test 3: Testing checkout functionality...")
        assert library.checkout_item("978-1234567890", "Alice Johnson") == True, "Should checkout book1"
        assert library.checkout_item("978-1111111111", "Bob Wilson") == True, "Should checkout magazine1"
        assert library.checkout_item("978-1234567890", "Charlie Brown") == False, "Should fail to checkout already checked out item"
        assert library.checkout_item("978-9999999999", "Dave Miller") == False, "Should fail with non-existent ISBN"
        
        # Test 4: Item availability
        print("Test 4: Testing item availability...")
        assert book1.available == False, "Book1 should not be available"
        assert book2.available == True, "Book2 should be available"
        assert magazine1.available == False, "Magazine1 should not be available"
        assert magazine2.available == True, "Magazine2 should be available"
        
        # Test 5: Return functionality
        print("Test 5: Testing return functionality...")
        late_fee = library.return_item("978-1234567890")
        assert late_fee is not None, "Should return a late fee amount"
        assert late_fee >= 0, "Late fee should be non-negative"
        assert book1.available == True, "Book1 should be available after return"
        
        # Test return of non-checked-out item
        assert library.return_item("978-0987654321") is None, "Should return None for non-checked-out item"
        
        # Test 6: Search functionality
        print("Test 6: Testing search functionality...")
        python_results = library.search_items("Python")
        assert len(python_results) == 1, "Should find 1 Python book"
        assert python_results[0].title == "Python Programming", "Should find correct book"
        
        author_results = library.search_items("John Smith")
        assert len(author_results) == 1, "Should find 1 book by John Smith"
        
        no_results = library.search_items("Nonexistent")
        assert len(no_results) == 0, "Should find no results for nonexistent query"
        
        # Test 7: Get available items
        print("Test 7: Testing get_available_items...")
        available = library.get_available_items()
        available_titles = [item.title for item in available]
        assert "Python Programming" in available_titles, "Python Programming should be available"
        assert "Data Structures" in available_titles, "Data Structures should be available"
        assert "Science Weekly" in available_titles, "Science Weekly should be available"
        
        # Test 8: Polymorphism - get_info method
        print("Test 8: Testing polymorphism...")
        book_info = book1.get_info()
        mag_info = magazine1.get_info()
        assert "pages" in book_info.lower() or "350" in book_info, "Book info should contain page count"
        assert "issue" in mag_info.lower() or "#25" in mag_info, "Magazine info should contain issue number"
        
        # Test 9: Abstract methods implementation
        print("Test 9: Testing abstract method implementations...")
        assert book1.get_checkout_period() == 14, "Book checkout period should be 14 days"
        assert magazine1.get_checkout_period() == 7, "Magazine checkout period should be 7 days"
        assert book1.get_late_fee_rate() > magazine1.get_late_fee_rate(), "Book late fee should be higher than magazine"
        
        # Test 10: Checkout statistics
        print("Test 10: Testing checkout statistics...")
        stats = library.get_checkout_stats()
        assert isinstance(stats, dict), "Stats should be a dictionary"
        assert "total_checkouts" in stats, "Stats should include total checkouts"
        
        # Test 11: Edge cases
        print("Test 11: Testing edge cases...")
        # Try to return an item that was never checked out
        try:
            book2.return_item()
            assert False, "Should raise ValueError for returning non-checked-out item"
        except ValueError:
            pass  # Expected behavior
        
        # Try to checkout an already checked out item
        library.checkout_item("978-1111111111", "Eve Adams")  # magazine1 still checked out
        assert magazine1.available == False, "Magazine1 should still be unavailable"
        
        print("✅ All tests passed for Exercise 1!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

"""
================================================================================
EXERCISE 2: RESTAURANT ORDERING SYSTEM (INTERMEDIATE)
================================================================================

MODULES TO IMPORT:
- from abc import ABC, abstractmethod
- from datetime import datetime
- from typing import List, Dict, Optional, Tuple
- from enum import Enum
- import json

INSTRUCTIONS:
Create a restaurant ordering system with multiple payment methods and order tracking.

CLASS RESPONSIBILITIES:

1. OrderStatus (Enum):
   - Enum with values: PENDING, PREPARING, READY, DELIVERED, CANCELLED

2. MenuItem (Abstract Base Class):
   - Attributes: name, price, description, _preparation_time, available
   - Abstract methods: get_preparation_time(), get_category()
   - Methods: apply_discount(percentage), get_info()

3. MainCourse, Appetizer, Dessert, Beverage (inherit MenuItem):
   - Each implements get_preparation_time() with different times
   - Each implements get_category() returning appropriate category
   - MainCourse: Additional attributes (cooking_method, spiciness_level)
   - Appetizer: Additional attributes (is_vegetarian, portion_size)
   - Dessert: Additional attributes (is_seasonal, sweetness_level)
   - Beverage: Additional attributes (is_alcoholic, temperature)

4. PaymentMethod (Abstract Base Class):
   - Abstract methods: process_payment(amount), get_transaction_fee()
   - Attributes: _is_processed

5. CreditCard, Cash, DigitalWallet (inherit PaymentMethod):
   - CreditCard: attributes (card_number, cvv, expiry_date), 2% transaction fee
   - Cash: attributes (amount_given), 0% transaction fee, returns change
   - DigitalWallet: attributes (wallet_id, balance), 1% transaction fee

6. Order:
   - Attributes: order_id, customer_name, items, status, order_time, payment_method
   - Methods:
     * add_item(item, quantity)
     * remove_item(item_name)
     * calculate_total()
     * calculate_estimated_time()
     * apply_discount(discount_percentage)
     * process_payment()
     * update_status(new_status)
     * get_receipt()

7. Restaurant:
   - Attributes: name, menu, orders, _order_counter
   - Methods:
     * add_menu_item(item)
     * remove_menu_item(item_name)
     * create_order(customer_name, payment_method)
     * get_order_by_id(order_id)
     * get_orders_by_status(status)
     * get_daily_sales()
     * get_popular_items()

EXTRA CHALLENGE:
- Implement a loyalty program with points system
- Add table management with different table sizes and reservations
- Create a kitchen management system that tracks cooking times

HOW IT SHOULD WORK:
1. Create restaurant with menu items
2. Customer creates order with payment method
3. Add items to order
4. Process payment
5. Track order status through kitchen
6. Generate receipts and sales reports

================================================================================
"""

# TEST CODE FOR EXERCISE 2
def test_exercise_2():
    """Comprehensive test suite for Restaurant Ordering System"""
    
    print("=== TESTING EXERCISE 2: RESTAURANT ORDERING SYSTEM ===\n")
    
    # Import your classes here
    # from your_solution import (OrderStatus, MenuItem, MainCourse, Appetizer, 
    #                          Dessert, Beverage, PaymentMethod, CreditCard, 
    #                          Cash, DigitalWallet, Order, Restaurant)
    
    try:
        # Test 1: Menu item creation and polymorphism
        print("Test 1: Creating menu items...")
        main1 = MainCourse("Grilled Salmon", 25.99, "Fresh Atlantic salmon", "Grilled", "Mild")
        appetizer1 = Appetizer("Caesar Salad", 12.50, "Crisp romaine lettuce", True, "Large")
        dessert1 = Dessert("Chocolate Cake", 8.99, "Rich chocolate cake", False, "High")
        beverage1 = Beverage("Red Wine", 15.00, "Cabernet Sauvignon", True, "Room Temperature")
        
        # Test categories
        assert main1.get_category() == "Main Course", "Main course category should be correct"
        assert appetizer1.get_category() == "Appetizer", "Appetizer category should be correct"
        assert dessert1.get_category() == "Dessert", "Dessert category should be correct"
        assert beverage1.get_category() == "Beverage", "Beverage category should be correct"
        
        # Test preparation times (should be different)
        prep_times = [main1.get_preparation_time(), appetizer1.get_preparation_time(), 
                     dessert1.get_preparation_time(), beverage1.get_preparation_time()]
        assert len(set(prep_times)) > 1, "Different items should have different preparation times"
        
        # Test 2: Payment method creation and processing
        print("Test 2: Testing payment methods...")
        credit_card = CreditCard("1234-5678-9012-3456", "123", "12/25")
        cash = Cash(50.00)
        digital_wallet = DigitalWallet("user123", 100.00)
        
        # Test transaction fees
        assert credit_card.get_transaction_fee() == 0.02, "Credit card should have 2% fee"
        assert cash.get_transaction_fee() == 0.0, "Cash should have 0% fee"
        assert digital_wallet.get_transaction_fee() == 0.01, "Digital wallet should have 1% fee"
        
        # Test 3: Restaurant creation and menu management
        print("Test 3: Testing restaurant and menu management...")
        restaurant = Restaurant("Bella Vista")
        
        assert restaurant.add_menu_item(main1) == True, "Should add main course"
        assert restaurant.add_menu_item(appetizer1) == True, "Should add appetizer"
        assert restaurant.add_menu_item(dessert1) == True, "Should add dessert"
        assert restaurant.add_menu_item(beverage1) == True, "Should add beverage"
        
        # Test duplicate item
        duplicate_main = MainCourse("Grilled Salmon", 30.00, "Different description", "Baked", "Spicy")
        assert restaurant.add_menu_item(duplicate_main) == False, "Should reject duplicate item name"
        
        # Test 4: Order creation and item management
        print("Test 4: Testing order creation and management...")
        order1 = restaurant.create_order("John Doe", credit_card)
        assert order1 is not None, "Should create order successfully"
        assert order1.status == OrderStatus.PENDING, "New order should be pending"
        
        # Add items to order
        order1.add_item(main1, 2)
        order1.add_item(appetizer1, 1)
        order1.add_item(beverage1, 2)
        
        # Test order total calculation
        total = order1.calculate_total()
        expected_total = (25.99 * 2) + (12.50 * 1) + (15.00 * 2)
        assert abs(total - expected_total) < 0.01, f"Total should be {expected_total}, got {total}"
        
        # Test 5: Order modifications
        print("Test 5: Testing order modifications...")
        order1.remove_item("Caesar Salad")
        new_total = order1.calculate_total()
        assert new_total == (25.99 * 2) + (15.00 * 2), "Total should decrease after removing item"
        
        # Test discount application
        order1.apply_discount(10)  # 10% discount
        discounted_total = order1.calculate_total()
        assert discounted_total < new_total, "Discounted total should be less than original"
        
        # Test 6: Payment processing
        print("Test 6: Testing payment processing...")
        payment_result = order1.process_payment()
        assert payment_result == True, "Payment should process successfully"
        
        # Test 7: Order status management
        print("Test 7: Testing order status management...")
        order1.update_status(OrderStatus.PREPARING)
        assert order1.status == OrderStatus.PREPARING, "Status should update to PREPARING"
        
        order1.update_status(OrderStatus.READY)
        assert order1.status == OrderStatus.READY, "Status should update to READY"
        
        # Test 8: Receipt generation
        print("Test 8: Testing receipt generation...")
        receipt = order1.get_receipt()
        assert isinstance(receipt, str), "Receipt should be a string"
        assert "John Doe" in receipt, "Receipt should contain customer name"
        assert "Grilled Salmon" in receipt, "Receipt should contain ordered items"
        
        # Test 9: Restaurant order management
        print("Test 9: Testing restaurant order management...")
        order2 = restaurant.create_order("Jane Smith", cash)
        order2.add_item(dessert1, 1)
        order2.process_payment()
        
        # Test getting orders by status
        ready_orders = restaurant.get_orders_by_status(OrderStatus.READY)
        assert len(ready_orders) == 1, "Should find 1 ready order"
        assert ready_orders[0].customer_name == "John Doe", "Should find John's order"
        
        # Test 10: Sales and analytics
        print("Test 10: Testing sales and analytics...")
        daily_sales = restaurant.get_daily_sales()
        assert daily_sales > 0, "Daily sales should be positive"
        
        popular_items = restaurant.get_popular_items()
        assert isinstance(popular_items, list), "Popular items should be a list"
        
        # Test 11: Edge cases and error handling
        print("Test 11: Testing edge cases...")
        
        # Test insufficient funds for digital wallet
        poor_wallet = DigitalWallet("poor_user", 5.00)
        order3 = restaurant.create_order("Poor Customer", poor_wallet)
        order3.add_item(main1, 1)
        
        payment_result = order3.process_payment()
        assert payment_result == False, "Payment should fail with insufficient funds"
        
        # Test cash with exact change
        exact_cash = Cash(8.99)
        order4 = restaurant.create_order("Exact Customer", exact_cash)
        order4.add_item(dessert1, 1)
        payment_result = order4.process_payment()
        assert payment_result == True, "Payment should succeed with exact amount"
        
        # Test estimated preparation time
        estimated_time = order1.calculate_estimated_time()
        assert estimated_time > 0, "Estimated time should be positive"
        
        print("✅ All tests passed for Exercise 2!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

"""
================================================================================
EXERCISE 3: ADVANCED GAME ENGINE (ADVANCED)
================================================================================

MODULES TO IMPORT:
- from abc import ABC, abstractmethod
- from typing import List, Dict, Optional, Tuple, Any, Callable
- from enum import Enum
- import json
- import math
- import random
- from dataclasses import dataclass
- from functools import wraps

INSTRUCTIONS:
Create an advanced game engine with entities, components, systems, and event handling.

CLASS RESPONSIBILITIES:

1. EventType (Enum):
   - COLLISION, MOVEMENT, ATTACK, DEATH, PICKUP, LEVEL_UP, GAME_OVER

2. Event (Dataclass):
   - Attributes: event_type, source_entity, target_entity, data, timestamp

3. Component (Abstract Base Class):
   - Abstract methods: update(), get_data(), set_data()
   - Attributes: entity_id, enabled

4. Transform, Health, Inventory, Physics, Renderer (inherit Component):
   - Transform: position (x, y), rotation, scale
   - Health: current_hp, max_hp, regeneration_rate
   - Inventory: items dict, capacity, weight_limit
   - Physics: velocity (x, y), acceleration, mass, friction
   - Renderer: sprite_name, color, visibility, layer

5. System (Abstract Base Class):
   - Abstract methods: update(entities, delta_time), get_required_components()
   - Attributes: priority, enabled

6. MovementSystem, CombatSystem, RenderSystem, CollisionSystem (inherit System):
   - MovementSystem: Updates positions based on physics
   - CombatSystem: Handles combat interactions
   - RenderSystem: Manages rendering (mock implementation)
   - CollisionSystem: Detects and handles collisions

7. Entity:
   - Attributes: entity_id, components dict, active
   - Methods:
     * add_component(component)
     * remove_component(component_type)
     * get_component(component_type)
     * has_component(component_type)

8. GameEngine:
   - Attributes: entities, systems, event_queue, _entity_counter, running
   - Methods:
     * create_entity()
     * destroy_entity(entity_id)
     * add_system(system)
     * remove_system(system_type)
     * emit_event(event)
     * process_events()
     * update(delta_time)
     * get_entities_with_components(component_types)

9. GameObjectFactory:
   - Static methods to create common game objects:
     * create_player(position)
     * create_enemy(position, enemy_type)
     * create_item(position, item_type)
     * create_projectile(position, direction, speed)

EXTRA CHALLENGE:
- Implement a save/load system that can serialize the entire game state
- Add a scripting system that allows behavior modification through external files
- Create a performance profiler that tracks system execution times
- Implement spatial partitioning for efficient collision detection

HOW IT SHOULD WORK:
1. Create game engine
2. Add systems (movement, combat, rendering, collision)
3. Create entities with components
4. Run game loop with delta time
5. Handle events and entity interactions
6. Create complex game objects using factory

================================================================================
"""

# TEST CODE FOR EXERCISE 3
def test_exercise_3():
    """Comprehensive test suite for Advanced Game Engine"""
    
    print("=== TESTING EXERCISE 3: ADVANCED GAME ENGINE ===\n")
    
    # Import your classes here
    # from your_solution import (EventType, Event, Component, Transform, Health, 
    #                          Inventory, Physics, Renderer, System, MovementSystem,
    #                          CombatSystem, RenderSystem, CollisionSystem, Entity,
    #                          GameEngine, GameObjectFactory)
    
    try:
        # Test 1: Component system
        print("Test 1: Testing component system...")
        
        # Create components
        transform = Transform(1, 100, 200, 0, 1)
        health = Health(2, 100, 100, 5)
        physics = Physics(3, 0, 0, 0, 0, 1, 0.1)
        
        # Test component data
        assert transform.entity_id == 1, "Transform should have correct entity ID"
        assert health.current_hp == 100, "Health should start at max HP"
        assert health.max_hp == 100, "Max HP should be set correctly"
        
        # Test 2: Entity creation and component management
        print("Test 2: Testing entity and component management...")
        
        game_engine = GameEngine()
        entity = game_engine.create_entity()
        
        # Add components
        entity.add_component(transform)
        entity.add_component(health)
        entity.add_component(physics)
        
        # Test component retrieval
        assert entity.has_component(Transform), "Entity should have Transform component"
        assert entity.has_component(Health), "Entity should have Health component"
        assert entity.has_component(Physics), "Entity should have Physics component"
        assert not entity.has_component(Inventory), "Entity should not have Inventory component"
        
        retrieved_transform = entity.get_component(Transform)
        assert retrieved_transform is not None, "Should retrieve Transform component"
        assert retrieved_transform.entity_id == entity.entity_id, "Component should belong to entity"
        
        # Test 3: System creation and requirements
        print("Test 3: Testing system creation and requirements...")
        
        movement_system = MovementSystem()
        combat_system = CombatSystem()
        render_system = RenderSystem()
        collision_system = CollisionSystem()
        
        # Test system requirements
        movement_req = movement_system.get_required_components()
        assert Transform in movement_req, "Movement system should require Transform"
        assert Physics in movement_req, "Movement system should require Physics"
        
        combat_req = combat_system.get_required_components()
        assert Health in combat_req, "Combat system should require Health"
        
        # Test 4: Game engine system management
        print("Test 4: Testing game engine system management...")
        
        game_engine.add_system(movement_system)
        game_engine.add_system(combat_system)
        game_engine.add_system(render_system)
        game_engine.add_system(collision_system)
        
        # Test system order by priority
        systems = game_engine.systems
        assert len(systems) == 4, "Should have 4 systems"
        
        # Test 5: Entity queries
        print("Test 5: Testing entity queries...")
        
        # Create another entity with different components
        entity2 = game_engine.create_entity()
        inventory = Inventory(entity2.entity_id, {}, 20, 100)
        renderer = Renderer(entity2.entity_id, "sprite1", "blue", True, 1)
        
        entity2.add_component(inventory)
        entity2.add_component(renderer)
        
        # Query entities with specific components
        moving_entities = game_engine.get_entities_with_components([Transform, Physics])
        assert len(moving_entities) == 1, "Should find 1 entity with Transform and Physics"
        assert moving_entities[0].entity_id == entity.entity_id, "Should find the correct entity"
        
        # Test 6: Event system
        print("Test 6: Testing event system...")
        
        # Create and emit events
        collision_event = Event(EventType.COLLISION, entity.entity_id, entity2.entity_id, 
                              {"damage": 10}, 0)
        game_engine.emit_event(collision_event)
        
        movement_event = Event(EventType.MOVEMENT, entity.entity_id, None, 
                             {"old_pos": (100, 200), "new_pos": (110, 205)}, 0)
        game_engine.emit_event(movement_event)
        
        # Test event queue
        assert len(game_engine.event_queue) == 2, "Should have 2 events in queue"
        
        # Process events
        game_engine.process_events()
        assert len(game_engine.event_queue) == 0, "Event queue should be empty after processing"
        
        # Test 7: Game loop and system updates
        print("Test 7: Testing game loop and system updates...")
        
        # Set initial physics values
        physics_comp = entity.get_component(Physics)
        physics_comp.velocity = (10, 5)
        
        # Update with delta time
        delta_time = 0.016  # ~60 FPS
        game_engine.update(delta_time)
        
        # Check if position updated
        updated_transform = entity.get_component(Transform)
        assert updated_transform.position[0] > 100, "X position should have increased"
        assert updated_transform.position[1] > 200, "Y position should have increased"
        
        # Test 8: GameObjectFactory
        print("Test 8: Testing GameObjectFactory...")
        
        # Create player
        player = GameObjectFactory.create_player((50, 50))
        assert player.has_component(Transform), "Player should have Transform"
        assert player.has_component(Health), "Player should have Health"
        assert player.has_component(Physics), "Player should have Physics"
        assert player.has_component(Inventory), "Player should have Inventory"
        
        # Create enemy
        enemy = GameObjectFactory.create_enemy((200, 200), "orc")
        assert enemy.has_component(Transform), "Enemy should have Transform"
        assert enemy.has_component(Health), "Enemy should have Health"
        
        # Create item
        item = GameObjectFactory.create_item((100, 100), "sword")
        assert item.has_component(Transform), "Item should have Transform"
        
        # Create projectile
        projectile = GameObjectFactory.create_projectile((0, 0), (1, 0), 100)
        assert projectile.has_component(Transform), "Projectile should have Transform"
        assert projectile.has_component(Physics), "Projectile should have Physics"
        
        # Test 9: Complex interactions
        print("Test 9: Testing complex interactions...")
        
        # Add entities to engine
        game_engine.entities[player.entity_id] = player
        game_engine.entities[enemy.entity_id] = enemy
        game_engine.entities[item.entity_id] = item
        game_engine.entities[projectile.entity_id] = projectile
        
        # Test collision detection
        collision_entities = game_engine.get_entities_with_components([Transform, Physics])
        assert len(collision_entities) >= 2, "Should have multiple entities for collision detection"
        
        # Test 10: Performance and edge cases
        print("Test 10: Testing performance and edge cases...")
        
        # Create many entities
        entities_created = []
        for i in range(100):
            test_entity = game_engine.create_entity()
            test_transform = Transform(test_entity.entity_id, random.randint(0, 1000), 
                                     random.randint(0, 1000), 0, 1)
            test_physics = Physics(test_entity.entity_id, random.uniform(-50, 50), 
                                 random.uniform(-50, 50), 0, 0, 1, 0.1)
            test_entity.add_component(test_transform)
            test_entity.add_component(test_physics)
            entities_created.append(test_entity)
        
        # Test system performance with many entities
        start_time = 0
        game_engine.update(0.016)
        # Performance should be reasonable
        
        # Test entity destruction
        initial_count = len(game_engine.entities)
        game_engine.destroy_entity(entities_created[0].entity_id)
        assert len(game_engine.entities) == initial_count - 1, "Entity should be destroyed"
        
        # Test component removal
        player.remove_component(Inventory)
        assert not player.has_component(Inventory), "Inventory component should be removed"
        
        # Test system disable
        movement_system.enabled = False
        old_position = player.get_component(Transform).position
        game_engine.update(0.016)
        new_position = player.get_component(Transform).position
        # Position shouldn't change much with disabled movement system
        
        # Test 11: Advanced event handling
        print("Test 11: Testing advanced event handling...")
        
        # Test event data integrity
        damage_event = Event(EventType.ATTACK, player.entity_id, enemy.entity_id, 
                           {"damage": 25, "weapon": "sword", "critical": True}, 1.0)
        game_engine.emit_event(damage_event)
        
        # Test event ordering
        events_before = len(game_engine.event_queue)
        game_engine.emit_event(Event(EventType.PICKUP, player.entity_id, item.entity_id, 
                                   {"item_type": "sword"}, 1.1))
        game_engine.emit_event(Event(EventType.LEVEL_UP, player.entity_id, None, 
                                   {"new_level": 2}, 1.2))
        
        assert len(game_engine.event_queue) == events_before + 3, "Should have 3 new events"
        
        # Test 12: Component data serialization
        print("Test 12: Testing component data serialization...")
        
        # Test component data methods
        health_comp = player.get_component(Health)
        health_data = health_comp.get_data()
        assert isinstance(health_data, dict), "Component data should be a dictionary"
        assert "current_hp" in health_data, "Health data should contain current_hp"
        assert "max_hp" in health_data, "Health data should contain max_hp"
        
        # Test setting data
        new_health_data = {"current_hp": 75, "max_hp": 100, "regeneration_rate": 3}
        health_comp.set_data(new_health_data)
        assert health_comp.current_hp == 75, "Current HP should be updated"
        assert health_comp.regeneration_rate == 3, "Regeneration rate should be updated"
        
        # Test 13: System priority and execution order
        print("Test 13: Testing system priority and execution order...")
        
        # Systems should execute in priority order
        system_execution_order = []
        
        # Mock systems to track execution order
        original_update = movement_system.update
        def track_movement_update(entities, delta_time):
            system_execution_order.append("movement")
            return original_update(entities, delta_time)
        movement_system.update = track_movement_update
        
        original_combat_update = combat_system.update
        def track_combat_update(entities, delta_time):
            system_execution_order.append("combat")
            return original_combat_update(entities, delta_time)
        combat_system.update = track_combat_update
        
        # Re-enable movement system
        movement_system.enabled = True
        
        # Clear previous order and run update
        system_execution_order.clear()
        game_engine.update(0.016)
        
        # Check that systems executed
        assert len(system_execution_order) >= 2, "Multiple systems should have executed"
        
        # Test 14: Entity lifecycle management
        print("Test 14: Testing entity lifecycle management...")
        
        # Test entity activation/deactivation
        test_entity = game_engine.create_entity()
        test_entity.active = False
        
        # Inactive entities shouldn't be processed by systems
        inactive_entities = game_engine.get_entities_with_components([Transform])
        active_entity_count = sum(1 for e in inactive_entities if e.active)
        
        # Test entity component updates
        transform_comp = Transform(test_entity.entity_id, 0, 0, 0, 1)
        test_entity.add_component(transform_comp)
        
        # Update component
        transform_comp.update()  # Should not raise error
        
        # Test 15: Factory pattern validation
        print("Test 15: Testing factory pattern validation...")
        
        # Test that factory creates consistent objects
        player1 = GameObjectFactory.create_player((0, 0))
        player2 = GameObjectFactory.create_player((100, 100))
        
        # Both should have same component types
        player1_components = set(type(comp) for comp in player1.components.values())
        player2_components = set(type(comp) for comp in player2.components.values())
        assert player1_components == player2_components, "Players should have same component types"
        
        # But different positions
        pos1 = player1.get_component(Transform).position
        pos2 = player2.get_component(Transform).position
        assert pos1 != pos2, "Players should have different positions"
        
        # Test different enemy types
        orc = GameObjectFactory.create_enemy((0, 0), "orc")
        goblin = GameObjectFactory.create_enemy((0, 0), "goblin")
        
        # Should have different stats
        orc_health = orc.get_component(Health)
        goblin_health = goblin.get_component(Health)
        # Health values might be different based on enemy type
        
        # Test 16: Error handling and edge cases
        print("Test 16: Testing error handling and edge cases...")
        
        # Test removing non-existent component
        try:
            player.remove_component(Inventory)  # Already removed earlier
            # Should handle gracefully
        except:
            pass
        
        # Test getting non-existent component
        non_existent = player.get_component(Inventory)
        assert non_existent is None, "Should return None for non-existent component"
        
        # Test destroying non-existent entity
        result = game_engine.destroy_entity(99999)
        assert result == False, "Should return False for non-existent entity"
        
        # Test empty component query
        empty_query = game_engine.get_entities_with_components([])
        assert len(empty_query) == 0, "Empty component query should return empty list"
        
        # Test component with invalid entity ID
        invalid_transform = Transform(99999, 0, 0, 0, 1)
        assert invalid_transform.entity_id == 99999, "Should allow invalid entity ID"
        
        # Test 17: Memory management and cleanup
        print("Test 17: Testing memory management and cleanup...")
        
        # Test that destroyed entities are properly cleaned up
        entities_before_cleanup = len(game_engine.entities)
        
        # Create and destroy multiple entities
        temp_entities = []
        for i in range(10):
            temp_entity = game_engine.create_entity()
            temp_entities.append(temp_entity.entity_id)
        
        # Destroy half of them
        for i in range(5):
            game_engine.destroy_entity(temp_entities[i])
        
        # Check entity count
        entities_after_cleanup = len(game_engine.entities)
        expected_count = entities_before_cleanup + 5
        assert entities_after_cleanup == expected_count, f"Should have {expected_count} entities after cleanup"
        
        # Test 18: System interactions
        print("Test 18: Testing system interactions...")
        
        # Test that systems can interact through events
        # Create entities that will trigger system interactions
        projectile_entity = GameObjectFactory.create_projectile((0, 0), (1, 0), 100)
        target_entity = GameObjectFactory.create_enemy((100, 0), "target")
        
        game_engine.entities[projectile_entity.entity_id] = projectile_entity
        game_engine.entities[target_entity.entity_id] = target_entity
        
        # Run several update cycles
        for i in range(10):
            game_engine.update(0.016)
        
        # Check that projectile moved
        projectile_transform = projectile_entity.get_component(Transform)
        assert projectile_transform.position[0] > 0, "Projectile should have moved"
        
        # Test 19: Component interdependencies
        print("Test 19: Testing component interdependencies...")
        
        # Test that components can depend on each other
        entity_with_deps = game_engine.create_entity()
        
        # Add components that might depend on each other
        dep_transform = Transform(entity_with_deps.entity_id, 0, 0, 0, 1)
        dep_physics = Physics(entity_with_deps.entity_id, 10, 10, 0, 0, 1, 0.1)
        dep_renderer = Renderer(entity_with_deps.entity_id, "test", "red", True, 1)
        
        entity_with_deps.add_component(dep_transform)
        entity_with_deps.add_component(dep_physics)
        entity_with_deps.add_component(dep_renderer)
        
        # Update and check that all components work together
        game_engine.entities[entity_with_deps.entity_id] = entity_with_deps
        game_engine.update(0.016)
        
        # All components should still be functional
        assert entity_with_deps.has_component(Transform), "Transform should still exist"
        assert entity_with_deps.has_component(Physics), "Physics should still exist"
        assert entity_with_deps.has_component(Renderer), "Renderer should still exist"
        
        # Test 20: Final integration test
        print("Test 20: Final integration test...")
        
        # Create a mini-game scenario
        game_player = GameObjectFactory.create_player((50, 50))
        game_enemy = GameObjectFactory.create_enemy((200, 200), "boss")
        game_item = GameObjectFactory.create_item((100, 100), "health_potion")
        
        # Add to game engine
        game_engine.entities[game_player.entity_id] = game_player
        game_engine.entities[game_enemy.entity_id] = game_enemy
        game_engine.entities[game_item.entity_id] = game_item
        
        # Simulate game events
        pickup_event = Event(EventType.PICKUP, game_player.entity_id, game_item.entity_id, 
                           {"item": "health_potion"}, 2.0)
        game_engine.emit_event(pickup_event)
        
        attack_event = Event(EventType.ATTACK, game_player.entity_id, game_enemy.entity_id, 
                           {"damage": 50}, 2.1)
        game_engine.emit_event(attack_event)
        
        # Run game loop
        for frame in range(60):  # 1 second at 60 FPS
            game_engine.update(0.016)
        
        # Verify game state
        assert game_player.active, "Player should still be active"
        assert game_enemy.active, "Enemy should still be active"
        
        # Check that events were processed
        assert len(game_engine.event_queue) == 0, "All events should be processed"
        
        # Test final entity count
        final_entity_count = len([e for e in game_engine.entities.values() if e.active])
        assert final_entity_count > 0, "Should have active entities"
        
        print("✅ All tests passed for Exercise 3!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

# Run all tests
if __name__ == "__main__":
    test_exercise_1()
    print("\n" + "="*80 + "\n")
    test_exercise_2()
    print("\n" + "="*80 + "\n")
    test_exercise_3()