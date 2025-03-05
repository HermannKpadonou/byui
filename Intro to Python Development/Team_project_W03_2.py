"""
Author: Brother Hermann

Purpose: Grade Calculator Program
"""
print('Welcome to the Grade Calculator Program')

Grade = int(input('Please enter your grade:'))
if Grade >= 90 :
   letter = 'A  '
elif Grade >= 80 :
   letter = 'B  '
elif Grade >= 70 :
   letter = 'C  '
elif Grade >= 60 :
   letter = 'D  '
else:
   letter = 'F  '
print (f"Your grade is an: {letter}")

if Grade >= 70:
    print('Suceessful,proud of you!')
else:
    print("Don't give up,the next time you will be successful")

# stretch challenge
sign = Grade % 10
if sign >= 7:
    sign = '+'
elif sign <= 3:
    sign = '-'
else:
    sign = ' '
print (f"Your grade is an: {letter}{sign}")

print('Thanks for using the Grade Calculator Program')