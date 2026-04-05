"""
Problem Statement: Frog Jump with K Distances
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. 
At a time the frog can climb any number of steps from 1 to K. A height[N] array is given. 
The energy consumed in a jump from stair i to stair j is abs(height[i]- height[j]). 
Find the minimum energy required to reach the last stair.
"""

# Time Complexity: O(k^n) since at each of the n steps, we can branch out to k possible jumps.
# Space Complexity: O(n) for the recursion call stack, as maximum depth is n.
def frog_k_jumps_rec(energy_levels, k, current_level=0):
    # This is a naive recursive Top-Down approach. We explore all paths by trying all jumps from 1 up to k.
    min_energy = float('inf')
    
    # Base case: we reached the last step.
    if current_level == len(energy_levels)-1:
        return 0
        
    # Try jumping 1 step, 2 steps, ..., up to k steps.
    for i in range(1, k+1):
        # We must ensure we don't jump past the last step; fixed `current_level+i` (was `current_level+k`)
        if current_level+i < len(energy_levels):
            kjump_min_answer = frog_k_jumps_rec(energy_levels, k, current_level+i) + abs(energy_levels[current_level+i]-energy_levels[current_level])
            min_energy = min(min_energy, kjump_min_answer)
    
    return min_energy

# Time Complexity: O(n*k) because there are n states, and for each state we run a loop of size k.
# Space Complexity: O(n) for the recursion call stack + O(n) for the memoization array map.
def frog_k_jumps_rec_dp(energy_levels, k, current_level=0, dp_array=None):
    # Top-Down DP with Memoization. We cache our results so we don't recalculate the same path.
    min_energy = float('inf')
    dp_array = [None for _ in range(len(energy_levels))] if dp_array is None else dp_array
    
    if current_level == len(energy_levels)-1:
        return 0
        
    # Crucial fix: check `is not None` as 0 is a valid cache value.
    if dp_array[current_level] is not None:
        return dp_array[current_level]
        
    for i in range(1, k+1):
        # Fixed to check current_level+i rather than current_level+k
        if current_level+i < len(energy_levels):
            kjump_min_answer = frog_k_jumps_rec_dp(energy_levels, k, current_level+i, dp_array) + abs(energy_levels[current_level+i]-energy_levels[current_level])
            min_energy = min(min_energy, kjump_min_answer)
            
    # Cache and return our calculated min_energy for the current step.
    dp_array[current_level] = min_energy
    return min_energy

# Time Complexity: O(n*k) as we traverse the n array elements backwards, and for each we do a loop of size k.
# Space Complexity: O(n) to store the dp_array. (Can be space optimized to O(k) by keeping only the last k elements)
def frog_k_jumps_rec_tab(energy_levels, k):
    # Bottom-up DP (Tabulation). We avoid recursion entirely.
    # Start from the end where required energy is 0, and compute the optimal strategy to move to the end.
    dp_array = [None for _ in range(len(energy_levels))]
    dp_array[-1] = 0 # Python's way to access the last element
    
    for i in range(len(dp_array)-2, -1, -1):
        min_energy = float('inf')
        # We iterate from 1 to k jumps. 
        # Note: We must NOT use 'k' for the loop variable, avoiding overriding the function argument 'k'!
        for step in range(1, k+1):
            if i+step < len(dp_array):
                k_step_call = dp_array[i+step] + abs(energy_levels[i+step]-energy_levels[i])
                # Carefully place the min calculation INSIDE the bounds check
                min_energy = min(min_energy, k_step_call)
        dp_array[i] = min_energy
        
    # The final answer is the optimal cost from the starting step 0
    return dp_array[0]

energy_levels = [10, 30, 40, 50, 20]
k = 3
result = frog_k_jumps_rec_tab(energy_levels, k)
print(f"Minimum energy required: {result}")