'''
0/1 Knapsack Problem using Dynamic Programming.
You have a knapsack with capacity W.
You are given n items with weights wt[] and values val[].
You cannot break items (0/1 property).
Maximize the total value in the knapsack.
'''

def knapsack_dp(W, wt, val, n):
    # Create a table to store results of subproblems
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # The result is stored in K[n][W]
    return K[n][W]

# Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"Values: {val}")
print(f"Weights: {wt}")
print(f"Capacity: {W}")
print(f"Maximum Profit (0/1 DP): {knapsack_dp(W, wt, val, n)}")
