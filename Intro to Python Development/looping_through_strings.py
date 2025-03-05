first_name = "MEDEMAKOU"
for letter in first_name:
    print(f"The letter is: {letter}")
    first_name = "Brigham"

fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter) # outputs a 'g' on the screen
word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")