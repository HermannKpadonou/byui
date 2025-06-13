
# provinces.py

def main():
    # 1. Read the contents of the file into a simple list.
    provinces_list = read_list("provinces.txt")
    
    # 2. Print the entire original list.
    print("Original list:")
    print(provinces_list)
    print() # Add a blank line for clarity

    # 3. Remove the first element from the list.
    provinces_list.pop(0)

    # 4. Remove the last element from the list.
    provinces_list.pop() # .pop() without an argument removes the last element

    # 5. Replace all occurrences of "AB" with "Alberta".
    # We use a loop to go through and modify the list.
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    print("Modified list:")
    print(provinces_list)
    print() # Add a blank line

    # 6. Count the number of "Alberta" elements and print the result.
    count = provinces_list.count("Alberta")
    print(f"The word 'Alberta' appears {count} times in the modified list.")


def read_list(filename):
    """
    Reads the contents of a text file into a simple list.
    Each line from the file becomes an element in the list.

    Parameter filename: the name of the text file to read.
    Returns: a list of strings.
    """
    # Create an empty list.
    text_list = []
    
    # Open the file in read mode ("rt" = read text).
    with open(filename, "rt") as txt_file:
        # Read the file line by line.
        for line in txt_file:
            # .strip() removes leading and trailing whitespace, including newlines.
            clean_line = line.strip()
            # Add the cleaned line to our list.
            text_list.append(clean_line)
            
    return text_list


# Call the main function to start the program.
if __name__ == "__main__":
    main()