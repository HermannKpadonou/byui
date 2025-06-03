"""
Author: Hermann KPADONOU
Purpose: Password Strength Checker
Milestone
"""

# Constants for character types
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

# File names
DICTIONARY_FILE = "wordlist.txt"
TOP_PASSWORDS_FILE = "toppasswords.txt"

def word_in_file(word, filename, case_sensitive=False):
    """
    Check if a word is in a file.
    
    Parameters:
        word (str): The word to search for.
        filename (str): The name of the file to search in.
        case_sensitive (bool): If True, the search is case-sensitive.
    
    Returns:
        bool: True if the word is found, False otherwise.
    """
    pass

def word_has_character(word, character_list):
    """
    Check if a word contains any of the specified characters.
    
    Parameters:
        word (str): The word to check.
        character_list (list): List of characters to search for.
    
    Returns:
        bool: True if the word contains any of the characters, False otherwise.
    """
    pass

def word_complexity(word):
    """
    Calculate the complexity of a word based on character variety.
    
    Parameters:
        word (str): The word to analyze.
    
    Returns:
        int: A complexity score based on character variety.
    """
    pass

def password_strength(password, min_length=10, strong_length=16):
    """
    Evaluates password strength based on length and complexity.
    
    Parameters:
        password (str): Password to evaluate.
        min_length (int): Minimum length for acceptable password.
        strong_length (int): Length considered very strong.
    
    Returns:
        int: Strength score between 0 and 5.
    """
    pass

def main():
    """
    Main function to execute the password strength evaluation.
    """
    print("Password Strength Checker")
    print("Enter passwords to check their strength (or 'q' to quit)")
    
    while True:
        password = input("Please enter a password: ")
        
        if password.lower() == 'q':
            print("Exiting the program.")
            break
        
    
        print(f"You entered: {password}")
        

if __name__ == "__main__":
    main()