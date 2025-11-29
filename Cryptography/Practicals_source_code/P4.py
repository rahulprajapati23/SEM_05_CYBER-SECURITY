import random
import string

def create_key():
    # Get all uppercase letters
    letters = list(string.ascii_uppercase)
    
    # Create a shuffled version of the alphabet
    shuffled_letters = letters.copy()
    random.shuffle(shuffled_letters)
    
    # Create the encryption and decryption dictionaries
    encrypt_key = {}
    decrypt_key = {}
    
    # Create the key mappings
    for i in range(len(letters)):
        encrypt_key[letters[i]] = shuffled_letters[i]
        decrypt_key[shuffled_letters[i]] = letters[i]
        
    return encrypt_key, decrypt_key

def encrypt(message, encrypt_key):
    # Convert message to uppercase
    message = message.upper()
    
    # Create encrypted message
    encrypted = ""
    
    # Go through each character in the message
    for char in message:
        # If it's a letter, encrypt it
        if char in encrypt_key:
            encrypted += encrypt_key[char]
        # If it's not a letter, keep it as is
        else:
            encrypted += char
            
    return encrypted

def decrypt(message, decrypt_key):
    # Create decrypted message
    decrypted = ""
    
    # Go through each character in the message
    for char in message:
        # If it's a letter, decrypt it
        if char in decrypt_key:
            decrypted += decrypt_key[char]
        # If it's not a letter, keep it as is
        else:
            decrypted += char
            
    return decrypted

def main():
    # Create encryption and decryption keys
    encrypt_key, decrypt_key = create_key()
    
    # Get message from user
    message = input("Enter a message to encrypt: ")
    
    # Encrypt the message
    encrypted = encrypt(message, encrypt_key)
    print(f"\nEncrypted message: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt(encrypted, decrypt_key)
    print(f"Decrypted message: {decrypted}")
    
    # Show the encryption key
    print("\nEncryption Key:")
    for letter in string.ascii_uppercase:
        print(f"{letter}", end="  ")
    print("\n")
    for letter in string.ascii_uppercase:
        print(f"{encrypt_key[letter]}", end="  ")
    

if __name__ == "__main__":
    main()
