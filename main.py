"""Contains the main function and the user interface (menus, display functions)."""

import os
from data_handler import (
    read_data,
    write_data,
    check_if_data_exist,
    create_data_files,
    ENCRYPTION_KEY_FILE,
    DATA_FOLDER_DIRECTORY,
)
from finance import initialize_variables_data


finance_data = None


def main():
    # * Setup
    setup()

    # * Main loop
    main_menu()

    # * Cleanup
    # print("\nThank you for using Self Budgeter! :)\n")

    #! TESTING
    # print(monthly_income)
    # print(total_balance)
    # print(decrypted_finance_data_json)


def main_menu():
    print(
        """\nWelcome to Self Budgeter\nPlease select an option:
    1. Summary
    2. Add Income
    3. Add Expense
    4. Exit"""
    )

    user_input = input("Option: ")
    if user_input == "1":
        display_summary()
    elif user_input == "2":
        display_add_income_menu()
    elif user_input == "3":
        display_add_expense_menu()
    elif user_input == "4":
        print("Exit")
        return
    else:
        print("Invalid input, please try again.")
        main_menu()


def display_summary():  #! TODO: finish display_summary function
    print("\nSummary")
    print("Total Balance: " + str(finance_data.total_balance))
    print(
        "Monthly Income: " + str(finance_data.add_totals(finance_data.monthly_income))
    )


def display_add_income_menu():  #! TODO: finish display_add_income_menu function
    print("Add Income")


def display_add_expense_menu():  #! TODO: finish display_add_expense_menu function
    print("Add Expense")


def add_income():  #! TODO: finish add_income function
    print("Add Income")


def setup():
    print("\nChecking for data folder...")
    if check_if_data_exist():
        print("Data folder exists")
        global finance_data
        finance_data = initialize_variables_data()
    else:
        print("Data folder does not exist...")
        print("Creating data files in documents folder...")
        create_data_files()
        finance_data = initialize_variables_data()


if __name__ == "__main__":
    main()
