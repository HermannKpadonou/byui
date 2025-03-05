option_menu = ['Add item','View cart' ,'Remove item','Compute total','Quit']
shopping_cart = []
prices = []

print ('Welcome in the shopping car program')
print ('Please,select one of the following :')

for i in range (len(option_menu)):
    print(f'{i+1}. {option_menu[i]} ')
option = int(input('Please enter an action:'))

while option != 5:
    if option == 1:
        item = input('What item would you like to add?')
        item = item.capitalize()
        shopping_cart.append(item)
        price = float(input('What is the price of the item?'))
        prices.append(price)
        print( item + ' has been added.')
    elif option == 2:
        print('The contents of the shopping cart are:')
        for item in shopping_cart:
            print(f'{i+1}. {item} - ${prices[i]}')
    elif option == 3:
        item = input('What item would you like to remove?')
        item = item.capitalize()
        if item in shopping_cart:
            index = shopping_cart.index(item)
            shopping_cart.append(index)
            prices.append(index)
            print(item + ' has been removed.')
    elif option == 4:
        total = 0
        total_price = 0
        for item in shopping_cart:
            total += 1
        for price in prices:
            total_price += 1

        print(f'The total price of the items in the cart is ${total}')
    else:
        print('Sorry, that was not a valid option.')
        print ('Please,select one of the following :')

    for i in range (len(option_menu)):
        print(f'{i+1}. {option_menu[i]} ')
        option = int(input('Please enter an action:'))
    if option == 5:
        print('Thank you for using the shopping cart program.')
    else:
        print('Sorry, that was not a valid option.')

print()
print('Thank you for using the shopping cart program.')