# Programming concepts phase 1 week 4 - Provided by Chat GPT for a self-stydying level 7 software dev student
## 1️⃣: Main - SOLID principles 
- **💥Purpose** - Solid principles is to engineer software that is maintainable, scalable, testable and orbust - Specially in the face of **Changing Requrements**. These principles provide a strategic foundation for writing *clean*, *modular* and *extensible object-oriented* code
### What does SOLID stands for 
1. **S - Single Responsibility Principle(SRP)**
    - Each class/module has only one, and only one, Reason to change
    - *Keep your classes laser-focused on a single thing on a single business capability*
2. **O - Open/Closed principle(OCP)**
    - "open for extention, closed for modification"
    - *Build extention points (via interface/abstract classes) so new features plug in without trwling through existing code*
3. **L - Liskow Substitiution Principle(LSP)**
    - Subtype must be subsuitable for their base types without altering the correcness of the program.
    - **Simply** - *if class A is the parent and class B is the child of A, Then anywhere you use A, You should be able to use B -- and your program should still behave correctly*
    - **Rule - If your base class promised something, the subclass must deliver, or you're violating LSP.**
4. **I - Interface Segregation Principle(ISP)**
    - Don't force clients to depend on methods they don't use
    - **Instead of one fat interface, split it into lean, role-specific interfaces**
5. **D - Dependacny Inversion Principle(DIP)**
    - depend on abstractions, not concretions
    - *High level module should not import low-level modules directly; Both should talk to an interface or abstract base class*

## 2️⃣ GRASP patterns
**Meaning** - *Genaral Responsibility Assignment Software patterns*
### 1. Creator 
   - A class should create instances of classes it contains or closely uses or aggregates.
   - *Example - A project creates task instances because tasks belong to a project. but a UserInterface Should never be in charge of instantiating Task object directly*
   - **Why does it matters** - Keeps object creation logical and contextual. Reduces coupling with external constructors.
### 2. Information Expert
   - *Assign a responsibility to the class that has the necessary information to fulfill it*
   - **Example** - if a *Task* onject holds data about deadlines , it should be responsible for calculating if it's overude. you wouldn't give that responsibility to *Project* or *User*
   - **Why does it matter** - it keeps your logic close to the data -- making your code easiar to reason about and test
### 3.  Controller 
