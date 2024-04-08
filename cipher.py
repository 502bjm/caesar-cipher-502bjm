def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate case (uppercase or lowercase)
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Apply the shift and wrap around if necessary
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

# Define a function to handle encryption/decryption and user interaction
def cipher_interaction():
    while True:
        choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").upper()
        
        if choice == 'Q':
            print("Exiting the program...")
            break
        
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))

        if choice == 'E':
            result = caesar_cipher(text, shift)
            print("Encrypted text:", result)
        elif choice == 'D':
            result = caesar_cipher(text, -shift)  # Use negative shift for decryption
            print("Decrypted text:", result)
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

# Call the function to start the interaction
cipher_interaction()

