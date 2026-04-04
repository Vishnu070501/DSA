def frog_jump( energy_levels, current_level=0, energy_till_now=0):
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

def frog_jump_tabulation(energy_levels, current_level):
    dp_array = [(None if i != len(energy_levels)-2 else abs(energy_levels[len(energy_levels)-1]-energy_levels[len(energy_levels)-2])) if i != len(energy_levels)-1 else 0 for i in range(len(energy_levels))]
    for 
print(f"result:{frog_jump_dp([10,20,30,10])}")

    
