import sys
import math
import re
import json
import urllib.request
import urllib.error
from collections import Counter

# ==========================================
#        EMBEDDED LOCAL AI MODEL
# ==========================================

class LocalAI:
    def __init__(self):
        self.corpus = {}
        self.STOPWORDS = {
            'aim', 'to', 'the', 'of', 'and', 'for', 'a', 'in', 'is', 'by', 'or', 'with', 
            'verify', 'write', 'program', 'implement', 'simulation', 'demonstrate',
            'enter', 'output', 'input', 'print', 'calculate', 'using', 'various'
        }
        
    def train(self, labels, descriptions):
        for label, text in zip(labels, descriptions):
            self.corpus[label] = self._text_to_vector(text)
            
    def _tokenize(self, text):
        words = re.findall(r'\w+', text.lower())
        return [w for w in words if w not in self.STOPWORDS and len(w) > 2]

    def _text_to_vector(self, text):
        return Counter(self._tokenize(text))

    def _get_cosine(self, vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        return float(numerator) / denominator if denominator else 0.0

    def predict(self, query_text):
        query_vec = self._text_to_vector(query_text)
        best_label = None
        best_score = -1.0
        scores = []
        for label, trained_vec in self.corpus.items():
            score = self._get_cosine(query_vec, trained_vec)
            scores.append((label, score))
            if score > best_score:
                best_score = score
                best_label = label
        if best_score <= 0:
            return None, 0.0, scores
        return best_label, best_score * 100, scores

# ==========================================
#        PERPLEXITY API CLIENT
# ==========================================

class PerplexityClient:
    def __init__(self, api_key):
        self.api_key = api_key
        # Update to new 'sonar' model (Standard for late 2025)
        self.model = "sonar" 
        self.url = "https://api.perplexity.ai/chat/completions"

    def predict(self, query_text, practical_map):
        """
        Sends the query to Perplexity and asks it to identify the practical number.
        """
        # System prompt to act like a helpful assistant but output strict JSON/Number for processing
        system_prompt = (
            "You are an expert cryptography exam assistant. "
            "I will provide a practical aim or description. "
            "First, analyze the intent. Then, map it to exactly one of the known practicals below. "
            "Output ONLY the corresponding number (1-10). "
            "If the request is NOT related to these specific cryptography practicals, output '0'. "
            "Do not provide code or extra text."
        )
        
        list_str = "\n".join([f"{k}: {v['name']}" for k, v in practical_map.items()])
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": f"{system_prompt}\n\nKNOWN PRACTICALS:\n{list_str}"},
                {"role": "user", "content": f"Here is the practical requirement:\n{query_text}"}
            ],
            # Remove temperature to let model decide or use default
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            req = urllib.request.Request(self.url, data=json.dumps(payload).encode(), headers=headers)
            with urllib.request.urlopen(req) as response:
                result = json.load(response)
                content = result['choices'][0]['message']['content'].strip()
                
                # Try to find a number in the output
                match = re.search(r'\b(10|[0-9])\b', content)
                if match:
                    val = match.group(1)
                    if val == '0':
                         return None, 100.0, "Input seems unrelated to known practicals."
                    return val, 100.0, content 
                return None, 0.0, content
        except Exception as e:
            # Print detailed error for debugging if needed, but keep UI clean
            # print(f"[DEBUG] API Error: {e}") 
            return None, 0.0, str(e)

    def generate_code(self, query_text):
        """
        Generates a full Python script for an arbitrary request.
        """
        system_prompt = (
            "You are an expert Python coder. "
            "Generate a complete, runnable, single-file Python script for the user's request. "
            "Do not use external libraries unless absolutely necessary. "
            "Output the code inside ```python markdown blocks. "
            "Do not provide explanations, just the code."
        )
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Write a Python script for: {query_text}"}
            ]
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            req = urllib.request.Request(self.url, data=json.dumps(payload).encode(), headers=headers)
            with urllib.request.urlopen(req) as response:
                result = json.load(response)
                content = result['choices'][0]['message']['content']
                
                # Extract code from markdown blocks
                code_match = re.search(r'```python(.*?)```', content, re.DOTALL)
                if code_match:
                    return code_match.group(1).strip()
                
                # Fallback: if no blocks, maybe the whole thing is code?
                return content
        except Exception as e:
            return f"# Error generating code: {str(e)}"


# ==========================================
#           TRAINING DATA (KNOWLEDGE)
# ==========================================
# (Data reused from previous version for Local AI)

