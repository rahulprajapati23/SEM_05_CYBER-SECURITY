def encrypt_caesar(text):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - ascii_offset + 3) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result


def decrypt_caesar(text):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - ascii_offset - 3) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result


def encrypt_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result


def decrypt_shift(text, shift):
    return encrypt_shift(text, -shift)


def brute_force(ciphertext, original_text):
    print("\nBrute Force Analysis:")
    print("\nTest Cases:")
    print(f"Original Text: {original_text}")
    print(f"Ciphertext: { ciphertext}")
    print("\nTrying different shift values:")

    for shift in range(1, 26):
        decrypted = encrypt_shift(ciphertext, -shift)
        print(f"Testing... by Shift Value: {shift}: {decrypted}")
        if decrypted == original_text:
            print(f"\nSuccess! Found correct shift value: {shift}")
            break
    else:
        print("\nNo matching shift value found")


def main():
    plain_text = input("Enter the text to encrypt: ")
    shift_value = int(input("Enter shift value (0-25) for custom shift cipher: "))

    shift_value = shift_value % 26

    print("\n=== Classic Caesar Cipher (Shift = 3) ===")
    caesar_encrypted = encrypt_caesar(plain_text)
    print(f"Encrypted: {caesar_encrypted}")
    caesar_decrypted = decrypt_caesar(caesar_encrypted)
    print(f"Decrypted: {caesar_decrypted}")

    print(f"\n=== Custom Shift Cipher (shift = {shift_value}) ===")
    shift_encrypted = encrypt_shift(plain_text, shift_value)
    print(f"Encrypted : {shift_encrypted}")
    shift_decrypted = decrypt_shift(shift_encrypted, shift_value)
    print(f"Decrypted: {shift_decrypted}")

    brute_force(shift_encrypted, plain_text)


if __name__ == "__main__":
    main()
