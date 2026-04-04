def fibonacci_series(limit):
    result = []
    if limit ==1:
        return [0,1]
    result = fibonacci_series(limit-1);
    result.append(result[len(result)-1]+result[len(result)-2])
    return result
    
def get_fibo_ele(limit):
    #recursion is top dowm approach where we go towards the base case from top calculate the answers
    if limit <=1:
        return limit
    return get_fibo_ele(limit-2)+get_fibo_ele(limit-1)

# Time Complexity: O(n) because each fibonacci number up to 'limit' is computed only once.
# Space Complexity: O(n) for the recursion call stack + O(n) for the memoization array map.
def get_fibo_dp(limit, array_map=None):
    # Memoization (Top-Down DP): By observing the recursion tree (Euler's path), we notice 
    # overlapping subproblems. We use an array map to store computed answers to avoid recalculating them(array map of size limit+1 because we see answers being calculated from 0 to ).
    
    # Initialize the memoization array uniquely on the very first function call.
    if array_map is None:
        array_map = [None for _ in range(limit+1)]
        
    # Base cases: fibo of 0 is 0, and fibo of 1 is 1.
    if limit <= 1:
        return limit
        
    # Before computing, check if we've already found and cached the answer for this 'limit'
    if array_map[limit]:
        return array_map[limit]
    else:
        # If not, recursively calculate the (n-1)th element
        last_ele = get_fibo_dp(limit-1, array_map)
        # Store the computed result in our memoization map
        array_map[limit-1] = last_ele
        
        # Recursively calculate the (n-2)th element
        second_last = get_fibo_dp(limit-2, array_map)
        # Store the computed result for the second part as well
        array_map[limit-2] = second_last

    return last_ele+second_last
    
def tabulation_fibo(limit):
    # In tabulation method (Bottom-Up DP), we first initialize a map/array to store results.
    # The size is limit + 1 to store answers from 0 up to 'limit'.
    dp_array = [None for _ in range(limit+1)]
    
    # This is the reverse of recursion. Recursion is a top-down approach, while this is bottom-up.
    # For example, we start by calculating and storing the base cases directly: fibo(0) and fibo(1).
    dp_array[0]=0
    dp_array[1]=1
    
    # Then we iterate from 2 to limit, filling the array using the previously calculated values.
    # Time Complexity: O(n) since we loop n times.
    # Space Complexity: O(n) since we use an array of size n+1.
    for i in range(2, limit+1):
        dp_array[i] = dp_array[i-2] + dp_array[i-1]
    return dp_array[limit]

def tabulation_fibo_opt(limit):
    # Space Optimization: In the tabulation method above, computing the next element
    # strictly requires only the last two elements. Thus, we don't need a full array.
    # We can just keep track of the two previous values using simple variables.
    
    before_before_i = 0 # Represents fibo(0) initially
    before_i = 1        # Represents fibo(1) initially
    
    # Time Complexity: O(n) since we loop from 2 to limit.
    # Space Complexity: O(1) since we only use constant space variables, not an array.
    for i in range(2, limit+1):
        i_th_ele = before_before_i + before_i
        
        # Shift the pointers one step forward for the next iteration
        before_before_i = before_i
        before_i = i_th_ele
        
    return i_th_ele



print(tabulation_fibo_opt(100))