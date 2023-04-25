def main():
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


if __name__ == "__main__":
    main()