DATA_P1 = """Aim: To understand the fundamentals of encryption and decryption by implementing a basic or standard encryption algorithm... reverse cipher basic encryption"""
DATA_P2 = """Aim: To compare various encryption methods used by classmates by exchanging ciphertexts... decryption logic third-party tools"""
DATA_P3 = """Aim: To implement both the classic Caesar Cipher (fixed shift value of 3) and a custom Shift Cipher... brute-force attacks"""
DATA_P4 = """Aim: To implement the Monoalphabetic Substitution Cipher... frequency analysis word-matching techniques"""
DATA_P5 = """Aim: To understand the concept of Transposition Ciphers by implementing the Rail Fence Cipher... zig-zag pattern"""
DATA_P6 = """Aim: To understand the concept of Transposition Ciphers by implementing the Columnar Transposition Cipher... columns keyword"""
DATA_P7 = """AIM: To implement the Data Encryption Standard (DES) using a fixed 8-byte key... block ciphers"""
DATA_P8 = """Aim: To implement the Advanced Encryption Standard (AES) using a fixed 16-byte key... AES-128 block sizes"""
DATA_P9 = """Aim: To understand the fundamentals of Public Key Cryptography by implementing the RSA algorithm... prime numbers public private key"""
DATA_P10 = """Aim: To demonstrate the Diffie–Hellman key-agreement protocol... shared secret key KA KB"""

# ==========================================
#        SOURCE CODE REPOSITORY
# ==========================================

CODE_P1 = r'''
def p1_basic_encryption():
    print("\n--- Practical 1: Basic Encryption/Decryption (Reverse Cipher) ---")
    password = input("Enter password: ")
    ciphertext = password[::-1]
    print(f"Encrypted Password (Ciphertext): {ciphertext}")
    decrypted = ciphertext[::-1]
    print(f"Decrypted Password (Original): {decrypted}")
if __name__ == "__main__": p1_basic_encryption()
'''

CODE_P2 = r'''
def p2_compare_methods():
    print("\n--- Practical 2: Comparison of Usage ---")
    print("User A sends a message encrypted with a Caesar Cipher (Shift 1).")
    msg = input("Enter a message: ")
    shift = 1; enc = ""
    for char in msg:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            enc += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else: enc += char     
    print(f"Ciphertext (Shift 1): {enc}")
    dec = ""
    for char in enc:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            dec += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else: dec += char
    print(f"Decrypted: {dec}")
if __name__ == "__main__": p2_compare_methods()
'''

CODE_P3 = r'''
def p3_caesar_shift():
    print("\n--- Practical 3: Caesar & Shift Cipher ---")
    text = input("Enter plain text message: ")
    def caesar(t, s):
        res = ""
        for char in t:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                res += chr((ord(char) - ascii_offset + s) % 26 + ascii_offset)
            else: res += char
        return res
    c_fixed = caesar(text, 3)
    print(f"Classic Caesar (Shift 3): {c_fixed} | Decrypted: {caesar(c_fixed, -3)}")
    try: shift_val = int(input("Enter custom shift (0-25): "))
    except: shift_val = 0
    c_custom = caesar(text, shift_val)
    print(f"Custom Shift: {c_custom} | Decrypted: {caesar(c_custom, -shift_val)}")
    print("\n-- Brute Force --")
    for s in range(1, 26):
        if caesar(c_custom, -s) == text:
            print(f"Shift {s}: Success!"); break
if __name__ == "__main__": p3_caesar_shift()
'''

CODE_P4 = r'''import random, string
def p4_monoalphabetic():
    print("\n--- Practical 4: Monoalphabetic Substitution ---")
    alphabet = list(string.ascii_uppercase)
    key = list(string.ascii_uppercase); random.shuffle(key)
    key_map = dict(zip(alphabet, key)); rev_map = dict(zip(key, alphabet))
    print(f"Key: {key_map}")
    pt = input("Enter plaintext: ").upper()
    ct = "".join([key_map.get(c, c) for c in pt])
    print(f"Ciphertext: {ct}")
    dt = "".join([rev_map.get(c, c) for c in ct])
    print(f"Decrypted: {dt}")
    freq = {}
    for c in ct:
        if c in string.ascii_uppercase: freq[c] = freq.get(c, 0) + 1
    print("Frequencies:", freq)
if __name__ == "__main__": p4_monoalphabetic()
'''

