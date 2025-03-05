"""
Author: Brother Hermann

Purpose: milestone Shopping Cart
"""
option_menu = ['Add item','View cart' ,'Remove item','Compute total','Quit']
shopping_cart = []

# milestone

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
      print(item + ' has been added.')
   elif option == 2:
      print('The contents of the shopping cart are:')
      for item in shopping_cart:
         item = item.capitalize()
         print(item)
   elif option == 3:
      item = input('What item would you like to remove?')
      item = item.capitalize()
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
   else:
      print('Sorry, that was not a valid option.')
   print ('Please,select one of the following :')

   for i in range (len(option_menu)):
      print(f'{i+1}. {option_menu[i]} ')
   option = int(input('Please enter an action:'))
else:
   print('Thank you for using the shopping cart program.')
# end of milestone