#
# Jae Lee Park
# Sep 8, 2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
amountofpurchase = 0.0
state_tax = 0.0
county_tax = 0.0
total_tax = 0.0
total_sale = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025
# Get the amount of the purchase.
amountofpurchase = float(input('Enter the amount of purchase:'))

# Calculate the state sales tax.
state_tax = amountofpurchase * STATE_TAX_RATE

# Calculate the county sales tax.
county_tax = amountofpurchase * COUNTY_TAX_RATE

# Calculate the total tax.
total_tax = state_tax + county_tax

# Calculate the total of the sale.
total_sale = amountofpurchase + total_tax

# Print information about the sale.
print('Amount of purchase $' + format(amountofpurchase, ',.2f'),\
    'State tax: $' + format(state_tax ,',.2f'),\
    'County tax: $' + format(county_tax ,',.2f'),\
    'Total tax: $' + format(total_tax ,',.2f'),\
    'Total sale: $' + format(total_sale ,',.2f'), sep = '\n')
