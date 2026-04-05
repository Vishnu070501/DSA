"""
Problem Statement: Rotting Oranges
You are given an m x n grid where each cell can have one of three values: 
0 representing an empty cell, 1 representing a fresh orange, or 2 representing a rotten orange. 
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. 
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

def get_non_rotten_neighbours(matrix, current_rotten):
    r,c = current_rotten
    result = []
    for del_row in range(-1,2):
        current_row = r+del_row
        if current_row>=0 and current_row<len(matrix) and matrix[current_row][c]==1:
            result.append((current_row,c))

    for del_col in range(-1,2):
        current_col = c+del_col
        if current_col>=0 and current_col<len(matrix[0]) and matrix[r][current_col]==1:
            result.append((r,current_col))
    return result

def rot(matrix, rotten):
    oranges_rotten = []
    for rotten_orange in rotten:
        oranges_to_rot = get_non_rotten_neighbours(matrix, rotten_orange)
        for fresh_orange in oranges_to_rot:
            r,c = fresh_orange
            matrix[r][c]=2
        oranges_rotten.extend(oranges_to_rot)
    return oranges_rotten

def time_taken(matrix):
    rotten_oranges = []
    # get all rotten oranges initially
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c]==2:
                rotten_oranges.append((r,c))
    result_time = 0
    # use them to rot in batches at each second
    while True:
        rotten_oranges = rot(matrix, rotten_oranges)
        result_time+=1
        fresh_oranges_left = 0
        #count for any left fresh oranges
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==1:
                    fresh_oranges_left +=1
        if len(rotten_oranges)<=0 or fresh_oranges_left<=0:
            break
    return result_time if fresh_oranges_left<=0 else -1


my_matrix = [
    [2,1,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,2],
    [1,1,2,0,0]
]

print(time_taken(my_matrix))