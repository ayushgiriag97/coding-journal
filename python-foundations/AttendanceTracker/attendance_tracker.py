import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "attendance_log.txt")

VALID_STATUSES = {"Present", "Absent", "Late"}

def initialize_tracker():
    """Initialize the attendance log file safely."""
    try:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            f.write("--- Course Attendance Log ---\n")
        print("Attendance tracker initialized.")
    except OSError as e:
        print(f"Error initializing log file: {e}")

def validate_student_entry(name, status):
    """Validate student name and attendance status."""
    if not isinstance(name, str) or not name.strip():
        print("❌ Invalid name. Please enter a non-empty string.")
        return False
    if status not in VALID_STATUSES:
        print(f"❌ Invalid status '{status}'. Must be one of {VALID_STATUSES}.")
        return False
    return True

def mark_attendance():
    """Prompt user to enter student attendance interactively."""
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            while True:
                name = input("Enter student name (or 'q' to quit): ").strip()
                if name.lower() == 'q':
                    break
                status = input("Enter status (Present/Absent/Late): ").strip().capitalize()
                if validate_student_entry(name, status):
                    # Count current lines to keep numbering consistent
                    line_count = sum(1 for _ in open(LOG_FILE, 'r', encoding='utf-8')) - 1
                    f.write(f"{line_count + 1}. {name} - {status}\n")
                    print(f"✅ Recorded: {name} - {status}")
    except OSError as e:
        print(f"Error writing to log file: {e}")

def view_attendance_history():
    """Read and display attendance history with error handling."""
    try:
        if not os.path.exists(LOG_FILE):
            print("⚠️ No attendance log found. Please initialize first.")
            return
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                print("\n--- Attendance History ---")
                print(content)
            else:
                print("⚠️ Attendance log is empty.")
    except OSError as e:
        print(f"Error reading log file: {e}")

def menu():
    """Menu-driven CLI for attendance tracker."""
    while True:
        print("\n📋 Attendance Tracker Menu")
        print("1. Initialize tracker")
        print("2. Mark attendance")
        print("3. View attendance history")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            initialize_tracker()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance_history()
        elif choice == "4":
            print("👋 Exiting Attendance Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
