"""
Author: Brother Hermann

Purpose: Grade Calculator Program
"""
#Consider the following example:
print ('Welcome to the adventure game!')
print ('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
item = input('please,enter your choice:')
if item.lower() == 'match':
    print ('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?')
    action = input('please,enter your choice:')
elif item.lower() == 'flashlight':
    print ('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
    action = input('please,enter your choice:')    