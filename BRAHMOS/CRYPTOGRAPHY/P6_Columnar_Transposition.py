import math

def p6_columnar():
    print("\n--- Practical 6: Columnar Transposition Cipher ---")
    msg = input("Enter message: ").replace(" ", "")
    key = input("Enter keyword: ")
    
    # Encryption
    col = len(key)
    row = int(math.ceil(len(msg) / col))
    fill_null = int((row * col) - len(msg))
    msg_list = list(msg)
    msg_list.extend('_' * fill_null)
    
    matrix = [msg_list[i: i + col] for i in range(0, len(msg_list), col)]
    
    key_seq = sorted([(k, i) for i, k in enumerate(key)])
    cipher = ""
    for k, idx in key_seq:
        for r in range(row):
            cipher += matrix[r][idx]
    
    print(f"Ciphertext: {cipher}")
    
    # Decryption
    idx_map = [0] * col
    for i, (k, original_idx) in enumerate(key_seq):
        idx_map[original_idx] = i 

    dec_matrix = [['' for _ in range(col)] for _ in range(row)]
    curr_idx = 0
    for k, original_idx in key_seq: # Read in column order based on key
        for r in range(row):
            if curr_idx < len(cipher):
                dec_matrix[r][original_idx] = cipher[curr_idx]
                curr_idx += 1
                
    decoded = ""
    for r in range(row):
        decoded += "".join(dec_matrix[r])
    
    print(f"Decrypted (with padding): {decoded}")

if __name__ == "__main__":
    p6_columnar()
