import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "attendance_log.txt")

def initialize_tracker():
    with open(LOG_FILE, 'w') as f:  
        f.write("--- Course Attendance Log --- \n")

def mark_attendance(students):
    with open(LOG_FILE, 'a') as f:  
        for index, (name, status) in enumerate(students):
            f.write(f"{index + 1}. {name} - {status} \n")

def view_attendance_history():
    with open(LOG_FILE, 'r') as f:  
        print(f.read())

if __name__ == "__main__":
    initialize_tracker()

    print("Logging attendance data...")
    students = [
        ("Aarav Sharma", "Present"),
        ("Priya Koirala", "Absent"),
        ("Rohan Thapa", "Present"),
        ("Sneha Adhikari", "Late"),
        ("Manish Gurung", "Present"),
        ("Kritika Shrestha", "Absent"),
        ("Sajan Lama", "Present"),
        ("Nisha Rai", "Present"),
        ("Dipesh KC", "Late"),
        ("Alisha Tamang", "Present")
    ]
    mark_attendance(students)

    print("\nPrinting history from file: \n")
    view_attendance_history()

