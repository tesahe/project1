from typing import List

class Expense:
    def __init__(self, name, category, price) -> None:
        self.name = name
        self.category = category
        self.price = float(price)

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.price:.2f}>"

def user_input():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        selected = int(input("Enter category number 1-5:")) - 1
        if selected in range(len(expense_categories)):
            selected_category = expense_categories[selected]
            new_expense = Expense(name=expense_name, category=selected_category, price=expense_amount)
            return new_expense
        else:
            print("Invalid input, please try again!")

def write_csv(expense: Expense, expense_file_path):
    print(f"Saving expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.price}\n")

def read_csv(expense_file_path, budget):
    print("Summarizing budget.")
    expenses: List[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, selected_category, expense_amount = line.strip().split(",")
            expenses.append(Expense(name=expense_name, category=selected_category, price=float(expense_amount)))

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.price

    print("Expenses by category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}:   ${amount:.2f}")

    total_spent = sum(expense.price for expense in expenses)
    print(f"Total spent this month: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")

def add_budget(budget, amount):
    """Increase the budget."""
    budget += amount
    print(f"Added ${amount:.2f} to budget. New budget: ${budget:.2f}")
    return budget

def remove_budget(budget, amount):
    """Decrease the budget."""
    if amount > budget:
        print("Cannot remove more than the current budget.")
        return budget
    budget -= amount
    print(f"Removed ${amount:.2f} from budget. New budget: ${budget:.2f}")
    return budget

def clear_all_entries(expense_file_path):
    """Clear all entries from the expenses file."""
    with open(expense_file_path, "w") as f:
        pass
    print("Cleared all expense entries.")

def main():
    print("Hello")
    expense_file_path = "expenses.csv"
    budget = 2000

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Add Budget")
        print("4. Remove Budget")
        print("5. Clear All Entries")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            expense = user_input()
            write_csv(expense, expense_file_path)
        elif choice == "2":
            read_csv(expense_file_path, budget)
        elif choice == "3":
            amount = float(input("Enter amount to add to budget: "))
            budget = add_budget(budget, amount)
        elif choice == "4":
            amount = float(input("Enter amount to remove from budget: "))
            budget = remove_budget(budget, amount)
        elif choice == "5":
            clear_all_entries(expense_file_path)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
