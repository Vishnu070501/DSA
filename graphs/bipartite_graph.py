"""
Problem Statement: Is Graph Bipartite?
There is an undirected graph with n nodes. Return true if and only if it is bipartite. 
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that 
every edge in the graph connects a node in set A and a node in set B.
"""

#rule of thumb leniar graphs are bipartite, if there is a cycle of odd length then the graph is not bipartite
# Time Complexity: O(V + E) verifying all connected component edges iteratively via queue structure.
# Space Complexity: O(V) space used for the BFS queue mapping dynamically.
def bfs_filling(adjacency_list, node, start_color, colors):
    """
    Performs a component traversal using an iterative stack (DFS-like behavior)
    to color the graph and check for bipartiteness.
    
    Args:
        adjacency_list: Graph representation as an array of neighbor lists.
        node: The starting node to color.
        start_color: The color (0 or 1) assigned to the start node.
        colors: Array tracking the colors of all nodes (None if uncolored).
        
    Returns:
        bool: True if this component can be bipartitely colored, False if a conflict is found.
    """
    colors[node] = start_color
    helper_stack = [node]

    while len(helper_stack) > 0:

        node = helper_stack.pop()
        neighbours = adjacency_list[node]

        for neighbour in neighbours:

            neighbour_color = colors[neighbour]

            # already colored
            if neighbour_color is not None:

                if neighbour_color == colors[node]:
                    return False

            # not colored
            else:
                colors[neighbour] = 1 if colors[node] != 1 else 0
                helper_stack.append(neighbour)

        # print(f"helper stack:{helper_stack}")

    return True
# Time Complexity: O(V + E) exploring all branches safely via recursion.
# Space Complexity: O(V) bounding the recursive call stack traversing paths symmetrically.
def dfs_filling(adjacency_list, node, start_color, colors):
    """
    Performs Depth-First Search (DFS) recursively to find if the graph component is bipartite.
    
    Args:
        adjacency_list: Graph representation as an array of neighbor lists.
        node: The currently visited node.
        start_color: The color assigned to the current node.
        colors: Array tracking the assigned colors of all nodes.
        
    Returns:
        bool: True if valid bipartite coloring is possible, False if a conflict is found.
    """
    colors[node] = start_color
    neighbors = adjacency_list[node]
    for neighbor in neighbors:
        if colors[neighbor] is not None:
            if colors[neighbor] == colors[node]:
                return False
        else:
            neighbors_answer = dfs_filling(adjacency_list, neighbor, 0 if start_color==1 else 1, colors)
            if not neighbors_answer:
                return False
    return True

# Time Complexity: O(V + E) traversing entire matrix systematically efficiently natively.
# Space Complexity: O(V) tracking array blocks bounding variables intelligently natively.
def is_bipartite(adjacency_list):
    """
    Checks if the entire graph represented by the adjacency_list is bipartite.
    Iterates over all nodes to handle disconnected components.
    
    Args:
        adjacency_list: Assumes 1-based indexing where index 0 is None or ignored.
        
    Returns:
        bool: True if the graph is bipartite, False otherwise.
    """
    # Initialize all nodes with 'None' indicating they are uncolored
    colors = [None for _ in range(len(adjacency_list))]
    
    for node in range(1,len(adjacency_list)):
        # Process component only if the node hasn't been colored yet
        if colors[node] is None:
            neighbor_colors = [colors[i] for i in adjacency_list[node]]
            
            # Check if it's safe to start coloring the current node with 1
            if all([ele!=1 for ele in neighbor_colors]):
                if not bfs_filling(adjacency_list, node, 1, colors):
                    return False
                    
            # Or check if it's safe to start coloring it with 0
            elif all([ele!=0 for ele in neighbor_colors]):
                if not bfs_filling(adjacency_list, node, 0, colors):
                    return False
                    
            # If neighbors have both 0 and 1, the graph cannot be bipartite
            else:
                return False
            # if all([ele!=1 for ele in neighbor_colors]):
            #     if not dfs_filling(adjacency_list, node, 1, colors):
            #         return False
            # elif all([ele!=0 for ele in neighbor_colors]):
            #     if not dfs_filling(adjacency_list, node, 0, colors):
            #         return False
            # else:
            #     return False
    return True

adjacency_list = [
    None,
    [2],
    [3,6],
    [2,4],
    [3,5,7],
    [4,6],
    [2,5],
    [4,8],
    [7]
]
# adjacency_list = [
#     None,
#     [2],
#     [3,6],
#     [2,9],
#     [9,5,7],
#     [4,6],
#     [2,5],
#     [4,8],
#     [7],
#     [3,4]
# ]
print(f"is bipartite:{is_bipartite(adjacency_list)}")