import os

# Dynamic Path Setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_LOG_FILE = os.path.join(SCRIPT_DIR, "raw_server_logs.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "error_report.txt")


def create_raw_logs():
    """Generates the raw server log file for analysis."""
    logs = [
        "INFO - 10:01 - User login successful\n",
        "WARNING - 10:05 - High memory usage detected\n",
        "ERROR - 10:07 - Database connection failed\n",
        "INFO - 10:10 - User logout successful\n",
        "ERROR - 10:12 - API Gateway timeout exception\n",
        "INFO - 10:15 - Background worker completed\n"
    ]
    with open(RAW_LOG_FILE, 'w', encoding='utf-8') as f:
        f.writelines(logs)


def analyze_and_export():
    """Reads raw_server_logs.txt line-by-line using readline(),

    filters out critical errors, and exports a clean summary report.
    """
    total_lines = 0
    errors_list = []

    # 1. Read & Parse line-by-line
    with open(RAW_LOG_FILE, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break  # End of file reached
            
            total_lines += 1
            
            # Extract and format error logs
            if line.startswith("ERROR"):
                stripped_line = line.strip()
                split_line = stripped_line.split(" - ")
                # Format: [Time] Message
                errors_list.append(f"[{split_line[1]}] {split_line[2]}")

    # 2. Export Summary Report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("=== CRITICAL REPORT ===\n\n")
        f.write(f"Total Lines Processed: {total_lines}\n")
        f.write(f"Total Errors Logged: {len(errors_list)}\n\n")
        f.write("Detected Errors:\n")
        
        for index, value in enumerate(errors_list, start=1):
            f.write(f"{index}. {value}\n")

    print(f"Analysis Complete! Processed {total_lines} lines. Found {len(errors_list)} errors.")


if __name__ == "__main__":
    create_raw_logs()
    analyze_and_export()
