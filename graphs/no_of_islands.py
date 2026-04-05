"""
Problem Statement: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands. An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically.
"""

def get_unvisited_neighbours(current_node, matrix, visited_matrix):
    result = []
    for del_row in range(-1,2):
        for del_column in range(-1,2):
            current_row = current_node[0]+del_row
            current_col = current_node[1]+del_column
            if (current_row>=0 and current_row<len(matrix)) and (current_col>=0 and current_col<len(matrix[0])) and matrix[current_row][current_col] and not visited_matrix[current_row][current_col]:
                result.append((current_row,current_col))
    return result

def bfs(matrix, visited_matrix, start):
    queue = [start]
    visited_matrix[start[0]][start[1]]=True
    while len(queue)>0:
        current_ele = queue.pop(0)
        neighbours = get_unvisited_neighbours(current_ele, matrix, visited_matrix)
        
        for ele in neighbours:
            visited_matrix[ele[0]][ele[1]] = True
            queue.append(ele)

def dfs(matrix, visited_matrix, start):
    visited_matrix[start[0]][start[1]]=True
    neighbours = get_unvisited_neighbours(start, matrix, visited_matrix)
    for ele in neighbours:
        if not visited_matrix[ele[0]][ele[1]]:
            dfs(matrix, visited_matrix, ele)


def count_islands(matrix):
    visited_matrix = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] and not visited_matrix[i][j]:
                # bfs(matrix, visited_matrix, (i,j))
                dfs(matrix, visited_matrix, (i,j))
                result +=1

    return result


my_matrix = [
    [1,1,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [1,1,0,0,0]
]

print(count_islands(my_matrix))