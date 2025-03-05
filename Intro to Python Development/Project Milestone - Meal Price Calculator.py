"""
Author: Brother Hermann

Purpose: Meal Price Calculator
"""

# Project Milestone - Meal Price Calculator
print()
price_child_meal = float(input("What is the price of a child's meal?"))
price_adult_meal = float(input("What is the price of an adult's meal?"))
number_of_children = int(input('How many children are there?'))
number_of_adults = int(input('How many adults are there?'))
sales_tax_rate = float(input('What is the sales tax rate?'))
print()
Subtotal = (price_child_meal * number_of_children) + (price_adult_meal * number_of_adults)
print(f'Subtotal: {Subtotal}')
# End of Milestone