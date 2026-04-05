"""
Problem Statement: M-Coloring Problem
Given an undirected graph and an integer M. The task is to determine if the graph can be colored 
with at most M colors such that no two adjacent vertices of the graph are colored with same color. 
Print 1 if it is possible to colour vertices and 0 otherwise.
"""

def is_color_possible(node, color, adjacency_list, color_map):
    for neighbor in adjacency_list[node]:
        if color_map[neighbor]==color:
            return False
    return True

def m_coloring( colors, adjacency_list, color_map=None, node= 0):
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

