
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def primitive_root(q):
    # A simple checker for primitive root (not efficient for huge numbers but fine for labs)
    def power(x, y, p):
        res = 1
        x = x % p
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

    s = set()
    if gcd(2, q) != 1: return -1 # Simple check
    
    phi = q - 1
    # Find prime factors of phi to check potential roots
    factors = set()
    temp = phi
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)

    for r in range(2, q):
        flag = False
        for p in factors:
            if power(r, phi // p, q) == 1:
                flag = True
                break
        if not flag:
            return r
    return -1

def p10_diffie_hellman():
    print("\n--- Practical 10: Diffie-Hellman Key Exchange ---")
    # q is prime, alpha is primitive root
    # For demo, user enters or we pick small ones
    try:
        q = int(input("Enter a prime number q: "))
    except:
        q = 23
        print(f"Invalid input, using q={q}")

    alpha = primitive_root(q)
    if alpha == -1:
        print(f"Could not check primitive root easily for {q}, defaulting alpha=5")
        alpha = 5
    else:
        print(f"Calculated primitive root alpha: {alpha}")
        
    # User A
    xa = int(input(f"User A: Enter private key XA (1 <= XA <= {q-1}): "))
    ya = pow(alpha, xa, q)
    print(f"User A Public Key YA: {ya}")
    
    # User B
    xb = int(input(f"User B: Enter private key XB (1 <= XB <= {q-1}): "))
    yb = pow(alpha, xb, q)
    print(f"User B Public Key YB: {yb}")
    
    # Exchange happens...
    print("Exchanging keys...")
    
    # Calculate Shared Keys
    ka = pow(yb, xa, q)
    kb = pow(ya, xb, q)
    
    print(f"User A Shared Secret KA: {ka}")
    print(f"User B Shared Secret KB: {kb}")
    
    if ka == kb:
        print("Success! Keys match.")
    else:
        print("Error: Keys do not match.")

if __name__ == "__main__":
    p10_diffie_hellman()
