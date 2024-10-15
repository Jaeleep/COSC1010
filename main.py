#
# Jae Lee Park
# Oct 15, 2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Declare all local variables
myfile = 0
line = 0
number = 0

# Open the file.
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Closse the file.
myfile.close()