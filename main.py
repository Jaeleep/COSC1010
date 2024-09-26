#
# Jae Lee Park
# Sep 26, 2024
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.

#Initialize the conversion factor
inches_per_foot = 12

# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * inches_per_foot

# Get the number of feet from the user
feet = int(input('Enter the number of feet: '))

# Calculate the distance in inches using the conversion function
inches = feet_to_inches(feet)

# Display the result
print(feet, 'feet equals', inches, 'inches')