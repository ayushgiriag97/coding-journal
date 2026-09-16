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
    pass

def filter_spending():
    pass

def analyse_spending():
    pass

def category_analysis():
    pass


add_expenses(date_in,description_in,category_in,amount_in)
