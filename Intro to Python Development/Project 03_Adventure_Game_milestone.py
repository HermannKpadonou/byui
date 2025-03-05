"""
Author: Brother Hermann

Purpose: My Adventure Game
"""
# Welcome to my adventure game
# Milestone

print('Welcome to my adventure game!')
print()
print('level 1')
print()
# first scenario = level 1
print('''You have been selected to participate in the national lottery. 
this consists of opening 3 doors at each level;
When you open the right door, you go straight to the next level.
But when you open the second chance door, you get another try.
however,the game is over when you open the wrong door or you reach the end of the game.''')
print('Good luck!')
name = input('What is your name? ')
print(f'Hello {name.upper()}!')
print()
print('You are in front of 3 doors in ORANGE,WHITE,GREEN colors .')
print()
print('You have to choose one of the doors to open.')
print()
print('Which door do you want to open?')
door = input('please,enter your choice:')
if door.upper() == 'ORANGE':
    print('Well done! You have opened the right door.you can go to the next level.')
    print()
    print('Welcome to level 2')
    print()
    
elif door.upper() == 'WHITE':
     print('You have opened the second chance door,You can choose the other 2 remaining doors .')
     print()
     print('Which door do you want to open?')
     door = input('please,enter your choice:')
     if door.upper() == 'ORANGE':
         print('Well done! You have opened the right door.you can go to the next level.')
     print()
     print('level 2')
     print()
else:
    print('oups,You have opened the wrong door, the game is over.')
    print()
    print('GAME OVER')
    print()
    print(f'Goodbye {name.upper} Next time will be good!')
# end to milestone
    



