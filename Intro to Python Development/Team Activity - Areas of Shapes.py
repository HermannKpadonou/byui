"""
Author: Brother Hermann

Purpose: Team Activity - Areas of Shapes

This program  contains how calculate the areas shapes.

"""


# I. Core Requirements
# 1. Calculate the area of a square
print()
side_length = input('What is the length of a side of square?')
area_square = float(side_length)**2
print('The area of the square is: ' + str(area_square))

# 2. Calculate the area of a rectangle
print()
length_rectangle = input('What is the length of rectangle?')
width_rectangle = input('What is the width of rectangle?')
#  I used float() because the input is decimal forme.
area_rectangle = float(length_rectangle)*float(width_rectangle)
print('The area of the rectangle is: ' + str(area_rectangle))

# 3. Calculate the area of a circle
print()
radius_circle = input('What is the radius of circle?')
#  I used float() because the input is decimal forme.
area_circle = 3.14*float(radius_circle)**2
print('The area of the circle is: ' + str(area_circle))


# II.Stretch Challenge
import math
# 1.Use pi from the math module
print()
radius_circle = input('What is the radius of circle?')
area_circle = math.pi*float(radius_circle)**2
print('The area of the circle is: ' + str(area_circle))

# 2. Calculate with a single  value
import math
single_length_value = input('Please,enter a number of your choice.')
area_square = float(single_length_value)**2
area_of_circle = math.pi*float(single_length_value)**2
volume_of_cube = float(single_length_value)**3
volume_of_sphere = (4/3)*math.pi*float(single_length_value)**3
print()
print('The area of the square is: ' + str(area_square))
print('The area of the circle is: ' + str(area_of_circle))
print('The volume of the cube is: ' + str(volume_of_cube))
print('The volume of the sphere is: ' + str(volume_of_sphere))

# 3. Whrite the area shapes in square centimeters and convert in square meters
print()
side_length = input('What is the length of a side of square?')
area_square = float(side_length)**2
area_square_squared_meter = area_square / 10000
print('The area of the square is: ' + str(area_square) + 'cm²')
print('The area of the square is:'  + str(area_square_squared_meter) + 'm²')
print()
length_rectangle = input('What is the length of rectangle?')
width_rectangle = input('What is the width of rectangle?')
area_rectangle = float(length_rectangle)*float(width_rectangle)
area_rectangle_squared_meter = area_rectangle / 10000
print('The area of the rectangle is: ' + str(area_rectangle)+ 'cm²')
print('The area of the rectangle is: ' + str(area_rectangle_squared_meter)  + 'm²')
print()
radius_circle = input('What is the radius of circle?')
area_circle = 3.14*float(radius_circle)**2
area_circle_squared_meter = area_circle / 10000
print('The area of the circle is: ' + str(area_circle) + 'cm²')
print('The area of the circle is: ' + str(area_circle_squared_meter) + 'm²')
 #End of the program




