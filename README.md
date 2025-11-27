# Personal Financial Tracker

Goal: Solves the problem of tracking personal expenses and income, helping users manage their budgets.

Description: User run the program. Program ask the date of transaction in particular formate and user input the date in such formate. In case user used other formate, the program asks user to input the date again in right formate. After the user wrote a date and push enter, pprogram asks user to input amount or empty string to start over. After User wrote an amount and push enter, program will write the date and the amount to the txt file and show an actual balance. 

## Installation

In your virtual environment install requierment dependecies using the following command 

`pip install -r requirements.txt`

### Running tests 

Tests can be ran with the following command 

`pytest test_main.py`

There are two tests in the `pytest test_main.py` file, for the one of the tests, which name `test_get_balance`, file test_database.txt downloading needed.