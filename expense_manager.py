import json
from expense import Expense


class ExpenseManager:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

                for item in data:
                    expense = Expense(
                        item["amount"],
                        item["category"],
                        item["description"],
                        item["date"]
                    )
                    self.expenses.append(expense)

        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self):
        data = [expense.to_dict() for expense in self.expenses]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_expense(self):
        try:
            amount = float(input("Enter amount: ₹"))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")

            expense = Expense(
                amount,
                category,
                description,
                date
            )

            self.expenses.append(expense)
            self.save_expenses()

            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount entered.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\n===== ALL EXPENSES =====")

        for index, expense in enumerate(self.expenses, start=1):
            print(
                f"{index}. ₹{expense.amount} | "
                f"{expense.category} | "
                f"{expense.description} | "
                f"{expense.date}"
            )

    def search_expense(self):
        keyword = input("Enter category to search: ").lower()

        found = False

        for expense in self.expenses:
            if expense.category.lower() == keyword:
                print(
                    f"₹{expense.amount} | "
                    f"{expense.category} | "
                    f"{expense.description} | "
                    f"{expense.date}"
                )
                found = True

        if not found:
            print("No matching expenses found.")

    def delete_expense(self):
        self.view_expenses()

        if not self.expenses:
            return

        try:
            choice = int(input("Enter expense number to delete: "))

            if 1 <= choice <= len(self.expenses):
                deleted = self.expenses.pop(choice - 1)
                self.save_expenses()

                print(f"Deleted expense: {deleted.description}")

            else:
                print("Invalid choice.")

        except ValueError:
            print("Enter a valid number.")

    def monthly_summary(self):
        summary = {}

        for expense in self.expenses:
            category = expense.category

            summary[category] = summary.get(category, 0) + expense.amount

        print("\n===== MONTHLY SUMMARY =====")

        for category, total in summary.items():
            print(f"{category}: ₹{total:.2f}")