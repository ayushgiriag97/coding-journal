# 🏦 Smart Bank Account System

A secure, terminal-based banking application built in Python that demonstrates core Object-Oriented Programming (OOP) concepts, data protection through encapsulation, and interactive session management.

---

## 🚀 Key Features & Architecture

### 1. Encapsulation & Data Protection
* **Protected Attributes (`_balance`, `_username`, `_password`):** Prevents uncontrolled modification of critical state.
* **Property Decorators:** Enforces validation (e.g., blocking negative balances) with clean syntax.

### 2. Financial Operations
* **Validated Deposits & Withdrawals:** Ensures only positive deposits and prevents overdrafts.
* **Interest System:** Preview monthly earnings and auto-apply interest every 30 days (handles multiple months if overdue).
* **Transaction History:** Logs deposits, withdrawals, and interest applications.
* **Safe Input Validation:** Prevents crashes on invalid numeric input.

### 3. Authentication & Session Management
* **Credential Verification:** Dictionary lookup for constant-time validation.
* **Password Security:** Hidden input via `getpass`.
* **Persistent Session Loop:** Keeps user logged in for continuous operations.

---

## 📜 Example Menu
--- BANK MENU ---

1. Check Balance  
2. Deposit  
3. Withdraw  
4. Preview Monthly Interest  
5. Apply Monthly Interest (Auto after 30 days)  
6. View Transaction History  
7. Exit

