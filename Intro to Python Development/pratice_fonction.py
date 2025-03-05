"""
Author: Brother Hermann

Purpose: Team Activity - Areas of Shapes

This program  contains how calculate the areas shapes.

"""

import math
# I. Core Requirements
# 1. function to calculate the area of a square
def compute_area_square(side_length):
    area_square = float(side_length)**2
    return area_square

# 2. function to Calculate the area of a rectangle
def compute_area_rectangle(length_rectangle, width_rectangle):
    area_rectangle = float(length_rectangle)*float(width_rectangle)
    return area_rectangle

# 3. function to Calculate the area of a circle
def compute_area_circle(radius_circle):
    area_circle = math.pi*float(radius_circle)**2
    return area_circle

# I) CORE REQUIREMENTS
print()
side_length = input('What is the length of a side of square?')
print()
length_rectangle = input('What is the length of rectangle?')
width_rectangle = input('What is the width of rectangle?')
print()
radius_circle = input('What is the radius of circle?')
print()
square_area = compute_area_square(side_length)
rectangle_area = compute_area_rectangle(length_rectangle, width_rectangle)
circle_area = compute_area_circle(radius_circle)
print(f"The area of the square is {square_area:.2f}")
print(f"The area of the rectangle is {rectangle_area:.2f}")
print(f"The area of the circle is {circle_area:.2f}")

# II) STRENGTH

shape = ['square','rectangle','circle']

print()
print('What type of shape do you have ')
print('''press the number to choose a type of shape:
1.square
2.rectangle
3.circle
''')
choice = int(input())
for i in range (len(shape)):
    i += 1
    if i == 1:
        print()
        side_length = input('What is the length of a side of square?')
        square_area = compute_area_square(side_length)
        print(f"The area of the square is {square_area:.2f}")
    elif i == 2:
        print()
        length_rectangle = input('What is the length of rectangle?')
        width_rectangle = input('What is the width of rectangle?')
        rectangle_area = compute_area_rectangle(length_rectangle, width_rectangle)
        print(f"The area of the rectangle is {rectangle_area:.2f}")
    elif i == 3:
        print()
        radius_circle = input('What is the radius of circle?')
        circle_area = compute_area_circle(radius_circle)
        print(f"The area of the circle is {circle_area:.2f}") 
    else:
        print('''Invalid choice. Please choose a valid shape:
        1.square
        2.rectangle
        3.circle
        ''')