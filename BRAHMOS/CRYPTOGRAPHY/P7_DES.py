
# Try imports for DES
try:
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import pad, unpad
    HAS_CRYPTO_LIB = True
except ImportError:
    HAS_CRYPTO_LIB = False

def p7_des():
    print("\n--- Practical 7: DES (Data Encryption Standard) ---")
    if not HAS_CRYPTO_LIB:
        print("Error: 'pycryptodome' library not found. Install it via 'pip install pycryptodome' to run this practical.")
        print("Fallback explanation: DES uses a 64-bit block size and 56-bit key.")
        return

    text = input("Enter 8-byte plaintext (or less, will be padded): ")
    key_str = "8bytekey" # Fixed 8 byte key
    key = key_str.encode('utf-8')
    
    cipher = DES.new(key, DES.MODE_ECB) # Using ECB as per requirement "without modes of operations" implied simplicity, but library requires a mode. ECB is simplest/direct.
    input_bytes = text.encode('utf-8')
    input_padded = pad(input_bytes, 8) 
    
    ct_bytes = cipher.encrypt(input_padded)
    print(f"Ciphertext (Hex): {ct_bytes.hex()}")
    
    # Decrypt
    dec_cipher = DES.new(key, DES.MODE_ECB)
    pt_bytes = unpad(dec_cipher.decrypt(ct_bytes), 8)
    print(f"Decrypted: {pt_bytes.decode('utf-8')}")

if __name__ == "__main__":
    p7_des()
