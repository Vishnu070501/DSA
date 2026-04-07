"""
Problem Statement: Maximum Sum of Non-Adjacent Elements (House Robber)
Given an array of integers, find the maximum sum of a subsequence such that 
no two elements in the subsequence are adjacent in the original array.
"""
#when question comes try all possible ways, get me minimum possible or maximum problem or count all possible ways then understand it is a recursion,get me the best way or the worst way
#how to understand dp is if it is a recursion problem and in the recursive calls you see calls for a particular number being repeated in the euler's path then we can memoize
#recursion shortcut(while drawing the tree for euler)
# 1.try to represent a problem in terms of Index
# 2.do all possible things at that index 
# 3.if it is count question it add all results and count, if min get the minimum of the ways, or max get the max of the ways
def non_adjacent_max(array, subseq_indices, index):
    if index == len(array):
        return sum([array[i] for i in subseq_indices])
    element_added_max_sum = None
    max_sum = float('-inf')
    if len(subseq_indices) ==0 or subseq_indices[len(subseq_indices)-1] != index-1:
        subseq_indices.append(index)
        element_added_max_sum = non_adjacent_max( array, subseq_indices, index+1)
        subseq_indices.pop()
    element_non_added_max_sum = non_adjacent_max( array, subseq_indices, index+1)
    max_sum = max(element_non_added_max_sum, element_added_max_sum if element_added_max_sum is not None else float('-inf'))
    return max_sum
print(f"Original unmemoizable output: {non_adjacent_max([2,1,4,9], [],0)}")

"""When to use 'Path Trackers' and 'Accumulators' vs 'Return Values' in Recursion:

1. Passing Path Trackers & Accumulators Down the Tree:
   Carrying an array (representing the path) or an accumulator variable (like `current_sum`, 
   `current_max`, or `current_min`) down the recursion tree (in the Euler Path) is useful 
   when you need to build up state to process or side-effect exactly at the leaf nodes. For example:
   - Printing every single valid subsequence or path you selected.
   - Finding all possible combinations / permutations recursively.
   - Calculating an aggregate on the way down, and then printing/returning the fully 
     accumulated sum/max/min directly at the base case when the path tracker is ready(this involves carrying another variable down the tree(current_sum/max/min)).Then the sum/min/max can be returned at the end.
   
   In these scenarios, you generally build the state on the way down (pre-order computation),
   and process it natively at the base case before backtracking.

   HOWEVER, this completely destroys Memoization efficiency! If you pass `current_sum` 
   down into the recursive calls, your DP "State" is now defined by both `index` AND `current_sum`. 
   Since `current_sum` can hold thousands of wildly different unique values along different 
   paths, your number of distinct states balloons exponentially.

2. Using Return Values (Required for DP):
   If you only need an aggregate result (like "maximum sum"), you should NEVER pass the 
   accumulator down the tree. Instead, you should calculate the result on the way BACK UP 
   the tree (post-order computation).
   - Let the base case return a baseline integer safely.
   - Let the parent nodes take those returned integers, apply `max()` or `min()`,  or sum() or any other 
     operation depending on the problem, and organically return the aggregated result up to their parent.
   
This "Return Value" approach elegantly replaces path/accumulator variables, removing the history 
from the arguments. This collapses your distinct States (down to simply just `index`) 
and allows DP Memoization to operate flawlessly in O(N) time.

-------------------------------------------------------------------------------------
Why this specific function CANNOT be efficiently memoized:
1. Dynamic Programming / Memoization requires storing the answer for a specific "State" to avoid recalculating it. 
2. In your `non_adjacent_max` above, the State is determined by `index` and the ENTIRE `subseq_indices` array history.
3. Because the history of what you chose in the past is carried around, the number of distinct states becomes O(2^N). 
4. To elegantly memoize this problem, we need to restructure the base recursive approach to ONLY pass `index` as the state, 
   accumulating the values on the way UP the recursion tree rather than relying on a separate array parameter.
"""

# STEP 1: The Proper Recursive Form (No Array Passed)
# Time Complexity: O(2^N) | Space Complexity: O(N)
def non_adjacent_max_proper(array, index):
    # Base cases
    if index >= len(array):
        return 0
        
    # Option 1: We "Pick" the element at `index`. 
    # That means we cannot pick `index + 1`, so we jump straight to `index + 2`.
    pick = array[index] + non_adjacent_max_proper(array, index + 2)
    
    # Option 2: We "Not Pick" the element. 
    # We move onto the very next index `index + 1`.
    not_pick = 0 + non_adjacent_max_proper(array, index + 1)
    
    return max(pick, not_pick)

