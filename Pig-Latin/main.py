#
# Jae Lee Park
# Nov 6, 2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
#
# Declare local variables
sentence = ""    
pig_latin_sentence = ""  

# Main function
def main():
    global sentence  
    global pig_latin_sentence  

    # Get a sentence from the user
    sentence = input("Enter a sentence to convert to Pig Latin: ")

    # Convert the sentence to Pig Latin
    pig_latin_sentence = convert_to_pig_latin(sentence)

    # Display the Pig Latin sentence
    print("Pig Latin:", pig_latin_sentence)

# Function to convert each word in a sentence to Pig Latin
def convert_to_pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []  

    # Convert each word to Pig Latin
    for word in words:
        if len(word) > 1:
            pig_latin_word = word[1:] + word[0] + "ay"  
        else:
            pig_latin_word = word + "ay"  
        
        pig_latin_words.append(pig_latin_word.upper())  

    # Join all the Pig Latin words into a single string
    return " ".join(pig_latin_words)

# Call the main function
main()