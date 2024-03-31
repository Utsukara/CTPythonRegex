import re

# Problem Statement:
# You have a string containing various price formats from an international e-commerce site. Standardize all prices to the format 'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.

# Code Example:

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
# Standardize all prices to 'USD XX.XX' format
# Your code here
standardized_price_data = re.sub(r"(\$?)(\d+\.\d+)(\s?USD|\$)?", r"USD \2", price_data)

# Extract only the standardized prices
standardized_prices = re.findall(r"USD \d+\.\d+", standardized_price_data)

print("Standardized Prices:")
for price in standardized_prices:
    print(price)

# Expected Outcome:

# Convert all price formats in the string to a standardized 'USD XX.XX' format.
# Use re.sub() to perform the necessary replacements and format transformations.