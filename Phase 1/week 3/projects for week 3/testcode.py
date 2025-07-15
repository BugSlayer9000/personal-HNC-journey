import unittest
from datetime import datetime, timedelta
import sys
import os

# Test Suite for Exercise 1: Library Management System
class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # You'll need to import your classes here
        # from your_library_module import Book, Member, Library
        pass
    
    def test_book_creation_and_validation(self):
        """Test book creation with valid and invalid ISBN."""
        # Test valid ISBN (13 digits)
        try:
            book = Book("Python Programming", "John Doe", "9780123456789", 2023, "Programming")
            self.assertEqual(book.isbn, "9780123456789")
            self.assertTrue(book.is_available())
        except Exception as e:
            self.fail(f"Valid book creation failed: {e}")
        
        # Test invalid ISBN
        with self.assertRaises(ValueError):
            Book("Invalid Book", "Author", "123", 2023, "Fiction")
    
    def test_member_borrowing_limits(self):
        """Test member borrowing limits and book tracking."""
        member = Member("Alice Smith", "M001", "alice@email.com")
        library = Library()
        
        # Add books to library
        books = [
            Book("Book 1", "Author 1", "9780123456781", 2023, "Fiction"),
            Book("Book 2", "Author 2", "9780123456782", 2023, "Fiction"),
            Book("Book 3", "Author 3", "9780123456783", 2023, "Fiction"),
            Book("Book 4", "Author 4", "9780123456784", 2023, "Fiction")
        ]
        
        for book in books:
            library.add_book(book)
        
        library.register_member(member)
        
        # Test borrowing within limit
        for i in range(3):
            result = library.checkout_book(books[i].isbn, member.member_id)
            self.assertTrue(result)
        
        # Test borrowing beyond limit
        result = library.checkout_book(books[3].isbn, member.member_id)
        self.assertFalse(result)
    
    def test_book_search_functionality(self):
        """Test different search methods."""
        library = Library()
        books = [
            Book("Python Basics", "John Smith", "9780123456781", 2023, "Programming"),
            Book("Java Advanced", "John Smith", "9780123456782", 2023, "Programming"),
            Book("Mystery Novel", "Jane Doe", "9780123456783", 2023, "Fiction")
        ]
        
        for book in books:
            library.add_book(book)
        
        # Search by author
        john_books = library.search_by_author("John Smith")
        self.assertEqual(len(john_books), 2)
        
        # Search by genre
        programming_books = library.search_by_genre("Programming")
        self.assertEqual(len(programming_books), 2)
        
        # Search by title
        python_books = library.search_by_title("Python")
        self.assertEqual(len(python_books), 1)
    
    def test_reservation_system(self):
        """Test the extra challenge: book reservation system."""
        library = Library()
        book = Book("Popular Book", "Famous Author", "9780123456789", 2023, "Fiction")
        member1 = Member("Alice", "M001", "alice@email.com")
        member2 = Member("Bob", "M002", "bob@email.com")
        
        library.add_book(book)
        library.register_member(member1)
        library.register_member(member2)
        
        # Member1 checks out the book
        self.assertTrue(library.checkout_book(book.isbn, member1.member_id))
        
        # Member2 reserves the book
        self.assertTrue(library.reserve_book(book.isbn, member2.member_id))
        
        # Member1 returns the book
        library.return_book(book.isbn, member1.member_id)
        
        # Check if member2 gets notification about availability
        reservations = library.get_reservations(book.isbn)
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].member_id, member2.member_id)


