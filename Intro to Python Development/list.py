friends = []

friend = None

while friend != 'end':
    friend = input('Enter the name of a friend: ')
    if friend != 'end':
        friends.append(friend)
print()
print('Your friends are: ')

for friend in friends:
    print(friend)
print()