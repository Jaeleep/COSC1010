#
# Jae Lee Park
# Sep 26, 2024
# Kilometer Converter Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.
# 
# Initialize the conversion factor
conversion_factor = 0.6214

# Get the distance in kilometers from the user
kilometers = float(input('Enter the distance in kilometers: '))

# Calculate the distance in miles using the conversion formula
miles = kilometers * conversion_factor

# Display the result
print(kilometers, 'kilometers euqals', miles, 'miles.')