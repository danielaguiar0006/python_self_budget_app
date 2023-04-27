"""Contains functions related to handling data (reading, writing, encryption, decryption)."""

import os
import json
from encryption_util import generate_key, encrypt_data, decrypt_data


DATA_FOLDER_DIRECTORY = "../../Documents/Self_Budgeter/data"
FINANCE_DATA_FILE = os.path.join(DATA_FOLDER_DIRECTORY, "finance_data.json")
ENCRYPTION_KEY_FILE = os.path.join(DATA_FOLDER_DIRECTORY, "encryption_key.key")


# read_data and write_data functions securely through encryption
def read_data(file_path, key):
    if not os.path.exists(file_path):
        return {}

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = decrypt_data(key, encrypted_data)
    return json.loads(decrypted_data)


def write_data(file_path, data, key):
    encrypted_data = encrypt_data(key, json.dumps(data))

    with open(file_path, "wb") as file:
        file.write(encrypted_data)


# Check for data folder on user's computer
def check_if_data_exist():
    if os.path.exists(DATA_FOLDER_DIRECTORY):
        #! REMOVED: update_variables_data()
        return True
    else:
        #! REMOVED: create_data_files()
        return False


# Create default data files
def create_data_files():
    finance_data_template = {
        "total_balance": 3,
        "monthly_income": {
            "salary": 1,
            "rental_income": 2,
        },
        "monthly_expenses": {
            "rent": 0,
            "groceries": 0,
            "utilities": 0,
            "insurance": 0,
        },
        "savings": {
            "emergency_fund": 0,
            "retirement": 0,
        },
    }

    # Create data folder in documents folder
    os.makedirs(DATA_FOLDER_DIRECTORY)

    # Use a key from a file or generate and store it in a file (DO NOT hardcode the key in your code)
    encryption_key = generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(encryption_key)

    # Create finance_data.json file using newly generated encryption key
    write_data(FINANCE_DATA_FILE, finance_data_template, encryption_key)
