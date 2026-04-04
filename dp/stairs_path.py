#when question comes try all possible ways, get me minimum possible or maximum problem or count all possible ways then understand it is a recursion,get me the best way or the worst way
#how to understand dp is if it is a recursion problem and in the recursive calls you see calls for a particular number being repeated in the euler's path then we can memoize
#recursion shortcut(while drawing the tree for euler)
# 1.try to represent a problem in terms of Index
# 2.do all possible things at that index 
# 3.if it is count question it add all results and count, if min get the minimum of the ways, or max get the max of the ways
def stairs_path_recursion(start, end, path_till_now=[], result_paths=None):
    if result_paths is None:
        result_paths = []

    if start == end:
        return result_paths.append([*path_till_now])
    
    path_till_now.append(1)
    stairs_path_recursion(start+1, end, path_till_now, result_paths)
    path_till_now.pop()

    if start +2 <= end:
        path_till_now.append(2)
        stairs_path_recursion(start+2, end, path_till_now, result_paths)
        path_till_now.pop()

    return result_paths

def stairs_path_recursion_with_return(start, end):#here no need to carry result path and path till now in the recursion stack because we are building and returning the result here,(path till now calcultion ) we are calculating the paths from the child paths by appending one or two steps at there starts 
    result_paths = []
    if start == end:
        return [[]] #because result paths is an arrray of arrays(and only single way to reach from here is to just stand)
    
    paths_from_next_step = stairs_path_recursion_with_return(start+1, end)
    paths_from_next_step = [[1, *ele] for ele in paths_from_next_step]

    result_paths.extend(paths_from_next_step)

    if start +2 <= end:
        paths_from_next_to_next_step =stairs_path_recursion_with_return(start+2, end)
        paths_from_next_to_next_step = [[2, *ele] for ele in paths_from_next_to_next_step]
        result_paths.extend(paths_from_next_to_next_step)

    return result_paths

def stairs_path_dp(start, end, one_d_map=None):#here no need to carry result path and path till now in the recursion stack because we are building and returning the result here,(path till now calcultion ) we are calculating the paths from the child paths by appending one or two steps at there starts 
    result_paths = []
    if one_d_map is None:
        one_d_map = [ None for _ in range(end+1)]

    if start == end:
        return [[]] #because result paths is an array of arrays(and only single way to reach from here is to just stand)
    if start > end:
        return [] #because no ways from here
    
    if one_d_map[start]:
        return one_d_map[start]
    paths_from_next_step = stairs_path_recursion_with_return(start+1, end)
    one_d_map[start+1] = paths_from_next_step
    paths_from_next_step = [[1, *ele] for ele in paths_from_next_step]

    # result_paths.extend(paths_from_next_step)
    result_paths += paths_from_next_step

    # if start +2 <= end:
    #     paths_from_next_to_next_step =stairs_path_recursion_with_return(start+2, end)
    #     one_d_map[start+2] = paths_from_next_to_next_step
    #     paths_from_next_to_next_step = [[2, *ele] for ele in paths_from_next_to_next_step]
    #     result_paths.extend(paths_from_next_to_next_step)

    paths_from_next_to_next_step =stairs_path_recursion_with_return(start+2, end)
    one_d_map[start+2] = paths_from_next_to_next_step
    paths_from_next_to_next_step = [[2, *ele] for ele in paths_from_next_to_next_step]
    result_paths+=paths_from_next_to_next_step
    
    return result_paths

def stairs_path_tabulation(start, end):
    # Tabulation (Bottom-up DP): Initialize memo array for paths from 'i' to 'end'
    one_d_map = [[] for _ in range(end+1)]
    
    # Base case: There's exactly 1 path from 'end' to 'end' which is taking 0 steps
    one_d_map[end] = [[]]
    
    # Fill backwards from 'end-1' down to 'start' stair
    for i in range(end - 1, start - 1, -1):
        # 1. Paths if we take a 1-step leap from 'i'
        paths_1_step = [[1, *path] for path in one_d_map[i+1]]
        
        # 2. Paths if we take a 2-step leap from 'i', ensuring we don't jump past 'end'
        paths_2_step = []
        if i + 2 <= end:
            paths_2_step = [[2, *path] for path in one_d_map[i+2]]
            
        # Combine paths for taking 1 step or 2 steps from stair 'i'
        one_d_map[i] = paths_1_step + paths_2_step
        
    return one_d_map[start]

def stairs_path_tabulation_opt(start, end):
    # Space Optimization: Just like in Fibonacci, we only ever need the paths from the 
    # exact next step (i+1) and the step after that (i+2) to calculate paths for step 'i'.
    # We do NOT need to maintain an entire array of size 'end+1'.
    
    if start == end:
        return [[]]
        
    # 'next_step' initially holds paths from 'end' to 'end'
    next_step = [[]]
    # 'next_next_step' initially holds paths from 'end+1' (which is out of bounds, so empty)
    next_next_step = []
    
    current_step = []
    
    for i in range(end - 1, start - 1, -1):
        # 1. Take a 1-step leap: prepend 1 to paths starting from the immediate next stair
        paths_1_step = [[1, *path] for path in next_step]
        
        # 2. Take a 2-step leap: prepend 2 to paths starting from two stairs down
        paths_2_step = [[2, *path] for path in next_next_step]
            
        current_step = paths_1_step + paths_2_step
        
        # Shift our state windows backward for the next iteration
        next_next_step = next_step
        next_step = current_step
        
    return current_step

print("Array Tabulation Paths:\t\t", stairs_path_tabulation(0, 4))
print("Space Opt Tabulation Paths:\t", stairs_path_dp(0, 4))