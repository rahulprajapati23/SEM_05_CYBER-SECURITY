


def encrypt(plain_text, keyword):
    columns = [""] * len(keyword)
    for i, char in enumerate(plain_text):
        columns[i % len(keyword)] += char
    sorted_keyword = sorted((char, i) for i, char in enumerate(keyword))
    cipher_text = "".join(columns[i] for char, i in sorted_keyword)
    return cipher_text


def decrypt(cipher_text, keyword):
    num_full_rows = len(cipher_text) // len(keyword)
    num_short_cols = len(cipher_text) % len(keyword)

    col_lengths = [
        num_full_rows + (1 if i < num_short_cols else 0) for i in range(len(keyword))
    ]

    sorted_keyword = sorted((char, i) for i, char in enumerate(keyword))

    columns = [""] * len(keyword)

    index = 0
    for char, i in sorted_keyword:
        columns[i] = cipher_text[index : index + col_lengths[i]]
        index += col_lengths[i]

    plain_text = ""
    for row in range(num_full_rows + (1 if num_short_cols > 0 else 0)):
        for col in range(len(keyword)):
            if row < len(columns[col]):
                plain_text += columns[col][row]

    return plain_text

if __name__ == "__main__":
    text = "HELLOTRANSPOSITIONCIPHER"
    keyword = "KEYWORD"

    print(f"Keyword: {keyword}")
    encrypted = encrypt(text, keyword)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, keyword)
    print("Decrypted:", decrypted)
    keywords = ["KEY", "WORD", "LONGERKEY"]
    for kw in keywords:
        print(f"\nKeyword: {kw}")
        encrypted = encrypt(text, kw)
        print("Encrypted:", encrypted)

        decrypted = decrypt(encrypted, kw)
        print("Decrypted:", decrypted)
    text_with_padding = "HELLOTRANSPOSITIONCIPHE"
    keyword = "PADDING"
    print(f"\nKeyword: {keyword} with padding")
    encrypted = encrypt(text_with_padding, keyword)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, keyword)
    print("Decrypted:", decrypted)
