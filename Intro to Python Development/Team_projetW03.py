"""
Author: Brother Hermann

Purpose: Grade Calculator Program
"""
print('Welcome to the Grade Calculator Program')

Grade = float(input('Please enter your grade:'))
if Grade >= 90 :
    print('Your grade is an A.')
elif Grade >= 80 :
    print('Your grade is a B.')
elif Grade >= 70 :
    print('Your grade is a C.')
elif Grade >= 60 :
    print('Your grade is a D.')
elif Grade < 60:
    print('Your grade is an F.')
if Grade >= 70:
    print('Suceessful,proud of you!')
else:
    print("Don't give up,the next time you will be successful")

print('Thanks for using the Grade Calculator Program')