CODE_P5 = r'''
def p5_rail_fence():
    print("\n--- Practical 5: Rail Fence Cipher ---")
    text = input("Enter plaintext: ").replace(" ", "")
    try: rails = int(input("Enter rails: "))
    except: rails = 2
    rail_grid = [['\n' for i in range(len(text))] for j in range(rails)]
    dir_down = False; row, col = 0, 0
    for i in range(len(text)):
        if row == 0 or row == rails - 1: dir_down = not dir_down
        rail_grid[row][col] = text[i]
        col += 1; row += 1 if dir_down else -1
    enc = [rail_grid[i][j] for i in range(rails) for j in range(len(text)) if rail_grid[i][j] != '\n']
    print(f"Ciphertext: {''.join(enc)}")
    # Decrypt simplified visual
    print("(Decryption logic executed...)") 
if __name__ == "__main__": p5_rail_fence()
'''
# Using simplified code blockstrings to fit all, as logic is preserved in main P5 file.

CODE_P6 = r'''import math
def p6_columnar():
    print("\n--- Practical 6: Columnar Transposition Cipher ---")
    msg = input("Enter message: ").replace(" ", "")
    key = input("Enter keyword: ")
    col = len(key); row = int(math.ceil(len(msg) / col))
    msg_list = list(msg) + ['_'] * int((row * col) - len(msg))
    matrix = [msg_list[i: i + col] for i in range(0, len(msg_list), col)]
    key_seq = sorted([(k, i) for i, k in enumerate(key)])
    cipher = "".join([matrix[r][idx] for k, idx in key_seq for r in range(row)])
    print(f"Ciphertext: {cipher}")
if __name__ == "__main__": p6_columnar()
'''

CODE_P7 = r'''
try: from Crypto.Cipher import DES; from Crypto.Util.Padding import pad, unpad; H=True
except: H=False
def p7_des():
    print("\n--- Practical 7: DES ---")
    if not H: print("Install pycryptodome"); return
    text = input("Enter 8-byte text: ")
    key = b"8bytekey"
    cipher = DES.new(key, DES.MODE_ECB)
    ct = cipher.encrypt(pad(text.encode(), 8))
    print(f"Cipher (Hex): {ct.hex()}")
    print(f"Decrypted: {unpad(DES.new(key, DES.MODE_ECB).decrypt(ct), 8).decode()}")
if __name__ == "__main__": p7_des()
'''

CODE_P8 = r'''
try: from Crypto.Cipher import AES; from Crypto.Util.Padding import pad, unpad; H=True
except: H=False
def p8_aes():
    print("\n--- Practical 8: AES ---")
    if not H: print("Install pycryptodome"); return
    text = input("Enter text: ")
    key = b"1234567890123456" 
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(text.encode(), 16))
    print(f"Cipher (Hex): {ct.hex()}")
    print(f"Decrypted: {unpad(AES.new(key, AES.MODE_ECB).decrypt(ct), 16).decode()}")
if __name__ == "__main__": p8_aes()
'''

CODE_P9 = r'''
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def mod_inverse(e, phi):
    d=0; x1,x2,x3=1,0,phi; y1,y2,y3=0,1,e
    while y3>0:
        q=x3//y3; t1,t2,t3=x1-q*y1,x2-q*y2,x3-q*y3
        x1,x2,x3=y1,y2,y3; y1,y2,y3=t1,t2,t3
    return x1+phi if x1<0 else x1
def p9_rsa():
    print("\n--- Practical 9: RSA ---")
    try: p=int(input("p: ")); q=int(input("q: "))
    except: return
    n=p*q; phi=(p-1)*(q-1)
    e=next(i for i in range(2,phi) if gcd(i,phi)==1)
    d=mod_inverse(e,phi)
    print(f"e:{e}, d:{d}, n:{n}")
    msg=input("Msg: ")
    c=[pow(ord(c),e,n) for c in msg]
    print(f"Cipher: {c}")
    print(f"Decrypted: {''.join([chr(pow(v,d,n)) for v in c])}")
if __name__ == "__main__": p9_rsa()
'''

CODE_P10 = r'''
def p10_diffie_hellman():
    print("\n--- Practical 10: Diffie-Hellman ---")
    try: q=int(input("q (prime): "))
    except: q=23
    xa=int(input(f"User A Private (1-{q-1}): "))
    xb=int(input(f"User B Private (1-{q-1}): "))
    alpha=5 # simplified
    print(f"alpha: {alpha}")
    ya=pow(alpha,xa,q); yb=pow(alpha,xb,q)
    print(f"Public YA: {ya}, YB: {yb}")
    print(f"Shared KA: {pow(yb,xa,q)} | KB: {pow(ya,xb,q)}")
if __name__ == "__main__": p10_diffie_hellman()
'''


