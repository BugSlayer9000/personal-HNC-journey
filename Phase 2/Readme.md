# Weekly Reflection - Phase 2 Week 4

**Week of:** 13th of Oct 25 - 19th of Oct 25  
**Phase Focus:** File Handling, GUI, Data Validation & Error Handling

## 🎯 This Week's Goals
<!-- What did you plan to accomplish this week? -->
- [x] Input Handling
- [x] Exception hierarchy & custom exceptions
- [ ] Django 15 hour course pt1 (Moved to next week)

## ✅ What I Accomplished
<!-- What did you actually complete? Be specific! -->

### Concepts Learned

- **Exception Hierarchy:** Learned how Python organizes exceptions in a hierarchical tree structure with `BaseException` at the top and `Exception` as the base for most user-defined exceptions. Understood that parent exceptions catch all their child exceptions (e.g., `LookupError` catches both `IndexError` and `KeyError`). Mastered the importance of exception ordering - specific exceptions must be caught before general ones.

- **Custom Exceptions:** Learned to create application-specific exception classes that inherit from `Exception`. Understood how to store additional data in exceptions (like balance and shortage in banking errors). Practiced building multi-level exception hierarchies where base exceptions group related errors together, making code more maintainable and self-documenting.

- **Exception Handling Best Practices:** Learned to always use `raise` to trigger exceptions (not `return`), include meaningful error messages, call `super().__init__()` in custom exceptions, and catch exceptions at appropriate levels of specificity. Understood when to let exceptions propagate vs when to handle them locally.

### Code/Projects Completed

- **Exercise 1 - Exception Hierarchy Exploration:** [Phase 2/week 3/Exception hierarchy & custom exceptions/Exercises/Exercise 1]
  - **What it does:** Demonstrates how parent/child exception relationships work, showing that `LookupError` catches `IndexError`, and illustrates the critical importance of exception catching order
  - **Key techniques used:** Try-except blocks, multiple exception handlers, demonstrating correct vs incorrect exception ordering
  - **Grade:** Completed ✓ (Basic understanding demonstrated)

- **Exercise 2 - Bank Account System:** [Phase 2/week 3/Exception hierarchy & custom exceptions/Exercises/Exercise 2]
  - **What it does:** Implements a banking system with custom exceptions (`AccountError`, `NegativeAmountError`, `InsufficientFundsError`) that store additional data like balance, amount, and calculated shortage
  - **Key techniques used:** Custom exception hierarchy, storing exception data, proper use of `raise` statements, exception inheritance from base class
  - **Grade:** 100% ✓ (Significant improvement after applying feedback - all fixes implemented correctly)

- **Exercise 3 - Student Grade Management:** [Phase 2/week 3/Exception hierarchy & custom exceptions/Exercises/Exercise 3]
  - **What it does:** Built a comprehensive gradebook system with multi-level exception hierarchy managing student records and grades with proper validation
  - **Key techniques used:** Complex exception hierarchy (`StudentSystemError` → `InvalidStudentIDError`, `DuplicateStudentError`, `StudentNotFoundError`, `GradeError` → `GradeOutOfRangeError`, `InvalidGradeTypeError`), dictionary operations, input validation, OOP principles
  - **Grade:** 78% (B+) - Good effort with one critical issue (GradeError inheritance) and some validation edge cases to fix

### Practice Problems Solved

- **Exercise 1:** Beginner level (⭐⭐☆☆☆) - Reinforced understanding of exception hierarchy and catching order
- **Exercise 2:** Intermediate level (⭐⭐⭐☆☆) - Initially struggled with raising vs returning exceptions, but successfully corrected after feedback
- **Exercise 3:** Intermediate-Advanced level (⭐⭐⭐⭐☆) - Main challenge was ensuring proper multi-level inheritance (missed that `GradeError` should inherit from `StudentSystemError` not `Exception`). Also struggled with hard-coding subjects instead of flexible design

## 📊 Self-Assessment

**Rate your understanding (1-5 scale):**

- **Exception Hierarchy:** [4/5] - Good understanding of parent-child relationships and catching order. Can explain why specific exceptions must come before general ones. Still need to internalize when to use which level of catching.

- **Custom Exceptions:** [4/5] - Comfortable creating custom exception classes with additional attributes. Successfully implemented exception hierarchies. Need more practice on designing flexible vs rigid exception structures (e.g., hard-coded subjects issue in Exercise 3).

