# Time Complexity: O(2^n) because from each step we can take a 1-step or 2-step jump, leading to an exponential recursion tree.
# Space Complexity: O(n) for the recursion call stack, as the maximum depth of recursion will be the number of energy levels.
def frog_jump( energy_levels, current_level=0, energy_till_now=0):
    # This is a naive recursive approach (Top-Down) where we explore all possible paths.
    # At each step, we branch out to 1-step and 2-step jumps, accumulating the total energy.
    min_energy = float('inf')
    if current_level == len(energy_levels)-1:
        min_energy = min(min_energy, energy_till_now)
        return min_energy
    energy_for_one_step = abs(energy_levels[current_level+1]-energy_levels[current_level])
    energy_till_now += energy_for_one_step
    min_energy = min(min_energy,frog_jump(energy_levels, current_level+1, energy_till_now))
    energy_till_now -= energy_for_one_step

    if current_level+2 <= len(energy_levels)-1:
        energy_for_two_step = abs(energy_levels[current_level+2]-energy_levels[current_level])
        energy_till_now += energy_for_two_step
        min_energy = min(min_energy,frog_jump(energy_levels, current_level+2, energy_till_now))
        energy_till_now -= energy_for_two_step

    return min_energy

# Time Complexity: O(n) because the minimum energy for each level/stair is computed only once.
# Space Complexity: O(n) for the recursion call stack + O(n) for the memoization array map.
def frog_jump_dp(energy_levels, current_level=0, answer_map=None):
    # ISSUE FIXED: We removed `energy_till_now`. In Top-Down DP, the state should only represent 
    # "what is the minimum cost FROM this current level TO the end?"
    # If we pass accumulated energy down, we ruin memoization because different paths will reach 
    # the same 'current_level' with different 'energy_till_now', causing cache conflicts!

    # Initialize answer_map once
    if answer_map is None:
        answer_map = [None for _ in range(len(energy_levels))]
        
    # Base case: if we are already at the last level, it takes 0 energy to reach the end bounds
    if current_level == len(energy_levels) - 1:
        return 0
        
    # Important to explicitly check `is not None` because 0 is a valid cached energy value!
    if answer_map[current_level] is not None:
        return answer_map[current_level]
        
    min_energy = float('inf')
    
    # 1. Calculate taking a 1-step leap
    energy_for_one_step = abs(energy_levels[current_level+1] - energy_levels[current_level])
    # The total cost of this path = (cost of this jump) + (min cost from new platform to end)
    cost1 = energy_for_one_step + frog_jump_dp(energy_levels, current_level+1, answer_map)
    min_energy = min(min_energy, cost1)

    # 2. Calculate taking a 2-step leap
    if current_level + 2 <= len(energy_levels) - 1:
        energy_for_two_step = abs(energy_levels[current_level+2] - energy_levels[current_level])
        cost2 = energy_for_two_step + frog_jump_dp(energy_levels, current_level+2, answer_map)
        min_energy = min(min_energy, cost2)
        
    # Memoize our answer for this specific stair BEFORE returning
    answer_map[current_level] = min_energy
    return min_energy

# Time Complexity: O(n) since we iterate backward through the array elements, computing in constant time.
# Space Complexity: O(n) since we use an array of size n (length of energy_levels).
def frog_jump_tabulation(energy_levels):
    # In tabulation method (Bottom-Up DP), we first initialize an array to store results.
    # We conceptually work backward: starting from the last stair (where cost to reach the end is 0)
    # and compute the optimal cost for each previous stair up to the starting step.
    dp_array = []
    dp_array = [None for _ in range(len(energy_levels))]
    
    # Base case: to go from the last stair to the last stair costs 0 energy.
    dp_array[len(dp_array)-1] = 0
    for i in range(len(energy_levels)-2,-1,-1):
        one_step_call = dp_array[i+1]+abs(energy_levels[i+1]-energy_levels[i])
        two_step_call = None
        if i+2 < len(energy_levels):
            two_step_call = dp_array[i+2]+abs(energy_levels[i+2]-energy_levels[i])

        dp_array[i] = min(one_step_call, two_step_call if two_step_call else float('inf'))

    return dp_array[0]

# Time Complexity: O(n) since we loop backward from the second last element down to the first element.
# Space Complexity: O(1) since we only use constant space variables instead of a full DP array.
def frog_jum_tab_opt(energy_levels):
    # Space Optimization: In the tabulation method above, to compute the answer for the current step `i`,
    # we strictly only need the answers for `i+1` (1-step jump) and `i+2` (2-step jump).
    # Thus, we don't need a full array. We can just keep track of the two upcoming values using simple variables.
    
    second_last_item_dp_array_or_min_after_one_step = 0
    last_item_dp_array_or_min_after_two_step = None
    for i in range(len(energy_levels)-2,-1,-1):
        one_step_call = second_last_item_dp_array_or_min_after_one_step+abs(energy_levels[i+1]-energy_levels[i])
        two_step_call = None
        if last_item_dp_array_or_min_after_two_step is not None:
            two_step_call = last_item_dp_array_or_min_after_two_step+abs(energy_levels[i+2]-energy_levels[i])
        last_item_dp_array_or_min_after_two_step = second_last_item_dp_array_or_min_after_one_step
        second_last_item_dp_array_or_min_after_one_step = min(one_step_call, two_step_call if two_step_call is not None else float('inf'))
        

    return second_last_item_dp_array_or_min_after_one_step
print(f"result:{frog_jum_tab_opt([10,20,30,10])}")

    
