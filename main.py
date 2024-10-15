#
# Jae Lee park
# Oct 14, 2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Declare local varaibles
myfile = 0
line = 0
number = 0
total = 0
count = 0

# Open the file
myfile = open('numbers.txt', 'r')

# Read each lin in the file and calculate total and count
for line in myfile:
    number = int(line)
    total += number
    count += 1

# Calculate the average if count is greater than 0.
if count > 0:
    average = total / count
    print('The average of the numbers is:', average)


# Close the file.
myfile.close()