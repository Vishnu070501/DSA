"""
Problem Statement: Detect Cycle in a Directed Graph
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, 
check whether it contains any cycle or not.
"""

def detect_cyle(adjacency_list, node, visited, path_visited):
    """
    Performs Depth-First Search (DFS) to find if there is a cycle in a directed graph.
    Uses two arrays: one to track overall visited nodes, and another to track nodes in the current DFS traversal path.
    
    Args:
        adjacency_list: Directed graph represented as an adjacency list.
        node: The currently visited node.
        visited: Array tracking nodes visited across all DFS calls to avoid redundant work.
        path_visited: Array tracking nodes visited in the current DFS path specifically to detect back-edges (cycles).
        
    Returns:
        bool: True if a back-edge (cycle) is detected, False otherwise.
    """
    # Mark the node as visited both globally and in the current traversal path
    visited[node] = True
    path_visited[node] = True
    
    neighbours = adjacency_list[node]
    
    for neighbour in neighbours:
        # If the neighbour has not been visited yet, recursively call DFS
        if not visited[neighbour]:
            neighbor_answer = detect_cyle(adjacency_list, neighbour, visited, path_visited)
            # If the recursive call detected a cycle, propagate True upwards
            if neighbor_answer:
                return True
        # If the neighbour is already visited
        else:
            # Check if it was visited in the *current* path as well
            # If it is in the current path, we have found a back-edge, meaning there's a cycle
            if visited[neighbour] and path_visited[neighbour]:
                return True
                
    # Before backtracking out of this node, unmark it from the current path
    path_visited[node] = False
    return False


def helper(adjacency_list):
    """
    Checks if a directed graph has any cycles. Handles disconnected graph 
    components by attempting to start DFS from every unvisited node.
    
    Args:
        adjacency_list: Assuming 1-based indexing for nodes where index 0 is None or empty.
        
    Returns:
        bool: True if AT LEAST ONE cycle exists in the entire graph, False if the graph is acyclic.
    """
    # visited array tracks if a node was ever processed during the algorithm
    visited = [False for _ in adjacency_list]
    # path_visited array tracks if a node is part of the recursive call stack (current path)
    path_visited = [*visited]
    
    # Iterate through all nodes (1 to n)
    for ele in range(1,len(adjacency_list)):

        # Process the node only if it hasn't been visited before
        if not visited[ele]:
            # If DFS finds a cycle starting from this node, the graph has a cycle
            if detect_cyle(adjacency_list, ele, visited, path_visited):
                return True
                
    # If all nodes are processed without finding any back-edges, the graph is acyclic
    return False

# adjacency_list = [
#     None,
#     [2],
#     [3],
#     [4,7],
#     [5],
#     [6],
#     [],
#     [5],
#     [2,9],
#     [10],
#     [8]
# ]
adjacency_list = [
    None,
    [2],
    [3],
    [4,7],
    [5],
    [6],
    [],
    [5],
    [2,9],
    [10],
    []
]
print(helper(adjacency_list))