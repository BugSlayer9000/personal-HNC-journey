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
    def __init__(self, usernam, password):
        self.__username = usernam
        self.__password = password
    
    def check_password(self, password) -> bool:
        if self.__password == password:
            return True
        else:
            return False
    
    def change_password(self, old, new) -> bool:
        if old == self.__password:
            self.__password = new
            return True
        else:
            return False
    
    def get_username(self) -> str:
        return self.__username

# test solution

user = User("samod", "samod1")
print(user.check_password("samod1")) # True
print(user.check_password("samod2")) # wrong password # False
print(user.change_password("samod1", "oshadhi1")) # True
print(user.change_password("samod2", "oshadhi1")) # wrong one # False
print(user.get_username()) 
            



