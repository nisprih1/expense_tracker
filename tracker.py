import csv
from datetime import datetime

def add_expense():
    date = datetime.now.strftime('%Y-%m-%d')    
    category = input("add category (Example- Food, Travel, Bills): ")
    description = input("write description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter in nnumeric value.")
        return

    with open("expenses.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("data added successfully!")

if _name_ == "_main_":
    print("Daily Expense Tracker")
    add_expense()
