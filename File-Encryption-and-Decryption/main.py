#
# Jae Lee Park
# Nov 12, 2024
# File Encryption and Decryption Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Define a dictionary of codes for encryption
    codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '&', 'c': '1', 
        'D': '*', 'd': '2', 'E': '(', 'e': '3', 'F': ')', 'f': '4',
        'G': '-', 'g': '5', 'H': '_', 'h': '6', 'I': '+', 'i': '7',
        'J': '=', 'j': '8', 'K': '{', 'k': '}', 'L': '[', 'l': ']',
        'M': '|', 'm': ':', 'N': ';', 'n': '"', 'O': '<', 'o': '>',
        'P': ',', 'p': '.', 'Q': '/', 'q': '?', 'R': '!', 'r': '`',
        'S': '~', 's': '^', 'T': '$', 't': '€', 'U': '£', 'u': '¥',
        'V': '¢', 'v': '©', 'W': '®', 'w': '™', 'X': '§', 'x': 'µ',
        'Y': '¶', 'y': '÷', 'Z': '±', 'z': '∞'
    }
    
    # Reverse the dictionary for decryption
    reverse_codes = {value: key for key, value in codes.items()}

    # Ask user if they want to encrypt or decrypt
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? ").strip().lower()
    
    if choice == 'e':
        # Encrypt the file
        with open('text.txt', 'r') as infile:
            content = infile.read()

        encrypted_content = ''
        for char in content:
            encrypted_content += codes.get(char, char)  # Encrypt letters, leave others as-is

        with open('encrypted.txt', 'w') as outfile:
            outfile.write(encrypted_content)

        print("Encryption complete. Encrypted content written to 'encrypted.txt'.")

    elif choice == 'd':
        # Decrypt the file
        with open('encrypted.txt', 'r') as infile:
            encrypted_content = infile.read()

        decrypted_content = ''
        for char in encrypted_content:
            decrypted_content += reverse_codes.get(char, char)  # Decrypt symbols, leave others as-is

        print("Decrypted content:")
        print(decrypted_content)
    
    else:
        print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")

main()