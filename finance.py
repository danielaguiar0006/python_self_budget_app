"""Contains functions and classes related to finance data manipulation and calculations."""

from data_handler import (
    read_data,
    DATA_FOLDER_DIRECTORY,
    ENCRYPTION_KEY_FILE,
    FINANCE_DATA_FILE,
)
from finance_data import FinanceData


encryption_key = None
decrypted_finance_data_json = None

total_balance = 0.00
monthly_income = []
monthly_expenses = []
savings = []


# Initialize global variables
def initialize_variables_data():
    finance_data = FinanceData()

    # Using encryption_key.key file on user's pc to get encryption key
    with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
        encryption_key = key_file.read()

    # Using encryption key to decrypt decrypted_finance_data.json file
    decrypted_finance_data_json = read_data(FINANCE_DATA_FILE, encryption_key)
    finance_data.update(decrypted_finance_data_json)

    return finance_data
