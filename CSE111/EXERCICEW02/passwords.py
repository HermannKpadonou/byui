"""
Author: Hermann KPADONOU
Purpose: Password Strength
"""



def word_in_file(word, filename,case_sensitive=True):
    """
    Check if a word is in a file.
    
    Parameters:
        word (str): The word to search for.
        filename (str): The name of the file to search in.
        case_sensitive (bool): If True, the search is case-sensitive; otherwise, it is case-insensitive.
    
    Returns:
        bool: True if the word is found, False otherwise.
    """
    with open("wordlist.txt", 'r') as wordlist_file:
        for line in wordlist_file:
            if case_sensitive:
                if word in line.strip():
                    return True
            else:
                if word.lower() in line.strip().lower():
                    return True
                
    return False
    
    with open('toppasswords.text', 'r') as file:
        for line in file:
            if case_sensitive:
                if word in line.strip():
                    return True
            else:
                if word.lower() in line.strip().lower():
                    return True
    return False


    

def word_has_characters(word, character_list):
    """
    Check if a word contains any of the specified characters.
    
    Parameters:
        word (str): The word to check.
        characters (str): A string of characters to search for in the word.
    
    Returns:
        bool: True if the word contains any of the characters, False otherwise.
    """
    #Constants for character type

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

   

def word_complexity(word):
    """
    Calculate the complexity of a word based on its length and character variety.
    
    Parameters:
        word (str): The word to analyze.
    
    Returns:
        int: A complexity score based on the length and variety of characters in the word.
    """
    pass    

def password_strength(password,min_length,strong_length ):
    """
    Determine the strength of a password based on its length, character variety, and presence in a dictionary.
    
    Parameters:
        password (str): The password to evaluate.
        min_length (int): The minimum length for a password to be considered strong.
        strong_length (int): The length above which a password is considered very strong.
    
    Returns:
        str: A string indicating the strength of the password ("weak", "strong", or "very strong").
    """
    pass

def main():
    """
    Main function to execute the password strength evaluation.
    Prompts the user for a password and evaluates its strength.
    """
    # Get a password from the user
    
    
    # Define minimum and strong length criteria
    
    
    # Evaluate the password strength
    
    
    # Display the result
    pass
# Call the main function to start the program
if __name__ == "__main__":
    main()