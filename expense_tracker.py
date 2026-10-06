# Expense Tracker
# Python Project

expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Travel", "amount": 500},
    {"category": "Shopping", "amount": 800},
    {"category": "Food", "amount": 300},
    {"category": "Bills", "amount": 1000}
]


def display_expenses(expenses):
    print("Expenses:")
    for expense in expenses:
        print(expense["category"], "-", expense["amount"])


def calculate_summary(expenses):
    amounts = [expense["amount"] for expense in expenses]

    total = sum(amounts)
    highest = max(amounts)
    average = total / len(amounts)

    print("\nExpense Summary")
    print("Total Expense:", total)
    print("Highest Expense:", highest)
    print("Average Expense:", average)


display_expenses(expenses)
calculate_summary(expenses)
