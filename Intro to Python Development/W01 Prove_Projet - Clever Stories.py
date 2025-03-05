"""
Author: Brother Hermann

Purpose: Prove Projet-Clever Stories

This program also contains a way to implement a Mad Libs.

"""

# I Choose the variables 'verb', 'verb1','verb2' to avoid conflict in my script.

print('Please enter the following:')
print()
adjective = input('Adjective: ')
animal = input('Animal: ')
verb = input('verb: ')
exclamation = input('exclamation: ')
verb1 = input('verb: ')
verb2 = input('verb: ')

#Showing Creativity and Exceeding Requirements
#I wanted [verb] with my  [adjective] [noun]. We all laughed like an [animal].

verb3 = input('verb: ') 
adjective1 = input('Adjective: ')
singular_noun = input('noun: ')
animal1 = input('Animal: ')

# Normal part
print()
print('Your story is:')
print()
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb} down the hallway. "{exclamation.title()}!" I yelled. But all')
print(f'I could think to do was to {verb1} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb2}' )
print('right in front of my family.')

# creativity part
print(f'I wanted {verb3} with my  {adjective1} {singular_noun}. We all laughed like an {animal1}.')

# as I chose simples quotes, the doubles quotes in the story were not affected.
