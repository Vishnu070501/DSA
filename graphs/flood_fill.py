def flood_fill(matrix, start, colour):
    matrix_copy = [[*row] for row in matrix]
    
    dfs( matrix_copy, start, colour)
    return matrix_copy


def get_neightbours_of_same_color(matrix, node, colour):
    r,c = node
    result = []
    for del_col in range(-1,2):
        curr_r = r+del_col
        if (curr_r>=0 and curr_r<len(matrix)) and matrix[curr_r][c]==colour:
            result.append((curr_r,c))

    for del_col in range(-1,2):
        curr_c = c+del_col
        if (curr_c>=0 and curr_c<len(matrix[0])) and matrix[r][curr_c]==colour:
            result.append((r,curr_c))
    return result
def dfs(matrix, start, colour, start_color=None):
    r,c = start
    if start_color is None:
        start_color = matrix[r][c]
    matrix[r][c] = colour
    neighbours = get_neightbours_of_same_color(matrix, start, start_color)

    for ele in neighbours:
        dfs( matrix, ele, colour)


    
    
my_matrix = [
    [1,1,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [1,1,0,0,0]
]

print(flood_fill(my_matrix, (4,1), 3))