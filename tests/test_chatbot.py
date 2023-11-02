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
from src.chatbot import get_account , get_balance


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
        
            expected_error = "Account number must be a whole number. "
            self.assertEqual(str(context.exception), expected_error)
            
        
    #3
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
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    



