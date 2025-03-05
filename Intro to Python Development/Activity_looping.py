"""
Author: Brother Hermann
Purpose: Capitalizes letters in a string.
"""
word ='commitment'
favorite_letter = input('What is your favorite letter? ')

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()  

# 3
for letter in word:
    if letter.lower() == favorite_letter.lower():
        print('_', end="")
    else:
        print(letter.lower(), end="")
        


