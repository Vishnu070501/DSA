"""
Problem Statement: Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells. 
A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
"""

def is_valid(sudoku_board, value, x, y):
    # check for the same row
    if any(ele == value for ele in sudoku_board[x]):
        return False 
    # check for same value in column
    if any(sudoku_board[i][y] == value for i in range(len(sudoku_board))):
        return False
    
    #checking inside the box
    start_row_index,start_col_index = -1,-1
    if x < 3:
        start_row_index = 0
    elif x < 6:
        start_row_index = 3
    else:
        start_row_index = 6
        
    if y < 3:
        start_col_index = 0
    elif y < 6:
        start_col_index = 3
    else:
        start_col_index = 6
    
    for i in range(start_row_index, start_row_index+3):
        for j in range(start_col_index, start_col_index+3):
            if sudoku_board[i][j]==value:
                return False
            
    return True

def is_valid_opt(sudoku_board, value, x, y):
    #iterated the whole row, column and the sub-matrix using the same I variable
    for i in range(9):
        if sudoku_board[x][i]==value:
            return False
        elif sudoku_board[i][y]==value:
            return False
        elif (sudoku_board[((x//3)*3)+(i//3)][((y//3)*3)+(i%3)]==value):
            return False
        
    return True
        
def solve(sudoku_board):
    
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[i])):
            if sudoku_board[i][j] is None:
                for value in range(1,10):
                    if is_valid_opt(sudoku_board, value, i, j):
                        sudoku_board[i][j]=value
                        #if all is filled and the recursion returns true after the final box is filled at line number 46,let the box be filled 
                        if solve(sudoku_board):
                            return True
                        #if its false then only backtrack as we need just one solution
                        else:
                            sudoku_board[i][j]=None
                #no value fillable
                return False
    # if it is out of both the loops means no empty cells therefore a valid solution
    return True

sudoku_board = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9, 8, None, None, None, None, 6, None],

    [8, None, None, None, 6, None, None, None, 3],
    [4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],

    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5],
    [None, None, None, None, 8, None, None, 7, 9]
]

solve(sudoku_board)

print("answer1:")
for row in sudoku_board:
    print(row)
    
my_empty_board = [[None for _ in range(9)] for _ in range(9)]
solve(my_empty_board)

print("answer2:")
for row in sudoku_board:
    print(row)