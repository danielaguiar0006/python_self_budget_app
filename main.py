import os
import json
from encryption_util import generate_key, encrypt_data, decrypt_data


DATA_FOLDER_DIRECTORY = "../../Documents/Self_Budgeter/data"
FINANCE_DATA_FILE = DATA_FOLDER_DIRECTORY + "/finance_data.json"
ENCRYPTION_KEY_FILE = DATA_FOLDER_DIRECTORY + "/key.key"

encryption_key = None


def main():
    # Setup
    check_for_data()

    # Main loop
    main_menu()

    # Cleanup
    print("\nThank you for using Self Budgeter! :)\n")


def main_menu():
    print(
        """\nWelcome to Self Budgeter
    Please select an option:
    1. Summary
    2. Add Income
    3. Add Expense
    4. Exit"""
    )

    user_input = input("Option: ")
    if user_input == "1":
        display_summary()
    elif user_input == "2":
        add_income_menu()
    elif user_input == "3":
        add_expense_menu()
    elif user_input == "4":
        print("Exit")
        return
    else:
        print("Invalid input, please try again.")
        main_menu()


def display_summary():
    print("Summary")


def add_income_menu():
    print("Add Income")


def add_expense_menu():
    print("Add Expense")


# Checking for data folder on user's computer
def check_for_data():
    print("\nChecking for data folder...")

    if os.path.exists(DATA_FOLDER_DIRECTORY):
        print("Data folder exists")

        with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
            encryption_key = key_file.read()
    else:
        print("Data folder does not exist...")
        create_data_files()


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


def create_data_files():
    finance_data_template = {
        "total_balance": 0,
        "monthly_income": {
            "salary": 0,
            "rental_income": 0,
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

    print("Creating data files in documents folder...")
    os.makedirs(DATA_FOLDER_DIRECTORY)

    # Use a key from a file or generate and store it in a file (DO NOT hardcode the key in your code)
    encryption_key = generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(encryption_key)

    write_data(FINANCE_DATA_FILE, finance_data_template, encryption_key)


if __name__ == "__main__":
    main()
