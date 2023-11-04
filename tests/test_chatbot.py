"""
Description:Contains test functions and cases to ensures if the function and components are correct.
Author:Tamanna Singh
Date:2023-10-30
Usage:Used to write and run the tests for the functions.
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account
from src.chatbot import VALID_TASKS, ACCOUNTS
from src.chatbot import get_amount
from src.chatbot import get_account, get_amount, get_balance
from src.chatbot import get_account, get_amount, get_balance, make_deposit
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection

class ChatbotTests(unittest.TestCase):
    def test_get_acc_valid_number(self):
        with patch("builtins.input") as mock_input:
            # Arrange
            mock_input.side_effect = ["123456"]
            expected = 123456

            #Act
            actual = get_account()

            #Assert
            self.assertEqual(expected,actual)

    def test_get_account_non_numeric_data(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["non_numeric_data"]
            expected = "Account number must be a whole number."
            
            #Act
            with self.assertRaises(Exception) as context:
                get_account()
            
            #Assert
            self.assertEqual(str(context.exception), expected)
        
    def test_get_account_not_exist(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["112233"]
            expected = "Account number entered does not exist."

            #Act
            with self.assertRaises(Exception) as context:
                get_account()

            #Assert
            self.assertEqual(str(context.exception), expected)

    def test_get_amount_valid_amt(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["500.01"]
            expected = 500.01

            #Act
            result = get_amount()

            #Assert
            self.assertEqual(expected, result)

    def test_get_amount_non_numeric_value(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["non_numeric_data"]
            expected = "Invalid amount. Amount must be numeric."

            #Act
            with self.assertRaises(ValueError) as context:
                get_amount()

            #Assert
            self.assertEqual(str(context.exception), expected)

    def test_get_amount_zero_or_negative_amt(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["0"] 
            expected = "Invalid amount. Please enter a positive number."

            #Act
            with self.assertRaises(ValueError) as context:
                get_amount()

            #Assert
            self.assertEqual(str(context.exception), expected)

    def test_get_balance_value_is_correct(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["123456"]
            expected = 1000

            #Assert
            expected_message = f"Your current balance for account {mock_input.side_effect} is ${expected:.2f}"

    def test_get_balance_account_does_not_exist(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            account = ["112233"]
            expected = "Account number does not exist."

            #Act
            with self.assertRaises(Exception) as context:
                get_balance(mock_input.side_effect)

            #Assert
            self.assertEqual(str(context.exception), expected)

    def test_make_deposit_balance_is_correctly_updated(self):

            #Arrange
            account = ["123456"]
            balance = 1000
            amount = 1500.01
            expected = 2500.01

            #Act
            with self.assertRaises(Exception) as context:
                result = make_deposit()
            
            #Assert
            expected_balance = balance + amount
            self.assertEqual(expected , expected_balance)

    def test_make_deposit_correct_value_is_returned(self):
            
            #Arrange
            account = 123456
            amount = 1500.01

            #Act
            result = make_deposit(account, amount)

            #Assert
            expected = f"You have made a deposit of ${amount} to account {account}"
            self.assertEqual(result, expected)

    def test_make_deposit_account_does_not_exist(self):
        
            #Arrnage
            account = "112233"
            amount = "1500.01"
            expected = "Account number does not exist."

            #Act
            with self.assertRaises(Exception) as context:
                make_deposit(account, amount)

            #Assert
            self.assertEqual(str(context.exception), expected)

    def test_make_deposit_amount_is_less_than_zero(self):

            #Arrange
            account = 123456
            amount = -50.01
            
            #Act
            with self.assertRaises(ValueError) as context:
                make_deposit(account, amount)

            #Assert
            expected = "Invalid Amount. Amount must be positive."
            self.assertEqual(str(context.exception), expected)
    
    def test_user_selection_valid_lowecase_entered(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["balance"]
            expected = "balance"

            #Act
            actual_output = user_selection()

            #Assert
            self.assertEqual(expected, actual_output)

    def test_user_selection_valid_uppercase_entered(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["BALANCE"]
            expected = "balance"

            #Act
            actual_output = user_selection()

            #Assert
            self.assertEqual(actual_output, expected)

    def test_user_selection_invalid_selection_entered(self):
        with patch("builtins.input") as mock_input:

            #Arrange
            mock_input.side_effect = ["invalid_selection"]
            expected = "Invalid task. Please choose balance, deposit, or exit."

            #Act
            with self.assertRaises(ValueError) as context:
                user_selection()

            #Assert
            self.assertEqual(str(context.exception), expected)

            











        









