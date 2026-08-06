menu = [
    ["Dhal-Bhat", "120", "Khana", "Yes", "Yes"],
    ["Masala Chiya", "30", "Drink", "Yes", "Yes"],
    ["Dharane Kalo Bungur", "400", "Khana", "No", "Yes"],
    ["Sekuwa", "200", "Khana", "No", "Yes"],
    ["", "100", "Khana", "Yes", "Yes"],          # edge case: empty name
    ["Momo", "abc", "Khana", "Yes", "Yes"],      # edge case: invalid price
    ["Pizza", "250", "Khana", "Maybe", "Yes"],   # edge case: invalid veg flag
    ["Burger", "150", "Khana", "No", "No"]       # edge case: unavailable
]

def validate_item(item):
    """Validate menu item structure and values."""
    if not isinstance(item, list) or len(item) != 5:
        print(f"⚠️ Skipping malformed item: {item}")
        return False
    
    name, price, category, veg_flag, available_flag = item
    
    if not isinstance(name, str) or not name.strip():
        print(f"⚠️ Invalid name in item: {item}")
        return False
    
    try:
        price_val = int(price)
        if price_val < 0:
            print(f"⚠️ Negative price in item: {item}")
            return False
    except ValueError:
        print(f"⚠️ Invalid price in item: {item}")
        return False
    
    if veg_flag not in {"Yes", "No"}:
        print(f"⚠️ Invalid veg flag in item: {item}")
        return False
    
    if available_flag not in {"Yes", "No"}:
        print(f"⚠️ Invalid availability flag in item: {item}")
        return False
    
    return True

def display_menu():
    print("\n Full Menu:")
    for item in menu:
        if validate_item(item):
            print(item)

def display_veg_items():
    print("\n Veg Items Only:")
    for item in menu:
        if validate_item(item) and item[3] == "Yes":
            print(item)

def display_nonveg_items():
    print("\n Non-Veg Items (Price > 100 & Available):")
    for item in menu:
        if validate_item(item):
            price_val = int(item[1])
            if item[3] == "No" and price_val > 100 and item[4] == "Yes":
                print(item)

def search_item():
    query = input("🔍 Enter dish name to search: ").strip().lower()
    found = False
    for item in menu:
        if validate_item(item):
            name = item[0].lower()
            if query in name:
                found = True
                print("\n✅ Found Item:")
                print(f"Name: {item[0]}")
                print(f"Price: {item[1]}")
                print(f"Category: {item[2]}")
                print(f"Veg: {item[3]}")
                print(f"Available: {item[4]}")
    if not found:
        print(f"❌ No item found matching '{query}'.")

def menu_cli():
    while True:
        print("\n=== Menu Options ===")
        print("1. Show full menu")
        print("2. Show veg items")
        print("3. Show non-veg items (price > 100 & available)")
        print("4. Search item by name")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            display_menu()
        elif choice == "2":
            display_veg_items()
        elif choice == "3":
            display_nonveg_items()
        elif choice == "4":
            search_item()
        elif choice == "5":
            print(" Exiting menu viewer. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu_cli()
