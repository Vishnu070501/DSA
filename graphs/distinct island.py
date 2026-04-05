"""
Problem Statement: Number of Distinct Islands
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group 
of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct 
if and only if one island is equal to another (not rotated or reflected).
"""

from copy import deepcopy


# Time Complexity: O(V + E) for graphs, scaling structurally with node bounds.
# Space Complexity: O(V) spanning auxiliary stacks natively.
def dfs_island_shaped(matrix, starting_point, visited_matrix, base):
    """
    Depth-First Search (DFS) to traverse an island and compute its shape relative to a base point.
    By subtracting the base point coordinates from the current cell coordinates, 
    identically shaped islands will have the exact same list of relative coordinates.
    """
    base_row, base_col = base
    row, col = starting_point
    
    # Base cases for recursion to stop:
    # 1. Out of bounds checking (row or col < 0, or exceeds matrix dimensions)
    # 2. Cell is already visited
    # 3. Cell is water (0) instead of land (1)
    if (
        row < 0
        or col < 0
        or row == len(matrix)
        or col == len(matrix[0])
        or visited_matrix[row][col]
        or matrix[row][col] != 1
    ):
        return []

    # Mark the current cell as visited
    visited_matrix[row][col] = True
    
    # Store the position of the current cell relative to the starting point of this island (base)
    shape_visited = [(row - base_row, col - base_col)]

    # Recursively visit all 4 adjacent directions (Top, Right, Bottom, Left)
    shape_visited.extend(
        dfs_island_shaped(matrix, (row - 1, col), visited_matrix, base) # Top
    )
    shape_visited.extend(
        dfs_island_shaped(matrix, (row, col + 1), visited_matrix, base) # Right
    )
    shape_visited.extend(
        dfs_island_shaped(matrix, (row + 1, col), visited_matrix, base) # Bottom
    )
    shape_visited.extend(
        dfs_island_shaped(matrix, (row, col - 1), visited_matrix, base) # Left
    )

    return shape_visited


# Time Complexity: O(V + E) for graphs, scaling structurally with node bounds.
# Space Complexity: O(V) spanning auxiliary stacks natively.
def distinct_islands(matrix):
    """
    Finds and returns the number of distinct islands in a given matrix (grid).
    An island is distinct if it cannot be mapped to another island by translation.
    """
    # Create a 2D array of the same size to keep track of visited cells
    visited_matrix = [[False for ele in row] for row in matrix]
    
    # Optional: operate on a deep copy of the matrix instead of modifying original
    copy_matrix = deepcopy(matrix)
    
    # A set to store unique shapes of the islands discovered
    visited_islands = set()
    
    # Iterate through every cell of the matrix
    for i in range(len(copy_matrix)):
        for j in range(len(copy_matrix[i])):
            # If the current cell is unvisited and happens to be part of an island (value = 1)
            if not visited_matrix[i][j] and copy_matrix[i][j]:
                # Launch a DFS from the current cell acting as the "base" point of the new island.
                # The DFS returns a list of relative coordinates representing the island's unique shape.
                
                # You are getting the error "cannot add list to set" because in Python:
                # set can only store hashable (immutable) objects
                # and list is mutable, so it cannot be added to a set ❌
                
                # Therefore, we convert the result to an immutable tuple so it can be stored in the set.
                visited_islands.add(
                    tuple(dfs_island_shaped(copy_matrix, (i, j), visited_matrix, (i, j)))
                )
                
    # The number of unique tuples in the set gives the number of distinct islands
    return len(visited_islands)


# Example test case
print(
    distinct_islands([
        [1, 1, 0, 1, 1], 
        [1, 0, 0, 0, 0], 
        [0, 0, 0, 1, 1], 
        [1, 1, 0, 1, 0]
        ])
)
