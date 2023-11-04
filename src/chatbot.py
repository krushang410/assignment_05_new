"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Krushang Bhatt}
Date: 2023-10-31
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account() -> int:

    """
    function does not include parameters and should return an integer
    
    Returns:
            result(int): Entered account number.

    Raises: 
           ValueError: Entered a non-numeric value.
           Exception: Entered invalid account number.
    
    """
    try:
        acc_number = int(input("Please enter your account number: "))
    except Exception:
        raise ValueError("Account number must be a whole number.")
    if acc_number not in ACCOUNTS:
        raise Exception("Account number entered does not exist.")
    return acc_number

def get_amount() -> float:
    """
    funtion does not includes any parameters and should return a float.

    Returns:
            result(float): Entered valid amount.

    Raises:
            ValueError: If entered amount is negative or invalid.
            Exception: If invalid amount is entered or less than zero.
    """
    try:
        amount = float(input("Enter the transaction amount:"))
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")
    if amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    return amount

def get_balance(account: int) -> str:
    """
    retrieve the balance of a particular account.

    Args:
        account (int): Account number of a person.

    Returns:
        str: Message showing account balance.

    Raises:
        Exception: If an account number does not exists in the ACCOUNTS dictionary.
    """
    if account in ACCOUNTS:
        balance = ACCOUNTS[account] ["balance"]
        return f"Your current balance for account {account} is ${balance:.2f}"
    else:
        raise Exception("Account number does not exist.")

def make_deposit(account: int, amount: float) -> str:
    """
    Recieves two parameters.
    Given two arguments,this function returns a string.

    Args:
        account(int): Account number to deposit the amount.
        amount(float): Amount of money deposited.

    Returns:
        str: Message indicating confirmation of deposit.

    Raises:
        Exception: If the account number does not exists in the ACCOUNTS dictionary.
        ValueError: If the amount is not greater than zero. 

    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    
    ACCOUNTS[account]["balance"] += amount
    return f"You have made a deposit of ${amount} to account {account}"
   
def user_selection() -> str:
    """
    Return the selection to lowercase.And no parameters are taken.

    Returns:
        str: User's selected task in lowercase.

    Raises:
        ValueError: If invalid user selection is provided.
    """
    user_choice = input("What would you like to do (balance/deposit/exit)?").lower()
    if user_choice in VALID_TASKS:
        return user_choice
    else:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    

# try:
#     num = user_selection()
#     print(num)
# except ValueError as e:
#     print(e)

## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION

def chatbot():
    
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            selection= user_selection()
            
            if selection != "exit":

                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        account= get_account()


                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)

                    if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED
                        ## ABOVE, AND PRINT THE RESULT:
                        balance = get_balance(account)
                        print (f"Your current balance for account {account} is ${balance}")         

                    else:
                        # Amount validation.
                        valid_amount = False
                while valid_amount == False:
                    try:
                        ## CALL THE get_amount FUNCTION HERE
                        ## AND CAPTURE THE RESULTS IN A VARIABLE 
                        amount= get_amount()

                        valid_amount = True
                    except Exception as e:
                        # Invalid amount.
                        print(e)
                        ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                        ## VARIABLES account AND amount DEFINED ABOVE AND 
                        deposit_output= make_deposit(account, amount)
                        print(f"You have made a deposit of ${amount} to account {account}")

            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
                # Invalid selection:
                print(e)

if __name__ == "__main__":
    chatbot()