from bank_account import BankAccount
from bank_exeptions import NegativeAmountError, InsufficientFundsError, AccountError


def main():
    print("=== Bank Account System Test ===\n")
    
    # Create account with £100
    account = BankAccount(100)
    print(f"Initial balance: £{account.get_balance():.2f}\n")
    
    # Test 1: Successful deposit
    try:
        print("Depositing £50.00...")
        account.deposit(50)
        print()
    except AccountError as e:
        print(f"Error: {e}\n")
    
    # Test 2: Insufficient funds
    try:
        print("Attempting to withdraw £200.00...")
        account.withdraw(200)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        print(f"You are short £{e.shortage:.2f}\n")
    except AccountError as e:
        print(f"Error: {e}\n")
    
    # Test 3: Negative deposit
    try:
        print("Attempting to deposit -£30.00...")
        account.deposit(-30)
    except NegativeAmountError as e:
        print(f"Error: {e}\n")
    except AccountError as e:
        print(f"Error: {e}\n")
    
    # Test 4: Negative withdrawal
    try:
        print("Attempting to withdraw -£20.00...")
        account.withdraw(-20)
    except NegativeAmountError as e:
        print(f"Error: {e}\n")
    except AccountError as e:
        print(f"Error: {e}\n")
    
    # Test 5: General AccountError catch
    try:
        print("Attempting invalid operation...")
        account.withdraw(1000)
    except AccountError as e:
        print(f"Account Error: {e}\n")
    
    print(f"Final balance: £{account.get_balance():.2f}")


if __name__ == "__main__":
    main()