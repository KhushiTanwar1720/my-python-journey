expenses = []
def add_expense():
    expense_name = input("Enter the expense name: ")
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    expense = {
        "name":expense_name,
        "amount":amount,
        "category":category
    }    
    expenses.append(expense)
def view_expenses():
    if not expenses:
        print("No expenses added yet.")
        return
    for expense in expenses:
        print("Name:",expense["name"])
        print("Amount:",expense["amount"])
        print("Category:",expense["category"])
        print("----------------------")
def total_expense():
    total = 0
    if not expenses:
        print("No expenses added yet.")
        return

    for expense in expenses:
        total = total + expense["amount"]
    print("Total Expense:",total)
    print("--------------------")

def category_total():
    category_totals ={}
    if not expenses:
        print("No expenses added yet.")
        return
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
            
    print("\nCategory-wise Total:")
    for category, total in category_totals.items():
        print(category, ":", total)
            
while True:
    print("\n Expense Tracker!")
    print("1. Add Expenses")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Category-wise Total")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_total()
    elif choice == "5":
        print("Thank You! ")
        break
    else:
        print("Invalid Choice!")