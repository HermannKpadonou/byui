"""
Author: Brother Hermann

Purpose: Meal Price Calculator
"""

# Project - Meal Price Calculator
# I use the double quotes to make the code more readable
print()
print('Welcome to the Meal Price Calculator')
print()
price_child_meal = float(input("What is the price of a child's meal?"))
price_adult_meal = float(input("What is the price of an adult's meal?"))
number_of_children = int(input("How many children are there?"))
number_of_adults = int(input("How many adults are there?"))
sales_tax = float(input("What is the sales tax rate?"))
print()
Subtotal = (price_child_meal * number_of_children) + (price_adult_meal * number_of_adults)
print(f"Subtotal: ${Subtotal:.2f}")
Sales_tax = Subtotal * sales_tax / 100
print(f"Sales Tax: ${Sales_tax:.2f}")
Total = Subtotal + Sales_tax
print(f"Total: ${Total:.2f}")
print()
payment_amount = float(input("What is the payment amount?"))
change = payment_amount - Total
print(f'Change: ${change:.2f}')

# Creativity and Exceeding Requirements
# to make discounts for Black Friday and Loyalty Card
# the discount is available for the family only
discount_black_friday = float(input("What is the discount for Black Friday?"))
discount_loyalty_card = float(input("What is the discount for Loyalty Card?"))
total_discount = (discount_black_friday + discount_loyalty_card) / 100
print()
print(f"Total Discount: ${total_discount:.2f}")
total_after_discount = Total - (Total * total_discount)
print(f"Total after discount: ${total_after_discount:.2f}")
New_change = payment_amount - total_after_discount
print(f"New Change: ${New_change:.2f}")
print()
print("Thank you for using the Meal Price Calculator")
# end of code