"""
Problem Statement: Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

# STEP 1: Pure Recursion
# How it works:
# We start at the top-left (0,0) and explore all possible paths to the bottom-right!
# Option 1: We can move "Down" (m + 1)
# Option 2: We can move "Right" (n + 1)
# Base Case 1: If we go out of bounds, we return infinity since it's an invalid path.
# Base Case 2: If we reach the destination at the bottom-right, we return the value of that cell.
# (Bug Fix: Previously, going out of bounds returned 0, making invalid paths falsely optimal. Fixed to return float('inf')!)
# Time Complexity: O(2^(m*n)) | Space Complexity: O(m + n) for recursion stack.
def min_path_sum(matrix, m=0, n=0):
    if m>=len(matrix) or n >= len(matrix[m]):
        return float('inf')
    if m == len(matrix) - 1 and n == len(matrix[0]) - 1:
        return matrix[m][n]
    
    down_call = matrix[m][n] + min_path_sum(matrix, m+1, n)
    right_call = matrix[m][n] + min_path_sum(matrix, m, n+1)
    if m== len(matrix)-1 and n==(len(matrix[0]))-1:
        print(down_call,right_call)
    return min(down_call, right_call)

# STEP 2: Memoization (Top-Down DP)
# How we memoized it:
# 1. We cache the minimum path sum securely in a 2D `cache` dynamically initialized with None.
# 2. Before recursing, we check if the coordinate state (m, n) has organically been calculated already.
# Time Complexity: O(m * n) seamlessly perfectly evaluating each matrix coordinate once! 
# Space Complexity: O(m + n) recursive call stack + O(m * n) DP cache
def min_path_sum_memo(matrix, m=0, n=0, cache=None):
    if cache is None:
        cache = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
    if m>=len(matrix) or n >= len(matrix[m]):
        return float('inf')
    if m == len(matrix) - 1 and n == len(matrix[0]) - 1:
        return matrix[m][n]
        
    if m<len(matrix) and n<len(matrix[0]) and cache[m][n] is not None:
        return cache[m][n]
    
    down_call = matrix[m][n] + min_path_sum_memo(matrix, m+1, n, cache)
    right_call = matrix[m][n] + min_path_sum_memo(matrix, m, n+1, cache)
    cache[m][n] = min(down_call, right_call)
    return cache[m][n]

# STEP 3: Tabulation (Bottom-Up DP)
# How Memoize mapped securely to Tabulation form:
# - Instead of recursing top-down, we explicitly traverse the grid directly backwards from bottom-right to top-left natively!
# - Our base_case mathematically changes from 0 to float('inf') to cleanly punish out-of-bounds paths.
# Time Complexity: O(m * n) iteratively sweeping the matrix perfectly natively.  
# Space Complexity: O(m * n) organically generating the entire DP structurally.
def min_path_sum_tab( matrix):
    cache = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    base_case = float('inf')
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,-1,-1):
            if i == len(matrix)-1 and j == len(matrix[0])-1:
                cache[i][j] = matrix[i][j]
                continue
                
            down_call=None
            right_call=None
            if i==len(matrix)-1:
                down_call=base_case
            else:
                down_call = cache[i+1][j]
            if j==len(matrix[i])-1:
                right_call=base_case
            else:
                right_call=cache[i][j+1]
            cache[i][j]=matrix[i][j]+min(down_call,right_call)
    return cache[0][0]

# STEP 4: Space Optimization
# How did Tabulation get memory optimized?:
# - Notice `cache[i][j]` only purely looks at `cache[i+1][j]` (immediate row below) and `cache[i][j+1]` (current row right).
# - We compress the entire 2D `cache` into uniquely maintaining just two vectors natively: `next_row` and `current_row`.
# Time Complexity: O(M * N) perfectly maintained natively. 
# Space Complexity: Slashed fundamentally from O(M * N) structurally down to strictly O(N)!
def min_path_sum_tab_opt( matrix):
    current_row = [None for _ in range(len(matrix[0]))]
    next_row = [*current_row]
    base_case = float('inf')
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,-1,-1):
            if i == len(matrix)-1 and j == len(matrix[0])-1:
                current_row[j] = matrix[i][j]
                continue
                
            down_call=None
            right_call=None
            if i==len(matrix)-1:
                down_call=base_case
            else:
                down_call = next_row[j]
            if j==len(matrix[i])-1:
                right_call=base_case
            else:
                right_call=current_row[j+1]
            current_row[j]=matrix[i][j]+min(down_call,right_call)
        next_row = [*current_row]
    return current_row[0]   
                
print(f"Minimum Path Sum: {min_path_sum([[5,9,6], 
                                                 [11,5,2]])}")