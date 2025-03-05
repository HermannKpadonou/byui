"""
Author: Brother Hermann

Purpose: ID Badge Generator
"""
First_name = input('what your first name?')
Last_name = input('What is your last name?')
Email_Address = input('Please,enter your email address.')
Phone_number = input('Please,enter your phone number.')
Job_title = input('Please,Enter your job title.')
ID_Number = input('Please,Enter your ID Number.')
Hair = input('Please,Enter your hair color.')
Eyes = input('Please,Enter your eyes color.')
Month = input('Please,Enter the month.')
Training = input('Training : Yes or No.')
ouput = f'{Last_name}, {First_name}'

# Core Requirements
print('The ID Card is:')
print('---------------------------------')
print(ouput)
print(Job_title)
print('ID '+ ID_Number)
print()
print(Email_Address)
print(Phone_number)
# Stretch Challenge
print()
print('Hair:'+ Hair + '     '+ 'Eyes:' + Eyes )
print('Month:'+ Month + '   '+ 'Training:' + Training )
print('---------------------------------')