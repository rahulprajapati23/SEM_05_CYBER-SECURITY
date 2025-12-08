
# Try imports for AES
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    HAS_CRYPTO_LIB = True
except ImportError:
    HAS_CRYPTO_LIB = False

def p8_aes():
    print("\n--- Practical 8: AES (Advanced Encryption Standard) ---")
    if not HAS_CRYPTO_LIB:
        print("Error: 'pycryptodome' library not found. Install it via 'pip install pycryptodome' to run this practical.")
        return

    text = input("Enter plaintext: ")
    # Fixed 16 byte key
    key_str = "1234567890123456" 
    key = key_str.encode('utf-8')
    
    cipher = AES.new(key, AES.MODE_ECB)
    input_bytes = text.encode('utf-8')
    input_padded = pad(input_bytes, 16)
    
    ct_bytes = cipher.encrypt(input_padded)
    print(f"Ciphertext (Hex): {ct_bytes.hex()}")
    
    # Decrypt
    dec_cipher = AES.new(key, AES.MODE_ECB)
    pt_bytes = unpad(dec_cipher.decrypt(ct_bytes), 16)
    print(f"Decrypted: {pt_bytes.decode('utf-8')}")

if __name__ == "__main__":
    p8_aes()
