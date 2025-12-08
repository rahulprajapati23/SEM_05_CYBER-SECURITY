
def p2_compare_methods():
    print("\n--- Practical 2: Comparison of Usage ---")
    print("This practical is a simulation of exchanging ciphers.")
    print("Scenario: User A sends a message encrypted with a Caesar Cipher (Shift 1).")
    
    msg = input("Enter a message to 'send' to a classmate: ")
    shift = 1
    enc = ""
    for char in msg:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            enc += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            enc += char
            
    print(f"Your Ciphertext (Shift 1): {enc}")
    print("Attempting to decrypt using logic...")
    
    # Decrypt
    dec = ""
    for char in enc:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            dec += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            dec += char
    
    print(f"Decrypted: {dec}")
    print("Conclusion: Simple shifts are easy to break but good for basics.")

if __name__ == "__main__":
    p2_compare_methods()
