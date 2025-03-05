"""
Author: Brother Hermann

Purpose: milestone Shopping Cart
"""
option_menu = ['Add item','View cart' ,'Remove item','Compute total','Quit']
shopping_cart = []
prices = []

print ('Welcome in the shopping cart program')
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
           