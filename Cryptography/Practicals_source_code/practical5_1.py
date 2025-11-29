def encrypt(plain_text, key):
    cipher_text = [''] * key
    row = 0
    direction_down = False

    for char in plain_text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        cipher_text[row] += char
        row += 1 if direction_down else -1

    return ''.join(cipher_text)

def decrypt(cipher_text, key):
    rail = [''] * key
    row = 0
    direction_down = None

    for char in cipher_text:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row] += char
        row += 1 if direction_down else -1

    return ''.join(rail)

if __name__ == "__main__":
    text = "HELLORAILFENCECIPHER"
    for key in range(2,5):
        print(f"Key: {key}")
        encrypted = encrypt(text, key)
        print("Encrypted:", encrypted)

        decrypted = decrypt(encrypted, key)
        print("Decrypted:", decrypted)