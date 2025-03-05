# Tire_Volume Hermann KPADONOU
from math import pi
'''
The size of a car tire in the United States is represented with three numbers like this: 205/60R15.
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits.
The volume of space inside a tire can be approximated with this formula: v = 
π 2 w a + 2,540 dwa
10,000,000,000
'''

W= float(input("Pease,Enter the width of the tire in mm (ex 205) "))
A= float(input("Enter the aspect ratio of the tire (ex 60) "))
D= float(input("Enter the diameter of the wheel in inches (ex 15) "))

volume=(pi **2 (W * A + 2540 * D )* W * A) / 10000000000

print(f"The approximate volume is: {volume} liters")