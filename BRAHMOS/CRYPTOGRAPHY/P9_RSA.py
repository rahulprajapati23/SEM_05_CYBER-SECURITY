
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 > 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x1 < 0:
        x1 += phi
    return x1

def p9_rsa():
    print("\n--- Practical 9: RSA ---")
    try:
        p = int(input("Enter prime p: "))
        q = int(input("Enter prime q: "))
    except:
        print("Invalid number.")
        return
        
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    
    # 1 < e < phi, gcd(e, phi) = 1
    e = 0
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break
            
    print(f"Selected Public Exponent e: {e}")
    d = mod_inverse(e, phi)
    print(f"Calculated Private Exponent d: {d}")
    
    print(f"Public Key: ({e}, {n})")
    print(f"Private Key: ({d}, {n})")
    
    msg = input("Enter message (letters only for demo): ")
    # Encrypt
    cipher_vals = []
    for char in msg:
        m_val = ord(char)
        c_val = pow(m_val, e, n)
        cipher_vals.append(c_val)
        
    print(f"Ciphertext (Values): {cipher_vals}")
    
    # Decrypt
    dec_msg = ""
    for val in cipher_vals:
        m_val = pow(val, d, n)
        dec_msg += chr(m_val)
        
    print(f"Decrypted Message: {dec_msg}")

if __name__ == "__main__":
    p9_rsa()
