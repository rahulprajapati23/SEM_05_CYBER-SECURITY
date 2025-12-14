import sys
import math
import re
import json
import urllib.request
import urllib.error
from collections import Counter
import time

# ==========================================
#        EMBEDDED LOCAL AI MODEL
# ==========================================

class LocalAI:
    def __init__(self):
        self.corpus = {}
        self.STOPWORDS = {
            'aim', 'to', 'the', 'of', 'and', 'for', 'a', 'in', 'is', 'by', 'or', 'with', 
            'verify', 'write', 'program', 'implement', 'simulation', 'demonstrate',
            'enter', 'output', 'input', 'print', 'calculate', 'using', 'various', 'analysis', 'algorithm'
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
        self.model = "sonar" 
        self.url = "https://api.perplexity.ai/chat/completions"

    def predict(self, query_text, practical_map):
        system_prompt = (
            "You are an expert Algorithm Design (AAD) exam assistant. "
            "I will provide a practical aim or description. "
            "First, analyze the intent. Then, map it to exactly one of the known practicals below. "
            "Output ONLY the corresponding key ID (e.g., '1.1', '2.1'). "
            "If the request is NOT related to these specific practicals, output '0'. "
            "Do not provide code or extra text."
        )
        
        list_str = "\n".join([f"{k}: {v['name']}" for k, v in practical_map.items()])
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": f"{system_prompt}\n\nKNOWN PRACTICALS:\n{list_str}"},
                {"role": "user", "content": f"Here is the practical requirement:\n{query_text}"}
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
                content = result['choices'][0]['message']['content'].strip()
                
                # Try to find the specific ID format in the output
                for k in practical_map.keys():
                    if k in content:
                        return k, 100.0, content
                
                if '0' in content:
                     return None, 100.0, "Input seems unrelated to known practicals."
                return None, 0.0, content
        except Exception as e:
            return None, 0.0, str(e)

    def generate_code(self, query_text):
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
                code_match = re.search(r'```python(.*?)```', content, re.DOTALL)
                if code_match:
                    return code_match.group(1).strip()
                return content
        except Exception as e:
            return f"# Error generating code: {str(e)}"


# ==========================================
#           TRAINING DATA (KNOWLEDGE)
# ==========================================

DATA_P1_1 = """Aim: To implement a chef competition scoring system where two chefs are compared on presentation, taste, and hygiene... basics list comparison"""
DATA_P1_2 = """Aim: To find a pair of elements in an array whose sum is closest to zero (Minimum Absolute Sum Pair)... brute force nested loops"""
DATA_P2_1 = """Aim: To compare the step counts of Loop, Equation/Formula, and Recursion methods for calculating the sum of N numbers... complexity analysis plot"""
DATA_P2_2 = """Aim: To compare the step counts of Iterative vs Recursive Fibonacci sequence generation... complexity analysis plot dynamic programming"""
DATA_P3_1 = """Aim: To compare the step counts (TC) of Bubble Sort, Insertion Sort, and Selection Sort... sorting algorithms complexity plot"""
DATA_P4_1 = """Aim: To implement the Coin Change problem using a Greedy algorithm approach to find minimum coins... greedy optimization"""
DATA_P5_1 = """Aim: To implement the 0/1 Knapsack problem using Dynamic Programming (DP)... maximize profit capacity optimization items weights values"""
DATA_P6_1 = """Aim: To implement Matrix Chain Multiplication using Dynamic Programming (DP) to find optimal parenthesization... matrix multiplication cost"""
DATA_P7_1 = """Aim: To implement the Longest Common Subsequence (LCS) problem using Dynamic Programming... string matching sequence"""
DATA_P8_1 = """Aim: To implement the Fractional Knapsack Problem using a Greedy approach... maximize profit capacity ratio sort"""
DATA_P9_1 = """Aim: To implement Huffman Coding for data compression using a greedy approach with a priority queue (heap)... compression encoding decoding tree"""
DATA_P10_1 = """Aim: To implement Dijkstra's Algorithm for finding the shortest paths from a source node to all other nodes in a graph... greedy graph shortest path"""
DATA_P11_1 = """Aim: To implement the Traveling Salesman Problem (TSP) using a Brute Force approach (Permutations)... graph sales path cost"""


# ==========================================
#        SOURCE CODE REPOSITORY
# ==========================================

CODE_P1_1 = r'''
def competition(chef_1, chef_2):
    chef1_point = 0
    chef2_point = 0
    for i in range(0, 3):
        if chef_1[i] > chef_2[i]:
            chef1_point += 1
        elif chef_2[i] > chef_1[i]:
            chef2_point += 1
    return chef1_point, chef2_point

def main():
    print("\n--- 01 Chef Competition ---")
    chef_1 = []
    chef_2 = []
    print("enter first chef's review{1.presentation,2.taste,3.hygiene}")
    for j in range(0, 3):
        chef_1.append(int(input(f"--<{j+1}>-- ")))
    print("enter second chef's review{1.presentation,2.taste,3.hygiene}")
    for j in range(0, 3):
        chef_2.append(int(input(f"--<{j+1}>-- ")))

    chef1_point, chef2_point = competition(chef_1, chef_2)
    print(f"point of chef_1={chef1_point}\npoint of chef_2={chef2_point}")

if __name__ == "__main__": main()
'''

CODE_P1_2 = r'''
def func(arr,n):
    min_num = float('inf')
    main = []
    for i in range(0, n):
        for j in range(i + 1, n):
            num = arr[i] + arr[j]
            abs_val = abs(num)
            if abs_val==min_num:
                main.append([arr[i], arr[j]])
            elif abs_val < min_num:
                main.clear()
                min_num = abs_val
                main = [[arr[i], arr[j]]]
    return main

def main():
    print("\n--- 01 Min Abs Sum Pair ---")
    arr = []
    while True:
        try:
            n_in = input("enter number of elements: ")
            if not n_in: break
            n=int(n_in)
            if n < 2:
                print("minimum 2 element is mandatory.")
            else:
                break
        except: break
    for i in range(0, n):
        arr.append(int(input(f"enter {i+1} element: ")))

    print(f"output: {func(arr,n)}")

if __name__ == "__main__": main()
'''

CODE_P2_1 = r'''
import matplotlib.pyplot as plt
recursion_steps = 0
def sum_loop(n):
    steps = 0
    total = 0
    for i in range(1, n + 1):
        total = total + i
        steps = steps + 1
    return total, steps
def sum_equation(n):
    steps = 1
    total = n * (n + 1) // 2
    return total, steps
def sum_recursive(n):
    global recursion_steps
    recursion_steps = recursion_steps + 1
    if n == 1:
        return 1
    return n + sum_recursive(n-1)

def main():
    print("\n--- 02 Sum Methods Analysis ---")
    n_values=[]
    try:
        N=int(input("enter how many test cases you want:"))
        for i in range(1,N+1):
            n_values.append(int(input("enter the no. of clients:")))
        loop_step_list = []
        equan_steps = []
        recur_steps = []
        print("Clients", "loop_steps", "equation_steps", "recursion_steps")
        for n in n_values:
            result_loop, loop_steps = sum_loop(n)
            result_equation, equation_steps = sum_equation(n)
            global recursion_steps
            recursion_steps = 0
            result_rec = sum_recursive(n)
            loop_step_list.append(loop_steps)
            equan_steps.append(equation_steps)
            recur_steps.append(recursion_steps)
            print(f" {n}     \t{loop_steps}  \t{equation_steps}\t\t{recursion_steps}")
        plt.plot(n_values, loop_step_list, label="Loop", marker='o',color='black')
        plt.plot(n_values, equan_steps, label="equation", marker='o')
        plt.plot(n_values, recur_steps, label="Recursion", marker='+',linestyle='dotted',color='yellow')
        plt.xlabel("N (Number of Clients)")
        plt.ylabel("Step Count")
        plt.title("Comparison of Step Counts for Sum Calculation Methods")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e: print(e)

if __name__ == "__main__": main()
'''

CODE_P2_2 = r'''
import matplotlib.pyplot as plt

def fib_iter(n):
    a, b = 0, 1
    steps = 0
    for month in range(n):
        a, b = b, a + b
        steps += 1
    return a, steps

def fib_recur(n):
    def helper(k):
        if k <= 1:
            return k, 1
        f1, s1 = helper(k - 1)
        f2, s2 = helper(k - 2)
        return f1 + f2, s1 + s2 + 1
    return helper(n)

def plot_steps():
    months = [2, 4, 12, 15, 18, 20] # reduced max for speed
    iter_steps = []
    recur_steps = []
    for m in months:
        _, steps_iter = fib_iter(m)
        _, steps_recur = fib_recur(m)
        iter_steps.append(steps_iter)
        recur_steps.append(steps_recur)
    plt.plot(months, iter_steps, label='Iterative')
    plt.plot(months, recur_steps, label='Recursive', linestyle='--')
    plt.xlabel('Months')
    plt.ylabel('Steps')
    plt.title('Steps Comparison')
    plt.legend()
    plt.show()

def main():
    print("\n--- 02 Fibonacci Analysis ---")
    n = 24
    pairs_iter, steps_iter = fib_iter(n)
    pairs_recur, steps_recur = fib_recur(n)
    print(f"Rabbit pairs after {n} months (Iterative): {pairs_iter}, Steps: {steps_iter}")
    print(f"Rabbit pairs after {n} months (Recursive): {pairs_recur}, Steps: {steps_recur}")
    plot_steps()

if __name__ == "__main__": main()
'''

CODE_P3_1 = r'''
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps += 1  
    return steps

def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        steps += 1  
        while j >= 0 and arr[j] > key:
            steps += 1  
            arr[j + 1] = arr[j]  
            steps += 1
            j -= 1
        arr[j + 1] = key
        steps += 1 
    return steps

def selection_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps += 1 
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        steps += 1 
    return steps

def main():
    print("\n--- 03 Sorting Analysis ---")
    sizes = [10, 50, 100, 150, 200]
    b_steps = []
    i_steps = []
    s_steps = []
    for size in sizes:
        data = []
        for k in range(size):
            data.append(random.randint(1, 500)) 
        print(f"data{size}:{data}")
        b_steps.append(bubble_sort(data.copy()))
        i_steps.append(insertion_sort(data.copy()))
        s_steps.append(selection_sort(data.copy()))

    plt.plot(sizes, b_steps, label="Bubble Sort", marker='o')
    plt.plot(sizes, i_steps, label="Insertion Sort", marker='o')
    plt.plot(sizes, s_steps, label="Selection Sort", marker='o')
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Steps (operations)")
    plt.title("Sorting Algorithm Comparison (Step Count)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__": main()
'''

CODE_P4_1 = r'''
import random as rd

def coin_counter(coins, tests):
    coins.sort(reverse=True)
    counts = []
    for i in range(0, len(tests)):
        min_count = float("inf")
        for start in range(len(coins)):
            temp_count = 0
            total = 0
            for j in range(start, len(coins)):
                temp_coin = coins[j]
                while tests[i] > total:
                    total += temp_coin
                    temp_count += 1
                if total > tests[i]:
                    total -= temp_coin
                    temp_count -= 1
            if total == tests[i] and temp_count < min_count:
                min_count = temp_count
        print(f"minimum number of coin for {tests[i]} is {min_count}")
        counts.append(min_count)
    return counts

def main():
    print("\n--- 04 Coin Change Greedy ---")
    coins = []
    try:
        num_coin = int(input("enter number of coins you have:"))
        for k in range(0, num_coin):
                coins.append(int(input(f"enter {k+1} coin:")))
        num = int(input("enter number of test_cases you want:"))
        choice = int(input("<0> take random element \n<1> enter elements manualy \n0 or 1:"))
        tests = []
        if choice == 0:
            for i in range(0, num):
                tests.append(rd.randint(1, 100))
            print(f"list:{tests}")
            coin_counter(coins, tests)
        elif choice == 1:
            for i in range(0, num):
                tests.append(int(input(f"enter {i+1} element:")))
            print(f"list:{tests}")
            coin_counter(coins, tests)
        else:
            print("invalid choice :(")
    except Exception as e: print(e)
    print("thank you:)")

if __name__ == "__main__": main()
'''

CODE_P5_1 = r'''
def knapsack_dp(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

def main():
    print("\n--- 05 0/1 Knapsack DP ---")
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(f"Values: {val}")
    print(f"Weights: {wt}")
    print(f"Capacity: {W}")
    print(f"Maximum Profit (0/1 DP): {knapsack_dp(W, wt, val, n)}")

if __name__ == "__main__": main()
'''

CODE_P6_1 = r'''
def matrix_chain_order(p):
    n = len(p) - 1 
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        m.append(row)
    s = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        s.append(row)
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s
def min_multi(s, i, j):
    if i == j:
        return f"A{i+1}"
    else:
        left = min_multi(s, i, s[i][j])
        right = min_multi(s, s[i][j]+1, j)
        return f"({left} x {right})"
def main():
    print("\n--- 06 Matrix Chain Multiplication ---")
    dimensions = [5, 10, 3, 12, 5, 50, 6]
    m, s = matrix_chain_order(dimensions)
    min_mult = m[0][len(dimensions)-2]
    min_req = min_multi(s, 0, len(dimensions)-2)
    print("Dimensions:", dimensions)
    print("Minimum number of multiplications:", min_mult)
    print("Optimal parenthesization:", min_req)

if __name__ == "__main__": main()
'''

CODE_P7_1 = r'''
def lcs(P, Q):
    m, n = len(P), len(Q)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if P[i-1] == Q[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs_seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if P[i-1] == Q[j-1]:
            lcs_seq.append(P[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    lcs_seq.reverse()
    return lcs_seq
def main():
    print("\n--- 07 Longest Common Subsequence ---")
    P = ['M', 'N', 'O', 'M']
    Q = ['M', 'L', 'N', 'O', 'M']
    result = lcs(P, Q)
    print(f"P: {P}")
    print(f"Q: {Q}")
    print("Longest Common Subsequence:", result)

if __name__ == "__main__": main()
'''

CODE_P8_1 = r'''
def fractional_knapsack(p, w, W):
    items = [(p[i], w[i], p[i]/w[i]) for i in range(len(p))]
    items.sort(key=lambda x: x[2], reverse=True)
    total_profit = 0
    fractions = []
    for profit, weight, ratio in items:
        if W == 0:
            break
        if weight <= W:
            total_profit += profit
            fractions.append(1)
            W -= weight
        else:
            frac = W / weight
            total_profit += profit * frac
            fractions.append(frac)
            W = 0 
    print("Fractions taken:", fractions)
    print("Total Profit:", total_profit)

def main():
    print("\n--- 08 Fractional Knapsack (Greedy) ---")
    p = [280, 100, 120, 120]
    w = [40, 10, 20, 24]
    W = 60
    fractional_knapsack(p, w, W)

if __name__ == "__main__": main()
'''

CODE_P9_1 = r'''
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
def main():
    print("\n--- 09 Huffman Coding ---")
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

if __name__ == "__main__": main()
'''

CODE_P10_1 = r'''
def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        visited[u] = True
        for v in range(n):
            if graph[u][v] != float('inf') and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    return dist
def main():
    print("\n--- 10 Dijkstra Algorithm ---")
    nodes = ["A", "B", "C", "D", "E"]
    graph = [
        [0, 20, 30, float('inf'), float('inf')],
        [float('inf'), 0, float('inf'), 15, float('inf')],
        [float('inf'), float('inf'), 0, float('inf'), 25],
        [float('inf'), float('inf'), float('inf'), 0, 10],
        [float('inf'), float('inf'), float('inf'), float('inf'), 0]
    ]
    start_node = "A"
    start_index = nodes.index(start_node)
    distances = dijkstra(graph, start_index)
    print("Source → Destination → Cost")
    for i, d in enumerate(distances):
        print(f"{start_node} → {nodes[i]} = {d}")

if __name__ == "__main__": main()
'''

CODE_P11_1 = r'''
from itertools import permutations
INF = float('inf')
def main():
    print("\n--- 11 TSP Brute Force ---")
    cost = [
        [INF, 20, 30, 10, 11],
        [15, INF, 16, 4, 2],
        [3, 5, INF, 2, 4],
        [19, 6, 18, INF, 3],
        [16, 4, 7, 16, INF]
    ]
    n = len(cost)
    cities = range(n)
    min_cost = INF
    best_path = None
    start = 0 
    for perm in permutations([i for i in cities if i != start]):
        path = [start] + list(perm) + [start]
        total = 0
        valid = True
        for i in range(len(path) - 1):
            c = cost[path[i]][path[i+1]]
            if c == INF:
                valid = False
                break
            total += c
        if valid and total < min_cost:
            min_cost = total
            best_path = path

    print("Minimum Path")
    for i in range(len(best_path) - 1):
        print(f"{best_path[i] + 1} – {best_path[i+1] + 1} = {cost[best_path[i]][best_path[i+1]]}")
    print(f"\nMinimum cost: {min_cost}")
    print("Path Taken:", " - ".join(str(x+1) for x in best_path))

if __name__ == "__main__": main()
'''

DB = {
    '1.1': {'data': DATA_P1_1, 'code': CODE_P1_1, 'name': 'P1.1 Chef Competition'},
    '1.2': {'data': DATA_P1_2, 'code': CODE_P1_2, 'name': 'P1.2 Min Abs Sum Pair'},
    '2.1': {'data': DATA_P2_1, 'code': CODE_P2_1, 'name': 'P2.1 Sum Methods Analysis'},
    '2.2': {'data': DATA_P2_2, 'code': CODE_P2_2, 'name': 'P2.2 Fibonacci Analysis'},
    '3.1': {'data': DATA_P3_1, 'code': CODE_P3_1, 'name': 'P3.1 Sorting Analysis'},
    '4.1': {'data': DATA_P4_1, 'code': CODE_P4_1, 'name': 'P4.1 Coin Change Greedy'},
    '5.1': {'data': DATA_P5_1, 'code': CODE_P5_1, 'name': 'P5.1 0/1 Knapsack DP'},
    '6.1': {'data': DATA_P6_1, 'code': CODE_P6_1, 'name': 'P6.1 Matrix Chain Mult'},
    '7.1': {'data': DATA_P7_1, 'code': CODE_P7_1, 'name': 'P7.1 LCS DP'},
    '8.1': {'data': DATA_P8_1, 'code': CODE_P8_1, 'name': 'P8.1 Fractional Knapsack'},
    '9.1': {'data': DATA_P9_1, 'code': CODE_P9_1, 'name': 'P9.1 Huffman Coding'},
    '10.1': {'data': DATA_P10_1, 'code': CODE_P10_1, 'name': 'P10.1 Dijkstra'},
    '11.1': {'data': DATA_P11_1, 'code': CODE_P11_1, 'name': 'P11.1 TSP Brute Force'}
}

def type_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print("========================================")
    print("      AAD EXAM MISSILE (ALGO-BOT)       ")
    print("========================================")
    
    print("Select AI Model:")
    print("1. Local Embedded AI (Free, Offline)")
    print("2. Perplexity AI (Online, Requires API Key)")
    mode_choice = input("Choice (1/2): ").strip()
    
    perplexity_key = None
    if mode_choice == '2':
        perplexity_key = input("Enter Perplexity API Key: ").strip()
        if not perplexity_key:
            print("[WARN] No key provided. Falling back to Local AI.")
            mode_choice = '1'

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
            type_print(f"[PERPLEXITY] Match found: {DB[lbl]['name']}")
            predicted_label = lbl
        else:
            print(f"[PERPLEXITY] Standard match not found. Generating custom solution...")
            custom_code = client.generate_code(user_input)
            with open("AAD_EXAM_GEN.py", "w", encoding='utf-8') as f:
                f.write(custom_code)
            type_print(f"\n[SUCCESS] Generated custom script: 'AAD_EXAM_GEN.py'")
            return 

    if mode_choice == '1' or predicted_label is None:
        lbl, conf, _ = local_ai.predict(user_input)
        if lbl is None:
            print("[LOCAL AI] No matching practical found.")
        else:
            target = DB.get(lbl)
            type_print(f"[LOCAL AI] I am {conf:.1f}% sure this is: {target['name']}")
            if conf < 15:
                if input(f"Confirm generation? (y/n): ").lower() != 'y':
                    lbl = input("Enter ID manually (e.g. 1.1): ")
            predicted_label = lbl

    if predicted_label in DB:
        with open("AAD_EXAM.py", "w", encoding='utf-8') as f:
            f.write(DB[predicted_label]['code'])
        type_print(f"\n[SUCCESS] Generated 'AAD_EXAM.py' with code for {DB[predicted_label]['name']}")
        type_print("Run it with: python AAD_EXAM.py")
    else:
        print("Selection cancelled or invalid.")

if __name__ == "__main__":
    main()
