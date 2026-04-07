"""
Problem Statement: Unique Grid Paths
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

(Note: In this specific implementation, `m` and `n` represent the 
exact zero-indexed coordinates of the target destination, so we traverse 
dynamically backwards from (m,n) safely down to the start at (0,0)!).
"""

# STEP 1: Pure Recursion
# How it works:
# We start at the target destination (m, n) and explore the grid perfectly backwards!
# Option 1: We could have come from the "Left" (n - 1)
# Option 2: We could have come from "Up" (m - 1)
# Base Case 1: If we safely hit (0,0), we found exactly 1 valid distinct path!
# Base Case 2: If our coordinates drop below 0, we went out of bounds (0 paths).
# Time Complexity: O(2^(m*n)) | Space Complexity: O(m + n) for recursion stack.
def unique_grid_paths(m, n):
    if m == 0 and n == 0:
        return 1
    if m < 0 or n < 0:
        return 0
        
    left_move_paths = unique_grid_paths(m, n-1)
    up_move_paths = unique_grid_paths(m-1, n)
    
    return left_move_paths + up_move_paths


# STEP 2: Memoization (Top-Down DP)
# How we memoized it:
# 1. State natively changes strictly based on `m` and `n`.
# 2. We build a 2D `dp_array` initialized gracefully with None to cache previous coordinate sums.
# Time Complexity: O(m * n) seamlessly perfectly evaluating each matrix coordinate once! 
# Space Complexity: O(m-1 + n-1) recursive call stack + O(m * n) DP Array
def unique_grid_paths_memo(m, n, dp_array=None):
    # Initialize DP array spanning [m+1] by [n+1] mathematically
    if dp_array is None:
        dp_array = [[None for _ in range(n+1)] for _ in range(m+1)]
    
    # Base Cases
    if m == 0 and n == 0:
        return 1
    if m < 0 or n < 0:
        return 0
    
    # Check if securely cached before recursing explicitly
    if dp_array[m][n] is not None:
        return dp_array[m][n]
        
    # (Bug Fix: Changed the recursion to call `unique_grid_paths_memo` and precisely pass the `dp_array`! 
    # Calling the raw recursive function here previously ignored memoization completely!).
    left_move_paths = unique_grid_paths_memo(m, n-1, dp_array)
    up_move_paths = unique_grid_paths_memo(m-1, n, dp_array)
    
    # Cache accurately before cleanly returning!
    dp_array[m][n] = left_move_paths + up_move_paths
    return dp_array[m][n]


# STEP 3: Tabulation (Bottom-Up DP)
# How Memoize mapped securely to Tabulation form:
# - Recursion evaluated deeply top-down from (m,n) down to (0,0).
# - Tabulation safely iterates completely Bottom-Up, running from row 0 to m strictly natively!
# - Base case `dp_array[0][0] = 1` is explicitly set up sequentially before exactly starting!
# Time Complexity: O(m * n) iteratively sweeping the matrix perfectly natively.  
# Space Complexity: O(m * n) organically generating the entire DP structurally.
def unique_grid_paths_tab(m, n):
    dp_array = [[None for _ in range(n+1)] for _ in range(m+1)]
    
    # Directly embed the Base Case explicitly natively
    dp_array[0][0] = 1
    
    # Iterating cleanly predictably scanning across the dynamic coordinates
    for i in range(0, m+1):
        for j in range(0, n+1):
            if dp_array[i][j] is None:
                # Safely bounds-check our "Left" and "Up" values exactly like in recursion iteratively
                up_val = dp_array[i-1][j] if i > 0 else 0
                left_val = dp_array[i][j-1] if j > 0 else 0
                
                dp_array[i][j] = up_val + left_val
                
    # Our inherently maximal path aggregate identically rests mathematically explicitly natively securely at [m][n]
    return dp_array[m][n]
# STEP 4: Space Optimization
# How did Tabulation get memory optimized?:
# - In a 2D matrix DP, notice how functionally `dp_array[row][col]` ONLY ever logically looks "Up" (`row-1`) and "Left" (`col-1`).
# - It explicitly NEVER looks at `row - 2` or earlier!
# - Therefore, storing the entire dynamically sized M x N matrix is a total waste of memory. We only ever need to hold:
#   1. The `prev_row` (acting securely as the native "Up" values)
#   2. The `curr_row` (being freshly calculated iteratively safely utilizing its own "Left" values)
# - At the end of natively parsing an entire row, we simply cleanly copy `curr_row` deeply into `prev_row` and securely clear `curr_row` dynamically for the next iteration!
# Time Complexity: O(M * N) perfectly maintained natively. 
# Space Complexity: Slashed fundamentally from O(M * N) structurally down to strictly O(N)!
def unique_grid_paths_tab_opt(m, n):
    prev_row = [0 for _ in range(n+1)]
    
    # Base Case embedded: Column 0 of every row logically dynamically defaults to 1 
    curr_row = [1 if i==0 else None for i in range(n+1)]

    for i in range(m+1):
        for j in range(n+1):
            
            # If it's not dynamically the Base Case natively, we cleanly calculate: "Up" + "Left"
            if curr_row[j] is None:
                # `prev_row[j]` acts perfectly exactly identical mathematically to `dp_array[i-1][j]`
                up_val = prev_row[j]
                left_val = curr_row[j-1] if j > 0 else 0
                
                curr_row[j] = up_val + left_val
                
        # Space Optimization Roll: Shift variables explicitly securely natively for the next matrix row iteration smoothly
        prev_row = [*curr_row]
        curr_row = [None for _ in range(n+1)]
        
    return prev_row[n]

print(f"Total Unique Paths (Matrix Output): {unique_grid_paths_tab_opt(2, 2)}")