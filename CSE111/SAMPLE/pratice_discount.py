"""
Author: Hermann KPADONOU
Purpose: Calculate the customer discount on Tuesday and Wednesday for a retail store.
Enhancements:

"""
#import a datetime module
from datetime import datetime
# Ask user for the subtotal
subtotal = float(input(" Please! Enter the subtotal: "))
discount_rate = 10 / 100
sales_tax_rate = .06

# Get the day of the week
current_date_time = datetime.now()
day_of_week = current_date_time.weekday()

# Compute and print the discount amount
day_of_week = 2
if day_of_week == 1 or day_of_week == 2:  # Tuesday or Wednesday
   if subtotal >= 50:
        discount = subtotal * discount_rate
        subtotal = subtotal - discount
        print(f"Discount amount: ${discount:.2f}")
   else:
        difference = 50 - subtotal
        print("Please! puchase  {difference:.2f} more to receive a discount.")
        print("Sorry! You are not eligible for a discount.")
else:
    print("Come back on Tuesday or Wednesday to receive a discount.")


# Compute and print the sales tax amount

sales_tax_amount = float(subtotal * sales_tax_rate)
print(f"Sales tax amount: ${sales_tax_amount:.2f}")


# Compute and print the total amount due
total_amount_due = subtotal + sales_tax_amount
print(f"Total amount due: ${total_amount_due:.2f}")

print ("Thank you for shopping with us!")
# # End of the program