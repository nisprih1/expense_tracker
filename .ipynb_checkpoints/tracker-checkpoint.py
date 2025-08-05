import csv
from datetime import datetime
import os

file_path = "expenses.csv"

# Function to create file if it doesn't exist
def create_csv_if_not_exists(path):
    if not os.path.exists(path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "description", "amount"])

# Function to get user input
def get_expense_input():
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Add category (Example - Food, Travel, Bills): ")
    description = input("Write description: ")
    amount = float(input("Enter amount: "))
    return [date, category, description, amount]

# Function to write to CSV
def add_expense_to_csv(path, expense):
    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)
    print("Data added successfully!")

# Main driver function
def main():
    create_csv_if_not_exists(file_path)
    expense = get_expense_input()
    add_expense_to_csv(file_path, expense)

# Run the script
if __name__ == "__main__":
    main()
