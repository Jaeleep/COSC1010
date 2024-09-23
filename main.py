#
# Jae Lee Park
# Sep 22, 2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
#Get the budgeted amount from the user.
budget = float(input('Enter the amount you have budgeted for the month:'))

# Initialize total expenses
total_expenses = 0

# Ask the user to enter expenses and keep a running total
more_expenses = 'y'

while more_expenses.lower() == 'y':
    expense = float(input('Enter an expensse: '))
    total_expenses += expense

    # Ask the user if they want to add another expense.
    more_expenses = input('Do you want to add another expense?: Type y for yes, n for no: ')

# Calculate if the user is over or under budget.
difference = budget - total_expenses

# Display the results to the user.
if difference > 0:
    print('You are under budget by $', round(difference, 2))
elif difference < 0:
    print('You are over budget by $', round(-difference, 2))
else:
    print('You have exactly met your budget.')