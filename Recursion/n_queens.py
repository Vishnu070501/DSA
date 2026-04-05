"""
Problem Statement: N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that 
no two queens attack each other. Given an integer n, return all distinct solutions.
"""

# Time Complexity: O(N) analyzing and iterating progressively through grid matrices checking linear zones tracking backwards incrementally.
# Space Complexity: O(1) in-place static grid verifications accessing memory without extending capacity footprint.
def is_safe(chess_board, x, y):
    # Iteratively traces grid intersections across columns extending validating path clearing boundaries.
    # (Note: Backtracking natively optimizes performance heavily using O(1) hash validations later mitigating need for iterating)
    i,j = x-1,y-1

    #upper left diagonal check
    while i>=0 and j>=0:
        if chess_board[i][j]:
            return False
        i-=1
        j-=1
    
    #same row towards left side check
    if any(chess_board[x]):
        return False
    
    i,j = x+1,y-1

    while i < len(chess_board) and j >=0:
        if chess_board[i][j]:
            return False
        i+=1
        j-=1
    #these are the 3 checks needed as we are going from left to right while filling the queens and column check not needed as each column is filled once and while backtracked we remove it 
    return True


    
# Time Complexity: O(N!) representing boundary permutations constrained sequentially filtering non-usable combinations outright effectively.
# Space Complexity: O(N) auxiliary allocation sets caching safe configurations hashing structural positions independently along paths extending execution.
def n_queens(solving_col_index, chess_board=None, left_row=None, left_upper_diagonal=None, left_lower_diagonal=None):
    # Leverages Backtracking algorithm intelligently hashing static mathematical constraints calculating relative structural collision patterns cleanly on deployment.
    # Sets configuration states natively ensuring backtracking accurately unwinds specific variables un-slotting queens preserving clean scope evaluation.
    
    if left_row is None:
        left_row = {row_index: False for row_index in range(len(chess_board))}

    if left_lower_diagonal is None:
        left_lower_diagonal = {
            row_col_sum: False
            for row_col_sum in range(len(chess_board) + len(chess_board[0]) - 1)
        }

    if left_upper_diagonal is None:
        left_upper_diagonal = {
            striver_formula_value: False
            for striver_formula_value in range(len(chess_board) + len(chess_board[0]) - 1)
        }

    #if the column we solvin past the last one print our chess board
    if solving_col_index == len(chess_board[0]):
        print("answer:")
        for row in chess_board:
            print(row)
        return 
    for row_index in range(len(chess_board)):

        #unoptimised way of checking if can place a queen makes O(n2) time
        # if is_safe(chess_board, row_index, solving_col_index):
        #     chess_board[row_index][solving_col_index]=True
        #     n_queens(solving_col_index+1, chess_board)
        #     chess_board[row_index][solving_col_index]=False
        # refer striver's vid 
        strivers_formula_value_for_cell = (len(chess_board)-1)+(solving_col_index - row_index)
        can_fill = (
            not left_row[row_index]
            and not left_lower_diagonal[row_index + solving_col_index]
            and not left_upper_diagonal[strivers_formula_value_for_cell]
        )

        if can_fill:
            chess_board[row_index][solving_col_index]=True
            left_row[row_index]=True#left row already filled
            left_lower_diagonal[row_index+solving_col_index]=True# in this hashmap we store the sum of indexes which are same if we move left lower diagonally(setting that sum diagonal as filled)
            left_upper_diagonal[strivers_formula_value_for_cell]=True#in this hashmap we find using the formula above we get same vals along the left upper diagonal so we set that to true

            n_queens(
                solving_col_index + 1,
                chess_board,
                left_row,
                left_upper_diagonal,
                left_lower_diagonal
            )
            
            chess_board[row_index][solving_col_index]=False
            left_row[row_index]=False
            left_lower_diagonal[row_index+solving_col_index]=False
            left_upper_diagonal[strivers_formula_value_for_cell]=False




n_queens(0, [[False for _ in range(4)] for _ in range(4)])