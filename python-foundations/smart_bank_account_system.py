# 1. Define your Class at the top (Global Scope)
class BankAccount:
    def __init__(self, username, password, balance=0.0):
        self._username = username
        self._password = password
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter    
    def balance(self, new_balance: float):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Error: Balance must be greater than or equal to 0")

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Deposit successful! New Balance: {self._balance}")
        else:
            print("Error: Amount to deposit must be greater than 0!")

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal successful! Remaining Balance: {self._balance}")
        else:
            print("Error: Insufficient funds or invalid amount!")


# 2. Database/Authentication System
authentication = {"Ayush": "1234567"}

# 3. Main Program Flow
username = input("Enter your username : ")
password = input("Enter your password : ")

# Check authentication
if username in authentication and authentication[username] == password:
    print("\nLogin successful!")
    
    # Create the object ONCE when logged in
    user1 = BankAccount(username, password, balance=500.0)

    # Keep the session open until the user chooses to exit
    while True:
        print("\n--- BANK MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        option = input("\nEnter option (1-4): ")

        if option == "1":
            print(f"Current Balance: ${user1.balance}") 
        elif option == "2":
            amt = float(input("Enter deposit amount: "))
            user1.deposit(amt)                        
        elif option == "3":
            amt = float(input("Enter withdrawal amount: "))
            user1.withdraw(amt)                       
        elif option == "4":
            print("Thank you for banking with us!")
            break                                     
        else:
            print("Invalid option, try again!")
else:
    print("\nInvalid username or password!")