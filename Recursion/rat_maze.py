"""
Problem Statement: Rat in a Maze Problem
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). 
Find all possible paths that the rat can take to reach from source to destination. 
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). 
Value 0 at a cell blocks the rat, while value 1 allows the rat to travel through it.
"""

#when question comes try all possible ways, get me minimum possible or maximum problem or count all possible ways then understand it is a recursion,get me the best way or the worst way
#recursion shortcut(while drawing the tree for euler):
# 1.try to represent a problem in terms of Index
# 2.do all possible things at that index 
# 3.if it is count question it add all results and count, if min get the minimum of the ways, or max get the max of the ways
# Time Complexity: O(1) mathematically assessing grid boundary indexes independently in constant time.
# Space Complexity: O(1) bounded verification parameters evaluated statically.
def can_make_move(matrix, destination, cells_visited):
    # Basic Boolean operator logic determining map bounds combinations recursively bounding paths safely natively.
    x,y = destination
    # if x== len(matrix) or y == len(matrix[0]):
    #     print("Hii")
    #     print(x < len(matrix) and y < len(matrix[0]) and x>=0 and y>=0 and matrix[x][y] and (destination not in cells_visited))
    
    return x < len(matrix) and y < len(matrix[0]) and x>=0 and y>=0 and matrix[x][y] and (destination not in cells_visited)

# Time Complexity: O(4^(N*N)) checking 4 coordinate variables repeatedly over exponentially growing branches.
# Space Complexity: O(N*N) auxiliary call-stack structurally spanning recursively natively cleanly.
def maze_paths( matrix, source, destination, cells_visited=[]):
    # Explores 4 independent directions natively tracing variables recursively checking blocks symmetrically natively.
    x1, y1 = source
    if source == destination:
        
        return ['']
    final_result = []
    # down
    if can_make_move(matrix, (x1+1, y1), cells_visited ):
        cells_visited.append(source)
        down_results =maze_paths(matrix, (x1+1, y1), destination)
        cells_visited.pop()
        down_results = ['D'+result for result in down_results]
        final_result.extend(down_results)
        
    # left
    if can_make_move(matrix, (x1, y1-1),  cells_visited ):
        cells_visited.append(source)
        left_results =maze_paths(matrix, (x1, y1-1), destination)
        cells_visited.pop()
        left_results = ['L'+result for result in left_results]
        final_result.extend(left_results)
    # right
    if can_make_move(matrix, (x1, y1+1),  cells_visited  ):
        cells_visited.append(source)
        right_results =maze_paths(matrix, (x1, y1+1), destination)
        cells_visited.pop()
        right_results = ['R'+result for result in right_results]
        final_result.extend(right_results)
    # up
    if can_make_move(matrix, (x1-1, y1),  cells_visited  ):
        cells_visited.append(source)
        up_results =maze_paths(matrix, (x1-1, y1), destination)
        cells_visited.pop()
        up_results = ['U'+result for result in up_results]
        final_result.extend(up_results)
        
    return final_result

# Time Complexity: O(4^(N^2)) generating combinations safely across grid constraints recursively systematically efficiently safely natively.
# Space Complexity: O(L * X) natively checking sequence allocations dynamically explicitly efficiently securely properly.
def maze_paths_opt( matrix, source, destination,turns_taken='', cells_visited=[], result=[] ):
    # Efficiently backtracks variables safely mitigating redundant string boundaries testing structures completely safely unconditionally correctly securely.
    
    if source == destination:
        result.append(turns_taken)
        return
    
    x1, y1 = source
    
    # down
    if can_make_move(matrix, (x1+1, y1), cells_visited ):
        turns_taken+='D'
        cells_visited.append((x1+1, y1))
        maze_paths_opt(matrix, (x1+1, y1), destination, turns_taken, cells_visited, result)
        turns_taken = turns_taken[:len(turns_taken)-1]
        cells_visited.pop()
    # left
    if can_make_move(matrix, (x1, y1-1), cells_visited ):
         turns_taken+='L'
         cells_visited.append((x1, y1-1))
         maze_paths_opt(matrix,  (x1, y1-1), destination, turns_taken, cells_visited, result)
         turns_taken = turns_taken[:len(turns_taken)-1]
         cells_visited.pop()
    # right
    if can_make_move(matrix, (x1, y1+1), cells_visited ):
         turns_taken+='R'
         cells_visited.append((x1, y1+1))
         maze_paths_opt(matrix, (x1, y1+1), destination, turns_taken, cells_visited, result)
         turns_taken = turns_taken[:len(turns_taken)-1]
         cells_visited.pop()
    # up
    if can_make_move(matrix, (x1-1, y1), cells_visited ):
         turns_taken+='U'
         cells_visited.append((x1-1, y1))
         maze_paths_opt(matrix, (x1-1, y1), destination, turns_taken, cells_visited, result)    
         turns_taken = turns_taken[:len(turns_taken)-1]
         cells_visited.pop()
         
    return result
    

def main(*args, **kwargs):
    row, col = map(int, input("Enter the rows and cols(split with space):").strip().split())
    matrix = [None for _ in range(row)]
    for row in range(row):
        matrix[row] = list(map(int, input(f"enter the row no {row+1} row with spaces ").strip().split()))
        
    print(f"maze paths optimised:{maze_paths_opt(matrix, (0,0), (len(matrix)-1, len(matrix[0])-1) )}")
    print(f"maze paths unoptimised: {maze_paths(matrix, (0,0),(len(matrix)-1, len(matrix[0])-1))}")
    
    
if __name__ == '__main__':
    main()
    
    
    
     