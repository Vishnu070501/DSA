"""
Problem Statement: Graph Traversal (BFS & DFS)
Generic graph theory problems and search algorithms for basic graph traversals.
"""

# Time Complexity: O(V + E) checking connected neighbors layer by layer natively.
# Space Complexity: O(V) to maintain the queue for unvisited neighbors dynamically.
def breadth_first_search(graph, start, visited):
    # Standard BFS queue implementation natively tracking explored vertices cleanly.
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


        
                
# Time Complexity: O(V + E) recursively exploring tree components fully.
# Space Complexity: O(V) tracking call stack depth directly proportional to graph sequence.
def depth_first_search(graph, start, visited=None):
    # Standard DFS traversing deeply into leaf nodes inherently executing safely.
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)
def main():
    u,v = input("enter the number of nodes and endges(seperated by spaces in a single line)").split()
    adjacency_matrix = [[None for _ in range(int(u)+1)] for _ in range(int(u)+1)]
    adjacency_list = [[] for _ in range(int(u)+1)]
    for edge in range(int(v)):
        x,y = input(f"enter the edges {edge+1}(seperated by spaces in a single line)").split()
        print(f"edge from {x} to {y}")
        adjacency_matrix[int(x)][int(y)] = 1
        adjacency_matrix[int(y)][int(x)] = 1
        adjacency_list[int(x)].append(int(y))
        adjacency_list[int(y)].append(int(x))
        
    print("Adjacency Matrix:")
    for row in adjacency_matrix[1:]:
        print(row[1:])
    print("Adjacency List:")
    for index in range(1, len(adjacency_list)):
        print(f"{index}: {adjacency_list[index]}")
        
    print("Full BFS traversal (all provinces):")
    visited = set()
    no_of_provinces = 0
    for node in range(1, len(adjacency_list)):
        if node not in visited:
            no_of_provinces += 1
            breadth_first_search(adjacency_list, node, visited)
    print(f"\nNumber of provinces after BFS: {no_of_provinces}")
    #hii
    print("\nFull DFS traversal (all provinces):")
    visited = set()
    no_of_provinces = 0
    for node in range(1, len(adjacency_list)):
        if node not in visited:
            no_of_provinces += 1
            depth_first_search(adjacency_list, node, visited)
    print(f"\nNumber of provinces after DFS: {no_of_provinces}")       
    
    
        
if __name__ == "__main__":
    main()