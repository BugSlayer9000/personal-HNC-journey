# Factory 

### purpose
- Encapsulate objects creation logic so you can create objects without exposing the creation code directly to the client. This follows **open/cloded principle(OCP)** -- add new objects types without modifying existing client code

### Why does it matters in the industry 
- Reduces coupling between code that uses and object code that creates it
- Centralises complex creation logic (eg - dipendacies,configaration)
- Allows runtime decition-making about which class to instantiate


### Basic structure 
- **Product** - interface or base class for the object being created
- **Contreate products** - Implementations for the product
- **Factory** - Contains a method that decides which product to create

  
