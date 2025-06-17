"""
Random number Progam Demonstrating lists
Author: Hermann KPADONOU help by Sister Sherlene
"""
import random
def append_random_numbers(numbers_list, quantity):

    """
    append quantity random numbers onto the numbers list
    between 0 and 100
    Parameters:
        numbers_list: list of numbers
        quantity: numbers of random numbers to appends
        
        Returns:nothing
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity):
    """
    append quantity random words onto the words list
    Parameters:
        words_list: list of words
        quantity: numbers of random words to appends
        
        Returns:nothing
    """
    words = ["arm","car", "cloud","head","heal","hydrogen","apple", "banana", "cherry","jog","join"]
    for _ in range(quantity):
        random_word = random.choice(words)
        words_list.append(random_word)
def main():

   #Create a list of numbers
   numbers_list = [16.2, 75.1, 52.3]
   print(f"Numbers list :{numbers_list}")

   #append one random number tothe list
   # and print the list
   append_random_numbers(numbers_list,1)
   print(f"Numbers list :{numbers_list}")

   #append three random numbers to the list
   # and print the list
   append_random_numbers(numbers_list,3)
   print(f"Numbers list :{numbers_list}")

   #Create a list of words
   words_list = []
   print(f"Words list :{words_list}")

    #append one random word to the list 
    # and print the list
    append_random_words(words_list, 1)
    print(f"Words list :{words_list}")
   
   #append three random words to the list
   # and print the list
    append_random_words(words_list, 1)
    print(f"Words list :{words_list}")

if __name__ == "__main__":
    main()