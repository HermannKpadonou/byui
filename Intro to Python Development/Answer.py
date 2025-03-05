
import math

def compute_area_square(side_length):
    return float(side_length) ** 2

def compute_area_rectangle(length, width):
    return float(length) * float(width)

def compute_area_circle(radius):
    return math.pi * (float(radius) ** 2)

shape = ['square','rectangle','circle']

print()
print('What type of shape do you have ')
print('''press the number to choose a type of shape:
1.square
2.rectangle
3.circle
''')
choice = int(input())
if choice == 1:
    print()
    side_length = input('What is the length of a side of square?')
    square_area = compute_area_square(side_length)
    print(f"The area of the square is {square_area:.2f}")
elif choice == 2:
    print()
    length_rectangle = input('What is the length of rectangle?')
    width_rectangle = input('What is the width of rectangle?')
    rectangle_area = compute_area_rectangle(length_rectangle, width_rectangle)
    print(f"The area of the rectangle is {rectangle_area:.2f}")
elif choice == 3:
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
