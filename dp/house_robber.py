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
# Because the houses are formatted in a circle, the very first house and the very last house are strictly adjacent!
# Therefore, we can never rob BOTH the first and the last house simultaneously in any scenario.
# 
# This splits the problem perfectly into two separate linear "House Robber" tasks (which we just previously solved!):
# 1. We skip the LAST house entirely, evaluating linearly from index 0 to N-2: `array[:-1]`
# 2. We skip the FIRST house entirely, evaluating linearly from index 1 to N-1: `array[1:]`
# The optimal answer is just the maximum result comparing these two separate sub-arrays!
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