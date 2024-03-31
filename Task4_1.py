import re

# Problem Statement:
# You have a list of product descriptions. Your task is to tag each product based on keywords in 
# the description. For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' 
# based on relevant keywords found in their descriptions.

# Code Example:

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
# Tag each product based on keywords in the description
# Your code here
electronics = []
apparel = []
home_kitchen = []

for description in descriptions:
    if re.search(r"smartphone|screen|memory", description, re.IGNORECASE):
        print(f"Tagged as Electronics: {description}")
        electronics.append(description)
    elif re.search(r"cotton|t-shirt", description, re.IGNORECASE):
        print(f"Tagged as Apparel: {description}")
        apparel.append(description)
    elif re.search(r"stainless steel|kitchen|knife", description, re.IGNORECASE):
        print(f"Tagged as Home & Kitchen: {description}")
        home_kitchen.append(description)

print("Electronics descriptions:")
for elec in electronics:
    print(elec)

print("Apparel descriptions:")
for app in apparel:
    print(app)

print("Home & Kitchen descriptions:")
for hk in home_kitchen:
    print(hk)

# Expected Outcome:

# Efficiently tag each product with the appropriate category ('Electronics', 'Apparel', 'Home & Kitchen') using regex to identify relevant keywords.
# Use regex to match specific product-related keywords in each description.