- **Exception Best Practices:** [3.5/5] - Learned the importance of `raise` vs `return`, proper inheritance, and meaningful error messages. Initially made mistakes but corrected them after feedback. Need more practice on edge case handling (None values, empty data structures).

**Overall week satisfaction:** [4/5]

**Reasoning:** Made significant progress and successfully completed all exercises. The improvement from Exercise 2 (initial 27%) to the corrected version (100%) shows good learning ability. Exercise 3 at 78% demonstrates understanding of complex concepts but reveals areas needing attention (multi-level inheritance, flexible design patterns, edge case handling). Feel confident with the fundamentals but need more practice with advanced patterns.

## 🤔 Challenges Faced

1. **Spelling Consistency:** Multiple typos in filenames and variable names (`exeptions` instead of `exceptions`, `massage` instead of `message`) - need to slow down and proofread
2. **Conceptual Errors:** Initially returned exceptions instead of raising them in Exercise 2 - learned that exceptions must be raised with `raise`, not returned
3. **Design Decisions:** Hard-coded subjects in Exercise 3 instead of flexible approach - need to think about scalability earlier in design process
4. **Multi-level Inheritance:** Missed that `GradeError` should inherit from `StudentSystemError` - need to carefully read hierarchy diagrams before implementing

## 🎯 Next Week's Goals
<!-- Based on this week's progress, what's next? -->

- [x] Fix Exercise 3 critical issues (GradeError inheritance, ID validation to exactly 6 digits)
- [ ] Add missing test case in Exercise 3 (demonstrate `StudentSystemError` catches all)
- [ ] Refactor Exercise 3 to use flexible subject handling
- [ ] Start Django 15 hour course pt1
- [ ] Begin Inventory Manager GUI extension with Django

### Areas needing more practice:

- **Multi-level Exception Hierarchies:** Need to carefully plan inheritance structures before coding. Practice: Create 2-3 small projects with 3+ level exception hierarchies to reinforce proper inheritance patterns

- **Edge Case Handling:** Often miss edge cases like None values, empty collections, boundary conditions. Planned approach: Create a checklist of common edge cases to test before submitting (None, empty, boundary values, type mismatches)

- **Flexible vs Hard-coded Design:** Tend to hard-code values that should be dynamic. Practice: Review each data structure and ask "What if requirements change?" before finalizing design

- **Attention to Detail:** Spelling errors and misread requirements. Approach: Implement a "pre-submission checklist" - spell check, verify all requirements met, test edge cases, ensure proper inheritance

## 📝 Notes for Future Me

### Things to remember for exams/interviews:

- **Exception hierarchy order is critical:** Always catch specific exceptions before general ones. Parent exceptions catch ALL children!
- **Custom exceptions should inherit from Exception, not BaseException** (unless you have a very specific reason)
- **Always `raise` exceptions, never `return` them** - this was a critical mistake in Exercise 2
- **Multi-level hierarchies:** Base exception → Category exceptions → Specific exceptions. Example: `StudentSystemError` → `GradeError` → `GradeOutOfRangeError`
- **Exception design pattern:** Store relevant data as attributes, generate meaningful messages in `__init__`, always call `super().__init__(message)`

### Connections to make with future topics:

- Exception handling will be crucial in Django for form validation and database operations
- Custom exceptions will make GUI error handling much cleaner and more user-friendly
- These patterns apply to all OOP languages - good foundation for future learning

### Personal observations about your learning style:

- **Learn by doing and correcting:** The 27% → 100% improvement in Exercise 2 shows I learn effectively from mistakes when given good feedback
- **Need to read requirements more carefully:** Missed the exact ID length requirement (exactly 6 vs 7+) and the GradeError inheritance
- **Benefit from structured exercises:** The progression from Exercise 1 (basic) → 2 (intermediate) → 3 (advanced) worked well
- **Should slow down and verify before submission:** Many issues could be caught with a simple pre-submission checklist

### Quick Reference - Common Mistakes to Avoid:
✓ Use `raise` not `return` for exceptions  
✓ Specific exceptions before general ones  
✓ Always call `super().__init__()` in custom exceptions  
✓ Check inheritance carefully in multi-level hierarchies  
✓ Test edge cases: None, empty, boundaries  
✓ Spell check everything (especially "exceptions" not "exeptions")  

---

**Confidence Level Going Into Next Week:** High (4/5) - Solid understanding of fundamentals with clear areas to improve. Ready to apply exception handling to Django projects.
