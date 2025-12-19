# Cryptography Practicals - Python Pseudocode & Syntax Explanation

This document contains Python code for 10 cryptography practicals. Each line is annotated with a comment explaining the syntax or logic used.

---

## Practical 1: Basic Encryption (Reverse Cipher)

```python
def p1_basic_encryption():                                      # Define a function named 'p1_basic_encryption'
    print("\n--- Practical 1: Basic Encryption ---")            # Print the header text to the console
    password = input("Enter password: ")                        # Prompt user for input and store it in variable 'password'
    
    # Simple Reverse Cipher
    ciphertext = password[::-1]                                 # Reverse the string 'password' using slicing [start:end:step] and assign to 'ciphertext'
    print(f"Encrypted Password (Ciphertext): {ciphertext}")      # Print formatted string displaying the encrypted text
    
    decrypted = ciphertext[::-1]                                # Reverse 'ciphertext' again to get back original text and assign to 'decrypted'
    print(f"Decrypted Password (Original): {decrypted}")        # Print the decrypted (original) text

if __name__ == "__main__":                                      # Check if script is running directly (not imported)
    p1_basic_encryption()                                       # Call the main function
```

---

## Practical 2: Comparison of Methods (Shift Cipher Simulation)

```python
def p2_compare_methods():                                       # Define function 'p2_compare_methods'
    print("\n--- Practical 2: Comparison of Usage ---")         # Print header
    # ... (Print simulation description lines) ...
    
    msg = input("Enter a message: ")                            # Get user input for message
    shift = 1                                                   # Set shift variable to integer 1
    enc = ""                                                    # Initialize empty string 'enc' for result
    
    for char in msg:                                            # Loop through each character 'char' in string 'msg'
        if char.isalpha():                                      # Check if character is a letter
            ascii_offset = 65 if char.isupper() else 97         # Set base ASCII value: 65 for uppercase, 97 for lowercase
            # logic: Convert char to ASCII, subtract base, add shift, mod 26 (wrap around), add base back, convert to char
            enc += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset) 
        else:                                                   # If character is not a letter (e.g., space, number)
            enc += char                                         # Append it unchanged
            
    print(f"Your Ciphertext (Shift 1): {enc}")                  # Print encrypted string
    
    # Decrypt Logic
    dec = ""                                                    # Initialize empty string 'dec'
    for char in enc:                                            # Loop through encrypted text
        if char.isalpha():                                      # Check if letter
            ascii_offset = 65 if char.isupper() else 97         # Determine case base value
            # logic: Same as encrypt but subtract shift
            dec += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:                                                   # Non-letter characters
            dec += char                                         # Keep unchanged
    
    print(f"Decrypted: {dec}")                                  # Print decrypted result

if __name__ == "__main__":                                      # Standard boilerplate to run script
    p2_compare_methods()                                        # Invoke function
```

---

## Practical 3: Caesar & Shift Cipher

```python
def p3_caesar_shift():                                          # Define function for Practical 3
    print("\n--- Practical 3: Caesar & Shift Cipher ---")       # Print title
    text = input("Enter plain text message: ")                  # Capture user input
    
    # Inner function for Caesar Logic
    def caesar(t, s):                                           # Define helper function 'caesar' taking text 't' and shift 's'
        res = ""                                                # Initialize result string
        for char in t:                                          # Iterate over characters
            if char.isalpha():                                  # Process only letters
                ascii_offset = 65 if char.isupper() else 97     # Handle case sensitivity
                # Apply shift formula: C = (P + s) mod 26
                res += chr((ord(char) - ascii_offset + s) % 26 + ascii_offset)
            else:
                res += char                                     # constant for non-letters
        return res                                              # Return the processed string
        
    # Fixed Shift Execution
    c_fixed = caesar(text, 3)                                   # Call caesar function with shift 3
    print(f"Classic Caesar (Shift 3): {c_fixed}")               # Show result
    
    # Custom Shift Execution
    try:                                                        # Start error handling block
        shift_val = int(input("Enter shift (0-25): "))          # Convert input string to integer
    except:                                                     # Catch errors (like non-integer input)
        shift_val = 0                                           # Fallback default
        
    c_custom = caesar(text, shift_val)                          # Encrypt with custom shift
    print(f"Custom Shift Ciphertext: {c_custom}")               # Print custom result
    
    # Brute Force Analysis
    print("\n-- Brute Force Analysis --")                       # Print section header
    for s in range(1, 26):                                      # Loop 's' from 1 to 25
        attempt = caesar(c_custom, -s)                          # Decrypt using negative shift '-s'
        print(f"Shift {s}: {attempt}")                          # Print attempt
        if attempt == text:                                     # Check if attempt matches original text
            print(f"-> Match found at Shift {s}")               # Announce success
            break                                               # Exit loop early

if __name__ == "__main__":                                      # Entry point check
    p3_caesar_shift()                                           # Run practical
```

