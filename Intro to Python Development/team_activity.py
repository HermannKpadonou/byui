"""
Author: Brother Hermann
Purpose: guess number
"""
# Activity 1
number = input('What is the number?')
guess = input('What is your guess?')
if number == guess:
    print('You guessed it!')
else:
    if number < guess:
        print('Higher')
    else:
        print('Lower')
# Activity 2
print()
number = input('What is the number?')
guess = input('What is your guess?')
while number != guess:
    if number < guess:
        print('Higher')
    else:
        print('Lower')
    guess = input('What is your guess?')
print('You guessed it!')
# Activity 3
print()
import random
number = random.randint(1, 100)
while guess != number:
    guess = int(input('What is your guess?'))
    if guess < number:
        print('Higher')
    elif guess > number:
        print('Lower')
    else:
        print('You guessed it!')

# Strech 1
print()
import random
number = random.randint(1, 100)
guess = int(input('What is your guess?'))
while guess != number:

