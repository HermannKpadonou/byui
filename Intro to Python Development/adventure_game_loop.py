# Welcome to my adventure game

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

# Define a list of color lists for each level
color = [['ORANGE','WHITE','GREEN'],['RED','BLUE','YELLOW'],['PINK','PURPLE']]

# Initialize a variable to store the current level
level = 1

# Initialize a variable to store the game status
game_over = False

# Use a while loop to repeat the game until game_over is True
while not game_over:
# Get the current color list based on the level
   current_color : color[level - 1]
# Print the current color list
print(f'You are in front of {len(current_color)} doors in {", ".join(current_color)} colors at level {level}.')
print()
print('You have to choose one of the doors to open.')
print()
print('Which door do you want to open?')
door = input('please,enter your choice: ')
# Use a for loop to iterate over the current color list
for i in range(len(current_color)):
# Check if the choice matches the color at index i
    if door.upper() == current_color[i]:
# If i is 0, then it is the right door
        if i == 0:
           print('Well done! You have opened the right door.you can go to the next level.')
           print()
# Increase the level by 1
level += 1
# Check if the level is greater than the length of the color list, which means the end of the game
if level > len(color):
    print('Congratulations! You have won the game.')
    print()
    print(f'Goodbye {name.upper()}! See you next time!')
# Set game_over to True to exit the loop
game_over = True
else:
# Otherwise, continue to the next level
print(f'Welcome to level {level}')
print()
# If i is 1, then it is the second chance door
elif i == 1:
print('You have opened the second chance door,You can choose the other remaining doors .')
print()
print('Which door do you want to open?')
door = input('please,enter your choice: ')
# Check if the second choice is the first color, which is the right door
if door.upper() == current_color[0]:
    print('Well done! You have opened the right door.you can go to the next level.')
print()
# Increase the level by 1
level += 1
# Check if the level is greater than the length of the color list, which means the end of the game
if level > len(color):
   print('Congratulations! You have won the game.')
print()
print(f'Goodbye {name.upper()}! See you next time!')
# Set game_over to True to exit t
