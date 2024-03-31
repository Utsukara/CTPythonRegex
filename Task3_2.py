import re

# Problem Statement:
# Write a Python program to validate a list of URLs. A valid URL should start with 
# 'http://' or 'https://', followed by a domain name.

# Code Example:

urls = ["https://example.com", "www.example.com", "http://test.com"]

valid_urls = []

for url in urls:
    if re.match(r"https?://", url):
        valid_urls.append(url)
    else:
        print(f"Invalid URL: {url}")

print("Valid URLs:")
for valid_url in valid_urls:
    print(valid_url)

# Validate each URL in the list
# Your code here
# Expected Outcome:

# Correctly identify and categorize valid and invalid URLs from the list.
# Use regex to validate the format of each URL.