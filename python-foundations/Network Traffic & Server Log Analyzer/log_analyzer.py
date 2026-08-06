import os

# Dynamic Path Setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_LOG_FILE = os.path.join(SCRIPT_DIR, "raw_server_logs.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "error_report.txt")

VALID_LEVELS = {"INFO", "WARNING", "ERROR"}

def create_raw_logs():
    """Generates the raw server log file for analysis."""
    logs = [
        "INFO - 10:01 - User login successful\n",
        "WARNING - 10:05 - High memory usage detected\n",
        "ERROR - 10:07 - Database connection failed\n",
        "INFO - 10:10 - User logout successful\n",
        "ERROR - 10:12 - API Gateway timeout exception\n",
        "INFO - 10:15 - Background worker completed\n",
        "INVALID - 10:20 - Bad log format\n"  # edge case: invalid level
    ]
    try:
        with open(RAW_LOG_FILE, 'w', encoding='utf-8') as f:
            f.writelines(logs)
        print("✅ Raw logs created successfully.")
    except OSError as e:
        print(f"❌ Error creating raw logs: {e}")

def parse_log_line(line):
    """Validate and parse a single log line."""
    parts = line.strip().split(" - ")
    if len(parts) != 3:
        print(f"⚠️ Skipping malformed line: {line.strip()}")
        return None
    level, time, message = parts
    if level not in VALID_LEVELS:
        print(f"⚠️ Skipping invalid log level '{level}' in line: {line.strip()}")
        return None
    return level, time, message

def analyze_and_export():
    """Reads raw_server_logs.txt line-by-line, filters errors, and exports a summary report."""
    total_lines = 0
    errors_list = []

    if not os.path.exists(RAW_LOG_FILE):
        print("⚠️ No raw log file found. Please generate logs first.")
        return

    try:
        with open(RAW_LOG_FILE, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                total_lines += 1

                parsed = parse_log_line(line)
                if parsed:
                    level, time, message = parsed
                    if level == "ERROR":
                        errors_list.append(f"[{time}] {message}")
    except OSError as e:
        print(f"❌ Error reading raw logs: {e}")
        return

    try:
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write("=== CRITICAL REPORT ===\n\n")
            f.write(f"Total Lines Processed: {total_lines}\n")
            f.write(f"Total Errors Logged: {len(errors_list)}\n\n")
            f.write("Detected Errors:\n")
            if errors_list:
                for index, value in enumerate(errors_list, start=1):
                    f.write(f"{index}. {value}\n")
            else:
                f.write("No critical errors detected.\n")
        print(f"✅ Analysis Complete! Processed {total_lines} lines. Found {len(errors_list)} errors.")
    except OSError as e:
        print(f"❌ Error writing report: {e}")

def view_report():
    """Display the generated error report."""
    if not os.path.exists(REPORT_FILE):
        print("⚠️ No report found. Please run analysis first.")
        return
    try:
        with open(REPORT_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                print("\n--- Error Report ---")
                print(content)
            else:
                print("⚠️ Report file is empty.")
    except OSError as e:
        print(f"❌ Error reading report: {e}")

def menu():
    """Menu-driven CLI for log analyzer."""
    while True:
        print("\n🖥️ Server Log Analyzer Menu")
        print("1. Generate raw logs")
        print("2. Analyze logs and export report")
        print("3. View error report")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            create_raw_logs()
        elif choice == "2":
            analyze_and_export()
        elif choice == "3":
            view_report()
        elif choice == "4":
            print("👋 Exiting Log Analyzer. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
