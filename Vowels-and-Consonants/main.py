#
# Jae Lee Park
# Nov 4, 2024
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Declare local variables
user_str = ""  # Variable to hold the user input string
vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels
v_count = 0  # Variable to hold the vowel count
c_count = 0  # Variable to hold the consonant count

# Main function
def main():
    global user_str  # Access the global variable
    global v_count, c_count  # Access the global variables for counts

    # Get a string from the user
    user_str = input('Enter a string of characters: ')
    
    # Calculate the number of vowels and consonants
    v_count = num_vowels(user_str)
    c_count = num_consonants(user_str)

    # Report the vowels and consonants
    print('That string has', v_count, 'vowels and', c_count, 'consonants.')

# The num_vowels function returns the number of vowels in the string passed as an argument
def num_vowels(s):
    # Initialize an accumulator for vowels
    v_count = 0

    # Count the vowels in s
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1  # Increment vowel count

    # Return the vowel count
    return v_count

# The num_consonants function returns the number of consonants in the string passed as an argument
def num_consonants(s):
    # Initialize an accumulator for consonants
    c_count = 0

    # Count the consonants in s
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1  # Increment consonant count

    # Return the consonant count
    return c_count

# Call the main function
main()