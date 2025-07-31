# Liskow Substitiution
- Video link - [Liskov Substitution Principle](https://www.youtube.com/watch?v=7hXi0N1oWFU)
## 🔥Robustness principle also known as postel's law 
- **Be conservative in what you do, be liberal in what you accept from others**
- We should be **Contravarient** in input and **covarient** in Output 
### Input 
   - The instance in the subtype needs to accept either what supertype is accepting or more 
### Output 
   - Our instance method should only return Values that are included in the set of possible values that the supertypr can return or something smaller like a a subset of that set
## 🔥**As extend this consists on 3 type rules and 4 behavioral rules**

## 3 Type Rules 
   1. Method parameters must be **contravariant**
   2. **Covariant** method return types
   3. No new exeptions. Only subtypes

## The Difference between Type rules and the Behaviour rules 
   - Notice how the pre condition can easily be captuered as a type
   - A method that actually accept all ints might not accept all ints. Maybe, a subject of all ints 

## 4 Behaviour Roules 

   1. Same or Stonger pre-conditions
      - For example - A method that requires an int might requre a non_negative int
   2. Same or stonger post-conditions
      - This defines what must be true after a method has been executed
      - For example -  A function that ruturns an absolute value of an int must never produce a negative number 
   3. Same or Stronger Single state invariants
   4. Same or stringer multi-state varients