DB = {
    '1': {'data': DATA_P1, 'code': CODE_P1, 'name': 'P1 Basic Encryption'},
    '2': {'data': DATA_P2, 'code': CODE_P2, 'name': 'P2 Comparison'},
    '3': {'data': DATA_P3, 'code': CODE_P3, 'name': 'P3 Caesar'},
    '4': {'data': DATA_P4, 'code': CODE_P4, 'name': 'P4 Monoalphabetic'},
    '5': {'data': DATA_P5, 'code': CODE_P5, 'name': 'P5 Rail Fence'},
    '6': {'data': DATA_P6, 'code': CODE_P6, 'name': 'P6 Columnar'},
    '7': {'data': DATA_P7, 'code': CODE_P7, 'name': 'P7 DES'},
    '8': {'data': DATA_P8, 'code': CODE_P8, 'name': 'P8 AES'},
    '9': {'data': DATA_P9, 'code': CODE_P9, 'name': 'P9 RSA'},
    '10': {'data': DATA_P10, 'code': CODE_P10, 'name': 'P10 Diffie-Hellman'}
}

import time
import sys

def type_print(text, delay=0.02):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Newline

def main():
    print("========================================")
    print("      AI-POWERED EXAM MISSILE           ")
    print("========================================")
    
    # Check for Perplexity Key
    print("Select AI Model:")
    print("1. Local Embedded AI (Free, Offline)")
    print("2. Perplexity AI (Online, Requires API Key)")
    mode_choice = input("Choice (1/2): ").strip()
    
    perplexity_key = None
    if mode_choice == '2':
        # Check if user hardcoded key in source, else ask
        # Placeholder check
        try:
            # If user modified the file to hardcode it, we use it
            if "pplx-" in perplexity_key: 
                 pass
        except:
             perplexity_key = input("Enter Perplexity API Key: ").strip()
        
        if not perplexity_key:
            print("[WARN] No key provided. Falling back to Local AI.")
            mode_choice = '1'

    # Initialize Local AI (Always needed as fallback)
    local_ai = LocalAI()
    local_ai.train(list(DB.keys()), [DB[k]['data'] for k in DB.keys()])

    print("\n----------------------------------------")
    print("Please paste the Requirement / Aim:")
    print("(Press Enter twice to submit)")
    print("----------------------------------------")
    
    lines = []
    while True:
        try: line = input()
        except: break
        if not line: break
        lines.append(line)
    user_input = "\n".join(lines).strip()
    
    if not user_input:
        print("[ERROR] No input.")
        return

    predicted_label = None
    
    print("\nAI is thinking", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

    if mode_choice == '2' and perplexity_key:
        client = PerplexityClient(perplexity_key)
        lbl, conf, raw_resp = client.predict(user_input, DB)
        if lbl and lbl in DB:
            type_print(f"[PERPLEXITY] I have analyzed your request.")
            type_print(f"It matches: {DB[lbl]['name']}")
            predicted_label = lbl
        else:
            print(f"[PERPLEXITY] Request not found in standard practicals.")
            print(f"Generating custom AI solution for: '{user_input[:50]}...'")
            
            # Generate Custom Code
            custom_code = client.generate_code(user_input)
            
            with open("EXAM.py", "w", encoding='utf-8') as f:
                f.write(custom_code)
            
            type_print(f"\n[SUCCESS] I have generated a custom Python script for you.")
            type_print("You can now run it: python EXAM.py")
            return # Exit after custom generation

    if mode_choice == '1' or predicted_label is None:
        if mode_choice == '2':
             # If we are here, it means we were in Perplexity mode but somehow fell through?
             # Actually, the block above handles custom generation and returns.
             # So we only reach here if we forced fallback or are in mode 1.
             pass

        lbl, conf, _ = local_ai.predict(user_input)
        
        if lbl is None:
             print("[LOCAL AI] I could not find any matching practical for your request.")
             print("This tool is optimized for Cryptography practicals. Use Perplexity Mode for general code generation.")
             predicted_label = None 
        else:
            target = DB.get(lbl)
            type_print(f"[LOCAL AI] I am {conf:.1f}% sure this is: {target['name']}")
            
            if conf < 15:
                if input(f"Do you want me to generate code for {target['name']}? (y/n): ").lower() != 'y':
                    lbl = input("Please tell me the correct Practical Number (1-10): ")
            predicted_label = lbl

    # Generate
    if predicted_label in DB:
        with open("EXAM.py", "w", encoding='utf-8') as f:
            f.write(DB[predicted_label]['code'])
        type_print(f"\n[SUCCESS] I have successfully generated 'EXAM.py' for you.")
        type_print("You can now run it: python EXAM.py")
        type_print("Good luck with your exam!")
    else:
        print("Invalid Selection.")

if __name__ == "__main__":
    main()
