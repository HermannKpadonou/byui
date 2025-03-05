"""
Author: Brother Hermann

Purpose: qualifying for a loan
"""
# Basics questions
print("For each of these questions, please provide a 1-10 rating:")

loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
level_income = int(input('How hight is your income? '))
down_payment= int(input ('How large is your down payment? '))

loan = False

if loan_size >= 5:
    if credit_history >= 7 and level_income >= 7:
        loan = True
    elif credit_history >= 7 and level_income >= 7:
         if down_payment >= 5:
             loan = True
         else:
             loan = False
    else:
        loan = False
else: 
    if loan_size < 5:
        loan = False
    else:
        if loan_size >= 7 or level_income >= 7:
            loan = True
        elif loan_size >= 4 and level_income >= 4:
            loan = True
        else:
            loan = False
if loan:
        print ('Yes,You qualified for the loan ')
else:
        print('Sorry,You are not qualified for the loan')

print ('Thanks to try the loan similator')
# end the code