"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
from unittest.mock import patch


ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:




## GIVEN CHATBOT FUNCTION
#01
def get_account() -> int:
    
    while True:
        try:
            account_number = int(input("Please enter your account number: "))
            if account_number in ACCOUNTS:
                return account_number
            else:
                raise Exception("Account number entered does not exist.")
        except ValueError:
            raise ValueError("Account number must be a whole number.")
    
#02

def get_balance(account : int) -> int :
    
    if account in ACCOUNTS:
        
        balance = ACCOUNTS[account]['balance']
        return f"your current balance for account {account} is $ {balance}" 
        #print("your current balance for account", account , "is" ,net_balance )
        
    else :
        raise Exception ("Account number does not exist.")
    
def get_balance(account : int) -> int :
    
    """
    Retrieve the balance of a specified account.

    Args:
        account : The account number for which to get the balance.

    Returns:
        str: A message with account number and its balance.

    Raises:
        Exception: If the account number is not  in the ACCOUNTS dictionary.
    """
    
    if account in ACCOUNTS:
        
        balance = ACCOUNTS[account]['balance']
        return f"your current balance for account {account} is $ {balance}" 
        #print("your current balance for account", account , "is" ,net_balance )
        
    else :
        raise Exception ("Account number does not exist.")
        
    
#print(get_balance(789012))

#3
def make_deposit(account : int , amount : float ) -> str :
    
    
    """
    updates balance with deposit from user
    
    arg : 
        account : checks the account number
        amount: transaction amount to be added in balance
        
    Returns:
        str: a message with deposite amount and corresponding account number
        
    Raises:
        Exception : if account number does not exist
        Valueerror : if account number entered is less than 0
    """
    
    if account  not in ACCOUNTS :
        
        raise Exception("Account number does not exist.")
    
    elif amount < 0  :
        raise ValueError ("Invalid Amount. Amount must be positive.")
    
    else:
        balance = ACCOUNTS[account]['balance']
        #new_balance = balance + amount
        ACCOUNTS[account]["balance"] += amount# updating dict
        print(ACCOUNTS)
        #print(new_balance)
    
    return  f"You have made a deposite of ${amount} to account {account} ."
        
        
print(ACCOUNTS)
print(make_deposit(789012,0))

## REQUIRES REVISION


"""
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
            ## selection:


            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:


                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""