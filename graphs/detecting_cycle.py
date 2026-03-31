def detect_bfs(adjacency_list, visited_array,start):
    queue = [{'node':start, 'parent':-1}]
    visited_array[start] = True
    while len(queue)>0:
        new_parent = queue.pop(0)
        adjacents = adjacency_list[new_parent['node']]
        for adjacent in adjacents:
            if adjacent==new_parent['parent']:
                continue
            elif adjacent!=new_parent['parent'] and not visited_array[adjacent]:
                visited_array[adjacent]=True
                queue.append({'node':adjacent,'parent': new_parent['node']})
            elif adjacent!=new_parent['parent'] and visited_array[adjacent]:
                return True
            
    return False
            
def detect_dfs(adjacency_list, start, parent, visited_array):
    visited_array[start]=True
    for neighbour in adjacency_list[start]:
        if not visited_array[neighbour]:
            if detect_dfs(adjacency_list, neighbour, start, visited_array):
                return True
        elif visited_array[neighbour] and parent != neighbour:
            return True
    return False

def detect_cycle(adjacency_list):
    visited_array = [False for _ in range(len(adjacency_list))]
    for i in range(1, len(adjacency_list)):
        # if not visited_array[i] and detect_bfs(adjacency_list, visited_array, i):
        #     return True
        if not visited_array[i] and detect_dfs(adjacency_list, i, -1, visited_array):
            return True
    return False


adjacency_list_true_example=[
    None,
    [2,3],
    [1,5],
    [1,6,4],
    [3],
    [2,7],
    [3,7],
    [5,6]
]
adjacency_list_false_example=[
    None,
    [2,3],
    [1,5],
    [1,6,4],
    [3],
    [2],
    [3],
    # [5,6]
]
print(detect_cycle(adjacency_list_false_example))