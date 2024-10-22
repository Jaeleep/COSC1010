#
# Jae Lee Park
# Oct 22, 2024
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Import the random module to generate random numbers
import random

# Declare local variables
lottery_numbers = []
random_number = 0

# Generate seven random numbers each between 0 and 9 and assign them to the list
for i in range(7):
    random_number = random.randint(0, 9)
    lottery_numbers.append(random_number)

# Display the lottery numbers
print("Here are your lottery numbers: ", end="")
for number in lottery_numbers:
    print(number, end="")
print()