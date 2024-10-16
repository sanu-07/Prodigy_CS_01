# Caesar Cipher Program
def encrypt(text, shift):
    result = ""
    # Loop through each character in the input text
    for char in text:
        if char.isalpha():  # Check if it's an alphabetic character
            shift_base = 65 if char.isupper() else 97  # Uppercase starts at ASCII 65, lowercase at 97
            # Perform the shift operation and add to the result
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just shifting backwards

# Main program
def main():
    # Input from the user
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
        if choice in ['E', 'D']:
            break
        print("Invalid choice. Please choose E or D.")
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (a number): "))

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

# Run the main function
if __name__ == "__main__":
    main()
