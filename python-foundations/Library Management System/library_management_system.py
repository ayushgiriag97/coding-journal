# 1. Imports / Dependencies
import os

# Dynamic Path Setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AVAILABLE_BOOK_FILE = os.path.join(SCRIPT_DIR, "available_book.txt")
BORROWED_BOOK_FILE = os.path.join(SCRIPT_DIR, "borrowed_book.txt")

user_db = {"Ayush": "12345"}


# 2. File I/O Helper Functions
def load_books(file_path):
    """Reads a text file and returns a list of book lists."""
    books = []
    if not os.path.exists(file_path):
        return books

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = [p.strip() for p in line.split("|")]
                # Parse types: [ISBN, Title, Price, Rating]
                if len(parts) == 4:
                    isbn, title, price, rating = parts
                    books.append([isbn, title, float(price), float(rating)])
                elif len(parts) == 2:
                    isbn, title = parts
                    books.append([isbn, title])
    return books


def save_books(file_path, books_list):
    """Writes a list of book lists back to the specified text file."""
    with open(file_path, "w", encoding="utf-8") as file:
        for book in books_list:
            # Format row depending on whether rating/price exist
            if len(book) == 4:
                file.write(f"{book[0]} | {book[1]} | {book[2]} | {book[3]}\n")
            elif len(book) == 2:
                file.write(f"{book[0]} | {book[1]}\n")


# 3. Class Definitions (Blueprints)
class Library:

    def available_book(self):
        """Displays all available books from file and offers ISBN lookup."""
        available_books = load_books(AVAILABLE_BOOK_FILE)

        print("\n--- Currently Available Books ---")
        if not available_books:
            print("No books available at the moment.")
        else:
            for book in available_books:
                print(f"ISBN: {book[0]} | Title: {book[1]} | Price: ${book[2]} | Rating: {book[3]}")
        
        choice = input("\nWould you like to check a specific ISBN? (y/n): ").strip().lower()
        if choice == 'y':
            search_isbn = input("Enter the book's ISBN to search: ")
            for row in available_books:
                if search_isbn in row:
                    print(f"The book '{row[1]}' is available!")
                    break
            else:
                print("Sorry, the book is currently unavailable!")

    def manage_borrowing(self):
        """Displays borrowed books and manages borrowing moves between files."""
        borrowed_books = load_books(BORROWED_BOOK_FILE)
        available_books = load_books(AVAILABLE_BOOK_FILE)

        print("\n--- Borrowed Books Section ---")
        print("Currently Borrowed Books:")
        if not borrowed_books:
            print("No books are currently borrowed.")
        else:
            for book in borrowed_books:
                print(f"ISBN: {book[0]} | Title: {book[1]}")

        print("\nOptions:")
        print("1. Borrow an available book")
        print("2. Check if a specific book is already borrowed")
        print("3. Return to Main Menu")
        
        sub_choice = input("Select an option (1-3): ").strip()

        if sub_choice == "1":
            search_isbn = input("Enter the ISBN of the book you want to borrow: ")
            for i, row in enumerate(available_books):
                if search_isbn in row:
                    # Move from available list to borrowed list
                    mov_row = available_books.pop(i)
                    borrowed_books.append(mov_row)

                    # Save updated lists back to BOTH files
                    save_books(AVAILABLE_BOOK_FILE, available_books)
                    save_books(BORROWED_BOOK_FILE, borrowed_books)

                    print(f"Success! You borrowed '{mov_row[1]}' (ISBN: {search_isbn}).")
                    break
            else:
                print(f"Book with ISBN: {search_isbn} is currently unavailable for borrowing!")

        elif sub_choice == "2":
            search_isbn = input("Enter the ISBN to check status: ")
            for row in borrowed_books:
                if search_isbn in row:
                    print(f"The book '{row[1]}' is currently borrowed.")
                    break
            else:
                print("This book is NOT in the borrowed list.")

    def return_book(self, ISBN):
        """Returns a borrowed book back to the available file."""
        borrowed_books = load_books(BORROWED_BOOK_FILE)
        available_books = load_books(AVAILABLE_BOOK_FILE)

        for i, row in enumerate(borrowed_books):
            if ISBN in row:
                mov_row = borrowed_books.pop(i)
                available_books.append(mov_row)

                # Persist changes back to disk
                save_books(BORROWED_BOOK_FILE, borrowed_books)
                save_books(AVAILABLE_BOOK_FILE, available_books)

                print(f"Thanks for returning '{mov_row[1]}'! It is now available again.")
                break
        else:
            print(f"Book with ISBN: {ISBN} is not in our borrowed list, but you can donate it!")

    def donate_book(self, ISBN, title, price, rating):
        """Adds a new book to available_book.txt file."""
        try:
            price = float(price)
            rating = float(rating)
        except ValueError:
            print("Price and rating must be numbers!")
            return

        if "" in (ISBN, title):
            print("Please fill all required data fields.")
        elif price <= 0:
            print("Price cannot be negative or 0.")
        elif rating < 0:
            print("Rating cannot be negative!")
        else:
            available_books = load_books(AVAILABLE_BOOK_FILE)
            donated_book = [ISBN, title, price, rating]
            available_books.append(donated_book)

            # Save the newly appended list to file
            save_books(AVAILABLE_BOOK_FILE, available_books)

            print(f"Thank you for donating '{title}' to the library!")

    def exit(self):
        print("Thank you for using the Library Management System!")



# 4. Helper / Utility Functions
def authenticate_user():
    """Handles username and password input & verification."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print()
    if username in user_db and user_db[username] == password:
        return True
    return False


# 5. Main Execution Block (The Entry Point)
if authenticate_user():
    u1 = Library()

    while True:
        print("\n==============================")
        print(" Library Management System ")
        print("==============================")
        print("1. View / Search Available Books")
        print("2. Borrow & View Borrowed Books")
        print("3. Return a Book")
        print("4. Donate a Book")
        print("5. Exit\n")

        try:
            option = int(input("Enter your option (1-5): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if option == 1:
            u1.available_book()

        elif option == 2:
            u1.manage_borrowing()

        elif option == 3:
            ISBN = input("Enter the book's ISBN to return: ")
            u1.return_book(ISBN)

        elif option == 4:
            ISBN = input("Enter the book's ISBN: ")
            title = input("Enter the book's Title: ")
            price = input("Enter the book's Price: ")
            rating = input("Enter the book's Rating: ")
            u1.donate_book(ISBN, title, price, rating)

        elif option == 5:
            u1.exit()
            break
        else:
            print("Invalid choice! Please pick an option between 1 and 5.")
else:
    print("Invalid username or password!")
