"""
Problem Statement: Ninja's Training
A Ninja has an 'N' days training schedule. He has to perform one of these three activities
(Running, Fighting Practice, or Learning New Moves) each day. Each activity has some merit 
points on each day. A Ninja cannot perform the same activity twice in a row. 
Discover the maximum merit points the ninja can earn.

Example:
Matrix of points:
Day 0: [10, 50,  1]
Day 1: [ 5, 100, 10]

Answer: 110 
(Day 0: Pick Activity 0 for 10 pts. Day 1: Pick Activity 1 for 100 pts. Total = 110)
"""

# STEP 1: Pure Recursion
# How it works: 
# We maintain the current `day` and the `last_activity` we executed previously.
# We iterate through all possible tasks for `day`. If the task is NOT the `last_activity`, 
# we pick it, add its points natively, and recursively push to `day+1` setting our newly picked 
# task as the updated `last_activity`.
# We exhaustively calculate all possible branching paths (O(3^N) time).
def ninja_training( matrix, day=0, last_activity=None):
    if day == len(matrix):
        return 0
    max_points = float("-inf")
    for i in range(len(matrix[day])):
        if i != last_activity:
            max_points = max(max_points, matrix[day][i] + ninja_training(matrix, day+1, i))
    return max_points


# STEP 2: Memoization (Top-Down DP)
# How we memoized it:
# 1. We identified the changing State natively breaking into: `day` and `last_activity`.
# 2. We initialized a `dp_array` of size [Days][Tasks] to cache the maximum points for that specific configuration.
# 3. Before doing the recursive loop, if `dp_array[day][last_activity]` is already rigorously calculated, we just instantly return it!
# Time Complexity drops exponentially safely from O(3^N) to O(N * 3). Space: O(N) Call Stack + O(N * 3) for the 2D cache.
def ninja_training_memo( matrix, day=0, last_activity=None, dp_array = None):
    if dp_array is None:
        dp_array = [[None for _ in range(len(matrix[i]))] for i in range(len(matrix))]
        
    if day == len(matrix):
        return 0
        
    # (Bug Fix: `if last_activity:` evaluates to False when `last_activity == 0`! 
    # Must explicitly use `is not None` to securely cache the 0th activity).
    if last_activity is not None and dp_array[day][last_activity] is not None:
        return dp_array[day][last_activity]
        
    max_points = float("-inf")
    for i in range(len(matrix[day])):
        if i != last_activity:
            max_points = max(max_points, matrix[day][i] + ninja_training_memo(matrix, day+1, i, dp_array))
            
    if last_activity is not None:
        dp_array[day][last_activity] = max_points
    
    return max_points


# STEP 3: Tabulation (Bottom-Up DP)
# How did Memoize cleanly map to Tabulation form?:
# - The Recursion Base Case (`day == len(matrix): return 0`) is embedded into the DP variables cleanly as `base_case = 0`.
# - Instead of recursing Top-Down deeply from Day 0, we flip to Bottom-Up, naturally iterating strictly backwards: `day` from N-1 down to 0.
# - Notice a shift identically in DP state meaning! The memoization tightly cached `dp[day][what_we_did_YESTERDAY]`. 
#   Your tabulation securely calculates `dp[day][what_we_do_TODAY]`, looking seamlessly ahead to `day+1` to pick a valid `other_task` safely.
def ninja_training_tab( matrix):
    dp_matrix = [[None for _ in range(len(matrix[i]))] for i in range(len(matrix))]
    base_case = 0
    
    # Iterate identically backward natively matching the collapse of the recursion tree
    for day in range(len(matrix)-1,-1,-1):
        for task in range(len(matrix[0])): # `task` corresponds strictly to the activity we pick TODAY
            # Pick today's task securely, then naturally query exactly Day + 1 for the optimal task that isn't today's task
            dp_matrix[day][task] = matrix[day][task] + max([matrix[day+1][other_task] for other_task in range(len(matrix[day+1]))if other_task != task]) if day+1<len(matrix) else base_case

    # The inherently maximum safely achievable value explicitly across all starting tasks on Day 0
    return max([dp_matrix[0][task] for task in range(len(matrix[0]))])
        

# STEP 4: Space Optimization
# How did we predictably optimize Tabulation Memory?:
# - In Tabulation flawlessly, cleanly notice `dp_matrix[day]` ONLY ever needs structurally to look dynamically at `dp_matrix[day+1]`.
# - The entire rest of the N x 3 matrix history is completely ignored.
# - We compress the entire 2D matrix stably into just two 1D Arrays of size 3.
#   1. `current_day_max_work_points` (representing `dp[day]`)
#   2. `next_day_max_work_points` (representing `dp[day+1]`)
# Space Complexity systematically drops from O(N*3) matrix down to tightly bounded O(1) natively!
def ninja_training_tab_opt(matrix):
    base_case = 0
    current_day_max_work_points = [None for _ in range(len(matrix[0]))]
    next_day_max_work_points = [*current_day_max_work_points]
    
    for i in range(len(matrix)-1,-1,-1):
        for current_day_work in range(len(current_day_max_work_points)):
            if i != len(matrix)-1: 
                current_day_max_work_points[current_day_work] = matrix[i][current_day_work]+max([next_day_max_work_points[next_day_work] for next_day_work in range(len(next_day_max_work_points)) if next_day_work!=current_day_work])
            else:
                current_day_max_work_points[current_day_work] = matrix[i][current_day_work]+base_case
        # Shift state efficiently seamlessly
        next_day_max_work_points = [*current_day_max_work_points]
        
    return max(current_day_max_work_points)

print(f"Max Ninja Training Merits: {ninja_training_tab_opt([[10,50,1], [5,100,10]])}")