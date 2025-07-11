# Abstraction 

# Reduce complexity by hiding unnecessary details

class EmailService:
    def _connect(self): # privet method because this is going to be used inside the class
        print("connecting to email server")
    
    def _authenticating(self): # privet method because this is going to be used inside the class
        print("authenticating!")
    
    def send_email(self): # this is where the process is happening and all the users in this class are going to interact with this instead of dealing with all the other methods (unnecessary complexity)
        self._connect()
        self._authenticating()
        print("sending Email")
    
    def _disconnect(self): # also gonna be used inside of the class 
        print("disconneting from the email service !")


email = EmailService()
email.send_email() #  makes the user easier to use the class otherwise it would be 5 methods in total which will make the code more complex as well