# Test Suite for Exercise 2: Shopping Cart System
class TestShoppingCartSystem(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        # from your_shopping_module import DigitalProduct, PhysicalProduct, ShoppingCart, etc.
        pass
    
    def test_product_polymorphism(self):
        """Test different product types behave correctly."""
        digital_product = DigitalProduct("E-book", 19.99, "EBOOK001", "Digital book", 5.2)
        physical_product = PhysicalProduct("Laptop", 999.99, "LAPTOP001", "Gaming laptop", 2.5, (30, 20, 5))
        
        # Digital products should have no shipping cost
        self.assertEqual(digital_product.calculate_shipping(), 0.0)
        
        # Physical products should have shipping cost based on weight
        self.assertGreater(physical_product.calculate_shipping(), 0.0)
        
        # Both should calculate tax differently
        digital_tax = digital_product.calculate_tax()
        physical_tax = physical_product.calculate_tax()
        self.assertNotEqual(digital_tax, physical_tax)
    
    def test_shopping_cart_operations(self):
        """Test cart add/remove operations and calculations."""
        cart = ShoppingCart()
        product1 = DigitalProduct("Software", 49.99, "SW001", "Productivity software", 1.0)
        product2 = PhysicalProduct("Mouse", 29.99, "MOUSE001", "Gaming mouse", 0.2, (10, 5, 3))
        
        # Add products
        cart.add_product(product1, 2)
        cart.add_product(product2, 1)
        
        # Check quantities
        self.assertEqual(cart.get_quantity(product1), 2)
        self.assertEqual(cart.get_quantity(product2), 1)
        
        # Test total calculation
        subtotal = cart.calculate_subtotal()
        expected_subtotal = (49.99 * 2) + (29.99 * 1)
        self.assertEqual(subtotal, expected_subtotal)
        
        # Remove product
        cart.remove_product(product1)
        self.assertEqual(cart.get_quantity(product1), 0)
    
    def test_discount_stacking(self):
        """Test the extra challenge: stackable discounts."""
        cart = ShoppingCart()
        product = DigitalProduct("Game", 59.99, "GAME001", "Video game", 8.0)
        cart.add_product(product, 1)
        
        # Apply percentage discount
        cart.apply_discount("SAVE20", 0.20)  # 20% off
        
        # Apply fixed amount discount
        cart.apply_discount("SAVE10", 10.0)  # $10 off
        
        # Check final total with stacked discounts
        total_without_discount = 59.99
        total_with_discounts = cart.calculate_total()
        
        # Should be less than original price
        self.assertLess(total_with_discounts, total_without_discount)
    
    def test_payment_processing(self):
        """Test different payment methods."""
        cart = ShoppingCart()
        product = PhysicalProduct("Book", 24.99, "BOOK001", "Programming book", 0.5, (20, 15, 2))
        cart.add_product(product, 1)
        
        # Test credit card payment
        cc_processor = CreditCardProcessor()
        payment_result = cc_processor.process_payment(cart.calculate_total(), "4111111111111111", "123", "12/25")
        self.assertTrue(payment_result.success)
        
        # Test PayPal payment
        paypal_processor = PayPalProcessor()
        payment_result = paypal_processor.process_payment(cart.calculate_total(), "user@example.com", "password")
        self.assertTrue(payment_result.success)
    
    def test_inventory_management(self):
        """Test inventory tracking for physical products."""
        product = PhysicalProduct("Limited Item", 99.99, "LIMITED001", "Limited edition", 1.0, (10, 10, 10))
        product.set_inventory(5)
        
        cart = ShoppingCart()
        
        # Should be able to add 5 items
        result = cart.add_product(product, 5)
        self.assertTrue(result)
        
        # Should not be able to add more than available
        result = cart.add_product(product, 1)
        self.assertFalse(result)


# Test Suite for Exercise 3: Task Management System
class TestTaskManagementSystem(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        # from your_task_module import Admin, Manager, Employee, Task, Project, etc.
        pass
    
    def test_user_role_permissions(self):
        """Test different user roles and their permissions."""
        admin = Admin("admin", "admin@company.com", "hashed_password")
        manager = Manager("manager", "manager@company.com", "hashed_password")
        employee = Employee("employee", "employee@company.com", "hashed_password")
        
        # Test permission levels
        self.assertTrue(admin.can_create_users())
        self.assertTrue(admin.can_delete_tasks())
        
        self.assertTrue(manager.can_assign_tasks())
        self.assertFalse(manager.can_create_users())
        
        self.assertTrue(employee.can_view_tasks())
        self.assertFalse(employee.can_delete_tasks())
    
    def test_task_creation_and_factory(self):
        """Test task factory and different task types."""
        admin = Admin("admin", "admin@company.com", "hashed_password")
        factory = TaskFactory()
        
        # Create different types of tasks
        bug_task = factory.create_task("Bug", "Fix login issue", admin, priority="High")
        feature_task = factory.create_task("Feature", "Add dark mode", admin, priority="Medium")
        meeting_task = factory.create_task("Meeting", "Team standup", admin, priority="Low")
        
        # Check task types and default values
        self.assertEqual(bug_task.task_type, "Bug")
        self.assertEqual(bug_task.priority, "High")
        
        self.assertEqual(feature_task.task_type, "Feature")
        self.assertEqual(feature_task.priority, "Medium")
        
        # Check if appropriate templates were applied
        self.assertIn("bug", bug_task.tags)
        self.assertIn("feature", feature_task.tags)
    
    def test_notification_observer_pattern(self):
        """Test observer pattern for notifications."""
        # Create notification service (singleton)
        notification_service = NotificationService.get_instance()
        
        # Create observers
        email_notifier = EmailNotifier()
        slack_notifier = SlackNotifier()
        
        # Subscribe observers
        notification_service.subscribe(email_notifier)
        notification_service.subscribe(slack_notifier)
        
        # Create task and change status
        admin = Admin("admin", "admin@company.com", "hashed_password")
        task = Task("Test Task", "Test description", admin)
        
        # Change task status should trigger notifications
        task.change_status("In Progress")
        
        # Check if notifications were sent
        self.assertEqual(len(email_notifier.sent_notifications), 1)
        self.assertEqual(len(slack_notifier.sent_notifications), 1)
    
    def test_project_management(self):
        """Test project-level operations."""
        admin = Admin("admin", "admin@company.com", "hashed_password")
        manager = Manager("manager", "manager@company.com", "hashed_password")
        employee = Employee("employee", "employee@company.com", "hashed_password")
        
        project = Project("Website Redesign", "Redesign company website", admin)
        
        # Add team members
        project.add_member(manager)
        project.add_member(employee)
        
        # Create tasks
        task1 = Task("Design mockups", "Create UI mockups", manager)
        task2 = Task("Implement frontend", "Code the frontend", employee)
        
        project.add_task(task1)
        project.add_task(task2)
        
        # Test progress calculation
        task1.change_status("Completed")
        progress = project.calculate_progress()
        self.assertEqual(progress, 50.0)  # 1 out of 2 tasks completed
    
    def test_command_pattern_undo_redo(self):
        """Test the extra challenge: command pattern with undo/redo."""
        admin = Admin("admin", "admin@company.com", "hashed_password")
        project = Project("Test Project", "Test project", admin)
        
        # Create task using command
        create_command = CreateTaskCommand(project, "New Task", "Task description", admin)
        create_command.execute()
        
        # Check task was created
        self.assertEqual(len(project.tasks), 1)
        
        # Undo the command
        create_command.undo()
        
        # Check task was removed
        self.assertEqual(len(project.tasks), 0)
        
        # Redo the command
        create_command.redo()
        
        # Check task was created again
        self.assertEqual(len(project.tasks), 1)
    
    def test_singleton_notification_service(self):
        """Test that notification service is a proper singleton."""
        service1 = NotificationService.get_instance()
        service2 = NotificationService.get_instance()
        
        # Both should be the same instance
        self.assertIs(service1, service2)
        
        # Test thread safety (basic test)
        import threading
        instances = []
        
        def create_instance():
            instances.append(NotificationService.get_instance())
        
        threads = [threading.Thread(target=create_instance) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        # All instances should be the same
        for instance in instances:
            self.assertIs(instance, service1)
    
    def test_task_status_transitions(self):
        """Test valid and invalid task status transitions."""
        admin = Admin("admin", "admin@company.com", "hashed_password")
        task = Task("Test Task", "Test description", admin)
        
        # Valid transitions
        self.assertTrue(task.change_status("In Progress"))
        self.assertTrue(task.change_status("Completed"))
        
        # Invalid transition (completed to todo)
        self.assertFalse(task.change_status("To Do"))
        
        # Test status history
        self.assertEqual(len(task.status_history), 3)  # Created, In Progress, Completed


def run_specific_test(exercise_number):
    """Run tests for a specific exercise."""
    test_classes = {
        1: TestLibrarySystem,
        2: TestShoppingCartSystem,
        3: TestTaskManagementSystem
    }
    
    if exercise_number in test_classes:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_classes[exercise_number])
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return result.wasSuccessful()
    else:
        print(f"Invalid exercise number: {exercise_number}")
        return False


def run_all_tests():
    """Run all tests for all exercises."""
    print("Running all OOP exercise tests...\n")
    
    all_passed = True
    for i in range(1, 4):
        print(f"{'='*50}")
        print(f"EXERCISE {i} TESTS")
        print(f"{'='*50}")
        passed = run_specific_test(i)
        all_passed = all_passed and passed
        print()
    
    print(f"{'='*50}")
    print(f"OVERALL RESULT: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    print(f"{'='*50}")
    
    return all_passed


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try:
            exercise_num = int(sys.argv[1])
            run_specific_test(exercise_num)
        except ValueError:
            print("Usage: python test_suite.py [exercise_number]")
            print("Example: python test_suite.py 1")
    else:
        run_all_tests()