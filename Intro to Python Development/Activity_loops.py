"""
Author: Brother Hermann

Purpose: Activity_loops
"""
# Activity 1

number = int(input('Please,type a positive number:'))
while number < 0:
    print('Sorry,that is a negative number.')
    number = int(input('Please,type a positive number:'))
print(f'Thank you,the number is {number}')

#Activity 2

answer = ''
while answer != 'yes':
    answer = input('May I have a piece of candy?')
print('Thank you')