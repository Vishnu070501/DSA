"""
Problem Statement: House Robber II (Circular Street)
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

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

# How we solve this using the previous logic:
# Because the houses are formatted in a circle, the very first house (Index 0) 
# and the very last house (Index N-1) are strictly adjacent. 
# Therefore, we can mathematically NEVER rob BOTH of them simultaneously.
# 
# This structurally splits the universe of all valid solutions into two sets:
# 1. Solutions that DO NOT include the LAST house: We aggressively enforce this by running DP strictly on `array[:-1]`.
# 2. Solutions that DO NOT include the FIRST house: We aggressively enforce this by running DP strictly on `array[1:]`.
# 
# Common Doubt: "What if the optimal run on `array[1:]` naturally decides to skip House 1 
# (the 2nd house) and House N-1 (the last house)? Doesn't that explicitly leave a safe 
# gap to add House 0 (the 1st house) to our total sum?"
# 
# Answer: YES! But we don't mechanically force House 0 into the `array[1:]` answer. 
# If picking House 0 was mathematically the highest yielding scenario, that EXACT sequence 
# natively is evaluated inside our OTHER sweeping sub-array (`array[:-1]`). 
# 
# `array[:-1]` fundamentally has House 0 available to pick! 
# Because Dynamic Programming evaluates EVERY single possible subset natively, it is mathematically 
# impossible for `array[:-1]` to "forget" or fail to pick House 0 if picking House 0 yields a higher sum! 
# It evaluates exactly what you are thinking: `max(Path WITH House 0, Path WITHOUT House 0)`.
# 
# Meanwhile, `array[1:]` never had access to House 0, returning just (X).
# Since DP guarantees the (X + House 0) path is evaluated inside `array[:-1]`, 
# taking the max() of both disjoint universes automatically and safely locks in the maximized outcome!
# 
# - Scenario A (Finds the absolute optimal path in [0 to N-2])
# - Scenario B (Finds the absolute optimal path in [1 to N-1])
# We guarantee that no matter what the optimal path is, one of these two sweeps will find it.
# Time Complexity: O(N) | Space Complexity: O(1)
def max_money_robber_can_make(house_vals):
    # Base case: You only have one house to rob.
    if len(house_vals) == 1:
        return house_vals[0]
        
    # We call our space optimized function explicitly on the two partitioned cases
    return max(
        non_adjacent_max_space_opt_reversed(house_vals[:-1]), 
        non_adjacent_max_space_opt_reversed(house_vals[1:])
    )

print(f"Maximum money the robber can make: {max_money_robber_can_make([2,3,2,2])}")