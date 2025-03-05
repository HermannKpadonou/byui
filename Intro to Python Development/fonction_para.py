def get_initial(name,force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0,1]
    return initial

first_name= input('please,Enter your first name:')
first_name_intial = get_initial(first_name,False)

surname = input('please,enter your surname:')
surname_initial = get_initial(surname,False)

print(f'Your initials are {first_name_intial}-{surname_initial}')