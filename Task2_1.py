
# Problem Statement:
# You have a script that extracts email addresses from a text but needs to be refined to exclude 
# certain domains (e.g., 'exclude.com'). 
# Modify the script to extract all email addresses except those from the specified domain.

# Code Example:

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b", text)

for email in emails:
    if email.endswith('exclude.com'):
        emails.remove(email)
print(emails)


# Expected Outcome:

# Adapt the regex pattern to exclude email addresses from 'exclude.com'.
# Ensure the script still extracts all other valid email addresses.