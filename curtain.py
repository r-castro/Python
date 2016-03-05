"""
curtains.py
Problem: Calculate how much material to buy, given the size of the windows.
Target Users: My friend who wants to make some curtains
Target System: GNU/Linux
Interface: Command-line
Functional Requirements: Print out the required length of fabric in meters
Print out the total price of the fabric
User must be able to input the measurements of the window
Testing: Simple run test
Maintainer: maintainer@website.com
"""

__version__ = 0.1
# To start with, all the measurements will be in cm
# Assume that the roll of material is going to be 140cm wide
# and that the price per meter will be 5 units of currency
roll_width = 140
price_per_metre = 5

# Prompt the user to input the window measurements in cm
window_height = input('Enter the height of the window (cm): ')
window_width = input('Enter the width of the window (cm): ')

# Add a bit for the hems
# First we must convert the string into a number
# otherwise we will get an error if we try to perform arithmetic on a text string
curtain_width = float(window_width) * 0.75 + 20
curtain_length = float(window_height) + 15

# Work out how many widths of cloth will be needed
# and figure out the total length of material for each curtain (in cm still)
widths = curtain_width / roll_width
total_length = curtain_length * widths

# Actually there are two curtains, so we must double the amount of material
# and then divide by 10 to get the number of meters
total_length = (total_length * 2) / 10

# Finally, work out how much it will cost
price = total_length * price_per_metre

# And print out the result
print("You need", total_length, "meters of cloth for ", price)
