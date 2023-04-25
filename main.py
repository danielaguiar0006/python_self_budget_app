import os
import json


DATA_FOLDER_DIRECTORY = "../../Documents/Self_Budgeter/data"

FINANCE_DATA_FILE = DATA_FOLDER_DIRECTORY + "/finance_data.json"
MONTHLY_INCOME_FILE = DATA_FOLDER_DIRECTORY + "/monthly_income.json"
MONTHLY_EXPENSES_FILE = DATA_FOLDER_DIRECTORY + "/monthly_expenses.json"


def main():
    check_for_data()
    main_menu()
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
    else:
        print(
            "Data folder does not exist, creating Data folder in User's Documents folder..."
        )
        os.makedirs(DATA_FOLDER_DIRECTORY)


if __name__ == "__main__":
    main()
