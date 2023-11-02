"""
Description: we are going to  practice your knowledge of Python functions by creating a chatbot that assists customers with banking tasks
Author:Krushang Bhatt
Date:30/10/2023
Usage:assists customers with banking tasks.
"""
import unittest
from unittest.mock import patch
import sys

sys.path.insert(1, "/../assignnment_05/sdf_assignment_5/src")
from src.chatbot import get_account , get_balance , make_deposit 
from src.chatbot import VALID_TASKS , ACCOUNTS


#test
class chatbottests_get_account(unittest.TestCase):
    
    def test_get_account_numeric(self):

 # arrange
        expected_output= 123456
        
        # act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]
        
        # assert
        self.assertEqual(expected_output,123456)

    def test_get_account_non_numeric(self):
        
        #arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"] 

        #act
        
            with self.assertRaises(ValueError) as context:
                get_account()
        
        #assert
        
            expected_error = "Account number must be a whole number."
            self.assertEqual(str(context.exception), expected_error)
            
        
    #Test
    
    def test_get_account_not_exist(self):
        
        # arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["112233"]
        
        #act
        
            with self.assertRaises(Exception) as context:
                get_account()
            
        #assert
            expected_error = "Account number entered does not exist."
            self.assertEqual(str(context.exception), expected_error)
            
 #2      
class chatbottests_get_balance(unittest.TestCase):
    #4
    def test_get_balance_correct_str_returned(self):
        
        #arrange
        input_value = 123456
        
        #act
        actual_output = get_balance(input_value)
        
        expected_output = "your current balance for account 123456 is $ 1000.0"
        #assert
        self.assertEqual(expected_output , actual_output)
    #5  
    def test_get_balance_exception_raised(self):
        
        #arrange
        input_value = 112233
        
        #act
        with self.assertRaises(Exception) as context:
            get_balance(input_value)

        expected_error_msg ="Account number does not exist."
        
        #assert
        self.assertEqual(str(context.exception), expected_error_msg)
    
#3

class chatbottests_make_deposit(unittest.TestCase):
    #6
    def test_make_deposite_balance_updated(self):
        
        #arrange
        account_number = 123456
        ammount_input = 1500
        
        #act
        ACCOUNTS[account_number]["balance"] = 1000.0
        expected_output = ammount_input + 1000
        
        actual_output = make_deposit(123456,1500.0)
        
        #assert
        self.assertEqual( ACCOUNTS[account_number]["balance"], expected_output)
    #7  
    def test_make_deposite_str_returned(self):
        
        #arrange  
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.
        input_amount=1000
        
        #act
        expected_output = "You have made a deposite of $1000 to account 123456 ."
        actual_output = make_deposit(account_number,input_amount)
        
        #assert
        self.assertEqual(expected_output , actual_output)
    
    #8
    def test_make_deposite_exception_error(self):
      
        #arrange
        input_value = 112233
        input_amount= 1500
        
        #act
        with self.assertRaises(Exception) as context:
            make_deposit(input_value , input_amount)

        expected_error_msg ="Account number does not exist."
        
        #assert
        self.assertEqual(str(context.exception), expected_error_msg)
        
    #9
    def test_make_deposite_value_error(self):
      
        #arrange
        input_value = 123456
        input_amount= -50
        
        #act
        with self.assertRaises(ValueError) as context:
            make_deposit(input_value , input_amount)

        expected_error_msg ="Invalid Amount. Amount must be positive."
        
        #assert
        self.assertEqual(str(context.exception), expected_error_msg)           
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    



