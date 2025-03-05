first_name = 'Hermann'
last_name = 'KPADONOU'
# ouput = 'Hello, ' + first_name + ' ' + last_name
# ouput = 'Hello, {} {}' .format(first_name, last_name)
ouput = 'Hello, {1} {0}' .format(first_name, last_name)
# Only available in Python 3
#ouput = f'Hello, {first_name} {last_name}'
print(ouput)