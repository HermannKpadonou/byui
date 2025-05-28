
import math

number = float(input("Enter a number: "))

print (math.sqrt(number)) 

if math.sqrt(number) < 100 :
    print("The square root is less than 100")
elif math.sqrt(number) > 100:  
    print("The square root is greater than 100")
else:
    print("The square root is equal to 100")
# # End of the program