---

## Practical 4: Monoalphabetic Substitution

```python
import random                                                   # Import random module for shuffling
import string                                                   # Import string module for alphabet constants

def p4_monoalphabetic():                                        # Define function
    print("\n--- Practical 4: Monoalphabetic ---")              # Print Header
    alphabet = list(string.ascii_uppercase)                     # Create list ['A', 'B', ..., 'Z']
    key = list(string.ascii_uppercase)                          # Create copy of alphabet list for key
    random.shuffle(key)                                         # Randomly reorder the 'key' list in-place
    
    # Mapping
    key_map = dict(zip(alphabet, key))                          # Zip creates pairs (A, Rand1)... dict makes it a map
    rev_map = dict(zip(key, alphabet))                          # Create reverse map for decryption
    
    pt = input("Enter plaintext: ").upper()                     # Get input and convert to uppercase
    
    # Encryption using list comprehension
    # logic: For each char 'c', get mapped value from key_map, or keep 'c' if not found
    ct = "".join([key_map.get(c, c) for c in pt])               
    print(f"Ciphertext: {ct}")                                  # Output ciphertext
    
    # Decryption
    dt = "".join([rev_map.get(c, c) for c in ct])               # Map back using reverse map
    print(f"Decrypted: {dt}")                                   # Output decrypted text
    
    # Frequency Analysis
    freq = {}                                                   # Initialize empty dictionary
    for c in ct:                                                # Loop through ciphertext characters
        if c in string.ascii_uppercase:                         # Count only letters
            freq[c] = freq.get(c, 0) + 1                        # Increment count: get current count (default 0) + 1
    print("Frequencies:", freq)                                 # Print freq dictionary

if __name__ == "__main__":
    p4_monoalphabetic()
```

---

## Practical 5: Rail Fence Cipher

```python
def p5_rail_fence():
    print("\n--- Practical 5: Rail Fence Cipher ---")
    text = input("Enter plaintext: ").replace(" ", "")          # Remove spaces from input
    rails = int(input("Enter number of rails: "))               # Get integer input for rails
    
    # --- Encryption ---
    # Create 2D list (matrix) filled with newlines '\n'
    rail_grid = [['\n' for i in range(len(text))] for j in range(rails)]
    
    dir_down = False                                            # Boolean flag for direction (zigzag)
    row, col = 0, 0                                             # Initialize indices
    
    for i in range(len(text)):                                  # Iterate through each char of text
        if row == 0 or row == rails - 1:                        # If at top or bottom rail...
            dir_down = not dir_down                             # ...reverse direction
            
        rail_grid[row][col] = text[i]                           # Place character in grid
        col += 1                                                # Move to next column
        row += 1 if dir_down else -1                            # Move row down or up based on flag
        
    # Extract ciphertext
    enc = []                                                    # List to hold chars
    for i in range(rails):                                      # Iterate rows
        for j in range(len(text)):                              # Iterate columns
            if rail_grid[i][j] != '\n':                         # If cell is not empty
                enc.append(rail_grid[i][j])                     # Add to result
    print(f"Ciphertext: {''.join(enc)}")                        # Join list and print
    
    # --- Decryption logic omitted for brevity ---

if __name__ == "__main__":
    p5_rail_fence()
```

