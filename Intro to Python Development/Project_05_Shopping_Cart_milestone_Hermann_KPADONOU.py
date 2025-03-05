"""
Author: Brother Hermann

Purpose: milestone Shopping Cart
"""
option_menu = [1,2,3,4,5]
shopping_cart = []
# Core Requirements : milestone
while True:
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    option = int(input('Please enter an action:'))
    if option == 1:
        item = input('What item would you like to add?')
        shopping_cart.append(item)
        print(item + ' has been added.')
    elif option == 2:
        print('The contents of the shopping cart are:')
        for item in shopping_cart:
            print(item)
    elif option == 3:
        item = input('What item would you like to remove?')
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(item + ' has been removed.')
        else:
            print('Sorry, that item is not in your cart.')
    elif option == 4:
        total = 0
        for item in shopping_cart:
            total += 1
        print('The total number of items in the cart is ' + str(total))
    elif option == 5:
        print('Thank you for using the shopping cart program.')
    else:
        print('Sorry, that was not a valid option.')
