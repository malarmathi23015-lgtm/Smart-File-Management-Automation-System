import os
import logging
from modules.helper import create_folder

def generate_report():

    try:

        create_folder("reports")

        with open("logs/operations.log", "r") as log_file:
            logs = log_file.read()

        with open("reports/report.txt", "w") as report:

            report.write(
                "SMART FILE MANAGER REPORT\n"
            )

            report.write("=" * 40 + "\n\n")

            report.write(logs)

        print("Report Generated Successfully!")

    except Exception as e:
        logging.error(f"Error generating report: {e}")
        print("Error:", e)