---

## Practical 6: Columnar Transposition

```python
import math                                                     # Import math for ceiling function

def p6_columnar():
    print("\n--- Practical 6: Columnar Transposition ---")
    msg = input("Enter message: ").replace(" ", "")             # Clean input
    key = input("Enter keyword: ")                              # Input Keyword (determines column order)
    
    # Setup Matrix Dimensions
    col = len(key)                                              # Columns = length of key
    row = int(math.ceil(len(msg) / col))                        # Rows = length of message / columns (rounded up)
    fill_null = int((row * col) - len(msg))                     # Calculate padding needed
    
    msg_list = list(msg)                                        # Convert message string to list
    msg_list.extend('_' * fill_null)                            # Append padding characters ('_')
    
    # Create Matrix (List of Lists)
    # logic: Slice msg_list into chunks of size 'col'
    matrix = [msg_list[i: i + col] for i in range(0, len(msg_list), col)]
    
    # Determine Column Order
    # logic: Pair key char with index, e.g., [('Z',0), ('A',1)], then sort by char -> [('A',1), ('Z',0)]
    key_seq = sorted([(k, i) for i, k in enumerate(key)])
    
    # Read Columns
    cipher = ""
    for k, idx in key_seq:                                      # Iterate through sorted columns
        for r in range(row):                                    # Iterate down rows
            cipher += matrix[r][idx]                            # Append char at [row][target_col_index]
            
    print(f"Ciphertext: {cipher}")                              # Print result

if __name__ == "__main__":
    p6_columnar()
```

---

## Practical 7: DES (Data Encryption Standard)

```python
# Try importing external crypto library
try:                                                            
    from Crypto.Cipher import DES                               # Import DES class
    from Crypto.Util.Padding import pad, unpad                  # Import padding utilities
    HAS_CRYPTO_LIB = True                                       # Set flag if success
except ImportError:
    HAS_CRYPTO_LIB = False                                      # Set flag if failed
    
def p7_des():
    if not HAS_CRYPTO_LIB:                                      # Check dependency
        print("Error: 'pycryptodome' library needed.")          # Warn user
        return

    text = input("Enter 8-byte plaintext: ")                    # Input text
    key = b"8bytekey"                                           # Define key as bytes (must be 8 bytes for DES)
    
    # Encryption
    cipher = DES.new(key, DES.MODE_ECB)                         # Create DES object in ECB mode
    input_bytes = text.encode('utf-8')                          # Convert text to bytes
    input_padded = pad(input_bytes, 8)                          # Pad bytes to multiple of 8
    
    ct_bytes = cipher.encrypt(input_padded)                     # Encrypt padded data
    print(f"Ciphertext (Hex): {ct_bytes.hex()}")                # Print as hex string
    
    # Decryption
    dec_cipher = DES.new(key, DES.MODE_ECB)                     # Create new cipher object for decrypt
    pt_bytes = unpad(dec_cipher.decrypt(ct_bytes), 8)           # Decrypt and remove padding
    print(f"Decrypted: {pt_bytes.decode('utf-8')}")             # Decode bytes back to string

if __name__ == "__main__":
    p7_des()
```

---

## Practical 8: AES (Advanced Encryption Standard)

```python
try:
    from Crypto.Cipher import AES                               # Import AES
    from Crypto.Util.Padding import pad, unpad
    HAS_CRYPTO_LIB = True
except ImportError:
    HAS_CRYPTO_LIB = False

def p8_aes():
    if not HAS_CRYPTO_LIB:
        return
        
    text = input("Enter plaintext: ")                           # Input
    key = b"1234567890123456"                                   # Key must be 16, 24, or 32 bytes for AES
    
    # Encryption
    cipher = AES.new(key, AES.MODE_ECB)                         # Initialize AES in ECB mode
    input_bytes = text.encode('utf-8')                          # Encode
    input_padded = pad(input_bytes, 16)                         # Pad to block size (16 for AES)
    
    ct_bytes = cipher.encrypt(input_padded)                     # Encrypt
    print(f"Ciphertext (Hex): {ct_bytes.hex()}")
    
    # Decryption
    dec_cipher = AES.new(key, AES.MODE_ECB)                     # Re-init cipher
    pt_bytes = unpad(dec_cipher.decrypt(ct_bytes), 16)          # Decrypt & Unpad
    print(f"Decrypted: {pt_bytes.decode('utf-8')}")             # Decode

if __name__ == "__main__":
    p8_aes()
```

