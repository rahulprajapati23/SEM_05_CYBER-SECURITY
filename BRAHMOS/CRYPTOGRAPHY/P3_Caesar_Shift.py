
def p3_caesar_shift():
    print("\n--- Practical 3: Caesar & Shift Cipher ---")
    text = input("Enter plain text message: ")
    
    # Part 1: Classic Caesar (Fixed Shift 3)
    def caesar(t, s):
        res = ""
        for char in t:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                res += chr((ord(char) - ascii_offset + s) % 26 + ascii_offset)
            else:
                res += char
        return res
        
    c_fixed = caesar(text, 3)
    print(f"Classic Caesar (Shift 3) Ciphertext: {c_fixed}")
    print(f"Classic Caesar Decrypted: {caesar(c_fixed, -3)}")
    
    # Part 2: Custom Shift
    try:
        shift_val = int(input("Enter custom shift value (0-25): "))
    except:
        shift_val = 0
        print("Invalid input, defaulting to 0")
        
    c_custom = caesar(text, shift_val)
    print(f"Custom Shift Ciphertext: {c_custom}")
    print(f"Custom Shift Decrypted: {caesar(c_custom, -shift_val)}")
    
    # Part 3: Brute Force
    print("\n-- Brute Force Analysis on Custom Ciphertext --")
    for s in range(1, 26):
        attempt = caesar(c_custom, -s)
        print(f"Shift {s}: {attempt}")
        if attempt == text:
            print(f"-> SUCCESS! Match found at Shift {s}")
            break

if __name__ == "__main__":
    p3_caesar_shift()
