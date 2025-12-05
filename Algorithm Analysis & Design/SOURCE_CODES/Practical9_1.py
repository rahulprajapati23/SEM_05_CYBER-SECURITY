import heapq

def make_node(freq, order, char=None, left=None, right=None):
    return (freq, order, char, left, right)

def build_huffman(chars_freq):
    heap = []
    order = 0

    for ch, f in chars_freq.items():
        heapq.heappush(heap, make_node(f, order, ch))
        order += 1

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        f = a[0] + b[0]
        merged = make_node(f, order, None, a, b)
        order += 1

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root):
    codes = {}

    def dfs(node, prefix):
        freq, order, char, left, right = node

        if char is not None:
            codes[char] = prefix or "0"
            return
        
        dfs(left, prefix + "0")
        dfs(right, prefix + "1")

    dfs(root, "")
    return codes


def encode(text, codes):
    return "".join(codes[ch] for ch in text)


def decode(bits, root):
    decoded = ""
    node = root

    for b in bits:
        freq, order, char, left, right = node

        node = left if b == "0" else right
        f, o, c, l, r = node

        if c is not None:
            decoded += c
            node = root

    return decoded

chars_freq = {'A':0.5, 'B':0.35, 'C':0.5, 'D':0.1, 'E':0.4, '-':0.2}

root = build_huffman(chars_freq)
codes = generate_codes(root)

print("Generated Huffman Codes →", codes)

print("\n--- Encoding Section ---")
text1 = "CAD-BE"
print("Given Text :", text1)
print("Encoded As :", encode(text1, codes))

print("\n--- Decoding Section ---")
text2 = "0011011100011100"
print("Bitstream  :", text2)
print("Decoded As :", decode(text2, root))
