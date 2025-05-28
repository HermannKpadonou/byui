pizza_price = 10.95
topping_price = 1.25

number_of_toppings = int(input("Enter the number of toppings: "))
total_price = pizza_price + (topping_price * number_of_toppings)
print(f"Total price: ${total_price:.2f}")


if number_of_toppings >= 5:
    reduce_price = 0.5 * total_price
    total_price -= reduce_price
    print(f"Discount applied: ${reduce_price:.2f}")
if total_price > 20:
    print("That's a lot of pizza!")
elif total_price < 10:
    print("That's a small pizza!")
else:
    print("That's a medium pizza!")
# # End of the program
# # The program ends here