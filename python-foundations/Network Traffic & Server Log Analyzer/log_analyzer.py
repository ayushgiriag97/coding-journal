import os

# Dynamic Path Setup (so your script never gets lost)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_LOG_FILE = os.path.join(SCRIPT_DIR, "raw_server_logs.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "error_report.txt")

# Dummy log data to write into your raw file
RAW_LOGS = [
    "INFO - 10:01 - User login successful\n",
    "WARNING - 10:05 - High memory usage detected\n",
    "ERROR - 10:07 - Database connection failed\n",
    "INFO - 10:10 - User logout successful\n",
    "ERROR - 10:12 - API Gateway timeout exception\n",
    "INFO - 10:15 - Background worker completed\n"
]


def create_raw_logs(data):
    """Write the RAW_LOGS list into RAW_LOG_FILE."""
    # TODO: Write your code here using utf-8 encoding
    with open(RAW_LOG_FILE, 'w' , encoding='utf-8') as f:
        f.writelines(data)


def analyze_and_export():
    """Read RAW_LOG_FILE line-by-line using readline(), find errors,

    and write a summary report to REPORT_FILE.
    """
    with open(RAW_LOG_FILE, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line != f.readline():
                 break
            else:
                print(line)

if __name__ == "__main__":
    create_raw_logs(RAW_LOGS)
    analyze_and_export()