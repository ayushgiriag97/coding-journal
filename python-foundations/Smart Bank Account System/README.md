# 🏦 Smart Bank Account System

A secure, terminal-based banking application built in Python that demonstrates core Object-Oriented Programming (OOP) concepts, data protection through encapsulation, and interactive session management.

---

## 🚀 Key Features & Architecture

### 1. Robust Encapsulation & Data Protection
* **Protected Internal Attributes (`_balance`, `_username`, `_password`):** Prevents direct, uncontrolled modification of critical financial state from outside the object boundary.
* **Property Decorators (`@property` & `@balance.setter`):** Implements managed getter and setter attributes to enforce real-time data validation (e.g., blocking negative balance assignments) without sacrificing clean attribute-access syntax.

### 2. Guarded Financial Operations
* **Validated Deposits:** Checks transaction inputs to ensure only positive monetary amounts increment the balance.
* **Overdraft Prevention:** Validates available funds during withdrawal attempts to ensure accounts cannot fall below `$0.00`.

### 3. Authentication & Session State Management
* **Credential Verification:** Uses dictionary lookup ($O(1)$ constant time complexity) to validate usernames and passwords before constructing account objects.
* **State Persistence via Session Loop:** Keeps the active user object persistent in memory within an interactive `while` loop, allowing continuous balance checks, deposits, and withdrawals without resetting state between actions.

---
