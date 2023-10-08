import csv
import getpass
import os
import time

# Define the path to the CSV file
CSV_FILE_PATH = "job_applications.csv"

# Check if the CSV file exists, and create it if it doesn't
if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Job Portal", "E-mail", "Username", "Company", "Date Applied", "Status", "Location", "Job Field"])

# Prompt the user to enter the job application details
job_portal = input("Job Portal: ")
email = input("E-mail: ")
username = input("Username: ")
#password = getpass.getpass("Password: ")
company = input("Company: ")
date_applied = time.strftime("%Y-%m-%d %H:%M:%S")
status = input("Status: ")
location = input("Location: ")
job_field = input("Job Field: ")

# Write the details to the CSV file
with open(CSV_FILE_PATH, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([job_portal, email, username, company, date_applied, status, location, job_field])

# Print a success message
print("Application saved successfully.")
