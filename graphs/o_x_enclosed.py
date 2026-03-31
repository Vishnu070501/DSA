def dfs(matrix, start, visited_matrix):
    neighbours = []
    r,c = start
    matrix[r][c] = True
    for del_row in range(-1,2):
        curr_row = r+del_row
        if curr_row>=0 and curr_row<len(matrix) and not visited_matrix[curr_row][c]:
            neighbours.append((curr_row,c))

    for del_col in range(-1,2):
        curr_col = c+del_col
        if curr_col>=0 and curr_col<len(matrix[0]) and not visited_matrix[r][curr_col]:
            neighbours.append((r,curr_col))

    for neigh in neighbours:
        row,col = neigh
        if matrix[row][col] == 'O':
            dfs(matrix, neigh, visited_matrix)


def o_x_enclosed(matrix):
    visited_matrix = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    copy_matrix = [[*row] for row in matrix]
    for i in range(len(matrix)):
        if matrix[0][i]=='O' and not visited_matrix[0][i]:
            dfs(matrix, (0,i), visited_matrix)

    for i in range(len(matrix[0])):
        if matrix[i][0]=='O' and not visited_matrix[i][0]:
            dfs(matrix, (0,i), visited_matrix)

    for i in range(len(matrix)):
        if matrix[len(matrix)-1][i]=='O' and not visited_matrix[len(matrix)-1][i]:
            dfs(matrix, (0,i), visited_matrix)

    for i in range(len(matrix[0])):
        if matrix[i][len(matrix[0])-1]=='O' and not visited_matrix[i][len(matrix[0])-1]:
            dfs(matrix, (0,i), visited_matrix)

    print(visited_matrix)
    for i in range(len(visited_matrix)):
        for j in range(len(visited_matrix[0])):
            if not visited_matrix[i][j] and copy_matrix[i][j]=='O':
                copy_matrix[i][j]='X'

    return copy_matrix


my_matrix = [
    ['X', 'X','X', 'X','X'],
    ['X', 'O','O', 'X','O'],
    ['X', 'X','O', 'X','O'],
    ['X', 'O','X', 'O','X'],
    ['O', 'O','X', 'X','X'],
]

result = o_x_enclosed(my_matrix)
for row in result:
    print(row)