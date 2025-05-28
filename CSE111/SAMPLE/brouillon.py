from datetime import datetime
datetime.now(tz=None)
print("Welcome in the discount day!")
print()
subtotal=float(input("Please, Enter your Subtotal!"))



if subtotal>= 50 and datetime.now().strftime('%A') == "Tuesday":
    discount= (subtotal*10)/100
    new_subtotal = subtotal-discount
    taxe= (new_subtotal*6)/100
    Total_amount= new_subtotal + taxe
    print(f"Congrats,You are {discount:.2f} discount today")
    print(f"${taxe:.2f}")
    print(f"Total_amount is  ${Total_amount:.2f}")
    
elif subtotal>= 50 and datetime.now().strftime('%A') == "Wednesday":
    discount= (subtotal*10)/100
    new_subtotal = subtotal-discount
    taxe= (new_subtotal*6)/100
    Total_amount= new_subtotal+ taxe
    print(f"Congrats,You are {discount:.2f} discount today")
    print(f"${taxe:.2f}")
    print(f"Total_amount is  ${Total_amount:.2}")

elif subtotal < 50 :
    print("Sorry,this amount have not a discount!")
    taxe= (subtotal*6)/100
    Total_amount=subtotal + taxe
    print(f"${taxe:.2f}")
    print(f"You pay ${Total_amount:.2f}") 

else:
    print("Sorry,No discount today!")
    taxe= (subtotal*6)/100
    Total_amount=subtotal + taxe
    print(f"${taxe:.2f}")
    print(f"You pay ${Total_amount:.2f}") 