# custom exeptions

# Base exeption
class AccountError(Exception):
    """Raised when there is an error in the account system"""
    pass


class NegativeAmountError(AccountError):
    
    """Raised when there is a negative amount"""
    
    def __init__(self, *args: object, amount:float) -> None:
        super().__init__(*args)
        self.amount = amount
        

class InsufficiebtFunds(Exception):
    """Raised when withdrawl exeeds abalance"""
    
    def __init__(self, *args: object, current_balance:float, reqested_amount:float) -> None:
        super().__init__(*args)
        self.current_balance = current_balance
        self.requested_amount = reqested_amount
    
    @property
    def get_shortage(self):
        return self.current_balance - self.requested_amount


