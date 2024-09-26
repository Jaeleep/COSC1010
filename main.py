#
# Jae Lee Park
# Sep 14,2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
lengthA = 0 # The length of rectangle A
widthA = 0 # The width of rectangle A
lengthB = 0 # The length of rectangle B
widthB = 0 # The width of rectangle B
areaA = 0 # The area of rectangle A
areaB = 0 # The area of rectangle B

# Get length A
lengthA = float(input('Enter the length of rectangle A: '))

# Get width A
widthA = float(input('Enter the width of rectangle A: '))

# Get length B
lengthB = float(input('Enter the length of rectangle B: '))

# Get width B
widthB = float(input('Enter the width of rectangle B: '))

# Calculate area A
areaA = lengthA * widthA

# Calculate area B
areaB = lengthB * widthB

# Print area comparison using if-elif-else statements
if areaA > areaB:
    print('\nRectangle A has a greater area.')
elif areaB > areaA:
    print('\nRectangle B has a greater area.')
else:
    print('\nBoth rectangles have the same area.')