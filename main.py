from expense_manager import ExpenseManager


def main():
    manager = ExpenseManager()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Monthly Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_expense()

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            manager.search_expense()

        elif choice == "4":
            manager.delete_expense()

        elif choice == "5":
            manager.monthly_summary()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()