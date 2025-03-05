cart = []

def add_item():
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    cart.append((item_name, item_price))
    print(f"{item_name} has been added to the cart.")

def view_cart():
    total_price = 0
    for index, (item_name, item_price) in enumerate(cart):
        print(f"{index + 1}. {item_name}: {item_price:.2f}")
        total_price += item_price
    print(f"Total price: {total_price:.2f}")

def remove_item():
    item_number = int(input("Enter the number of the item to remove: "))
    if 1 <= item_number <= len(cart):
        item_name, _ = cart.pop(item_number - 1)
        print(f"{item_name} has been removed from the cart.")
    else:
        print(f"Invalid item number.")