# Decorators in pytnon

- Credits [5 python decorators you should use](https://www.youtube.com/watch?v=JgxCY-tbWHA)

## 5 decorators you should use 

- ### Property decorator 

  - `@property` 
  - This will let use create a mthod as if it was a an attribute
  - **Specially when we have a privet atrribute in a class to get the value we can use a propery decorator to access**
  - There are getters and setter in property decorators as well as to set a value to a privet attribute without acessing directly
  - Example - [Click](https://github.com/BugSlayer9000/personal-HNC-journey/blob/main/Phase%201/week%205/Decorations/decorator.py)

- ### Staticmethod decorator

  - `@staticmethod`
  - only used to know if a method inside a class is static
  - To say method belong to class but not the instance
  - you can do this without the instance meaning you can call the method in the class without the classes instance
  - Example - [Click](https://github.com/BugSlayer9000/personal-HNC-journey/blob/main/Phase%201/week%205/Decorations/staticmethod.py)

- ### Classmethod dcorator

  - `@classmthod`
  - Pass the class as the first argument instead of an instance
  - Use this method when you wanna acess class atrribute or methods
  - Works on the class level data
  - Example - [Click](https://github.com/BugSlayer9000/personal-HNC-journey/blob/main/Phase%201/week%205/Decorations/classmethod.py)

- ### fucntools.cache

  - import fucntools
  - `@fucntools.cache`
  - This is useful when a fucntion has a contant computation
  - This will write a custom cache for us
  - Whenever your calling the same fucntion repeatedly with the same argument you can cache that result using this without writing you own cache
  - Example - [Click](https://github.com/BugSlayer9000/personal-HNC-journey/blob/main/Phase%201/week%205/Decorations/functoolsExample.py)

- ### dataclass
  
  - from dataclass import dataclass
  - `@dataclass`
  - Puts on top a class
  - Automatically fills up the boiler plate for your class
  - Both classes will behave the same way, but Product2 is more concise and easier to read
  - Example - [Click](https://github.com/BugSlayer9000/personal-HNC-journey/blob/main/Phase%201/week%205/Decorations/dataclassEx.py)