---

## Practical 9: RSA

```python
def gcd(a, b):                                                  # Helper: value Greatest Common Divisor
    while b:                                                    # Euclidean algorithm loop
        a, b = b, a % b
    return a

def mod_inverse(e, phi):                                        # Helper: Extended Euclidean for Modular Inverse
    # ... (Standard algorithm to find d such that d*e = 1 mod phi) ...
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 > 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x1 < 0: x1 += phi
    return x1

def p9_rsa():
    print("\n--- Practical 9: RSA ---")
    p = int(input("Enter prime p: "))                           # Input Prime 1
    q = int(input("Enter prime q: "))                           # Input Prime 2
    
    n = p * q                                                   # Calculate modulus
    phi = (p - 1) * (q - 1)                                     # Calculate Euler's totient
    
    # Calculate Public Exponent 'e'
    e = 0
    for i in range(2, phi):                                     # Iterate to find coprime to phi
        if gcd(i, phi) == 1:
            e = i
            break
            
    # Calculate Private Exponent 'd'
    d = mod_inverse(e, phi)                                     # d is modular inverse of e mod phi
    
    print(f"Public Key: ({e}, {n})")                            # Display keys
    print(f"Private Key: ({d}, {n})")
    
    msg = input("Enter message: ")
    
    # Encryption: C = M^e mod n
    cipher_vals = []
    for char in msg:                                            # Process each char
        m_val = ord(char)                                       # Convert char to integer
        c_val = pow(m_val, e, n)                                # Python's modular exponentiation pow(base, exp, mod)
        cipher_vals.append(c_val)                               # Store block
    print(f"Ciphertext: {cipher_vals}")
    
    # Decryption: M = C^d mod n
    dec_msg = ""
    for val in cipher_vals:
        m_val = pow(val, d, n)                                  # Decrypt integer
        dec_msg += chr(m_val)                                   # Convert back to char
    print(f"Decrypted: {dec_msg}")

if __name__ == "__main__":
    p9_rsa()
```

---

## Practical 10: Diffie-Hellman Key Exchange

```python
def p10_diffie_hellman():
    print("\n--- Practical 10: Diffie-Hellman ---")
    q = int(input("Enter prime number q: "))                    # Shared Prime
    alpha = int(input("Enter primitive root alpha: "))          # Shared Base (Primitive Root)
    
    # User A Key Gen
    xa = int(input(f"User A Private Key XA: "))                 # Private Key A
    ya = pow(alpha, xa, q)                                      # Public Key A = alpha^XA mod q
    print(f"User A Public Key YA: {ya}")
    
    # User B Key Gen
    xb = int(input(f"User B Private Key XB: "))                 # Private Key B
    yb = pow(alpha, xb, q)                                      # Public Key B = alpha^XB mod q
    print(f"User B Public Key YB: {yb}")
    
    print("Exchanging keys...")                                 # Simulation of exchange
    
    # Secret Calculation
    # User A computes: (Public Key B)^XA mod q
    ka = pow(yb, xa, q)
    
    # User B computes: (Public Key A)^XB mod q
    kb = pow(ya, xb, q)
    
    print(f"User A Secret: {ka}")
    print(f"User B Secret: {kb}")
    
    if ka == kb:                                                # Verify secrets match
        print("Success! Shared secrets match.")
    else:
        print("Error: Keys mismatch.")

if __name__ == "__main__":
    p10_diffie_hellman()
```
