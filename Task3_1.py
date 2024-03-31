
# Problem Statement:
# Develop a script to extract specific information from a formatted text. The text contains data entries delimited by semicolons and formatted as 'Key: Value'. Extract the value corresponding to a specific key.

# Code Example:

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here

occupations = re.findall(r"Occupation: ([^;]+)", text)

for occupation in occupations:
    print(occupation)

# Expected Outcome:

# Successfully extract the 'Occupation' value from the text.
# Implement a regex pattern that accurately targets and captures the desired data.