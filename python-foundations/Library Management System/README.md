# 📚 Smart Library Management System

A secure, terminal-based library management application built in Python that demonstrates core Object-Oriented Programming (OOP) principles, structured file persistence, and interactive session management.

---

## 🚀 Key Features & Architecture

### 1. Persistent File I/O Storage
* **File-Backed State (`load_books` & `save_books`):** Replaces volatile in-memory storage with persistent `.txt` files (`available_book.txt` and `borrowed_book.txt`), ensuring library inventories remain intact across program restarts.
* **Dynamic Path Resolution (`os.path`):** Utilizes `SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))` to guarantee seamless relative path referencing regardless of the working directory from which the script is launched.

### 2. Guarded Data Operations & Input Validation
* **Data Parsing & Type Safety:** Reads formatted text lines (`ISBN | Title | Price | Rating`), stripping whitespace and casting numeric data to `float` types with explicit `try...except ValueError` blocks to prevent unexpected runtime crashes.
* **Inventory Constraints:** Enforces strict validation during donations (e.g., rejecting empty fields, negative/zero prices, and negative ratings) to maintain catalog integrity.

### 3. State-Transfer Transaction Logic
* **Cross-File Data Movement (`pop` & `append`):** Simulates real-world inventory changes by removing a record from one collection and appending it to another when borrowing or returning books, then persisting both changes to disk simultaneously.
* **Safe Search & Lookup:** Implements `for...else` constructs combined with `enumerate()` for efficient $O(N)$ string and ISBN pattern matching without relying on manual status flags.

### 4. Authentication & Interactive Session Management
* **Credential Verification:** Uses dictionary lookup ($O(1)$ constant time complexity) to authenticate users prior to instantiating the core application interface.
* **Interactive CLI Loop:** Keeps the active session alive within a `while True:` loop, offering structured main menus and nested sub-menus for intuitive user interaction until an explicit exit signal is given.

---
## 🔑 Default Login Credentials

Use the following credentials to access the system:

- **Username:** Ayush  
- **Password:** 12345
