import os
import datetime

# Dynamic Path Setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SPENDING_DATA = os.path.join(SCRIPT_DIR, "spending_data.csv")


date_in = input("Enter a date (YYYY-MM-DD): ")
description_in = input("Enter a Description: ")
category_in = input("Enter a Category: ")
amount_in = input("Enter a Amount: ")

def add_expenses(data,description,category,amount):
    with open (SPENDING_DATA, "a", encoding="utf-8") as file:
        file.write(f"{data},{description},{category},{amount}\n")
        print("Data is saved")

def view_expenses():
    print(f"{'Date':<12}{'Description':<15}{'Category':<15}{'Amount':<10}")
    print("-" * 55) 
    with open(SPENDING_DATA, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = [p.strip() for p in line.split(",")]
                date_out, description_out, category_out, amount_out = parts
                print(f"{date_out:<12}{description_out:<15}{category_out:<15}Rs.{amount_out:<10}")

def filter_spending():
    pass

def analyse_spending():
    pass

def category_analysis():
    pass


add_expenses(date_in,description_in,category_in,amount_in)
view_expenses()
