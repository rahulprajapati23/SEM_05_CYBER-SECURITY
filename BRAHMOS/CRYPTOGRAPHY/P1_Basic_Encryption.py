
def p1_basic_encryption():
    print("\n--- Practical 1: Basic Encryption/Decryption (Reverse Cipher) ---")
    password = input("Enter password: ")
    
    # Simple Reverse Cipher for demonstration
    ciphertext = password[::-1]
    print(f"Encrypted Password (Ciphertext): {ciphertext}")
    
    decrypted = ciphertext[::-1]
    print(f"Decrypted Password (Original): {decrypted}")

if __name__ == "__main__":
    p1_basic_encryption()
