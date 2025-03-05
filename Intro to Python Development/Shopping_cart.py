"""
Author: Brother Hermann

Purpose: Shopping Cart
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
         price = float(input(f'What is the price of {item}?'))
         prices.append(price)
         print( item + ' has been added to the cart.')
      elif option == 2:
         print('The contents of the shopping cart are:')
         for i in  range (len(shopping_cart)):
            item = item.capitalize()
            print(f'{str(i+1)}.{shopping_cart[i]} - ${str(prices[i])}')
      elif option == 3:
         item = input('What item would you like to remove?')
         item = item.capitalize()
         if item in shopping_cart:
            index = shopping_cart.index(item)
            shopping_cart.remove(item)
            prices.remove(prices[index])
            print(item + ' has been removed.')
      elif option == 4:
         total_price = 0
         for price in prices:
            total_price += price
         print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
      else:
         print('Sorry, that was not a valid option.')
         print ('Please,select one of the following :')
   
      for i in range (len(option_menu)):
         print(f'{i+1}. {option_menu[i]} ')
      option = int(input('Please enter an action:'))

# creative part
# i added the delivery and the tva
# i added the total amount of the items in the cart
tva = 0.15
delivery = 5.00
total_amount = 0
for price in prices:
   total_amount += price + price * tva + delivery
print(f'The total amount of the items in the cart is ${total_amount}')
print('Thank you for using the shopping cart program.')
print()
print('Goodbye.')
# end of the program