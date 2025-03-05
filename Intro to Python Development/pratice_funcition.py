def compute_area_square(side_length):
    return compute_area_rectangle(side_length, side_length)

def compute_area_rectangle(length_rectangle, width_rectangle):
    area_rectangle = float(length_rectangle) * float(width_rectangle)
    return area_rectangle

def compute_area_circle(radius_circle):
    area_circle = 3.14 * float(radius_circle) ** 2
    return area_circle

while True:
    shape = input('What type of shape do you have? (square/rectangle/circle/quit): ')
    if shape == 'square':
        side_length = input('What is the length of a side of the square? ')
        square_area = compute_area_square(side_length)
        print(f"The area of the square is {square_area}")
    elif shape == 'rectangle':
        length_rectangle = input('What is the length of the rectangle? ')
        width_rectangle = input('What is the width of the rectangle? ')
        rectangle_area = compute_area_rectangle(length_rectangle, width_rectangle)
        print(f"The area of the rectangle is {rectangle_area}")
    elif shape == 'circle':
        radius_circle = input('What is the radius of the circle? ')
        circle_area = compute_area_circle(radius_circle)
        print(f"The area of the circle is {circle_area}")
    elif shape == 'quit':
        break