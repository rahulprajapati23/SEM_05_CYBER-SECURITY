def caesar_cipher(text, shift, mode='e'): 
    if mode == 'd': 
        shift = -shift
    processed_text = "" 
    for char in text: 
        if char.isalpha(): 
            shift_amount = shift % 26 
            if char.islower(): 
                start = ord('a') 
                processed_char = chr(start + (ord(char) - start + shift_amount) % 26) 
            else: 
                start = ord('A') 
                processed_char = chr(start + (ord(char) - start + shift_amount) % 26) 
            processed_text += processed_char 
        else: 
            processed_text += char 
    return processed_text 
text = input("Enter the text: ") 
shift = int(input("Enter the shift value: ")) 
mode = input("Enter 'e' to encrypt or 'd' to decrypt: ") 
result = caesar_cipher(text, shift, mode) 
print(f"Result: {result}")
