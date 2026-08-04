available_book = [
    ["978-0061120084", "To Kill a Mockingbird", 9.99, 4.8],
    ["978-0307277671", "The Road", 14.50, 4.2],
    ["978-0743273565", "The Great Gatsby", 10.99, 4.4],
    ["978-0451524935", "1984", 8.99, 4.7],
    ["978-0385472579", "Zen and the Art of Motorcycle Maintenance", 15.00, 4.1],
    ["978-0553386790", "Thinking, Fast and Slow", 16.99, 4.6]]

borrowed_book = [["978-0140449136", "The Odyssey", 12.99, 4.5],
    ["978-0141439600", "Pride and Prejudice", 11.50, 4.6],
    ["978-0374533557", "Sapiens: A Brief History of Humankind", 18.99, 4.7],
    ["978-0307387899", "The Kite Runner", 13.99, 4.5]]

class Library:
    def available_book(self, ISBN):
        for i ,row in enumerate(available_book) :
            if ISBN in row:
                print("The book is available")
                break
        else:
            print("Sorry the book is currently unavilable!")

    def borrow_book(self, ISBN):
        for i , row in enumerate(available_book):
            if ISBN in row:
                mov_row = available_book.pop(i)
                borrowed_book.append(mov_row)
                print(f"Book with this ISBN: {ISBN} is currently available!")
                break
        else:
            print(f"Book with this ISBN: {ISBN} is currently unavailable!")

    def borrowed_book(self, ISBN):
        for i , row in enumerate(borrowed_book):
            if ISBN in row:
                print("The book is borrowed")
                break
        else:
            print("The book is currently avilable!")

    def return_book(self, ISBN):
        for i , row in enumerate(borrowed_book):
            if ISBN in row:
                mov_row = borrowed_book.pop(i)
                available_book.append(mov_row)
                print("Thanks for returning the book!")
                break
        else:
            print(f"Book with this ISBN: {ISBN} is not ours, but hey you can always donate!")

    
    def donate_book(self , ISBN, title, price, rating):
        try:
            price = float(price)
            rating = float(rating)
        except ValueError:
            print("Price and rating must be numbers!")
            return

        if "" in (ISBN, title, price, rating):
            print("Please fill all the data.")
        elif price <= 0:
            print("Price cannot be negative or 0")
        elif rating < 0:
            print("Rating cannot be negative!")
        else:
            donated_book =[ISBN , title, price, rating]
            available_book.append(donated_book)
            print("Thank you for donating the book!")

    def exit(self):
        print("Thank you for using Library Management System!")


user_db ={"Ayush" : "12345"}

username = input("Enter your username : ")
password = input("Enter your password : ")
print()

u1 = Library()

if username in user_db and user_db[username] == password:

    while True:

        print("\nWelcome to the Library Management System:\n")

        print("1. Available Books")
        print("2. Borrow Book")
        print("3. Borrowed Books")
        print("4. Return Book")
        print("5. Donate Book")
        print("6. Exit \n")
    
        option = int(input("Enter your option : "))

        if option == 1:
            ISBN = input("Enter the books ISBN: ")
            u1.available_book(ISBN)

        elif option == 2:
            ISBN = input("Enter the books ISBN: ")
            u1.borrow_book(ISBN)

        elif option == 3:
            ISBN = input("Enter the books ISBN: ")
            u1.borrowed_book(ISBN)

        elif option == 4:
            ISBN = input("Enter the books ISBN: ")
            u1.return_book(ISBN)

        elif option == 5:
            ISBN = input("Enter the books ISBN: ")
            title = input("Enter the books Title: ")
            price = input("Enter the books Price: ")
            rating = input("Enter the books Rating: ")

            u1.donate_book(ISBN, title, price, rating)

        elif option == 6:
            u1.exit()
            break

else:
    print("Invalid username or password!")