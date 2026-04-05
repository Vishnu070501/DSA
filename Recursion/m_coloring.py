"""
Problem Statement: M-Coloring Problem
Given an undirected graph and an integer M. The task is to determine if the graph can be colored 
with at most M colors such that no two adjacent vertices of the graph are colored with same color. 
Print 1 if it is possible to colour vertices and 0 otherwise.
"""

# Time Complexity: O(V) where V represents the maximum degree (number of connected edges) of the node.
# Space Complexity: O(1) auxiliary space since we just evaluate against the existing adjacency mapping dynamically.
def is_color_possible(node, color, adjacency_list, color_map):
    # Checks whether it is safely valid to color a graph node with a specific color designation. 
    # Scans against directly adjacent neighbors assessing if they inherently share this exact identical color already.
    for neighbor in adjacency_list[node]:
        if color_map[neighbor]==color:
            return False
    return True

# Time Complexity: O(M^N) where N is the number of nodes and M is the number of maximum permitted color assignments.
# Space Complexity: O(N) for the backtracking call stack array traversing sequence plus the size of tracking color_map list.
def m_coloring( colors, adjacency_list, color_map=None, node= 0):
    # Backtracking recursive approach to cleanly color nodes. For the currently scoped node, it actively cycles completely through 1 to M colors.
    # If a viable valid pathway tracks all the way to completion it triggers True returning natively, else it effectively backtracks erasing footprint bindings out of color_map.
    if color_map is None:
        color_map = [None for _ in range(len(adjacency_list))]
    if node == len(adjacency_list):
        return True

    for color_code in range(1, colors+1):
        if is_color_possible(node, color_code, adjacency_list, color_map):
            color_map[node] = color_code
            if m_coloring( colors, adjacency_list, color_map, node+1):
                return True
            else:
                color_map[node]=None#backtrack
    
    return False


n, e = map(int, input("Please enter the number of nodes and edges: ").split())

my_graph = [[] for _ in range(n)]
for i in range(e):
    a,b = map(int,input("enter edge from a to b node(based indexing):").split())
    my_graph[a].append(b)
    my_graph[b].append(a)

colors = int(input("enter the number of colors to check:"))

print(f"can {colors} colors fill this graph:{m_coloring(colors, my_graph)}")

