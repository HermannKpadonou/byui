import math
number_item = int(input("Enter the number of items: "))
item_per_box = int(input("Enter the number of items per box: "))
number_of_boxes = math.ceil(number_item / item_per_box)
print(f"Number of boxes needed: {number_of_boxes}")
