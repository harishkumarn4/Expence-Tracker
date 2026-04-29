import json

expenses=[]

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_data()
    print("Expense added!")

def save_data():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def load_data():
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except:
        expenses = []

load_data()

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\nYour Expenses:")
    print("-" * 30)

    for exp in expenses:
        print(f"{exp['category']} - ₹{exp['amount']} - {exp['date']}")

def total_expense():
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for exp in expenses:
        total += exp["amount"]

    print(f"\nTotal spent: ₹{total}")


def monthly_summary():
    if not expenses:
        print("No expenses found.")
        return

    monthly_data = {}

    for exp in expenses:
        # extract year-month from date
        month = exp["date"][:7]   # "2026-04"

        if month in monthly_data:
            monthly_data[month] += exp["amount"]
        else:
            monthly_data[month] = exp["amount"]

    print("\nMonthly Spending:")
    print("-" * 30)

    for month, total in monthly_data.items():
        print(f"{month} : ₹{total}")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Monthly Spending")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        monthly_summary()
    elif choice == "5":
        break
    else:
        print("Invalid choice")