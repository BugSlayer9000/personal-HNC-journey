# samod subhasha
# ✅ Exercise 4: User Authentication
# Task:
# Create a User class:

# Private attributes: __username, __password

# Methods:

# check_password(password) – returns True/False

# change_password(old, new) – allows update if old matches

# get_username() – returns username

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def check_password(self, password) -> bool:
        if self.__password == password:
            return True
        else:
            return False
    
    def change_password(self, old, new) -> bool:
        # Suggested solution use of a already existing method instead of repeating myself
        if self.check_password(old):
            self.__password = new
            return True
        else:
            return False
        
        # my solution
        
        # if old == self.__password:
        #     self.__password = new
        #     return True
        # else:
        #     return False
    
    def get_username(self) -> str:
        return self.__username

# test solution

user = User("samod", "samod1")
print(user.check_password("samod1")) # True
print(user.check_password("samod2")) # wrong password # False
print(user.change_password("samod1", "oshadhi1")) # True
print(user.change_password("samod2", "oshadhi1")) # wrong one # False
print(user.get_username()) 
            


# ✅ What You Did Well
# Encapsulation (✔️)
# Both __username and __password are privately scoped. This is exactly what you'd expect in a secure system.

# Function Responsibility (✔️)

# check_password() handles verification cleanly.

# change_password() updates only when old password matches — essential security pattern.

# get_username() keeps things readable.

# Boolean Returns (✔️)
# You're returning results instead of printing. ✅ This is best practice for scalable systems (e.g., if used in a GUI or API later).

# Naming Conventions (✔️)
# Method and variable names are precise and readable. Pythonic.

# | Category                | Score       | Comments                                           
# | ----------------------- | --------    | -------------------------------------------------- 
# | Encapsulation           | ✅ 5/5     | Perfect use of private attributes                  
# | Method Design           | ✅ 5/5    | Clear, minimalistic, appropriate                   
# | Security Considerations | ⚠️ 3.5/5  | No strength validation, which is okay at HNC level 
# | Professional Structure  | ✅ 5/5    | Very clean, good method separation                 
# | Variable Naming         | ⚠️ 4/5    | One typo (`usernam`)                               






