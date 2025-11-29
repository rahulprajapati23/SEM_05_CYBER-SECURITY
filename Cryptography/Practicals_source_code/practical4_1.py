import random
import string

def create_key():
    letters = list(string.ascii_uppercase)
    shuffled_letters = letters.copy()
    random.shuffle(shuffled_letters)
    encrypt_key = {}
    decrypt_key = {}
    for i in range(len(letters)):
        encrypt_key[letters[i]] = shuffled_letters[i]
        decrypt_key[shuffled_letters[i]] = letters[i]
    return encrypt_key, decrypt_key

def encrypt(message, encrypt_key):
    message = message.upper()
    encrypted = ""
    for char in message:
        if char in encrypt_key:
            encrypted += encrypt_key[char]
        else:
            encrypted += char
    return encrypted

def decrypt(message, decrypt_key):
    decrypted = ""
    for char in message:
        if char in decrypt_key:
            decrypted += decrypt_key[char]
        else:
            decrypted += char
    return decrypted

def main():
    encrypt_key, decrypt_key = create_key()
    message = input("Enter a message to encrypt: ")
    encrypted = encrypt(message, encrypt_key)
    print(f"\nEncrypted message: {encrypted}")
    decrypted = decrypt(encrypted, decrypt_key)
    print(f"Decrypted message: {decrypted}")
    print("\nEncryption Key:")
    for letter in string.ascii_uppercase:
        print(f"{letter}", end="  ")
    print("\n")
    for letter in string.ascii_uppercase:
        print(f"{encrypt_key[letter]}", end="  ")

if __name__ == "__main__":
    main()
