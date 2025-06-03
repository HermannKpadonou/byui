"""
Author: Hermann KPADONOU
Purpose: Password Strength Checker
Project completion
"""

 #Constants for character type

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

# File names (constants for clarity)
dictionary_file = "wordlist.txt"
top_passwords_file = "toppasswords.txt"

def word_in_file(word, filename,case_sensitive=False):
    """
    Check if a word is in a file.
    
    Parameters:
        word (str): The word to search for.
        filename (str): The name of the file to search in.
        case_sensitive (bool): If True, the search is case-sensitive; otherwise, it is case-insensitive.
    
    Returns:
        bool: True if the word is found, False otherwise.
    """
    
    with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
    return False


def word_has_character(word, character_list):
    """
    Check if a word contains any of the specified characters.
    
    Parameters:
        word (str): The word to check.
        characters (str): A string of characters to search for in the word.
    
    Returns:
        bool: True if the word contains any of the characters, False otherwise.
    """
    for char_in_word in word:
        if char_in_word in character_list:
            return True
    return False

# Check if the word contains any of the specified characters
    

def word_complexity(word):
    """
    Calculate the complexity of a word based on character variety.
    
    Parameters:
        word (str): The word to analyze.
    
    Returns:
        int: A complexity score based on the length and variety of characters in the word.
    """
    complexity = 0
    # Check for character variety
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity  

def password_strength(password,min_length=10,strong_length=16):

     """
    Evaluates password strength based on length.
    Returns a score between 0 and 5 with descriptive feedback messages.

    Parameters:
        password (str): Password to evaluate
        min_strength (int): Minimum length for acceptable password (default: 10)
        max_strength (int): Length considered very strong (default: 16)

    Returns:
        int: Strength score between 0 and 5
    """
    # 1. Check if password is in the dictionary file (case-insensitive)
     if word_in_file(password, dictionary_file, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Check if password is in the top passwords list (case-sensitive)
     if word_in_file(password, top_passwords_file, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Check if password is too short
     if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Check if password is long enough to be considered strong by length
    # "longer than 15 characters" means length >= 16.
    # The strong_length parameter defaults to 16, so len(password) >= strong_length
     if len(password) >= strong_length: # As per prompt "longer than 15 characters"
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5. For remaining cases, strength is based on complexity
     complexity = word_complexity(password)
     strength = 1 + complexity  # Base score of 1 + complexity score

    # Enhancement: Provide more specific feedback for intermediate strengths
     if strength == 2:
        print("Password has low complexity. Try adding numbers, symbols, or uppercase letters.")
     elif strength == 3:
        print("Password has moderate complexity. Consider adding another character type (e.g., symbols if missing).")
     elif strength == 4:
        print("Password has good complexity. Adding one more character type would make it very strong.")
     else:
        print("Password has maximum complexity. Excellent choice!")
    
    # Ensure strength does not exceed 5 (e.g. if base was higher or complexity could go higher)
    # In this specific setup, 1 + 4 = 5, so it's capped correctly by the "long password" rule.
    # However, if complexity was 0 (empty string or no recognized chars), strength would be 1.
    # The "too short" rule usually catches empty strings first.
    # If password is e.g. "          " (10 spaces), complexity is 0, strength is 1. This seems fine.

     return strength

def main():
    """
    Main function to execute the password strength evaluation.
    Prompts the user for a password and evaluates its strength.
    """
    # Get a password from the user
    
    print("Password Strength Checker")
    print("Enter passwords to check their strength (or 'q' to quit)")
    
    while True:
        password = input("Please,Enter a password: ")
        
        if password.lower() == 'q':
            print("Exiting the program.")
            
        
        # Check if the password is in the wordlist or top passwords
        if word_in_file(password, "wordlist.txt") or word_in_file(password, "toppasswords.txt"):
            print("This password is too common. Please choose a different one.")
            continue
        
        # Calculate the complexity of the password
        complexity = word_complexity(password)
        
        # Evaluate the strength of the password
        strength_score = password_strength(password)

        # Display the results
        print(f"Password: {password}")
        print(f"Complexity Score: {complexity}")
        print(f"Strength Score: {strength_score}")

        # Creativity : If the strength is 4 or 5, register the password in a file
        
        if strength_score >= 4:  # main condition for registration
    
            with open("user_file.txt", "at") as user_file: 
                user_file.write(f"{password}\n")
            print(f"Password '{password}' registered successfully.")
        else: 
            print(f"Password strength for '{password}' is below 4, not registered.")
# Call the main function to start the program
if __name__ == "__main__":
    main()

