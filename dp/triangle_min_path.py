"""
Problem Statement: Triangle Path Minimum Sum
Given a triangle array, find the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index `j` on the current row `i`, you may move 
to either index `j` or index `j + 1` on the next row `i + 1`.
"""

# STEP 1: Pure Recursive Approach
# Time Complexity: O(2^N) | Space Complexity: O(N) where N is the number of rows
def triangle_path(matrix, m=0, n=0):
    # Base case: If we have reached the last row, 
    # the minimum path from this element to the bottom is just the element itself.
    if m==len(matrix)-1:
        return matrix[m][n]
        
    # Option 1: Move down to the same index `n` in the next row `m + 1`
    down_call = triangle_path(matrix, m+1, n)
    
    # Option 2: Move diagonally down to the next index `n + 1` in the next row `m + 1`
    diagonal_call = triangle_path(matrix, m+1, n+1)

    # Return the current element plus the minimum of the two possible paths downwards
    return matrix[m][n] + min(down_call, diagonal_call)


# STEP 2: Top-Down Memoization
# Time Complexity: O(N^2) | Space Complexity: O(N^2)
def triangle_path_memo(matrix, m=0, n=0, cache=None):
    # Initialize the 2D cache explicitly on the first call
    if cache is None:
        cache = [[None for _ in range(len(matrix[i]))] for i in range(len(matrix))]
        
    # Base Case: Reached the last row
    if m==len(matrix)-1:
        return matrix[m][n]
        
    # If the answer is already computed for this state, avoid re-evaluating it
    if cache[m][n] is not None:
        return cache[m][n]
        
    # Calculate the down path
    down_call = triangle_path_memo(matrix, m+1, n, cache)
    
    # Calculate the diagonal path
    diagonal_call = triangle_path_memo(matrix, m+1, n+1, cache)

    # Save the answer to the current state in our cache explicitly before returning
    cache[m][n] = matrix[m][n] + min(down_call, diagonal_call)

    return cache[m][n]


# STEP 3: Tabulation (Bottom-Up)
# Note on 2D Cache Tabulation Initialization:
# Instead of aggressively translating and flipping the base case logic dynamically(like in euler path traversal it goes branch by branch) inside the loops 
# (like tracking `if m == len(matrix)-1` mid-recursion), it is generally much easier in 2D 
# tabulation to statically initialize the entire "base case" row organically before starting.
# 
# (Note: This manual base-case array pre-population can often be replaced/avoided entirely if the 
# base cases merely return simple constants for out-of-bounds metrics—such as returning `0`, 
# `float('inf')`, or `float('-inf')`! In those cases, we can simply initialize an oversized 
# DP array uniformly defaulted to that boundary constant, seamlessly letting the loops absorb those 
# out-of-bounds reads without explicitly manually seeding a base row first.)
#
# Time Complexity: O(N^2) | Space Complexity: O(N^2)
def triangle_path_tab(matrix):
    # Initialize a clean DP cache sized perfectly to match our input matrix
    cache = [[None for _ in range(len(matrix[i]))] for i in range(len(matrix))]
    
    # 1. Translate the Base Case dynamically!
    # Explicitly calculate and fill the entire bottom row of the cache with the last row of the matrix.
    for j in range(len(matrix[len(matrix)-1])):
        cache[len(cache)-1][j] = matrix[len(matrix)-1][j]
        
    # 2. Iterate Bottom-Up explicitly backwards from the second-to-last row up to the top!
    for i in range(len(cache)-2,-1,-1):
        for j in range(len(cache[i])):
            # Read explicitly from our statically calculated cache layer beneath us
            down_call = cache[i+1][j]
            diagonal_call = cache[i+1][j+1]
            
            # Store organically into the DP!
            cache[i][j]= matrix[i][j]+min(down_call,diagonal_call)
            
    # The answer natively flows up to the absolute top of the triangle.
    return cache[0][0]


# STEP 4: Space Optimized Tabulation (Bottom-Up)
# Time Complexity: O(N^2) | Space Complexity: O(N) where N is the length of the last row
def triangle_path_tab_opt(matrix):
    # We only ever look back to the immediately previous row `i + 1` we calculated!
    # Therefore, carrying an entire 2D matrix cache around is an explicit waste of memory.
    # We natively just need a 1D `cache_next` to hold the results of the layer beneath us.
    cache_next = [None for _ in range(len(matrix[len(matrix)-1]))] 
    
    # Pre-populate our 'next' cache statically with the bottom row (our base cases)
    for j in range(len(cache_next)):
        cache_next[j] = matrix[len(matrix)-1][j]
        
    cache_curr = None
    
    # Trace linearly backwards explicitly from the second-to-last row up to the top!
    for i in range(len(matrix)-2,-1,-1):
        # Create an explicitly sized current row
        cache_curr = [None for _ in range(len(matrix[i]))]
        
        for j in range(len(cache_curr)):
            # Both down_call and diagonal_call explicitly pull from the 1D `cache_next` array
            down_call = cache_next[j]
            diagonal_call = cache_next[j+1]
            
            # Formulate the local current node organically!
            cache_curr[j]= matrix[i][j]+min(down_call,diagonal_call)
            
        # Shift the variables explicitly cleanly backwards so the current array becomes the "next" array 
        # for the next higher row. Unpack statically to pass by value.
        cache_next = [*cache_curr]
        
    # Ultimately terminating natively at cache_curr[0]
    return cache_curr[0] if cache_curr else cache_next[0]

print(f"Space Optimized Tabulation result:", triangle_path_tab_opt([
    [1],
    [2,3],
    [3,6,7],
    [8,9,6,10]
]))