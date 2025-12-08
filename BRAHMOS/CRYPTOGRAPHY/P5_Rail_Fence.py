
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def p5_rail_fence():
    print("\n--- Practical 5: Rail Fence Cipher ---")
    text = input("Enter plaintext: ").replace(" ", "")
    rails = get_int_input("Enter number of rails: ")
    
    # Encryption
    rail_grid = [['\n' for i in range(len(text))] for j in range(rails)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        rail_grid[row][col] = text[i]
        col += 1
        row += 1 if dir_down else -1
        
    enc = []
    for i in range(rails):
        for j in range(len(text)):
            if rail_grid[i][j] != '\n':
                enc.append(rail_grid[i][j])
    ciphertext = "".join(enc)
    print(f"Ciphertext: {ciphertext}")
    
    # Decryption
    rail_grid = [['\n' for i in range(len(ciphertext))] for j in range(rails)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        rail_grid[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1
        
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail_grid[i][j] == '*' and index < len(ciphertext):
                rail_grid[i][j] = ciphertext[index]
                index += 1
                
    res = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        if rail_grid[row][col] != '\n':
            res.append(rail_grid[row][col])
            col += 1
        row += 1 if dir_down else -1
    print(f"Decrypted: {''.join(res)}")

if __name__ == "__main__":
    p5_rail_fence()
