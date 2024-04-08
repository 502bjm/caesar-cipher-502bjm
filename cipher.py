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

# Get input from the user
plaintext = input("Enter the text to be shifted: ")

# Encrypt the text with a right shift of 5
shift = 5
encrypted_text = caesar_cipher(plaintext, shift)

# Display the output
print("Original text:", plaintext)
print("Shifted text:", encrypted_text)