print(f"Proper pure recursive output: {non_adjacent_max_proper([2,1,4,9], 0)}")
"""
how to go from memo to tab:(reverse recurion from top down to get the answer)(we go from bottom up on the tree)
1. declare the dp array
2. check the variavles that change in the euler's path
3.copy the recursion as it is instead of call use the stored value in dp array.
"""

# STEP 2: The Memoized Version (Top-Down DP)
# Time Complexity: O(N) | Space Complexity: O(N)
def non_adjacent_max_memo(array, index, memo=None):
    if memo is None:
        memo = {}
        
    if index >= len(array):
        return 0
        
    # Check if we have already calculated the answer for this exact `index`
    if index in memo:
        return memo[index]
        
    pick = array[index] + non_adjacent_max_memo(array, index + 2, memo)
    not_pick = 0 + non_adjacent_max_memo(array, index + 1, memo)
    
    # Save the answer before returning!
    memo[index] = max(pick, not_pick)
    return memo[index]

print(f"Memoized DP output:          {non_adjacent_max_memo([2,1,4,9], 0)}")


# STEP 3: The Proper Recursive Form (Reverse Approach: Last to First)
# Time Complexity: O(2^N) | Space Complexity: O(N)
def non_adjacent_max_proper_reverse(array, index):
    # Base cases for moving backwards
    if index < 0:
        return 0
    if index == 0:
        return array[0]
        
    # Option 1: "Pick" current element, jump over the immediately preceding one
    pick = array[index] + non_adjacent_max_proper_reverse(array, index - 2)
    
    # Option 2: "Not Pick" current element, move cleanly to the immediately preceding one
    not_pick = 0 + non_adjacent_max_proper_reverse(array, index - 1)
    
    return max(pick, not_pick)

print(f"Proper pure reversed recursive output: {non_adjacent_max_proper_reverse([2,1,4,9], len([2,1,4,9])-1)}")


# STEP 4: The Memoized Version (Reverse Approach: Last to First)
# Time Complexity: O(N) | Space Complexity: O(N)
def non_adjacent_max_memo_reverse(array, index, memo=None):
    if memo is None:
        memo = {}
        
    if index < 0:
        return 0
    if index == 0:
        return array[0]
        
    # Check if calculated
    if index in memo:
        return memo[index]
        
    pick = array[index] + non_adjacent_max_memo_reverse(array, index - 2, memo)
    not_pick = 0 + non_adjacent_max_memo_reverse(array, index - 1, memo)
    
    # Save the answer before returning
    memo[index] = max(pick, not_pick)
    return memo[index]

my_array = [2, 1, 4, 9]
print(f"Memoized DP reversed output:         {non_adjacent_max_memo_reverse(my_array, len(my_array)-1)}")


# STEP 5: Tabulation (Bottom-Up for the Reversed Approach)
# In Tabulation, we flip Recursion on its head! Instead of asking the "end" goal to trace back to the base case,
# we construct the base cases first, and dynamically build our way UP to the end relying purely on a `DP array`
# instead of the function call stack.
# Time Complexity: O(N) | Space Complexity: O(N)
def non_adjacent_max_tabulation_reversed(array):
    if not array:
        return 0
        
    # We create an array of identical size to strictly cache our results.
    dp = [0] * len(array)
    
    # 1. Translate the Base Case:
    # In the reversed recursion, `if index == 0: return array[0]`. 
    # In Tabulation, we statically assign that logic exactly to our DP array.
    dp[0] = array[0]
    
    # 2. Iterate Bottom-Up iteratively building subsequent indices natively instead of calling functions.
    for index in range(1, len(array)):
        
        # Option 1: "Pick". 
        # Instead of calling `recursive(index - 2)`, we just read `dp[index - 2]`.
        # (We strictly handle the out-of-bounds error manually when index < 2)
        pick = array[index] + (dp[index - 2] if index > 1 else 0)
        
        # Option 2: "Not Pick". 
        # Instead of calling `recursive(index - 1)`, we read from `dp[index - 1]`.
        not_pick = 0 + dp[index - 1]
        
        # Store in the DP organically!
        dp[index] = max(pick, not_pick)
        
    # The final answer inherently surfaces exactly at the last index.
    return dp[len(array) - 1]

