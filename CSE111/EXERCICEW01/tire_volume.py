"""
Author: Hermann KPADONOU
Purpose: Write a Python program named that reads from the keyboard the three numbers for a tire 
and computes and outputs the volume of space inside that tire and writes the result to a file with the date.
"""
# Tire Volume Calculation

# import math
# import the pi constant from the math module
from math import pi

W= float(input("Enter the width of the tire in mm (ex 205) "))
A= float(input("Enter the aspect ratio of the tire (ex 60) "))
D= float(input("Enter the diameter of the wheel in inches (ex 15) "))

volume = (pi * W ** 2 * A * (W * A + 2540 * D)) / 10000000000
print(f"The approximate volume is {volume:.2f} liters")


#  datetime module to get the current date and time
from datetime import datetime
# get the current date and time
current_date_time = datetime.now()      

# added code to write the volume to a file
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_time:%Y-%m-%d},{int(W)},{int(A)},{int(D)},{volume:.2f}\n", file=volumes_file)
    volumes_file.close()

'''
# print the contents of the file to verify the data was written correctly
with open("volumes.txt", "rt") as volumes_file:
    for line in volumes_file:
        print(line.strip())
'''
# Creativity: Ask the user if they want to purchase a tire based on the volume calculated.

ask_user = input("Do you want to purchase a tire? (yes/no) ")
ask_user = ask_user.lower()

if ask_user == "yes":
    if volume >= 70:
        price = 65.37
        print(f"The price of the tire is ${price:.2f}")
    elif 31 <= volume <= 70:
        price = 45.37
        print(f"The price of the tire is ${price:.2f}")
    elif volume <= 30:
        print("Sorry! The tire is too small.")

    if price is not None:
        number_of_tires = int(input("Enter the number of tires you want to purchase: "))
        full_name = input("Enter your full name: ")
        adress = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        total_price = price * number_of_tires

        with open("customers.txt", "at") as customers_file:
            print(f"Date: {datetime.now():%Y-%m-%d}\n", file=customers_file)
            print(f"Number of tires: {number_of_tires}\n", file=customers_file)
            print(f"Price per tire: ${price:.2f}\n", file=customers_file)
            print(f"Total price: ${total_price:.2f}\n", file=customers_file)
            print(f"Customer name: {full_name}\n", file=customers_file)
            print(f"Customer address: {adress}\n", file=customers_file)
            print(f"Customer phone number: {phone_number}\n", file=customers_file)
        print("your order has been placed successfully!")
        print (f"You will pay ${total_price:.2f} for {number_of_tires} tires.")
        print("Thank you for your order!")


else:
    print("Thank you for your time!")

'''
# print the contents of the file to verify the data was written correctly
with open("customers.txt", "rt") as customers_file:
    for line in customers_file:
        print(line.strip())
'''
# End of the program

       




