items = []
item = None

print('Please, Enter the items in the shopping list :')
while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        items.append(item)
print()
print('Your shopping list is: ')
for item in items:
    print(item)
print()
print('Your shopping list indexes is: ')
for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')
print()
print('Which item would you like to change?')
i = int(input('Enter the index of new item : '))
print('What is the new item?')
new_item = input('Enter the new item: ')
items[i] = new_item
print()
print('Your shopping list indexes is: ')
for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')
print()