print(f"Tabulation (Reversed) output:        {non_adjacent_max_tabulation_reversed(my_array)}")


# STEP 6: Tabulation (Bottom-Up for the Forward Approach)
# For the Forward Approach, our recursion evaluated `index=0` and moved towards `index=len(array)`.
# To tabulate Bottom-Up, we must build the base cases at the end of the array, and sweep down to index 0!
# Time Complexity: O(N) | Space Complexity: O(N)
def non_adjacent_max_tabulation_forward(array):
    if not array:
        return 0
        
    # We extend the DP array by 2 extra spaces at the end gracefully absorbing out-of-bounds jumps.
    # Base case for forward recursion was `if index >= len(array): return 0`.
    # That is natively satisfied here, as the trailing slots organically default to 0!
    dp = [0] * (len(array) + 2)
    
    # Start tracing linearly backwards explicitly from the tail of the array down to index 0.
    for index in range(len(array) - 1, -1, -1):
        
        # Option 1: "Pick". We access 2 blocks explicitly forward from our array.
        pick = array[index] + dp[index + 2]
        
        # Option 2: "Not Pick". We access 1 block explicitly forward.
        not_pick = 0 + dp[index + 1]
        
        # Build the DP layer cleanly statically!
        dp[index] = max(pick, not_pick)
        
    # Our original recursive run started by evaluating `index = 0`, so inherently, 
    # the tabulated outcome safely terminates exactly at dp[0].
    return dp[0]

print(f"Tabulation (Forward) output:         {non_adjacent_max_tabulation_forward(my_array)}")


# STEP 7: Space Optimization (Reversed Tabulation)
# Looking at the Reversed Tabulation, we calculate `dp[index]` by strictly relying on `dp[index - 1]` and `dp[index - 2]`. 
# Because we NEVER look back more than 2 spaces, storing an entire array of size N is a waste of memory!
# We can just use two variables to carry forward the historical "state".
# Time Complexity: O(N) | Space Complexity: O(1)
def non_adjacent_max_space_opt_reversed(array):
    if not array:
        return 0
        
    # prev aligns to dp[index - 1] (the very last step calculated)
    # prev2 aligns to dp[index - 2] (two steps back)
    # Base Case: When at index 0, our array[0] becomes our first "prev"
    prev = array[0]
    prev2 = 0
    
    for index in range(1, len(array)):
        # Option 1: "Pick". We add the current element to prev2.
        pick = array[index] + prev2
        
        # Option 2: "Not Pick". We just inherit the direct previous value securely.
        not_pick = 0 + prev
        
        curr = max(pick, not_pick)
        
        # Shift the variables forward for the next iteration natively
        prev2 = prev
        prev = curr
        
    return prev

print(f"Space Optimized (Reversed) output:   {non_adjacent_max_space_opt_reversed(my_array)}")


# STEP 8: Space Optimization (Forward Tabulation)
# Similarly, for the Forward Tabulation sweeping cleanly backward down to index 0,
# our `dp[index]` calculation uniquely depends on exactly `dp[index + 1]` and `dp[index + 2]`.
# We drop the N sequence array entirely and roll variables cleanly backwards.
# Time Complexity: O(N) | Space Complexity: O(1)
def non_adjacent_max_space_opt_forward(array):
    if not array:
        return 0
        
    # next1 aligns to dp[index + 1] (one space ahead conceptually)
    # next2 aligns to dp[index + 2] (two spaces ahead)
    # Both explicitly inherit our base-cases of trailing 0s dynamically.
    next1 = 0
    next2 = 0
    
    for index in range(len(array) - 1, -1, -1):
        # Option 1: "Pick" natively jumping to next2
        pick = array[index] + next2
        
        # Option 2: "Not Pick" dropping cleanly into next1
        not_pick = 0 + next1
        
        curr = max(pick, not_pick)
        
        # Shift our variables cleanly backward logically to wrap the rolling sequence
        next2 = next1
        next1 = curr
        
    return next1

print(f"Space Optimized (Forward) output:    {non_adjacent_max_space_opt_forward(my_array)}")
