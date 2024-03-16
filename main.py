"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
numchars = 18
color = "black"
woodtype = "oak"
# Charge for this sign.
charge += 35.00
# Number of characters.
if numchars > 5:
    charge += (numchars - 5) * 4.00
# Color of characters.
if color == "gold":
    charge += 15.00
# Type of wood.
if woodtype == "oak":
    charge += 20.00
# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))