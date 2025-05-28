"""
Author: Hermann KPADONOU
Purpose: Write a Python program named that reads from the keyboard the three numbers for a tire 
and computes and outputs the volume of space inside that tire
"""

# import math
# import the pi constant from the math module
from math import pi

# Tire volume calculation

W= float(input("Enter the width of the tire in mm (ex 205) "))
A= float(input("Enter the aspect ratio of the tire (ex 60) "))
D= float(input("Enter the diameter of the wheel in inches (ex 15) "))

volume = (pi * W ** 2 * A * (W * A + 2540 * D)) / 10000000000


print(f"The approximate volume is {volume:.2f} liters")

# end of the program


