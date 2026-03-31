#rule of thumb leniar graphs are bipartite, if there is a cycle of odd length then the graph is not bipartite
def bfs_filling(adjacency_list, node, start_color, colors):

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
def dfs_filling(adjacency_list, node, start_color, colors):
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

def is_bipartite(adjacency_list):
    colors = [None for _ in range(len(adjacency_list))]
    for node in range(1,len(adjacency_list)):
        if colors[node] is None:
            neighbor_colors = [colors[i] for i in adjacency_list[node]]
            if all([ele!=1 for ele in neighbor_colors]):
                if not bfs_filling(adjacency_list, node, 1, colors):
                    return False
            elif all([ele!=0 for ele in neighbor_colors]):
                if not bfs_filling(adjacency_list, node, 0, colors):
                    return False
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