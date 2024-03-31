import re

# Problem Statement: You have a log file represented as a string, containing timestamps and messages. 
# Write a script to reformat the timestamps from 'MM-DD-YYYY' to 'YYYY-MM-DD' and 
# anonymize any usernames mentioned in the log (format: '@username').

# Code Example:

log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."# Your solution here</span>

formatted_data = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", log_data)
anonymized_data = re.sub(r"@\w+", "[ANONYMIZED USER]", formatted_data)
for log in anonymized_data.split("."):
    print(log.strip())

# print(formatted_data)

# Expected Outcome:

# Correctly reformat the date in each log entry.
# Replace all instances of '@username' with '[ANONYMIZED USER]'.
# Use re.sub() effectively to achieve the desired text manipulations.