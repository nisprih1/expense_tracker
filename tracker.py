import csv
from datetime import datetime
import os


file_path = "expenses.csv"

if not os.path.exits(file_path):
    with open(file_path, 'w', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(["date","category","description","amount"])

def get_expense():
    date = datetime.now().strftime('%Y-%m-%d')    
    category = input("add category (Example- Food, Travel, Bills): ")
    description = input("write description: ")
    amount = float(input("Enter amount: "))
    return [date,category,description,amount]


def add_expense():
    with open("expenses.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("data added successfully!")


def main():
    create_csv_if_not_exists(FILE_PATH)
    expense = get_expense_input()
    add_expense_to_csv(FILE_PATH, expense)

if _name_ == "_main_":
    main()
