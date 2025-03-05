"""
Author: Brother Hermann

Purpose: My Adventure Game
"""
# Welcome to my adventure game
# for creativity, I added the name of the player in the script 
# I personalize the program
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
    # level 2
    # second scenario = level 2
    print('Welcome to level 2')
    print()
    print('''You are in front of 3 doors in RED,BLUE,YELLOW colors .''')
    print()
    print('You have to choose one of the doors to open.')
    print()
    print('Which door do you want to open?')
    door = input('please,enter your choice:')
    if door.upper() == 'BLUE':
        print('Well done! You have opened the right door.you can go to the next level.')
        print()
        # level 3
        # third scenario = level 3
        print('Welcome to level 3')
        print()
        print('''You are in front of 2 doors in PINK,PURPLE colors .''')
        print()
        print('You have to choose one of the doors to open.')
        print()
        print('Which door do you want to open?')
        door = input('please,enter your choice:')
        if door.upper() == 'PURPLE':
            print('Well done! You have opened the right door.')
            print()
            print(f'Great {name.upper()}, Congratulations! You have won the game.')
            print('You are the winner of the national lottery.')
            print('You have won a trip to the Bahamas.')
            print()
            print(f'Goodbye {name.upper()} See you next time!')
        else:
            print('oups,You have opened the wrong door, the game is over.')
            print()
            print('GAME OVER')
            print()
            print(f'Goodbye {name.upper()} Next time will be good!')
    elif door.upper() == 'YELLOW':
        print('You have opened the second chance door,You can choose the other 2 remaining doors .')
        print()
        print('Which door do you want to open?')
        door = input('please,enter your choice:')
        if door.upper() == 'BLUE':
            print('Well done! You have opened the right door.you can go to the next level.')
            print()
            # return level 3
            # third scenario = level 3
            print('Welcome to level 3')
            print()
            print('''You are in front of 2 doors in PINK,PURPLE colors .''')
            print()
            print('You have to choose one of the doors to open.')
            print()
            print('Which door do you want to open?')
            door = input('please,enter your choice:')
            if door.upper() == 'PURPLE':
                print('Well done! You have opened the right door.')
                print()
                print('Congratulations! You have won the game.')
            else:
                print('GAME OVER')
                print()
                print(f'Goodbye {name.upper()} Next time will be good!')
        else:
            print('GAME OVER')
            print()
            print(f'Goodbye {name.upper()} Next time will be good!')
    else:
        print('GAME OVER')
        print()
        print(f'Goodbye {name.upper()} Next time will be good!')
elif door.upper() == 'WHITE':
    print('You have opened the second chance door,You can choose the other 2 remaining doors .')
    print()
    print('Which door do you want to open?')
    door = input('please,enter your choice:')
    if door.upper() == 'ORANGE':
        print('Well done! You have opened the right door.you can go to the next level.')
        print()
        # level 2
        # second scenario = level 2
        print('Welcome to level 2')
        print()
        print('''You are in front of 3 doors in RED,BLUE,YELLOW colors .''')
        print()
        print('You have to choose one of the doors to open.')
        print()
        print('Which door do you want to open?')
        door = input('please,enter your choice:')
        if door.upper() == 'BLUE':
            print('Well done! You have opened the right door.you can go to the next level.')
            print()
            # level 3
            # third scenario = level 3
            print('Welcome to level 3')
            print()
            print('''You are in front of 2 doors in PINK,PURPLE colors .''')
            print()
            print('You have to choose one of the doors to open.')
            print()
            print('Which door do you want to open?')
            door = input('please,enter your choice:')
            if door.upper() == 'PURPLE':
                print('Well done! You have opened the right door.')
                print()
                print('Congratulations! You have won the game.')
                print()
                print(f'Goodbye {name.upper()} See you next time!')
            else:
                print('GAME OVER')
                print()
                print(f'Goodbye {name.upper()} Next time will be good!')
        elif door.upper() == 'YELLOW':
            print('You have opened the second chance door,You can choose the other 2 remaining doors .')
            print()
            print('Which door do you want to open?')
            door = input('please,enter your choice:')
            if door.upper() == 'BLUE':
                print('Well done! You have opened the right door.you can go to the next level.')
                print()
                # return level 3
                # third scenario = level 3
                print('Welcome to level 3')
                print()
                print('''You are in front of 2 doors in PINK,PURPLE colors .''')
                print()
                print('You have to choose one of the doors to open.')
                print()
                print('Which door do you want to open?')
                door = input('please,enter your choice:')
                if door.upper() == 'PURPLE':
                    print('Well done! You have opened the right door.')
                    print()
                    print('Congratulations! You have won the game.')
                    print()
                    print(f'Goodbye {name.upper()} See you next time!')
                else:
                    print('GAME OVER')
                    print()
                    print(f'Goodbye {name.upper()} Next time will be good!')
            else:
                print('GAME OVER')
                print()
                print(f'Goodbye {name.upper()} Next time will be good!')
        else:
            print('GAME OVER')
            print()
            print(f'Goodbye {name.upper()} Next time will be good!')
    else:
        print('GAME OVER')
        print()
        print(f'Goodbye {name.upper()} Next time will be good!')
else:
    print('GAME OVER')
    print()
    print(f'Goodbye {name.upper()} Next time will be good!')
exit()