expenses = []
def add_expenses():
    expenses_name = input("Enter the expense name: ")
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    expense = {
        "name":expenses_name,
        "amount":amount,
        "category":category
    }    
    expenses.append(expense)
def view_expenses():
    for expense in expenses:
        print("Name:",expense["name"])
        print("Amount:",expense["amount"])
        print("Category:",expense["category"])
        print("----------------------")
def total_expense():
    
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
        print("Total Expense:",total)
        print("--------------------")

while True:
    print("\n Expense Tracker!")
    print("1. Add Expenses")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank You! ")
        break
    else:
        print("Invalid Choice!")