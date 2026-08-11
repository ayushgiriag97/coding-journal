import datetime
import getpass

class BankAccount:
    def __init__(self, username, password, balance=0.0, interest_rate=0.05):
        self._username = username
        self._password = password
        self._balance = balance
        self._interest_rate = interest_rate  # default 5% annual
        self._last_interest_date = datetime.date.today()
        self._transactions = []  # track history

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposited ${amount:.2f}")
            print(f"✅ Deposit successful! New Balance: ${self._balance:.2f}")
        else:
            print("❌ Error: Deposit amount must be greater than 0!")

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrew ${amount:.2f}")
            print(f"✅ Withdrawal successful! Remaining Balance: ${self._balance:.2f}")
        else:
            print("❌ Error: Insufficient funds or invalid amount!")

    def authenticate(self, password: str) -> bool:
        return self._password == password

    def preview_monthly_interest(self):
        monthly_rate = self._interest_rate / 12
        monthly_interest = self._balance * monthly_rate
        print(f"Current Interest Rate: {self._interest_rate*100:.1f}% annually")
        print(f"Monthly Interest Rate: {monthly_rate*100:.2f}%")
        print(f"💰 You will earn: ${monthly_interest:.2f} at the end of this month")

    def auto_apply_interest(self):
        today = datetime.date.today()
        days_passed = (today - self._last_interest_date).days

        if days_passed >= 30:
            months_passed = days_passed // 30  # handle multiple months
            monthly_rate = self._interest_rate / 12
            for _ in range(months_passed):
                monthly_interest = self._balance * monthly_rate
                self._balance += monthly_interest
                self._transactions.append(f"Interest added: ${monthly_interest:.2f}")
            self._last_interest_date = today
            print(f"💹 Interest for {months_passed} month(s) applied!")
            print(f"✅ New Balance: ${self._balance:.2f}")
        else:
            print(f"⏳ Interest not yet due. {30 - days_passed} days remaining.")

    def show_transactions(self):
        print("\nTransaction History:")
        if not self._transactions:
            print("No transactions yet.")
        else:
            for t in self._transactions:
                print(f"- {t}")


# --- Database ---
accounts = {
    "Ayush": BankAccount("Ayush", "1234567", balance=500.0)
}

# --- Main Program Flow ---
username = input("Enter your username: ")
password = getpass.getpass("Enter your password (hidden): ")

if username in accounts and accounts[username].authenticate(password):
    print("\n🎉 Login successful!")
    user = accounts[username]

    menu = {
        "1": lambda: print(f"💰 Current Balance: ${user.balance:.2f}"),
        "2": lambda: safe_input(user.deposit, "Enter deposit amount: "),
        "3": lambda: safe_input(user.withdraw, "Enter withdrawal amount: "),
        "4": user.preview_monthly_interest,
        "5": user.auto_apply_interest,
        "6": user.show_transactions,
        "7": lambda: print("👋 Thank you for banking with us!")
    }

    def safe_input(func, prompt):
        try:
            amt = float(input(prompt))
            func(amt)
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    while True:
        print("\n--- BANK MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Preview Monthly Interest")
        print("5. Apply Monthly Interest (Auto after 30 days)")
        print("6. View Transaction History")
        print("7. Exit")

        option = input("\nEnter option (1-7): ")

        if option in menu:
            menu[option]()
            if option == "7":
                break
        else:
            print("❌ Invalid option, try again!")

else:
    print("\n❌ Invalid username or password!")
