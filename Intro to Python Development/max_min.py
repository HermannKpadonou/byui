people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 99
youngest_name = ''

for person_line in people:
    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])
    if age < youngest_age:
        youngest_age = age
        youngest_name  = name
print(f'The age of youngest person is : {youngest_age}')        
print(f'The youngest person is : {youngest_name}')
print('Thank you')