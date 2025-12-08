import random
import string

def p4_monoalphabetic():
    print("\n--- Practical 4: Monoalphabetic Substitution ---")
    alphabet = list(string.ascii_uppercase)
    key = list(string.ascii_uppercase)
    random.shuffle(key)
    key_map = dict(zip(alphabet, key))
    rev_map = dict(zip(key, alphabet))
    
    print(f"Generated Key Map: {key_map}")
    
    pt = input("Enter plaintext: ").upper()
    ct = "".join([key_map.get(c, c) for c in pt])
    print(f"Ciphertext: {ct}")
    
    dt = "".join([rev_map.get(c, c) for c in ct])
    print(f"Decrypted: {dt}")
    
    print("\n-- Frequency Analysis Simulation --")
    freq = {}
    for c in ct:
        if c in string.ascii_uppercase:
            freq[c] = freq.get(c, 0) + 1
    print("Letter Frequencies in Ciphertext:", freq)
    print("In a real attack, we would map these to standard English frequencies (E, T, A, O...).")

if __name__ == "__main__":
    p4_monoalphabetic()
