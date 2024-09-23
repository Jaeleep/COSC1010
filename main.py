#
# Jae Lee Park
# Sep 17, 2024
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.
total_bugs = 0 

# Get number of bugs collected each day using a for loop.
for  day in range(1, 6):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total_bugs += bugs

# Display the total number of bugs collected.
print(f'Total number of bugs collected over 5 days: {total_bugs}')