# custom exeptions

class AccountError(Exception):
    """Base exception for all account-related errors"""
    pass


class NegativeAmountError(AccountError):
    """Raised when a negative amount is provided"""
    
    def __init__(self, amount: float):
        self.amount = amount
        super().__init__(f"Amount cannot be negative: £{amount:.2f}")


class InsufficientFundsError(AccountError):
    """Raised when withdrawal exceeds available balance"""
    
    def __init__(self, current_balance: float, requested_amount: float):
        self.current_balance = current_balance
        self.requested_amount = requested_amount
        self.shortage = requested_amount - current_balance
        message = f"Insufficient funds. Need £{requested_amount:.2f}, but only £{current_balance:.2f} available"
        super().__init__(message)
    


