"""
Problem Statement: 01 Matrix / Distance of Nearest Cell having 1
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell. 
The distance between two adjacent cells is 1.
"""

from copy import deepcopy

# Time Complexity: O(1) processing immediate 4-directional neighboring bounds.
# Space Complexity: O(1) storing local queue variables internally explicitly.
def traverse_one_bfs(matrix, starting_point, distance_to_nearest_one):
    row,col = starting_point
    distance_marked = []
    for del_row in range(-1,2):
        current_row = row+del_row
        if del_row !=0 and current_row>=0 and current_row<len(matrix) and matrix[current_row][col]==None:
            matrix[current_row][col] = distance_to_nearest_one
            distance_marked.append((current_row,col))

    for del_col in range(-1,2):
        curent_col = col+del_col
        if del_col !=0 and curent_col>=0 and curent_col<len(matrix[0]) and matrix[row][curent_col]==None:
            matrix[row][curent_col] = distance_to_nearest_one
            distance_marked.append((row,curent_col))

    return distance_marked
    
#done using bfs as we take single step bfs wise and mark each of them as 1 distance from the nearest one
# Time Complexity: O(N*M) iterating cells using Multi-source BFS logic globally.
# Space Complexity: O(N*M) mapping auxiliary grid configurations conditionally efficiently.
def return_nearest_one(matrix):
    copy_matrix = [[None if ele!=1 else 0 for ele in row] for row in matrix]
    starting_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                starting_points.append((i,j))
    distance_to_nearest_one = 1
    while True:
        new_starting_points = []
        for ele in starting_points:
            new_starting_points.extend(traverse_one_bfs(copy_matrix, ele, distance_to_nearest_one))
        starting_points = deepcopy(new_starting_points)
        distance_to_nearest_one +=1
        if len(starting_points)<=0:
            break

    return copy_matrix

print(return_nearest_one([
    [0,0,0],
    [0,1,0],
    [1,0,0]
]))



    